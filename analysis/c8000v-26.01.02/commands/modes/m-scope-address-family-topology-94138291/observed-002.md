# scope-address-family-topology · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-002896

```text
(config-router-scope-af-topo)# no bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x345CEE38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a57efef1bb356cf9](../../evidence/conditions-sets-064.md#c-a57efef1bb356cf9) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002762

```text
(config-router-scope-af-topo)# no bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x345BCAB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002769

```text
(config-router-scope-af-topo)# no bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x345BBE68 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87b594c4d6dcd88d](../../evidence/conditions-sets-052.md#c-87b594c4d6dcd88d) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002810

```text
(config-router-scope-af-topo)# no bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x345CA030 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-276e201f831b17dd](../../evidence/conditions-sets-015.md#c-276e201f831b17dd) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-003019

```text
(config-router-scope-af-topo)# no bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x345CFC50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-fd6cda537b929d75](../../evidence/conditions-sets-098.md#c-fd6cda537b929d75) · [参数 P-c7888514a7534998](../../evidence/parameters-sets-015.md#p-c7888514a7534998) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002823

```text
(config-router-scope-af-topo)# no bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x345CC2C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5d48da5a23e8e211](../../evidence/conditions-sets-036.md#c-5d48da5a23e8e211) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002870

```text
(config-router-scope-af-topo)# no bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x345C6208 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c3ec135058645164](../../evidence/conditions-sets-076.md#c-c3ec135058645164) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002920

```text
(config-router-scope-af-topo)# no bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x345CBF58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-f6c5e214b2225f3e](../../evidence/conditions-sets-095.md#c-f6c5e214b2225f3e) · [参数 P-75e51e2c3101672c](../../evidence/parameters-sets-009.md#p-75e51e2c3101672c) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002897

```text
(config-router-scope-af-topo)# no bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x345CCF78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d9496dbc1b774f3c](../../evidence/conditions-sets-084.md#c-d9496dbc1b774f3c) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002965

```text
(config-router-scope-af-topo)# no bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x345CD548 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-52cb53fd4b934a64](../../evidence/conditions-sets-032.md#c-52cb53fd4b934a64) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002981

```text
(config-router-scope-af-topo)# no bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x345BFB70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002806

```text
(config-router-scope-af-topo)# no bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x345CAF08 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-756792ade7cc9960](../../evidence/conditions-sets-046.md#c-756792ade7cc9960) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-003011

```text
(config-router-scope-af-topo)# no bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x345CEAB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-7074cbe64013ab1e](../../evidence/state_effects-sets-024.md#s-7074cbe64013ab1e)

### observed_connections-003007

```text
(config-router-scope-af-topo)# no bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x345CE458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-490f75c1489b43a8](../../evidence/state_effects-sets-016.md#s-490f75c1489b43a8)

### observed_connections-003009

```text
(config-router-scope-af-topo)# no bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x345CE7A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-521caf4f5ae87226](../../evidence/state_effects-sets-018.md#s-521caf4f5ae87226)

### observed_connections-003005

```text
(config-router-scope-af-topo)# no bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345CE110 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-8c1164eac73e7e09](../../evidence/state_effects-sets-030.md#s-8c1164eac73e7e09)

### observed_connections-002929

```text
(config-router-scope-af-topo)# no bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x345C2B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002783

```text
(config-router-scope-af-topo)# no bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x345C9C80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-133a19ecba7cce81](../../evidence/conditions-sets-008.md#c-133a19ecba7cce81) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002688

```text
(config-router-scope-af-topo)# no bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x345BB6A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-daadd1d725ee3f94](../../evidence/conditions-sets-084.md#c-daadd1d725ee3f94) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002903

```text
(config-router-scope-af-topo)# no bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345BE520 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002732

```text
(config-router-scope-af-topo)# no bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x345C14A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-879c9419fc8ed990](../../evidence/conditions-sets-052.md#c-879c9419fc8ed990) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002959

```text
(config-router-scope-af-topo)# no bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345CD918 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4969fbb5328f8a37](../../evidence/conditions-sets-029.md#c-4969fbb5328f8a37) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002758

