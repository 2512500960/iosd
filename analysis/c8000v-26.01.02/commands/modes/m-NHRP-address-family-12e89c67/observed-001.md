# NHRP-address-family · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009796

```text
(config-router-af)# default import bgp <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34BE3550 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e06b676efe11b94e](../../evidence/conditions-sets-086.md#c-e06b676efe11b94e) · [状态效果 S-f755cc4fa95c26db](../../evidence/state_effects-sets-052.md#s-f755cc4fa95c26db)

### observed_connections-009797

```text
(config-router-af)# import bgp <number:1..4294967295> <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34BE3550 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous system number。

[条件 C-f810c0997581d29e](../../evidence/conditions-sets-096.md#c-f810c0997581d29e) · [参数 P-08fa0189d9fa98c6](../../evidence/parameters-sets-001.md#p-08fa0189d9fa98c6) · [状态效果 S-8dc3856a28817def](../../evidence/state_effects-sets-030.md#s-8dc3856a28817def)

### observed_connections-009795

```text
(config-router-af)# no import bgp <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34BE3550 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-677e9c0608947bd9](../../evidence/conditions-sets-040.md#c-677e9c0608947bd9) · [状态效果 S-2c17b673a7987c8f](../../evidence/state_effects-sets-010.md#s-2c17b673a7987c8f)
