# isis-flood-speed · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009600

```text
(config-isis-fspeed)# default exit-lsp-fast-flooding <cr>
```

Handler ` RVA 0x1070B0B0 `；selector ` 0 `；EOL ` RVA 0x34BE0748 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-22581c6a91be1da3](../../evidence/state_effects-sets-008.md#s-22581c6a91be1da3)

### observed_connections-009601

```text
(config-isis-fspeed)# default max-lsp-tx <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 54 `；EOL ` RVA 0x34BE04C0 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4ebde00a9760185](../../evidence/conditions-sets-076.md#c-c4ebde00a9760185) · [状态效果 S-22581c6a91be1da3](../../evidence/state_effects-sets-008.md#s-22581c6a91be1da3)

### observed_connections-009597

```text
(config-isis-fspeed)# default remote-psnp-delay <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 60 `；EOL ` RVA 0x34BE01A8 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-26f7abaf65b0ffce](../../evidence/conditions-sets-015.md#c-26f7abaf65b0ffce) · [状态效果 S-22581c6a91be1da3](../../evidence/state_effects-sets-008.md#s-22581c6a91be1da3)

### observed_connections-009593

```text
(config-isis-fspeed)# exit-lsp-fast-flooding <cr>
```

Handler ` RVA 0x1070B0B0 `；selector ` 0 `；EOL ` RVA 0x34BE0748 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009599

```text
(config-isis-fspeed)# max-lsp-tx <number:33..5000> <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 54 `；EOL ` RVA 0x34BE04C0 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MaxLSPTx。

[条件 C-d86d04201c2c587f](../../evidence/conditions-sets-083.md#c-d86d04201c2c587f) · [参数 P-2d8779e940be3c9b](../../evidence/parameters-sets-004.md#p-2d8779e940be3c9b)

### observed_connections-009596

```text
(config-isis-fspeed)# no exit-lsp-fast-flooding <cr>
```

Handler ` RVA 0x1070B0B0 `；selector ` 0 `；EOL ` RVA 0x34BE0748 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a4881acce448746f](../../evidence/state_effects-sets-035.md#s-a4881acce448746f)

### observed_connections-009598

```text
(config-isis-fspeed)# no max-lsp-tx <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 54 `；EOL ` RVA 0x34BE04C0 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c38d9e0ad119d4ec](../../evidence/conditions-sets-075.md#c-c38d9e0ad119d4ec) · [状态效果 S-a4881acce448746f](../../evidence/state_effects-sets-035.md#s-a4881acce448746f)

### observed_connections-009594

```text
(config-isis-fspeed)# no remote-psnp-delay <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 60 `；EOL ` RVA 0x34BE01A8 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f76eb2442b9fc08c](../../evidence/conditions-sets-096.md#c-f76eb2442b9fc08c) · [状态效果 S-a4881acce448746f](../../evidence/state_effects-sets-035.md#s-a4881acce448746f)

### observed_connections-009595

```text
(config-isis-fspeed)# remote-psnp-delay <number:1..10000> <cr>
```

Handler ` RVA 0x1070B130 `；selector ` 60 `；EOL ` RVA 0x34BE01A8 `。

模式根 ` RVA 0x34BE00A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Remote PSNP delay in msec。

[条件 C-6590ab896984a6c6](../../evidence/conditions-sets-039.md#c-6590ab896984a6c6) · [参数 P-78e2978dfb11b144](../../evidence/parameters-sets-009.md#p-78e2978dfb11b144)