```text
(config-router-scope-af-topo)# no bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x345BBAC0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9780fe2be46b60d7](../../evidence/conditions-sets-058.md#c-9780fe2be46b60d7) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002799

```text
(config-router-scope-af-topo)# no bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345CF1E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6b3bc92f1eb4ad98](../../evidence/conditions-sets-041.md#c-6b3bc92f1eb4ad98) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002932

```text
(config-router-scope-af-topo)# no bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x345C35E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002854

```text
(config-router-scope-af-topo)# no bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x345C3938 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cfdbe8760feeedb8](../../evidence/conditions-sets-080.md#c-cfdbe8760feeedb8) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002682

```text
(config-router-scope-af-topo)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e07495ed56793ecc](../../evidence/conditions-sets-086.md#c-e07495ed56793ecc) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002826

```text
(config-router-scope-af-topo)# no default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-1482dc0e582fe902](../../evidence/state_effects-sets-005.md#s-1482dc0e582fe902)

### observed_connections-002722

```text
(config-router-scope-af-topo)# no default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16d4bf7a7d5fc443](../../evidence/conditions-sets-009.md#c-16d4bf7a7d5fc443) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002731

```text
(config-router-scope-af-topo)# no distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8507c54e95cd8959](../../evidence/conditions-sets-051.md#c-8507c54e95cd8959) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002833

```text
(config-router-scope-af-topo)# no distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e5a4ccc65bf3890c](../../evidence/conditions-sets-089.md#c-e5a4ccc65bf3890c) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002840

```text
(config-router-scope-af-topo)# no distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a6304d86ad6f95f](../../evidence/conditions-sets-004.md#c-0a6304d86ad6f95f) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002838

```text
(config-router-scope-af-topo)# no distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-52458dab09ccdcb7](../../evidence/state_effects-sets-018.md#s-52458dab09ccdcb7)

### observed_connections-002676

```text
(config-router-scope-af-topo)# no flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0e6ae0e65ef7f08e](../../evidence/conditions-sets-006.md#c-0e6ae0e65ef7f08e) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002693

```text
(config-router-scope-af-topo)# no import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x345B9A18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0c800ed54083c83](../../evidence/conditions-sets-062.md#c-a0c800ed54083c83) · [状态效果 S-e556d94376eb467a](../../evidence/state_effects-sets-048.md#s-e556d94376eb467a)

### observed_connections-002876

```text
(config-router-scope-af-topo)# no import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x345BA798 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5076489d906cbe5](../../evidence/conditions-sets-082.md#c-d5076489d906cbe5) · [状态效果 S-3bbcd5c0dea84d52](../../evidence/state_effects-sets-013.md#s-3bbcd5c0dea84d52)

### observed_connections-002749

```text
(config-router-scope-af-topo)# no import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x345BAB78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4ecfb69fa69530ad](../../evidence/conditions-sets-031.md#c-4ecfb69fa69530ad) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002873

```text
(config-router-scope-af-topo)# no import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x345BA228 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b081c7193042454](../../evidence/conditions-sets-029.md#c-4b081c7193042454) · [状态效果 S-e04bb3581c23b8de](../../evidence/state_effects-sets-047.md#s-e04bb3581c23b8de)

### observed_connections-002674

```text
(config-router-scope-af-topo)# no input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c4824c7cac4b28be](../../evidence/conditions-sets-076.md#c-c4824c7cac4b28be) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002759

```text
(config-router-scope-af-topo)# no label mode <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 0 `；EOL ` RVA 0x344F20C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fda9fa1d85a7317e](../../evidence/conditions-sets-098.md#c-fda9fa1d85a7317e) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002772

```text
(config-router-scope-af-topo)# no metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002708

```text
(config-router-scope-af-topo)# no metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8221b40cbcf421f4](../../evidence/conditions-sets-050.md#c-8221b40cbcf421f4) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002791

```text
(config-router-scope-af-topo)# no metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b000c6ef41ba655a](../../evidence/conditions-sets-068.md#c-b000c6ef41ba655a) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002881

```text
(config-router-scope-af-topo)# no offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-b7414ba60af25c7b](../../evidence/conditions-sets-071.md#c-b7414ba60af25c7b) · [参数 P-583d525582bab90e](../../evidence/parameters-sets-007.md#p-583d525582bab90e) · [状态效果 S-fad28adc96c23fc1](../../evidence/state_effects-sets-053.md#s-fad28adc96c23fc1)

### observed_connections-002666

```text
(config-router-scope-af-topo)# no output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x344F0CD0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75b85446d28e76e2](../../evidence/conditions-sets-046.md#c-75b85446d28e76e2) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002750

```text
(config-router-scope-af-topo)# no passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66b93bc17fdac1bf](../../evidence/conditions-sets-040.md#c-66b93bc17fdac1bf) · [状态效果 S-2adfbee1cb0ae13c](../../evidence/state_effects-sets-010.md#s-2adfbee1cb0ae13c)

### observed_connections-002689

```text
(config-router-scope-af-topo)# no propagate-aspath <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 1 `；EOL ` RVA 0x344F1A40 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002696

```text
(config-router-scope-af-topo)# no propagate-community <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 2 `；EOL ` RVA 0x344F1CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002747

```text
(config-router-scope-af-topo)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e5a51106c0b763a](../../evidence/conditions-sets-012.md#c-1e5a51106c0b763a) · [状态效果 S-a74be56c29854711](../../evidence/state_effects-sets-035.md#s-a74be56c29854711)

### observed_connections-002754

```text
(config-router-scope-af-topo)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-003002

```text
(config-router-scope-af-topo)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-5a416169412196ba](../../evidence/conditions-sets-035.md#c-5a416169412196ba) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-915a5106949119ce](../../evidence/state_effects-sets-031.md#s-915a5106949119ce)

### observed_connections-003001

```text
(config-router-scope-af-topo)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-c27aae31069e8d90](../../evidence/conditions-sets-075.md#c-c27aae31069e8d90) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-d2336ce6c56499cb](../../evidence/state_effects-sets-045.md#s-d2336ce6c56499cb)

### observed_connections-002874

```text
(config-router-scope-af-topo)# no summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-2cd36336053d115f](../../evidence/conditions-sets-018.md#c-2cd36336053d115f) · [参数 P-aebe586c61a4934d](../../evidence/parameters-sets-013.md#p-aebe586c61a4934d) · [状态效果 S-7a8c6d13a7f5ebd4](../../evidence/state_effects-sets-026.md#s-7a8c6d13a7f5ebd4)

### observed_connections-002743

```text
(config-router-scope-af-topo)# no summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x344ED118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address。

[条件 C-a22537b1781681b8](../../evidence/conditions-sets-063.md#c-a22537b1781681b8) · [参数 P-b5381e36e4d9d9b2](../../evidence/parameters-sets-014.md#p-b5381e36e4d9d9b2) · [状态效果 S-7a8c6d13a7f5ebd4](../../evidence/state_effects-sets-026.md#s-7a8c6d13a7f5ebd4)

### observed_connections-002686

```text
(config-router-scope-af-topo)# no synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x345BAF38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6acc88802a133995](../../evidence/conditions-sets-041.md#c-6acc88802a133995) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002692

```text
(config-router-scope-af-topo)# no table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x345BB310 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6f5fdbe248f5527](../../evidence/conditions-sets-064.md#c-a6f5fdbe248f5527) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002681

```text
(config-router-scope-af-topo)# no version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x344EC5E8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-82c9e5afc55f7fb5](../../evidence/conditions-sets-051.md#c-82c9e5afc55f7fb5) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002879

```text
(config-router-scope-af-topo)# offset-list <number:0..99> in <number:0..16> <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-12bb4d7a589b9575](../../evidence/conditions-sets-007.md#c-12bb4d7a589b9575) · [参数 P-c7a3a04a4125a0f9](../../evidence/parameters-sets-015.md#p-c7a3a04a4125a0f9) · [状态效果 S-385c91dfae113f88](../../evidence/state_effects-sets-012.md#s-385c91dfae113f88)

### observed_connections-003116

```text
(config-router-scope-af-topo)# offset-list <number:0..99> in <number:0..16> <interface> <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-7eb4309a0a263880](../../evidence/conditions-sets-049.md#c-7eb4309a0a263880) · [缺口 G-f1106a52645aec46](../../evidence/gaps-sets-008.md#g-f1106a52645aec46) · [参数 P-c8b15b3c0e8177f2](../../evidence/parameters-sets-015.md#p-c8b15b3c0e8177f2) · [状态效果 S-385c91dfae113f88](../../evidence/state_effects-sets-012.md#s-385c91dfae113f88)

### observed_connections-002662

```text
(config-router-scope-af-topo)# output-delay <number:8..50> <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x344F0CD0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in milliseconds。

[条件 C-87dc876bfcb8bdb1](../../evidence/conditions-sets-053.md#c-87dc876bfcb8bdb1) · [参数 P-5dbd675bad51cba5](../../evidence/parameters-sets-007.md#p-5dbd675bad51cba5)

### observed_connections-003026

```text
(config-router-scope-af-topo)# passive-interface <interface> <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-49611bc98f9f478e](../../evidence/conditions-sets-029.md#c-49611bc98f9f478e) · [缺口 G-7544e03d398bc315](../../evidence/gaps-sets-005.md#g-7544e03d398bc315) · [参数 P-8efe1fe22fee311d](../../evidence/parameters-sets-011.md#p-8efe1fe22fee311d)

### observed_connections-002694

```text
(config-router-scope-af-topo)# passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66b93bc17fdac1bf](../../evidence/conditions-sets-040.md#c-66b93bc17fdac1bf) · [状态效果 S-2ca547d2661a6484](../../evidence/state_effects-sets-010.md#s-2ca547d2661a6484)

### observed_connections-002670

```text
(config-router-scope-af-topo)# propagate-aspath <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 1 `；EOL ` RVA 0x344F1A40 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e)

### observed_connections-002672

```text
(config-router-scope-af-topo)# propagate-community <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 2 `；EOL ` RVA 0x344F1CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e)

### observed_connections-003028

```text
(config-router-scope-af-topo)# redistribute <?router_action_proc_vpn@555589a41ce8> <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-43c752bcf7ab1565](../../evidence/conditions-sets-027.md#c-43c752bcf7ab1565) · [缺口 G-66dd1beef999a123](../../evidence/gaps-sets-004.md#g-66dd1beef999a123) · [状态效果 S-f52582c86d1c6c09](../../evidence/state_effects-sets-052.md#s-f52582c86d1c6c09)

### observed_connections-003127

```text
(config-router-scope-af-topo)# redistribute <?router_action_proc_vpn@555589a41ce8> ip level-1 into level-1 route-map <string> <cr>
```

Handler ` RVA 0xCF982D0 `；selector ` 0 `；EOL ` RVA 0x344F0028 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the route-map。

[条件 C-d9656354783b3a1e](../../evidence/conditions-sets-084.md#c-d9656354783b3a1e) · [缺口 G-8ee484e7fdb4e942](../../evidence/gaps-sets-005.md#g-8ee484e7fdb4e942) · [参数 P-2a7f70cd81c29bdc](../../evidence/parameters-sets-004.md#p-2a7f70cd81c29bdc) · [状态效果 S-97821208426ae9ca](../../evidence/state_effects-sets-032.md#s-97821208426ae9ca)

### observed_connections-002760

```text
(config-router-scope-af-topo)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-008b692901c793c4](../../evidence/conditions-sets-001.md#c-008b692901c793c4) · [参数 P-370af228ff313968](../../evidence/parameters-sets-005.md#p-370af228ff313968) · [状态效果 S-b2b99e1d1aa16382](../../evidence/state_effects-sets-038.md#s-b2b99e1d1aa16382)

### observed_connections-003021

```text
(config-router-scope-af-topo)# rewrite-evpn-rt-asn <cr>
```

Handler ` RVA 0xF1D1BF0 `；selector ` 2 `；EOL ` RVA 0x344F1750 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7be2b8d9f03eda3c](../../evidence/conditions-sets-048.md#c-7be2b8d9f03eda3c) · [缺口 G-5da6cabfdb8f51fa](../../evidence/gaps-sets-004.md#g-5da6cabfdb8f51fa) · [状态效果 S-d5b4b51efd40c266](../../evidence/state_effects-sets-045.md#s-d5b4b51efd40c266)

### observed_connections-003029

```text
(config-router-scope-af-topo)# segment-routing mpls <cr>
```

Handler ` RVA 0xF1D18E0 `；selector ` 1 `；EOL ` RVA 0x344F2A18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6956c72ed80e07be](../../evidence/conditions-sets-041.md#c-6956c72ed80e07be) · [缺口 G-3e5c3a0543b88091](../../evidence/gaps-sets-003.md#g-3e5c3a0543b88091) · [状态效果 S-4892871c6c28135f](../../evidence/state_effects-sets-016.md#s-4892871c6c28135f)

### observed_connections-003030

```text
(config-router-scope-af-topo)# segment-routing srv6 <cr>
```

Handler ` RVA 0xF1D1950 `；selector ` 1 `；EOL ` RVA 0x344F2DB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2ec55ad9f6740988](../../evidence/conditions-sets-018.md#c-2ec55ad9f6740988) · [缺口 G-a2d7f2aabcedca1c](../../evidence/gaps-sets-006.md#g-a2d7f2aabcedca1c) · [状态效果 S-79d2a4723239d15d](../../evidence/state_effects-sets-026.md#s-79d2a4723239d15d)

### observed_connections-002701

```text
(config-router-scope-af-topo)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc)

### observed_connections-002976

```text
(config-router-scope-af-topo)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-7f44ea3d5ff83041](../../evidence/conditions-sets-049.md#c-7f44ea3d5ff83041) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-8642eb04023b2323](../../evidence/state_effects-sets-028.md#s-8642eb04023b2323)

### observed_connections-002970

```text
(config-router-scope-af-topo)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-6568ff0a78495959](../../evidence/conditions-sets-039.md#c-6568ff0a78495959) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-42394155f848a6f9](../../evidence/state_effects-sets-014.md#s-42394155f848a6f9)

### observed_connections-002745

```text
(config-router-scope-af-topo)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-2cd36336053d115f](../../evidence/conditions-sets-018.md#c-2cd36336053d115f) · [参数 P-aebe586c61a4934d](../../evidence/parameters-sets-013.md#p-aebe586c61a4934d) · [状态效果 S-51be2931b5b16e1a](../../evidence/state_effects-sets-018.md#s-51be2931b5b16e1a)

### observed_connections-002771

```text
(config-router-scope-af-topo)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x344ED118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-3f5e81debf9ca30a](../../evidence/conditions-sets-025.md#c-3f5e81debf9ca30a) · [参数 P-2ab214fd5050f81f](../../evidence/parameters-sets-004.md#p-2ab214fd5050f81f) · [状态效果 S-6aefcdce776de1ef](../../evidence/state_effects-sets-023.md#s-6aefcdce776de1ef)

### observed_connections-003027

```text
(config-router-scope-af-topo)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-c9a95e2f9286010e](../../evidence/conditions-sets-078.md#c-c9a95e2f9286010e) · [缺口 G-8d657be8f4b6b909](../../evidence/gaps-sets-005.md#g-8d657be8f4b6b909) · [参数 P-4966d35a3f81136e](../../evidence/parameters-sets-006.md#p-4966d35a3f81136e) · [状态效果 S-ddaa58c972f3b962](../../evidence/state_effects-sets-047.md#s-ddaa58c972f3b962)

### observed_connections-002667

```text
(config-router-scope-af-topo)# synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x345BAF38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6acc88802a133995](../../evidence/conditions-sets-041.md#c-6acc88802a133995)

### observed_connections-002700

```text
(config-router-scope-af-topo)# table-map <string> <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x345BB310 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-d8a152bea95e15fa](../../evidence/conditions-sets-083.md#c-d8a152bea95e15fa) · [参数 P-dbeb215e95e3f5de](../../evidence/parameters-sets-017.md#p-dbeb215e95e3f5de)

### observed_connections-003025

```text
(config-router-scope-af-topo)# version <number:1..2> <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x344EC5E8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` rip version 1 or 2。

[条件 C-b9114fade3a00434](../../evidence/conditions-sets-071.md#c-b9114fade3a00434) · [缺口 G-c310642ed2073d18](../../evidence/gaps-sets-007.md#g-c310642ed2073d18) · [参数 P-cd04afd216b634a6](../../evidence/parameters-sets-016.md#p-cd04afd216b634a6) · [状态效果 S-9422574c0010a7d3](../../evidence/state_effects-sets-031.md#s-9422574c0010a7d3)
