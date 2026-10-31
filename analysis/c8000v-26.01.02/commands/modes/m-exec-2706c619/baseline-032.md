# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-023526

```text
(exec)# do-exec test ip nat show pool all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 1 `；EOL ` RVA 0x347DDC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023576

```text
(exec)# do-exec test ip nat show rule <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 2 `；EOL ` RVA 0x347DE508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Rule name。

[条件 C-75bc5b06ca4e328f](../../evidence/conditions-sets-046.md#c-75bc5b06ca4e328f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-83418bd3b9811e31](../../evidence/parameters-sets-010.md#p-83418bd3b9811e31) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023543

```text
(exec)# do-exec test ip nat show rule all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 3 `；EOL ` RVA 0x347DE208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017273

```text
(exec)# do-exec test ip nat-route database <cr>
```

Handler ` RVA 0x13725FC0 `；selector ` 0 `；EOL ` RVA 0x35C0F330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8fcafefb75f4a92e](../../evidence/state_effects-sets-031.md#s-8fcafefb75f4a92e)

### path-021275

```text
(exec)# do-exec test ip nbar batch-config end <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 5 `；EOL ` RVA 0x35259330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021255

```text
(exec)# do-exec test ip nbar batch-config start <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 4 `；EOL ` RVA 0x35259088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021289

```text
(exec)# do-exec test ip nbar byte-count-window disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 9 `；EOL ` RVA 0x352596A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-672b47b842936a13](../../evidence/state_effects-sets-022.md#s-672b47b842936a13)

### path-021197

```text
(exec)# do-exec test ip nbar caches clear <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 29 `；EOL ` RVA 0x35255258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023480

```text
(exec)# do-exec test ip nbar caches export <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 28 `；EOL ` RVA 0x35254FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3b46f8fae4be42bd](../../evidence/parameters-sets-005.md#p-3b46f8fae4be42bd) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023469

```text
(exec)# do-exec test ip nbar caches import <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 27 `；EOL ` RVA 0x35254CF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-693dea4536eeb117](../../evidence/parameters-sets-008.md#p-693dea4536eeb117) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021212

```text
(exec)# do-exec test ip nbar caches show <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 30 `；EOL ` RVA 0x35255500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021299

```text
(exec)# do-exec test ip nbar cedge-simulation disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 11 `；EOL ` RVA 0x35259C80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021285

```text
(exec)# do-exec test ip nbar cedge-simulation enable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 10 `；EOL ` RVA 0x352599D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021205

```text
(exec)# do-exec test ip nbar config-mode async <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 8 `；EOL ` RVA 0x35257498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021219

```text
(exec)# do-exec test ip nbar config-mode sync <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 7 `；EOL ` RVA 0x35257740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024648

```text
(exec)# do-exec test ip nbar dataplane-info-monitor memory-thresholds low <number:1..100> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 14 `；EOL ` RVA 0x3525A618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Low threshold in percents。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2360135968ca2bc4](../../evidence/parameters-sets-003.md#p-2360135968ca2bc4) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023585

```text
(exec)# do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state false <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 12 `；EOL ` RVA 0x3525A290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023568

```text
(exec)# do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state true <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 13 `；EOL ` RVA 0x35259FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021235

```text
(exec)# do-exec test ip nbar function <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 6 `；EOL ` RVA 0x35257AA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Function name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4af9a509018bb542](../../evidence/parameters-sets-006.md#p-4af9a509018bb542) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021189

```text
(exec)# do-exec test ip nbar npc disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 19 `；EOL ` RVA 0x35255B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023490

```text
(exec)# do-exec test ip nbar npc enable <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 18 `；EOL ` RVA 0x352558E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b8c3dd324e3e92e2](../../evidence/parameters-sets-014.md#p-b8c3dd324e3e92e2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023501

```text
(exec)# do-exec test ip nbar npc pack-mode allow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 21 `；EOL ` RVA 0x35256120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023510

```text
(exec)# do-exec test ip nbar npc pack-mode disallow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 22 `；EOL ` RVA 0x352563C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021209

```text
(exec)# do-exec test ip nbar npc save <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 20 `；EOL ` RVA 0x35255E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021312

```text
(exec)# do-exec test ip nbar set-max-protocol-id-no-cloud_ext <number:0..32767> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 15 `；EOL ` RVA 0x3525A950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` max protocol id without cloud extension。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-507a9096f4509329](../../evidence/parameters-sets-007.md#p-507a9096f4509329) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023595

```text
(exec)# do-exec test ip nbar set-protocol-feature-support <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 16 `；EOL ` RVA 0x3525AC88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Feature id；` unsigned_number ` Feature value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bdb8d401bdc33739](../../evidence/parameters-sets-014.md#p-bdb8d401bdc33739) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017431

```text
(exec)# do-exec test ip nbar show-features-activation <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 17 `；EOL ` RVA 0x3525AF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017409

```text
(exec)# do-exec test ip nbar show-fib-ad-info <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 31 `；EOL ` RVA 0x3525BA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021207

```text
(exec)# do-exec test ip nbar track-ip disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 24 `；EOL ` RVA 0x35256C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025254

```text
(exec)# do-exec test ip nbar track-ip enable <string> port <number:0..4294967295> vrf-id <number:0..4294967295> l4-proto <number:0..255> memory-size <number:0..20000> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 23 `；EOL ` RVA 0x35256978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv4/v6 to track；` unsigned_number ` port number；` unsigned_number ` VRF id；` unsigned_number ` L4 Protocol；` unsigned_number ` memory size in KB。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-74d155980cc4da67](../../evidence/parameters-sets-009.md#p-74d155980cc4da67) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021221

```text
(exec)# do-exec test ip nbar track-ip flush <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 25 `；EOL ` RVA 0x35256ED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021231

```text
(exec)# do-exec test ip nbar track-ip status <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 26 `；EOL ` RVA 0x35257180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017283

```text
(exec)# do-exec test ip omp flush <cr>
```

Handler ` RVA 0x137422E0 `；selector ` 0 `；EOL ` RVA 0x35C105C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-336c162ed488efdc](../../evidence/conditions-sets-020.md#c-336c162ed488efdc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a01e4c8b1df64af2](../../evidence/state_effects-sets-034.md#s-a01e4c8b1df64af2)

### path-021139

```text
(exec)# do-exec test ip pbr ipv6 attach <cr>
```

Handler ` RVA 0x10C6E4E0 `；selector ` 0 `；EOL ` RVA 0x34CF0520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5ec6ae704382b2d](../../evidence/conditions-sets-064.md#c-a5ec6ae704382b2d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a47d0de82aca1764](../../evidence/state_effects-sets-035.md#s-a47d0de82aca1764)

### path-021122

```text
(exec)# do-exec test ip pbr map <string> <cr>
```

Handler ` RVA 0x10C6E570 `；selector ` 0 `；EOL ` RVA 0x34CF0228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` PBR route-map name。

[条件 C-a5ec6ae704382b2d](../../evidence/conditions-sets-064.md#c-a5ec6ae704382b2d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e93b53fee09f3a16](../../evidence/parameters-sets-017.md#p-e93b53fee09f3a16) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021230

```text
(exec)# do-exec test ip rib api iprib_geteachroute <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 2 `；EOL ` RVA 0x3423BD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-362ce9cdb232149c](../../evidence/state_effects-sets-012.md#s-362ce9cdb232149c)

### path-013445

```text
(exec)# do-exec test ip rmap <cr>
```

Handler ` RVA 0xE207640 `；selector ` 0 `；EOL ` RVA 0x3423B1B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9c201c42927af4b3](../../evidence/conditions-sets-060.md#c-9c201c42927af4b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023470

```text
(exec)# do-exec test ip rmap batch-commit <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE208090 `；selector ` 0 `；EOL ` RVA 0x34234C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify rmapHandle；` unsigned_number ` Application: 1 - AAA。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ab77153375655df9](../../evidence/parameters-sets-013.md#p-ab77153375655df9) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023491

```text
(exec)# do-exec test ip rmap create <number:0..2147483647> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x34234FA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0a14d68c1ec1aa26](../../evidence/parameters-sets-001.md#p-0a14d68c1ec1aa26) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023536

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3423A5F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-6ed09e80c8297b9c](../../evidence/conditions-sets-043.md#c-6ed09e80c8297b9c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025125

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0xE203110 `；selector ` 0 `；EOL ` RVA 0x342357B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-272ac774548295cd](../../evidence/parameters-sets-003.md#p-272ac774548295cd) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025199

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> match destination tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 2 `；EOL ` RVA 0x34236208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` dgt id value。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6d91a93fa721550c](../../evidence/parameters-sets-009.md#p-6d91a93fa721550c) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025196

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x34235B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-937ae3c156e0cb63](../../evidence/parameters-sets-011.md#p-937ae3c156e0cb63) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025198

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> match source tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 1 `；EOL ` RVA 0x34235EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Security id value。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4ef7f2833cf942dd](../../evidence/parameters-sets-007.md#p-4ef7f2833cf942dd) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025128

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> match vrf <string> <cr>
```

Handler ` RVA 0xE2033E0 `；selector ` 0 `；EOL ` RVA 0x342364E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7568d67122bab58a](../../evidence/parameters-sets-009.md#p-7568d67122bab58a) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025138

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set color red <cr>
```

Handler ` RVA 0xE203F30 `；selector ` 0 `；EOL ` RVA 0x3423A160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-b503777d087c83f6](../../evidence/conditions-sets-070.md#c-b503777d087c83f6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-a7a8ff032c12b6d3](../../evidence/state_effects-sets-035.md#s-a7a8ff032c12b6d3)

### path-025130

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-global-nh <address> <cr>
```

Handler ` RVA 0xE205C50 `；selector ` 0 `；EOL ` RVA 0x34237A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ea7c91e852d793a4](../../evidence/parameters-sets-018.md#p-ea7c91e852d793a4) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025132

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-next-hop <address> <cr>
```

Handler ` RVA 0xE2059B0 `；selector ` 0 `；EOL ` RVA 0x34238050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of default next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b3295dd415de6554](../../evidence/parameters-sets-014.md#p-b3295dd415de6554) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-024988

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-nh-verify <cr>
```

Handler ` RVA 0xE205720 `；selector ` 0 `；EOL ` RVA 0x342382D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025202

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE205EF0 `；selector ` 0 `；EOL ` RVA 0x34237D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6835e23ae0bf3d34](../../evidence/parameters-sets-008.md#p-6835e23ae0bf3d34) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025136

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set df <number:0..65535> <cr>
```

Handler ` RVA 0xE204F40 `；selector ` 0 `；EOL ` RVA 0x34238BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of df。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-06c275ebd6daa0a6](../../evidence/parameters-sets-001.md#p-06c275ebd6daa0a6) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025126

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set gateway <address> <cr>
```

Handler ` RVA 0xE206C40 `；selector ` 0 `；EOL ` RVA 0x34236890 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of gateway。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e729039b021e96f0](../../evidence/parameters-sets-017.md#p-e729039b021e96f0) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025001

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x34239130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025197

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set gw-vrf <string> <address> <cr>
```

Handler ` RVA 0xE206EE0 `；selector ` 0 `；EOL ` RVA 0x34236BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of gateway。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2acbe67311ea0ecd](../../evidence/parameters-sets-004.md#p-2acbe67311ea0ecd) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025129

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set ip-global-nh <address> <cr>
```

Handler ` RVA 0xE2066E0 `；selector ` 0 `；EOL ` RVA 0x34237430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b63ee37da7e7cdd4](../../evidence/parameters-sets-014.md#p-b63ee37da7e7cdd4) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025201

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set ip-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE206980 `；selector ` 0 `；EOL ` RVA 0x34237758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ceeec3d0d198abf4](../../evidence/parameters-sets-016.md#p-ceeec3d0d198abf4) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025127

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0xE206440 `；selector ` 0 `；EOL ` RVA 0x34236EA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ac5b408e00df8dee](../../evidence/parameters-sets-013.md#p-ac5b408e00df8dee) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-024981

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set nh-verify <cr>
```

Handler ` RVA 0xE2061B0 `；selector ` 0 `；EOL ` RVA 0x34237120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025135

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set precedence <number:0..65535> <cr>
```

Handler ` RVA 0xE2051E0 `；selector ` 0 `；EOL ` RVA 0x342388D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c55c967820bd003f](../../evidence/parameters-sets-015.md#p-c55c967820bd003f) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025134

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set tos <number:0..65535> <cr>
```

Handler ` RVA 0xE205480 `；selector ` 0 `；EOL ` RVA 0x342385E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of tos。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4dce7f6ad2f960e0](../../evidence/parameters-sets-006.md#p-4dce7f6ad2f960e0) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-025137

```text
(exec)# do-exec test ip rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x34238EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e80fe2c3ff0d0f92](../../evidence/parameters-sets-017.md#p-e80fe2c3ff0d0f92) · [状态效果 S-5e5a56346e9a7de4](../../evidence/state_effects-sets-020.md#s-5e5a56346e9a7de4)

### path-023522

```text
(exec)# do-exec test ip rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3423A900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-55050655b3d5bb05](../../evidence/parameters-sets-007.md#p-55050655b3d5bb05) · [状态效果 S-b1f7b7c5a06082e8](../../evidence/state_effects-sets-038.md#s-b1f7b7c5a06082e8)

### path-021137

```text
(exec)# do-exec test ip rmap register <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x34234888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7f8a93636669cf1c](../../evidence/parameters-sets-010.md#p-7f8a93636669cf1c) · [状态效果 S-2bed534f493a6122](../../evidence/state_effects-sets-010.md#s-2bed534f493a6122)

### path-023485

```text
(exec)# do-exec test ip rmap remove <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x342352F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c35ad9aae5dc6839](../../evidence/parameters-sets-015.md#p-c35ad9aae5dc6839) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017343

```text
(exec)# do-exec test ip subscriber enable <cr>
```

Handler ` RVA 0x11A36370 `；selector ` 0 `；EOL ` RVA 0x355CF310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c6eed75834655e7](../../evidence/conditions-sets-030.md#c-4c6eed75834655e7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae40e8353ff1c592](../../evidence/state_effects-sets-037.md#s-ae40e8353ff1c592)

### path-023611

```text
(exec)# do-exec test ip subscriber interface association disable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 0 `；EOL ` RVA 0x355CF9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5496f91ad28240b3](../../evidence/conditions-sets-033.md#c-5496f91ad28240b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023610

```text
(exec)# do-exec test ip subscriber interface association enable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 1 `；EOL ` RVA 0x355CF740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-26b516dec827fb73](../../evidence/conditions-sets-015.md#c-26b516dec827fb73) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022010

```text
(exec)# do-exec test ipc FC <number:1..5> <number:0..50000> <cr>
```

Handler ` RVA 0xD3C63E0 `；selector ` 0 `；EOL ` RVA 0x33E33C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` threshold type；` unsigned_number ` Value。

[条件 C-f6a85b179112fa5b](../../evidence/conditions-sets-095.md#c-f6a85b179112fa5b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-569822aca9aeb7ed](../../evidence/parameters-sets-007.md#p-569822aca9aeb7ed) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018349

```text
(exec)# do-exec test ipc ack-drop <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6310 `；selector ` 0 `；EOL ` RVA 0x33E33138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` state。

[条件 C-732f7f082f4d9286](../../evidence/conditions-sets-045.md#c-732f7f082f4d9286) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-58b2f2cef5d5926b](../../evidence/parameters-sets-007.md#p-58b2f2cef5d5926b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018375

```text
(exec)# do-exec test ipc ack-pending <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6260 `；selector ` 0 `；EOL ` RVA 0x33E334C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` state。

[条件 C-cef75ef4b257cda1](../../evidence/conditions-sets-080.md#c-cef75ef4b257cda1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8a3569dabade40fa](../../evidence/parameters-sets-011.md#p-8a3569dabade40fa) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019013

```text
(exec)# do-exec test ipc ack-timer <number:0..50000> <cr>
```

Handler ` RVA 0xD3C65C0 `；selector ` 0 `；EOL ` RVA 0x33E3B6D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-90be1626a3d9d9fe](../../evidence/parameters-sets-011.md#p-90be1626a3d9d9fe) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014412

```text
(exec)# do-exec test ipc api <cr>
```

Handler ` RVA 0xD3C1A60 `；selector ` 0 `；EOL ` RVA 0x33E33EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014665

```text
(exec)# do-exec test ipc app-send <cr>
```

Handler ` RVA 0xD3C5F70 `；selector ` 0 `；EOL ` RVA 0x33E36440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024205

```text
(exec)# do-exec test ipc bundle mode seat on <cr>
```

Handler ` RVA 0xD3C4B50 `；selector ` 0 `；EOL ` RVA 0x33E3B080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-842b66e1c946bd30](../../evidence/state_effects-sets-028.md#s-842b66e1c946bd30)

### path-024195

```text
(exec)# do-exec test ipc bundle mode session on <cr>
```

Handler ` RVA 0xD3C4A80 `；selector ` 0 `；EOL ` RVA 0x33E3AD48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6d6c4c1c7c635d8c](../../evidence/state_effects-sets-023.md#s-6d6c4c1c7c635d8c)

### path-025065

```text
(exec)# do-exec test ipc bundle status seat <number:0..4294967295> seat-level on <cr>
```

Handler ` RVA 0xD3C4E20 `；selector ` 0 `；EOL ` RVA 0x33E3A950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a3276e418678fa92](../../evidence/parameters-sets-012.md#p-a3276e418678fa92) · [状态效果 S-26861b54bbff2680](../../evidence/state_effects-sets-009.md#s-26861b54bbff2680)

### path-025067

```text
(exec)# do-exec test ipc bundle status session <number:0..4294967295> <number:0..65535> on <cr>
```

Handler ` RVA 0xD3C4C20 `；selector ` 0 `；EOL ` RVA 0x33E3A570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-67bb089c8c087a64](../../evidence/parameters-sets-008.md#p-67bb089c8c087a64) · [状态效果 S-a87e279bdbe14c1f](../../evidence/state_effects-sets-036.md#s-a87e279bdbe14c1f)

### path-014515

```text
(exec)# do-exec test ipc callback <cr>
```

Handler ` RVA 0xD3C28E0 `；selector ` 0 `；EOL ` RVA 0x33E35280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014647

```text
(exec)# do-exec test ipc diag <cr>
```

Handler ` RVA 0xD3C50D0 `；selector ` 0 `；EOL ` RVA 0x33E36708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018399

```text
(exec)# do-exec test ipc driver stop <cr>
```

Handler ` RVA 0xD3FF9D0 `；selector ` 0 `；EOL ` RVA 0x33E41AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-67089e709fb5bf53](../../evidence/conditions-sets-040.md#c-67089e709fb5bf53) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5760015351b35725](../../evidence/state_effects-sets-019.md#s-5760015351b35725)

### path-018474

```text
(exec)# do-exec test ipc drop <number:0..9999> <cr>
```

Handler ` RVA 0xD3C1990 `；selector ` 0 `；EOL ` RVA 0x33E34468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` n: drop every nth packet sent; n=0 for no dropping。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-95af16f3e49d885d](../../evidence/parameters-sets-011.md#p-95af16f3e49d885d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024827

```text
(exec)# do-exec test ipc drop ack <number:65540..4294967295> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C1860 `；selector ` 0 `；EOL ` RVA 0x33E34A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port id；` unsigned_number ` Session id；` unsigned_number ` Number of ACKs to drop。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-71a0b4089b1449b0](../../evidence/parameters-sets-009.md#p-71a0b4089b1449b0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018503

```text
(exec)# do-exec test ipc drop next <cr>
```

Handler ` RVA 0xD3C1930 `；selector ` 0 `；EOL ` RVA 0x33E34718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024811

```text
(exec)# do-exec test ipc mcast appclass subscribe <string> <number:0..15> <cr>
```

Handler ` RVA 0xD452370 `；selector ` 0 `；EOL ` RVA 0x33E44940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-43a6c12fa7a112c4](../../evidence/parameters-sets-006.md#p-43a6c12fa7a112c4) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024828

```text
(exec)# do-exec test ipc mcast group close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD452A50 `；selector ` 0 `；EOL ` RVA 0x33E473E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` session id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5c89ea6d871c9a6c](../../evidence/parameters-sets-007.md#p-5c89ea6d871c9a6c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025054

```text
(exec)# do-exec test ipc mcast group create <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453670 `；selector ` 0 `；EOL ` RVA 0x33E45A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1dc629c309feb0c9](../../evidence/parameters-sets-003.md#p-1dc629c309feb0c9) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024823

```text
(exec)# do-exec test ipc mcast group locate <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453280 `；selector ` 0 `；EOL ` RVA 0x33E46438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-acb97f54bcda4b49](../../evidence/parameters-sets-013.md#p-acb97f54bcda4b49) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025057

```text
(exec)# do-exec test ipc mcast group member add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452C20 `；selector ` 0 `；EOL ` RVA 0x33E46F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` member id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7e52d3e5b9cd8270](../../evidence/parameters-sets-010.md#p-7e52d3e5b9cd8270) · [状态效果 S-804ef8684b82dc53](../../evidence/state_effects-sets-027.md#s-804ef8684b82dc53)

### path-024829

```text
(exec)# do-exec test ipc mcast group open <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD452570 `；selector ` 0 `；EOL ` RVA 0x33E477F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` mode of group open(1. reliable 2. unreliable)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-64e154c7c2bb31ab](../../evidence/parameters-sets-008.md#p-64e154c7c2bb31ab) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024069

```text
(exec)# do-exec test ipc mcast group remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452EE0 `；selector ` 0 `；EOL ` RVA 0x33E46B40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-87c59ea63b268029](../../evidence/parameters-sets-010.md#p-87c59ea63b268029) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024817

```text
(exec)# do-exec test ipc mcast group reserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD4533E0 `；selector ` 0 `；EOL ` RVA 0x33E45DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d67325ad12ec381b](../../evidence/parameters-sets-016.md#p-d67325ad12ec381b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025055

```text
(exec)# do-exec test ipc mcast group subscribe <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453040 `；selector ` 0 `；EOL ` RVA 0x33E467F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d154cfe91c8424b2](../../evidence/parameters-sets-016.md#p-d154cfe91c8424b2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024821

```text
(exec)# do-exec test ipc mcast group unreserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453540 `；selector ` 0 `；EOL ` RVA 0x33E46108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4cbd93331c44b6dc](../../evidence/parameters-sets-006.md#p-4cbd93331c44b6dc) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024822

```text
(exec)# do-exec test ipc mcast platform emulation <number:0..4294967295> disable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 0 `；EOL ` RVA 0x33E45560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024818

```text
(exec)# do-exec test ipc mcast platform emulation <number:0..4294967295> enable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 1 `；EOL ` RVA 0x33E452B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024814

```text
(exec)# do-exec test ipc mcast platform max-groups <number:0..15> <number:0..65535> <cr>
```

Handler ` RVA 0xD453D60 `；selector ` 0 `；EOL ` RVA 0x33E44FA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` zone number；` unsigned_number ` max group count。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-784d9380b4381ff2](../../evidence/parameters-sets-009.md#p-784d9380b4381ff2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021968

```text
(exec)# do-exec test ipc mcast platform registries <cr>
```

Handler ` RVA 0xD453E30 `；selector ` 0 `；EOL ` RVA 0x33E44C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014581

```text
(exec)# do-exec test ipc misc <cr>
```

Handler ` RVA 0xD3C40D0 `；selector ` 0 `；EOL ` RVA 0x33E35E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018900

```text
(exec)# do-exec test ipc ping <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C4640 `；selector ` 0 `；EOL ` RVA 0x33E3A0A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e106634c2595c7c8](../../evidence/parameters-sets-017.md#p-e106634c2595c7c8) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024206

```text
(exec)# do-exec test ipc port close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C8D40 `；selector ` 0 `；EOL ` RVA 0x33E38F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-53b2dab481ba7761](../../evidence/parameters-sets-007.md#p-53b2dab481ba7761) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024221

```text
(exec)# do-exec test ipc port create <string> <number:1..3> <cr>
```

Handler ` RVA 0xD3C7F80 `；selector ` 0 `；EOL ` RVA 0x33E37500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` port name；` unsigned_number ` method of message reception(1. callback 2. fast callback 3. queue)。

[条件 C-da4262f7637e28ed](../../evidence/conditions-sets-084.md#c-da4262f7637e28ed) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-127dda5a32adb5cf](../../evidence/parameters-sets-002.md#p-127dda5a32adb5cf) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024249

```text
(exec)# do-exec test ipc port free <number:0..4294967295> <number:1..1000000> <cr>
```

Handler ` RVA 0xD3C8FA0 `；selector ` 0 `；EOL ` RVA 0x33E39A10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` Number of messages。

[条件 C-2e07d5ccaf018ad8](../../evidence/conditions-sets-018.md#c-2e07d5ccaf018ad8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cbcec36820e3d032](../../evidence/parameters-sets-015.md#p-cbcec36820e3d032) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025162

```text
(exec)# do-exec test ipc port msend <number:0..4294967295> <number:0..65535> <number:0..65535> <number:1..1000000> <number:1..4064> <cr>
```

Handler ` RVA 0xD3C8300 `；selector ` 0 `；EOL ` RVA 0x33E38040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` start session id；` unsigned_number ` end session id；` unsigned_number ` number of messages to be sent；` unsigned_number ` size of message。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-78d8a152dee698ee](../../evidence/parameters-sets-009.md#p-78d8a152dee698ee) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022345

```text
(exec)# do-exec test ipc port notify enable <cr>
```

Handler ` RVA 0xD3C8F00 `；selector ` 0 `；EOL ` RVA 0x33E395B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37b8f438a3e51489](../../evidence/state_effects-sets-012.md#s-37b8f438a3e51489)

### path-024235

```text
(exec)# do-exec test ipc port open <number:0..4294967295> <number:1..3> <cr>
```

Handler ` RVA 0xD3C80F0 `；selector ` 0 `；EOL ` RVA 0x33E37A98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` mode of port open(1. reliable 2. unreliable 3. unrel-with-not)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d00235038e651bbb](../../evidence/parameters-sets-016.md#p-d00235038e651bbb) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022348

```text
(exec)# do-exec test ipc port remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C8DC0 `；selector ` 0 `；EOL ` RVA 0x33E392B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` port id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a00f33de364d076f](../../evidence/parameters-sets-012.md#p-a00f33de364d076f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022375

```text
(exec)# do-exec test ipc port send header <cr>
```

Handler ` RVA 0xD3C8890 `；selector ` 0 `；EOL ` RVA 0x33E38678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba078f8950c2bf1b](../../evidence/conditions-sets-072.md#c-ba078f8950c2bf1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8022e2086982deca](../../evidence/state_effects-sets-027.md#s-8022e2086982deca)

### path-014491

```text
(exec)# do-exec test ipc queue <cr>
```

Handler ` RVA 0xD3C2330 `；selector ` 0 `；EOL ` RVA 0x33E34FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018976

```text
(exec)# do-exec test ipc retry-period <number:0..50000> <cr>
```

Handler ` RVA 0xD3C6520 `；selector ` 0 `；EOL ` RVA 0x33E3B410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8966cb03db7d6b54](../../evidence/parameters-sets-011.md#p-8966cb03db7d6b54) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014589

```text
(exec)# do-exec test ipc rpc <cr>
```

Handler ` RVA 0xD3C1DE0 `；selector ` 0 `；EOL ` RVA 0x33E358B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024812

```text
(exec)# do-exec test ipc ru create <string> <number:1..15> conf <cr>
```

Handler ` RVA 0xD3FEFE0 `；selector ` 0 `；EOL ` RVA 0x33E40F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPC RU name；` unsigned_number ` Priority of IPC RU。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-799b680ccf4bb802](../../evidence/parameters-sets-009.md#p-799b680ccf4bb802) · [状态效果 S-14085dabaaf46e81](../../evidence/state_effects-sets-005.md#s-14085dabaaf46e81)

### path-021994

```text
(exec)# do-exec test ipc ru remove <string> <cr>
```

Handler ` RVA 0xD3FF380 `；selector ` 0 `；EOL ` RVA 0x33E412F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPC RU id to be removed(in hex)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d52691dd1900e41d](../../evidence/parameters-sets-016.md#p-d52691dd1900e41d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025157

```text
(exec)# do-exec test ipc ru tune-thresh <string> <number:1..6> rising major <number:0..10000> <cr>
```

Handler ` RVA 0xD3FF5E0 `；selector ` 0 `；EOL ` RVA 0x33E41728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPC RU id(in hex) whose threshold need to be tuned；` unsigned_number ` Entity to be thresholded: 1. Tx Session Usage 2. Rx Session Usage 3. Rx Port Usage 4. RU Usage 5. Reliable Session ACK pending 6. Seat level ACK pending ；` unsigned_number ` New threshold value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8d1eaef814f1e8b7](../../evidence/parameters-sets-011.md#p-8d1eaef814f1e8b7) · [状态效果 S-e969b2dff12a8672](../../evidence/state_effects-sets-049.md#s-e969b2dff12a8672)

### path-018398

```text
(exec)# do-exec test ipc seat-fc <number:0..1024> <cr>
```

Handler ` RVA 0xD3C61B0 `；selector ` 0 `；EOL ` RVA 0x33E33848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` state。

[条件 C-8fa375cafcd67fe5](../../evidence/conditions-sets-056.md#c-8fa375cafcd67fe5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c3cdd8e9175bec8d](../../evidence/parameters-sets-015.md#p-c3cdd8e9175bec8d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022225

```text
(exec)# do-exec test ipc size <number:0..100000> <number:0..1000> <cr>
```

Handler ` RVA 0xD3C3720 `；selector ` 0 `；EOL ` RVA 0x33E39DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IPC packet size；` unsigned_number ` Number of IPC packet。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-646aa7c03b43ab31](../../evidence/parameters-sets-008.md#p-646aa7c03b43ab31) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014432

```text
(exec)# do-exec test ipc slavecore <cr>
```

Handler ` RVA 0xD3C3CC0 `；selector ` 0 `；EOL ` RVA 0x33E34158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014469

```text
(exec)# do-exec test ipc slavelog <cr>
```

Handler ` RVA 0xD3C3D00 `；selector ` 0 `；EOL ` RVA 0x33E34D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014563

```text
(exec)# do-exec test ipc speed <cr>
```

Handler ` RVA 0xD3C3840 `；selector ` 0 `；EOL ` RVA 0x33E35B68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014607

```text
(exec)# do-exec test ipc split-init <cr>
```

Handler ` RVA 0xD3C1330 `；selector ` 0 `；EOL ` RVA 0x33E360B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014535

```text
(exec)# do-exec test ipc task-pool <cr>
```

Handler ` RVA 0xD3C2D00 `；selector ` 0 `；EOL ` RVA 0x33E35528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014346

```text
(exec)# do-exec test ipc toggle-mask-error <cr>
```

Handler ` RVA 0xD3FFA80 `；selector ` 0 `；EOL ` RVA 0x33E40B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024825

```text
(exec)# do-exec test ipc traffic <number:0..4294967295> <number:1..2147483647> <number:1..5> <number:1..50000> <cr>
```

Handler ` RVA 0xD3C5290 `；selector ` 0 `；EOL ` RVA 0x33E32570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Destination Seat ID or Port ID；` unsigned_number ` Number of messages to be sent；` unsigned_number `  1 - Unreliable 2 - Reliable Non-blocking 3 - RPC blocking 4 - Reliable Non-Blocking and Final Blocked 5 - Reliable Blocking；` unsigned_number ` Size of each IPC message。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8ec07d117ce331bc](../../evidence/parameters-sets-011.md#p-8ec07d117ce331bc) · [状态效果 S-5b42fa260bf424a2](../../evidence/state_effects-sets-020.md#s-5b42fa260bf424a2)

### path-021956

```text
(exec)# do-exec test ipc traffic abort <number:0..2147483647> <cr>
```

Handler ` RVA 0xD3C5D40 `；selector ` 0 `；EOL ` RVA 0x33E32A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` The process id which is sending the traffic。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-116ec98253371dfa](../../evidence/parameters-sets-002.md#p-116ec98253371dfa) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018803

```text
(exec)# do-exec test ipc watermark callback <cr>
```

Handler ` RVA 0xD3C6050 `；selector ` 0 `；EOL ` RVA 0x33E36F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018322

```text
(exec)# do-exec test ipc window-size <number:32..1024> <cr>
```

Handler ` RVA 0xD3C5130 `；selector ` 0 `；EOL ` RVA 0x33E32DB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` window-size。

[条件 C-0221e2aa7e8f9b9b](../../evidence/conditions-sets-001.md#c-0221e2aa7e8f9b9b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a42b339d50af46ca](../../evidence/parameters-sets-013.md#p-a42b339d50af46ca) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022180

```text
(exec)# do-exec test ipc zone seat2slave <number:2..15> <cr>
```

Handler ` RVA 0xD3C79C0 `；selector ` 0 `；EOL ` RVA 0x33E36A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-11ee00fec1791900](../../evidence/parameters-sets-002.md#p-11ee00fec1791900) · [状态效果 S-d5ecfc0059a714c1](../../evidence/state_effects-sets-045.md#s-d5ecfc0059a714c1)

### path-021454

```text
(exec)# do-exec test ipv6 access-list common enable <cr>
```

Handler ` RVA 0x12166310 `；selector ` 0 `；EOL ` RVA 0x357B0D38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-48d509607dca2c7a](../../evidence/state_effects-sets-016.md#s-48d509607dca2c7a)

### path-023703

```text
(exec)# do-exec test ipv6 dhcp-client lease-query address <address> <cr>
```

Handler ` RVA 0x12189610 `；selector ` 0 `；EOL ` RVA 0x357BD0A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-486f1516edce2b17](../../evidence/parameters-sets-006.md#p-486f1516edce2b17) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017480

```text
(exec)# do-exec test ipv6 dhcp-relay bulk-lease-query <cr>
```

Handler ` RVA 0x121AF430 `；selector ` 0 `；EOL ` RVA 0x357C3B48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017522

```text
(exec)# do-exec test ipv6 dhcp-relay ldra <cr>
```

Handler ` RVA 0x121AE630 `；selector ` 0 `；EOL ` RVA 0x357C3E30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021439

```text
(exec)# do-exec test ipv6 dhcp-server hostnum <number:0..4294967295> <cr>
```

Handler ` RVA 0x121D2540 `；selector ` 0 `；EOL ` RVA 0x357CED60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 32 bit host number in hex。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e77823c1af7cfc82](../../evidence/parameters-sets-017.md#p-e77823c1af7cfc82) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023753

```text
(exec)# do-exec test ipv6 nd client del <number:0..15> <cr>
```

Handler ` RVA 0x1231B440 `；selector ` 0 `；EOL ` RVA 0x357FCA70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bd545017980207cf](../../evidence/parameters-sets-014.md#p-bd545017980207cf) · [状态效果 S-9331b3a929971c11](../../evidence/state_effects-sets-031.md#s-9331b3a929971c11)

### path-021420

```text
(exec)# do-exec test ipv6 nd pd-limit <number:0..2147483647> <cr>
```

Handler ` RVA 0x123198C0 `；selector ` 0 `；EOL ` RVA 0x357FBA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-defb6b1a96e6831a](../../evidence/parameters-sets-017.md#p-defb6b1a96e6831a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023686

```text
(exec)# do-exec test ipv6 nd repopulate queue-size <number:1..512> <cr>
```

Handler ` RVA 0x123197B0 `；selector ` 0 `；EOL ` RVA 0x357FBD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Queue size。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6970d6f8d867e4bf](../../evidence/parameters-sets-008.md#p-6970d6f8d867e4bf) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017443

```text
(exec)# do-exec test ipv6 nd test-nsf <cr>
```

Handler ` RVA 0x12319920 `；selector ` 0 `；EOL ` RVA 0x357FB260 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021492

```text
(exec)# do-exec test ipv6 rib multicast add <cr>
```

Handler ` RVA 0x1230B6E0 `；selector ` 0 `；EOL ` RVA 0x357ECD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a9221de4cc56d913](../../evidence/conditions-sets-065.md#c-a9221de4cc56d913) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6330e8e28ca03203](../../evidence/state_effects-sets-021.md#s-6330e8e28ca03203)

### path-024998

```text
(exec)# do-exec test ipv6 rib pdb add <number:1..16> <number:1..255> <number:0..1> <cr>
```

Handler ` RVA 0x1230B4F0 `；selector ` 0 `；EOL ` RVA 0x357ED4E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ebee9a394e927907](../../evidence/parameters-sets-018.md#p-ebee9a394e927907) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023652

```text
(exec)# do-exec test ipv6 rib pdb del <number:1..16> <cr>
```

Handler ` RVA 0x1230B640 `；selector ` 0 `；EOL ` RVA 0x357ED140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4d58cc23e6e79a5d](../../evidence/parameters-sets-006.md#p-4d58cc23e6e79a5d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021351

```text
(exec)# do-exec test ipv6 rib queue start <cr>
```

Handler ` RVA 0x1230B430 `；selector ` 0 `；EOL ` RVA 0x357EC420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b26c1e73d57e482b](../../evidence/state_effects-sets-038.md#s-b26c1e73d57e482b)

### path-021368

```text
(exec)# do-exec test ipv6 rib suspend start <cr>
```

Handler ` RVA 0x1230B490 `；selector ` 0 `；EOL ` RVA 0x357EC780 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-97446d4d29ef6b5f](../../evidence/state_effects-sets-032.md#s-97446d4d29ef6b5f)

### path-023752

```text
(exec)# do-exec test ipv6 rmap create <number:1..7> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x3559CF80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-700266de357f47fd](../../evidence/parameters-sets-009.md#p-700266de357f47fd) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023847

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3559EEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-2e45070c430f0ff6](../../evidence/conditions-sets-018.md#c-2e45070c430f0ff6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-025140

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0x118BCAF0 `；selector ` 0 `；EOL ` RVA 0x3559D768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-131b5c4417a1f1af](../../evidence/parameters-sets-002.md#p-131b5c4417a1f1af) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-025210

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x3559DA70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-43c97c6f77edf50d](../../evidence/parameters-sets-006.md#p-43c97c6f77edf50d) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-025027

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x3559E720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-025142

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0x118BCDA0 `；selector ` 0 `；EOL ` RVA 0x3559DE00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IPv6 address of next-hop。

[条件 C-f111621d7996149d](../../evidence/conditions-sets-093.md#c-f111621d7996149d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9c64443c07b0a179](../../evidence/parameters-sets-012.md#p-9c64443c07b0a179) · [状态效果 S-53a8976cffabceda](../../evidence/state_effects-sets-018.md#s-53a8976cffabceda)

### path-025144

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set precedence <number:0..7> <cr>
```

Handler ` RVA 0x118BD130 `；selector ` 0 `；EOL ` RVA 0x3559E1B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ce115e51ed785080](../../evidence/parameters-sets-016.md#p-ce115e51ed785080) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-025146

```text
(exec)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x3559E4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0f25ae5261c5ab19](../../evidence/parameters-sets-002.md#p-0f25ae5261c5ab19) · [状态效果 S-ec5fe50039fcd078](../../evidence/state_effects-sets-050.md#s-ec5fe50039fcd078)

### path-023807

```text
(exec)# do-exec test ipv6 rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3559F180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-afea805b9cc43465](../../evidence/parameters-sets-013.md#p-afea805b9cc43465) · [状态效果 S-a28d4ef51c89abd5](../../evidence/state_effects-sets-034.md#s-a28d4ef51c89abd5)

### path-021473

```text
(exec)# do-exec test ipv6 rmap register <number:1..7> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x3559CBF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ffc4586fce516f90](../../evidence/parameters-sets-019.md#p-ffc4586fce516f90) · [状态效果 S-95f500a1acc2b168](../../evidence/state_effects-sets-032.md#s-95f500a1acc2b168)

### path-023769

```text
(exec)# do-exec test ipv6 rmap remove <string> <number:1..7> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x3559D2A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6ee64968fd4901d6](../../evidence/parameters-sets-009.md#p-6ee64968fd4901d6) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021384

```text
(exec)# do-exec test ipv6 static limit <number:0..32> <cr>
```

Handler ` RVA 0x12310D00 `；selector ` 0 `；EOL ` RVA 0x357F0F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f007846cc54b8f35](../../evidence/parameters-sets-018.md#p-f007846cc54b8f35) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017419

```text
(exec)# do-exec test ipv6 static policy <cr>
```

Handler ` RVA 0x12310CC0 `；selector ` 0 `；EOL ` RVA 0x357F0CA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017828

```text
(exec)# do-exec test isis clear counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 5 `；EOL ` RVA 0x34B792E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013851

```text
(exec)# do-exec test isis debug <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 0 `；EOL ` RVA 0x34B78708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017833

```text
(exec)# do-exec test isis ip address <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 3 `；EOL ` RVA 0x34B78F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023968

```text
(exec)# do-exec test isis lsp advertise lan-adj-sid <number:1..255> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 15 `；EOL ` RVA 0x34B9B8A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of items。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-555260a8b81f290e](../../evidence/parameters-sets-007.md#p-555260a8b81f290e) · [状态效果 S-4dff814cc9fc7a8c](../../evidence/state_effects-sets-017.md#s-4dff814cc9fc7a8c)

### path-018026

```text
(exec)# do-exec test isis lsp build <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 8 `；EOL ` RVA 0x34B9C870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017937

```text
(exec)# do-exec test isis lsp id <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 1 `；EOL ` RVA 0x34B9B520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021849

```text
(exec)# do-exec test isis lsp non_pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 13 `；EOL ` RVA 0x34B9C4E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a805277dabb1add5](../../evidence/state_effects-sets-035.md#s-a805277dabb1add5)

### path-021840

```text
(exec)# do-exec test isis lsp pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 12 `；EOL ` RVA 0x34B9C188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7d33abec443590b1](../../evidence/state_effects-sets-027.md#s-7d33abec443590b1)

### path-018065

```text
(exec)# do-exec test isis lsp purge <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 9 `；EOL ` RVA 0x34B9D118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021881

```text
(exec)# do-exec test isis lsp purge dr <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 10 `；EOL ` RVA 0x34B9CC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017978

```text
(exec)# do-exec test isis lsp refresh <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 11 `；EOL ` RVA 0x34B9BCF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013873

```text
(exec)# do-exec test isis nsap <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 2 `；EOL ` RVA 0x34B78BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017842

```text
(exec)# do-exec test isis show counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 6 `；EOL ` RVA 0x34B795E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013976

```text
(exec)# do-exec test isis spf <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 7 `；EOL ` RVA 0x34B9B0D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017851

```text
(exec)# do-exec test isis telemetry enable <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 21 `；EOL ` RVA 0x34B798B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-752b61a2ecb1531e](../../evidence/state_effects-sets-025.md#s-752b61a2ecb1531e)

### path-024936

```text
(exec)# do-exec test issu capability entry register <number:1..4294967295> <number:0..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap entry id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b7aee89a0684739a](../../evidence/parameters-sets-014.md#p-b7aee89a0684739a) · [状态效果 S-02a600269a7d72d8](../../evidence/state_effects-sets-001.md#s-02a600269a7d72d8)

### path-025101

```text
(exec)# do-exec test issu capability group register <number:1..4294967295> <number:1..100> <number:0..1> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap group id；` unsigned_number ` no_mandatory_entry 1=TRUE, 0=FALSE；` string ` Cap entry list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-edb3c0f496cab6b9](../../evidence/parameters-sets-018.md#p-edb3c0f496cab6b9) · [状态效果 S-acd9e9e311dc8cb9](../../evidence/state_effects-sets-037.md#s-acd9e9e311dc8cb9)

### path-024561

```text
(exec)# do-exec test issu capability type-list register <number:1..4294967295> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-369daa5871e461d5](../../evidence/parameters-sets-005.md#p-369daa5871e461d5) · [状态效果 S-20b2f632700ca99e](../../evidence/state_effects-sets-007.md#s-20b2f632700ca99e)

### path-023354

```text
(exec)# do-exec test issu client <number:1..9999> bits enable <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3ef334e0ec790657](../../evidence/parameters-sets-005.md#p-3ef334e0ec790657) · [状态效果 S-38e4242d78bcd530](../../evidence/state_effects-sets-013.md#s-38e4242d78bcd530)

### path-016857

```text
(exec)# do-exec test issu client register <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c4ed1603a0f79498](../../evidence/state_effects-sets-042.md#s-c4ed1603a0f79498)

### path-016811

```text
(exec)# do-exec test issu distributed show <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E60B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3a35226467aa2b54](../../evidence/state_effects-sets-013.md#s-3a35226467aa2b54)

### path-017032

```text
(exec)# do-exec test issu divc no-test <cr>
```

Handler ` RVA 0xD4BFE40 `；selector ` 0 `；EOL ` RVA 0x33E66EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-18432e3318b8a88c](../../evidence/state_effects-sets-006.md#s-18432e3318b8a88c)

### path-020882

```text
(exec)# do-exec test issu entity register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E618C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a8d135807cc9287b](../../evidence/parameters-sets-013.md#p-a8d135807cc9287b) · [状态效果 S-65a2a5ef8385a35f](../../evidence/state_effects-sets-022.md#s-65a2a5ef8385a35f)

### path-024580

```text
(exec)# do-exec test issu injected calc_mtu <number:0..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFC10 `；selector ` 0 `；EOL ` RVA 0x33E65928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-853668705988955a](../../evidence/parameters-sets-010.md#p-853668705988955a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023405

```text
(exec)# do-exec test issu injected capability <number:0..4294967295> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFCF0 `；selector ` 0 `；EOL ` RVA 0x33E65298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` capability entry id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-393798d128e2709a](../../evidence/parameters-sets-005.md#p-393798d128e2709a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023412

```text
(exec)# do-exec test issu injected comp_result <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD4BFC80 `；selector ` 0 `；EOL ` RVA 0x33E655D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` compatible result。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6361eb3e9623ecfb](../../evidence/parameters-sets-008.md#p-6361eb3e9623ecfb) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024947

```text
(exec)# do-exec test issu injected message <number:0..4294967295> <number:1..100> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFD60 `；selector ` 0 `；EOL ` RVA 0x33E64F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version；` unsigned_number ` message mtu。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7510cad559f30d36](../../evidence/parameters-sets-009.md#p-7510cad559f30d36) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020932

```text
(exec)# do-exec test issu injected register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4BFDE0 `；selector ` 0 `；EOL ` RVA 0x33E64B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0084d67a308f4e0e](../../evidence/parameters-sets-001.md#p-0084d67a308f4e0e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020912

```text
(exec)# do-exec test issu lossless session setup <cr>
```

Handler ` RVA 0xD4BF540 `；selector ` 0 `；EOL ` RVA 0x33E634F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-17b5b26f19eaa113](../../evidence/state_effects-sets-005.md#s-17b5b26f19eaa113)

### path-024935

```text
(exec)# do-exec test issu message group register <number:1..4294967295> <number:1..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg group id；` string ` msg type list ex: 1,2,3 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5853af0f9184149a](../../evidence/parameters-sets-007.md#p-5853af0f9184149a) · [状态效果 S-bbf2d79943b9b6d9](../../evidence/state_effects-sets-040.md#s-bbf2d79943b9b6d9)

### path-025098

```text
(exec)# do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <cr>
```

Handler ` RVA 0xD4BF240 `；selector ` 0 `；EOL ` RVA 0x33E61F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c8d4fce5568ed841](../../evidence/parameters-sets-015.md#p-c8d4fce5568ed841) · [状态效果 S-c73a20c9844c63d6](../../evidence/state_effects-sets-042.md#s-c73a20c9844c63d6)

### path-025181

```text
(exec)# do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <string> <cr>
```

Handler ` RVA 0xD4BF1A0 `；selector ` 0 `；EOL ` RVA 0x33E61F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver；` string ` dummy version list, ex: 2,3,5 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5787eb47f94b9f1d](../../evidence/parameters-sets-007.md#p-5787eb47f94b9f1d) · [状态效果 S-c73a20c9844c63d6](../../evidence/state_effects-sets-042.md#s-c73a20c9844c63d6)

### path-016974

```text
(exec)# do-exec test issu negative on <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-148fd2f63e1f9001](../../evidence/state_effects-sets-005.md#s-148fd2f63e1f9001)

### path-024576

```text
(exec)# do-exec test issu nego-version config <number:1..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BF6C0 `；selector ` 0 `；EOL ` RVA 0x33E66400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` new negotiated version。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-84abe38d8cd95294](../../evidence/parameters-sets-010.md#p-84abe38d8cd95294) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020950

```text
(exec)# do-exec test issu negotiate <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E65CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e3a16036306ccf7a](../../evidence/parameters-sets-017.md#p-e3a16036306ccf7a) · [状态效果 S-1a7d8b9ae2d5ffa2](../../evidence/state_effects-sets-006.md#s-1a7d8b9ae2d5ffa2)

### path-017017

```text
(exec)# do-exec test issu policy off <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66AD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cea5e7dcb1a25854](../../evidence/state_effects-sets-044.md#s-cea5e7dcb1a25854)

### path-016939

```text
(exec)# do-exec test issu session ipc <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a4a19b61f2b96d9b](../../evidence/state_effects-sets-035.md#s-a4a19b61f2b96d9b)

### path-024567

```text
(exec)# do-exec test issu shared message_session unregister <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BFA00 `；selector ` 0 `；EOL ` RVA 0x33E64010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-15f9d1914836288c](../../evidence/parameters-sets-002.md#p-15f9d1914836288c) · [状态效果 S-e29dfaad97695026](../../evidence/state_effects-sets-048.md#s-e29dfaad97695026)

### path-020962

```text
(exec)# do-exec test issu shared nego_session register <cr>
```

Handler ` RVA 0xD4BFB40 `；selector ` 0 `；EOL ` RVA 0x33E64428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6855f5023fb8f07f](../../evidence/state_effects-sets-022.md#s-6855f5023fb8f07f)

### path-024570

```text
(exec)# do-exec test issu shared negotiate <number:1..4294967295> <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BF7A0 `；selector ` 0 `；EOL ` RVA 0x33E64818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number `  message session id；` unsigned_number `  negotiation session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-002060df6e92087d](../../evidence/parameters-sets-001.md#p-002060df6e92087d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023404

```text
(exec)# do-exec test issu transform <number:1..4294967295> <number:1..100> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5bac2e1d7c4c7095](../../evidence/parameters-sets-007.md#p-5bac2e1d7c4c7095) · [状态效果 S-45d316d55ac8c677](../../evidence/state_effects-sets-015.md#s-45d316d55ac8c677)

### path-012604

```text
(exec)# do-exec test l2protocol-forward <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 32 `；EOL ` RVA 0x35E87788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b8bf6a5a94b9fbb4](../../evidence/conditions-sets-071.md#c-b8bf6a5a94b9fbb4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012601

```text
(exec)# do-exec test l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 31 `；EOL ` RVA 0x35E871A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-deebdbb24a64c9b4](../../evidence/conditions-sets-086.md#c-deebdbb24a64c9b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019051

```text
(exec)# do-exec test lacp disable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fd693d708a161413](../../evidence/state_effects-sets-054.md#s-fd693d708a161413)

### path-019015

```text
(exec)# do-exec test lacp disable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B14F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fd693d708a161413](../../evidence/state_effects-sets-054.md#s-fd693d708a161413)

### path-018973

```text
(exec)# do-exec test lacp disable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B14CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fd693d708a161413](../../evidence/state_effects-sets-054.md#s-fd693d708a161413)

### path-019078

```text
(exec)# do-exec test lacp enable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-57e28cd603691c70](../../evidence/state_effects-sets-019.md#s-57e28cd603691c70)

### path-019048

```text
(exec)# do-exec test lacp enable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B157D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-57e28cd603691c70](../../evidence/state_effects-sets-019.md#s-57e28cd603691c70)

### path-019010

```text
(exec)# do-exec test lacp enable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B15528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-57e28cd603691c70](../../evidence/state_effects-sets-019.md#s-57e28cd603691c70)

### path-022320

```text
(exec)# do-exec test lacp multi-chassis iccp-version <number:0..65535> <cr>
```

Handler ` RVA 0xC960530 `；selector ` 0 `；EOL ` RVA 0x33B38290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Version in ICCP connection TLV。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1fc392fcc1ad0e26](../../evidence/parameters-sets-003.md#p-1fc392fcc1ad0e26) · [状态效果 S-e9edd1bacd935779](../../evidence/state_effects-sets-049.md#s-e9edd1bacd935779)

### path-024224

```text
(exec)# do-exec test lacp timer wait fast default <cr>
```

Handler ` RVA 0xC8D32D0 `；selector ` 0 `；EOL ` RVA 0x33B166F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65bdb6371aaa68c5](../../evidence/state_effects-sets-022.md#s-65bdb6371aaa68c5)

### path-017024

```text
(exec)# do-exec test lim proximity-db enable <cr>
```

Handler ` RVA 0xC9242D0 `；selector ` 1 `；EOL ` RVA 0x33B1E4A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a2a91441a037a770](../../evidence/conditions-sets-063.md#c-a2a91441a037a770) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-adf129a08da74bcc](../../evidence/state_effects-sets-037.md#s-adf129a08da74bcc)

### path-025234

```text
(exec)# do-exec test mdns browse regtype <string> domain <string> periodicity <number:0..4294967295> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AA8B0 `；selector ` 0 `；EOL ` RVA 0x35D12E90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify in this form _servicename._protocol；` string ` Specify Domain or 0 for NULL；` unsigned_number ` Specify Periodicity in seconds；` unsigned_number ` Specify interface Index。

[条件 C-13390d35dddb1359](../../evidence/conditions-sets-008.md#c-13390d35dddb1359) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a5635059931d6d21](../../evidence/parameters-sets-013.md#p-a5635059931d6d21) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021474

```text
(exec)# do-exec test mdns browse stop <number:1..4294967295> <cr>
```

Handler ` RVA 0x142AA9D0 `；selector ` 0 `；EOL ` RVA 0x35D13180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter Request ID value。

[条件 C-4323fecd907d6eed](../../evidence/conditions-sets-026.md#c-4323fecd907d6eed) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f5e43b71021fa86d](../../evidence/parameters-sets-018.md#p-f5e43b71021fa86d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013706

```text
(exec)# do-exec test mdns cache <cr>
```

Handler ` RVA 0x142ABBE0 `；selector ` 1 `；EOL ` RVA 0x35D14068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cdeb48af9d6b443c](../../evidence/conditions-sets-079.md#c-cdeb48af9d6b443c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024694

```text
(exec)# do-exec test mdns resolve host <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAC10 `；selector ` 0 `；EOL ` RVA 0x35D13A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify HostName to Resolve；` unsigned_number ` Specify Interface Index。

[条件 C-b987c6223dae83b5](../../evidence/conditions-sets-072.md#c-b987c6223dae83b5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0467657afa55ba03](../../evidence/parameters-sets-001.md#p-0467657afa55ba03) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025235

```text
(exec)# do-exec test mdns resolve service <string> regtype <string> domain <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAAF0 `；selector ` 0 `；EOL ` RVA 0x35D13670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Service Instance Name；` string ` Specify in this form _servicename._protocol；` string ` Specify Domain name or 0 for NULL；` unsigned_number ` Specify Interface Index。

[条件 C-87b72df779a70c36](../../evidence/conditions-sets-052.md#c-87b72df779a70c36) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7a2f34b5b2da854f](../../evidence/parameters-sets-010.md#p-7a2f34b5b2da854f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013539

```text
(exec)# do-exec test mdns resync <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 9 `；EOL ` RVA 0x35D12098 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4ef83fd400480529](../../evidence/conditions-sets-031.md#c-4ef83fd400480529) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017416

```text
(exec)# do-exec test mdns srv-enum <number:0..1> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 11 `；EOL ` RVA 0x35D11E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter 0 for clear and 1 for request。

[条件 C-0b3ff354e90ab8d3](../../evidence/conditions-sets-005.md#c-0b3ff354e90ab8d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-79203c4ca1832bbb](../../evidence/parameters-sets-009.md#p-79203c4ca1832bbb) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013577

```text
(exec)# do-exec test mdns start <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 0 `；EOL ` RVA 0x35D126E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9375bf6b879237e9](../../evidence/conditions-sets-057.md#c-9375bf6b879237e9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013593

```text
(exec)# do-exec test mdns stop <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 1 `；EOL ` RVA 0x35D12990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3bb8ed1fefa860f](../../evidence/conditions-sets-076.md#c-c3bb8ed1fefa860f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024690

```text
(exec)# do-exec test mdns update bssid <address> client-mac <address> <cr>
```

Handler ` RVA 0x142ABAD0 `；selector ` 1 `；EOL ` RVA 0x35D14590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address；` address ` 48 bit mac address。

[条件 C-1303dcd8eb5786b3](../../evidence/conditions-sets-008.md#c-1303dcd8eb5786b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-54086fa71b463a2f](../../evidence/parameters-sets-007.md#p-54086fa71b463a2f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023768

```text
(exec)# do-exec test mdns update query-pak bssid-mac <address> <cr>
```

Handler ` RVA 0x142ABA60 `；selector ` 1 `；EOL ` RVA 0x35D148A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-1901f0514a971661](../../evidence/conditions-sets-010.md#c-1901f0514a971661) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cb5e5912b30e3de5](../../evidence/parameters-sets-015.md#p-cb5e5912b30e3de5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012380

```text
(exec)# do-exec test memory <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433F0E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016997

```text
(exec)# do-exec test memory create dangling-reference <cr>
```

Handler ` RVA 0xD79C2F0 `；selector ` 0 `；EOL ` RVA 0x33EE8D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-510d94078006d412](../../evidence/state_effects-sets-018.md#s-510d94078006d412)

### path-024594

```text
(exec)# do-exec test memory create leak type1 <number:28..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C5D0 `；selector ` 0 `；EOL ` RVA 0x33EE9470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` size of blocks to leak；` unsigned_number ` number of blocks to leak。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e7de55dec44fbd77](../../evidence/parameters-sets-017.md#p-e7de55dec44fbd77) · [状态效果 S-8e571fdb45e60913](../../evidence/state_effects-sets-030.md#s-8e571fdb45e60913)

### path-017068

```text
(exec)# do-exec test memory history <number:1..60> <cr>
```

Handler ` RVA 0xD79B850 `；selector ` 0 `；EOL ` RVA 0x33EEA5B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Period of history collection in minutes。

[条件 C-08349088d0705dd4](../../evidence/conditions-sets-004.md#c-08349088d0705dd4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bff5968e13295850](../../evidence/parameters-sets-015.md#p-bff5968e13295850) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013016

```text
(exec)# do-exec test memory nvram-multibus <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433EE50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025251

```text
(exec)# do-exec test mfib cb-support IPv4 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 1 `；EOL ` RVA 0x355AFA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-cae13a57f800f2d3](../../evidence/conditions-sets-078.md#c-cae13a57f800f2d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f3f238ba8bd70d5c](../../evidence/parameters-sets-018.md#p-f3f238ba8bd70d5c) · [状态效果 S-3182090d5340d857](../../evidence/state_effects-sets-011.md#s-3182090d5340d857)

### path-025252

```text
(exec)# do-exec test mfib cb-support IPv6 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 2 `；EOL ` RVA 0x355AFFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-cae13a57f800f2d3](../../evidence/conditions-sets-078.md#c-cae13a57f800f2d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b9f20fac51ecc555](../../evidence/parameters-sets-014.md#p-b9f20fac51ecc555) · [状态效果 S-89608882474e93a6](../../evidence/state_effects-sets-029.md#s-89608882474e93a6)

### path-014014

```text
(exec)# do-exec test mfib channel <cr>
```

Handler ` RVA 0x11667890 `；selector ` 0 `；EOL ` RVA 0x35524680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-100b38edda4757c6](../../evidence/conditions-sets-006.md#c-100b38edda4757c6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013879

```text
(exec)# do-exec test mfib enable <cr>
```

Handler ` RVA 0x11949710 `；selector ` 0 `；EOL ` RVA 0x355AC7B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c063568e2cb65da0](../../evidence/conditions-sets-074.md#c-c063568e2cb65da0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-74b7a73ca342a521](../../evidence/state_effects-sets-025.md#s-74b7a73ca342a521)

### path-014033

```text
(exec)# do-exec test mfib reload <cr>
```

Handler ` RVA 0x11667B00 `；selector ` 0 `；EOL ` RVA 0x35524B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-553f65663477b480](../../evidence/conditions-sets-033.md#c-553f65663477b480) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013391

```text
(exec)# do-exec test mgd-timer watch <cr>
```

Handler ` RVA 0xD7AD830 `；selector ` 0 `；EOL ` RVA 0x33EF0C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-70c71d1060e77073](../../evidence/state_effects-sets-024.md#s-70c71d1060e77073)

### path-019041

```text
(exec)# do-exec test mka macsec-sim off <cr>
```

Handler ` RVA 0x16085270 `；selector ` 1 `；EOL ` RVA 0x35EB9D78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d1482e4e73ff99d8](../../evidence/conditions-sets-081.md#c-d1482e4e73ff99d8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37b4247650f28dd0](../../evidence/state_effects-sets-012.md#s-37b4247650f28dd0)

### path-022359

```text
(exec)# do-exec test mka message-number initial-value <number:1..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 2 `；EOL ` RVA 0x35EBA128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 32-bit Message Number (default = 1)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2cc60459240682de](../../evidence/parameters-sets-004.md#p-2cc60459240682de) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022376

```text
(exec)# do-exec test mka message-number window-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 5 `；EOL ` RVA 0x35EBA3F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MN Window Size - # of MKPDUs (default = 0, off)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-76ba54810b928371](../../evidence/parameters-sets-009.md#p-76ba54810b928371) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022393

```text
(exec)# do-exec test mka packet-number initial-value <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 6 `；EOL ` RVA 0x35EBABB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 32-bit Packet Number (default = 1, PendingPNExhaustion at 3221225472)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5f2a7ac5cf4b91bf](../../evidence/parameters-sets-008.md#p-5f2a7ac5cf4b91bf) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014334

```text
(exec)# do-exec test mock btrace <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 4 `；EOL ` RVA 0x35FA0940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71e9699c7860bed3](../../evidence/conditions-sets-044.md#c-71e9699c7860bed3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014373

```text
(exec)# do-exec test mock chasfs <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 6 `；EOL ` RVA 0x35FA0E90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a676280344836c0b](../../evidence/conditions-sets-064.md#c-a676280344836c0b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014350

```text
(exec)# do-exec test mock chassis <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 5 `；EOL ` RVA 0x35FA0BE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c04c722c138e83e2](../../evidence/conditions-sets-074.md#c-c04c722c138e83e2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014433

```text
(exec)# do-exec test mock crypto <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 18 `；EOL ` RVA 0x35FA1930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eeb5ba0b1c800bd7](../../evidence/conditions-sets-092.md#c-eeb5ba0b1c800bd7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014383

```text
(exec)# do-exec test mock cyan <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 7 `；EOL ` RVA 0x35FA1138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-730afb9a1dde6901](../../evidence/conditions-sets-044.md#c-730afb9a1dde6901) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014313

```text
(exec)# do-exec test mock ei <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 8 `；EOL ` RVA 0x35FA0698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae63daa4b329aab2](../../evidence/conditions-sets-067.md#c-ae63daa4b329aab2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018186

```text
(exec)# do-exec test mock infra enqueue <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 1 `；EOL ` RVA 0x35F9F7E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a638a345f05fa8c2](../../evidence/conditions-sets-064.md#c-a638a345f05fa8c2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a060c4daa5a2bff6](../../evidence/state_effects-sets-034.md#s-a060c4daa5a2bff6)

### path-014277

```text
(exec)# do-exec test mock ipc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 11 `；EOL ` RVA 0x35FA0148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c2c6586647f7be09](../../evidence/conditions-sets-075.md#c-c2c6586647f7be09) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014257

```text
(exec)# do-exec test mock mcp <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 2 `；EOL ` RVA 0x35F9FEA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9be50e71f4ba7c1c](../../evidence/conditions-sets-060.md#c-9be50e71f4ba7c1c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014296

```text
(exec)# do-exec test mock misc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 3 `；EOL ` RVA 0x35FA03F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0d5511568893b821](../../evidence/conditions-sets-005.md#c-0d5511568893b821) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018501

```text
(exec)# do-exec test mock overlayfs system-call <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 20 `；EOL ` RVA 0x35FA1EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9b1b87d9958d4697](../../evidence/conditions-sets-060.md#c-9b1b87d9958d4697) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-159384508fdda034](../../evidence/state_effects-sets-005.md#s-159384508fdda034)

### path-014414

```text
(exec)# do-exec test mock real <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 9 `；EOL ` RVA 0x35FA1688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-160059a6fea2740e](../../evidence/conditions-sets-009.md#c-160059a6fea2740e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014240

```text
(exec)# do-exec test mock system <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 17 `；EOL ` RVA 0x35F9FBF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc8e32e775a81c75](../../evidence/conditions-sets-079.md#c-cc8e32e775a81c75) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014401

```text
(exec)# do-exec test mock tdl <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 10 `；EOL ` RVA 0x35FA13E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d65b17cf8c3b50e](../../evidence/conditions-sets-061.md#c-9d65b17cf8c3b50e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014453

```text
(exec)# do-exec test mock vaarg <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 19 `；EOL ` RVA 0x35FA1BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c0ae84cd8eb1ffa](../../evidence/conditions-sets-023.md#c-3c0ae84cd8eb1ffa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022062

```text
(exec)# do-exec test monitor clear config lock <cr>
```

Handler ` RVA 0xE4CE1F0 `；selector ` 0 `；EOL ` RVA 0x342CFCF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013928

```text
(exec)# do-exec test mrib disable <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x355A7AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19d38f0bae87dd65](../../evidence/conditions-sets-010.md#c-19d38f0bae87dd65) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1e7e10b351dd2294](../../evidence/state_effects-sets-007.md#s-1e7e10b351dd2294)

### path-017966

```text
(exec)# do-exec test mrib ip stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35376868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c509e16008966f7f](../../evidence/conditions-sets-076.md#c-c509e16008966f7f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9855bccfcc6983d](../../evidence/state_effects-sets-036.md#s-a9855bccfcc6983d)

### path-017959

```text
(exec)# do-exec test mrib ipv6 stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35540A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-745ad1cbbc0fb872](../../evidence/conditions-sets-045.md#c-745ad1cbbc0fb872) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f096b0c9c77d36f4](../../evidence/state_effects-sets-051.md#s-f096b0c9c77d36f4)

### path-025037

```text
(exec)# do-exec test mvpn ipv4 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x34790B08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-fe97fd1163db9d0a](../../evidence/conditions-sets-098.md#c-fe97fd1163db9d0a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e7edaa477d6f924d](../../evidence/parameters-sets-017.md#p-e7edaa477d6f924d) · [状态效果 S-388ad592778bb806](../../evidence/state_effects-sets-013.md#s-388ad592778bb806)

### path-021766

```text
(exec)# do-exec test mvpn ipv4 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x347910B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be506ef255ae8532](../../evidence/conditions-sets-073.md#c-be506ef255ae8532) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5bd2618d166ad401](../../evidence/state_effects-sets-020.md#s-5bd2618d166ad401)

### path-021753

```text
(exec)# do-exec test mvpn ipv4 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x34790E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb8b7d85c6e5b67a](../../evidence/conditions-sets-072.md#c-bb8b7d85c6e5b67a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5bd2618d166ad401](../../evidence/state_effects-sets-020.md#s-5bd2618d166ad401)

### path-025040

```text
(exec)# do-exec test mvpn ipv6 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x347916C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-5777c56982c57e1f](../../evidence/conditions-sets-034.md#c-5777c56982c57e1f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2d64e798f1d53ea9](../../evidence/parameters-sets-004.md#p-2d64e798f1d53ea9) · [状态效果 S-85ea70e35e736258](../../evidence/state_effects-sets-028.md#s-85ea70e35e736258)

### path-021773

```text
(exec)# do-exec test mvpn ipv6 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x34791C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8785db4633997928](../../evidence/conditions-sets-052.md#c-8785db4633997928) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9b8dafcc131e9f9](../../evidence/state_effects-sets-036.md#s-a9b8dafcc131e9f9)

### path-021762

```text
(exec)# do-exec test mvpn ipv6 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x347919C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687f5824f1d67310](../../evidence/conditions-sets-040.md#c-687f5824f1d67310) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9b8dafcc131e9f9](../../evidence/state_effects-sets-036.md#s-a9b8dafcc131e9f9)

### path-017063

```text
(exec)# do-exec test mvrp enable <number:0..1> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 2 `；EOL ` RVA 0x33B3ACD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enable - 1, Disable - 0。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2b2af8342a3221a3](../../evidence/parameters-sets-004.md#p-2b2af8342a3221a3) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021072

```text
(exec)# do-exec test mvrp joinin <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 1 `；EOL ` RVA 0x33B3AA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-347f484921822044](../../evidence/parameters-sets-004.md#p-347f484921822044) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021060

```text
(exec)# do-exec test mvrp new <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 0 `；EOL ` RVA 0x33B3A6D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-47e3eaebeb4262d6](../../evidence/parameters-sets-006.md#p-47e3eaebeb4262d6) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013290

```text
(exec)# do-exec test natmode suppress <cr>
```

Handler ` RVA 0xCF73670 `；selector ` 0 `；EOL ` RVA 0x33D44630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-59f870726d839e9c](../../evidence/state_effects-sets-019.md#s-59f870726d839e9c)

### path-014593

```text
(exec)# do-exec test netconf-agent history <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 1 `；EOL ` RVA 0x3462AA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014617

```text
(exec)# do-exec test netconf-agent summary <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 3 `；EOL ` RVA 0x3462AD20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013809

```text
(exec)# do-exec test ngdns config <cr>
```

Handler ` RVA 0xD177360 `；selector ` 0 `；EOL ` RVA 0x33DA53C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017708

```text
(exec)# do-exec test ngdns lookup <string> <cr>
```

Handler ` RVA 0xD177DF0 `；selector ` 0 `；EOL ` RVA 0x33DA5878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` lookup name。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-decc2673888888d4](../../evidence/parameters-sets-017.md#p-decc2673888888d4) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017657

```text
(exec)# do-exec test ngdns periodic dump <cr>
```

Handler ` RVA 0xD177180 `；selector ` 0 `；EOL ` RVA 0x33DA4720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025211

```text
(exec)# do-exec test ngdns periodic register fqdn-name <string> type both module-id <number:1..3> <cr>
```

Handler ` RVA 0xD176ED0 `；selector ` 0 `；EOL ` RVA 0x33DA4368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify FQDN；` unsigned_number ` module-id。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ed5b72c7cd03d32e](../../evidence/parameters-sets-018.md#p-ed5b72c7cd03d32e) · [状态效果 S-c1beaac5d3cf51cf](../../evidence/state_effects-sets-041.md#s-c1beaac5d3cf51cf)

### path-018895

```text
(exec)# do-exec test ngiosd process-isolation start <cr>
```

Handler ` RVA 0x1653B780 `；selector ` 0 `；EOL ` RVA 0x35F9EE48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a8cc348b13a5301f](../../evidence/state_effects-sets-036.md#s-a8cc348b13a5301f)

### path-022275

```text
(exec)# do-exec test ngiosd simulation prepare-failure enable <cr>
```

Handler ` RVA 0x1653B5E0 `；selector ` 0 `；EOL ` RVA 0x35F9E6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6170041f199a206a](../../evidence/state_effects-sets-021.md#s-6170041f199a206a)

### path-022297

```text
(exec)# do-exec test ngiosd simulation prepare-pass enable <cr>
```

Handler ` RVA 0x1653B520 `；selector ` 0 `；EOL ` RVA 0x35F9EA80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37a92a1d0d16cf55](../../evidence/state_effects-sets-012.md#s-37a92a1d0d16cf55)

### path-018861

```text
(exec)# do-exec test ngiosd simulation start <cr>
```

Handler ` RVA 0x1653B6A0 `；selector ` 0 `；EOL ` RVA 0x35F9E378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f154f6dfd1bd7e14](../../evidence/state_effects-sets-051.md#s-f154f6dfd1bd7e14)

### path-012516

```text
(exec)# do-exec test nhrp event <number:0..1500> <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 8 `；EOL ` RVA 0x34BEAEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` event code。

[条件 C-9cc23782aa3a848b](../../evidence/conditions-sets-061.md#c-9cc23782aa3a848b) · [缺口 G-5d6d54cbe3a6191a](../../evidence/gaps-sets-004.md#g-5d6d54cbe3a6191a) · [参数 P-6c57de9d403a368b](../../evidence/parameters-sets-009.md#p-6c57de9d403a368b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014826

```text
(exec)# do-exec test notify <string> <cr>
```

Handler ` RVA 0x15A6CE70 `；selector ` 0 `；EOL ` RVA 0x35DE3AB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-e2bc1f5c8b2db1af](../../evidence/conditions-sets-087.md#c-e2bc1f5c8b2db1af) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bb63f77282b0e6a2](../../evidence/parameters-sets-014.md#p-bb63f77282b0e6a2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021992

```text
(exec)# do-exec test nvram <string> clear remote-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 1 `；EOL ` RVA 0x33EB0A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018397

```text
(exec)# do-exec test nvram <string> explicit-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 0 `；EOL ` RVA 0x33EB0CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018425

```text
(exec)# do-exec test nvram <string> initialize <cr>
```

Handler ` RVA 0xD620830 `；selector ` 2 `；EOL ` RVA 0x33EB0F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024795

```text
(exec)# do-exec test odb client <number:1..256> add-static-tlv type <number:0..65535> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 2 `；EOL ` RVA 0x35856F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` TLV type。

[条件 C-80216fb1f9949281](../../evidence/conditions-sets-050.md#c-80216fb1f9949281) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4937c32f8d4b15b3](../../evidence/parameters-sets-006.md#p-4937c32f8d4b15b3) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021911

```text
(exec)# do-exec test odb client <number:1..256> deregister <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 1 `；EOL ` RVA 0x35856BE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-d53d47f92e3d412c](../../evidence/conditions-sets-082.md#c-d53d47f92e3d412c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025245

```text
(exec)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> add-tlv type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 8 `；EOL ` RVA 0x358585E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-603c5f71a51d9aa5](../../evidence/conditions-sets-037.md#c-603c5f71a51d9aa5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3761b49542bab2b5](../../evidence/parameters-sets-005.md#p-3761b49542bab2b5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025049

```text
(exec)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 7 `；EOL ` RVA 0x35858208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-41ec9c5c88dd2ce6](../../evidence/conditions-sets-026.md#c-41ec9c5c88dd2ce6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025214

```text
(exec)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> notify subscribe change <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 9 `；EOL ` RVA 0x35858930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-c1893af9033fb1f9](../../evidence/conditions-sets-075.md#c-c1893af9033fb1f9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-3b05fb34c44b2b97](../../evidence/state_effects-sets-013.md#s-3b05fb34c44b2b97)

### path-025236

```text
(exec)# do-exec test odb client <number:1..256> table <number:1..65534> add-row type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 6 `；EOL ` RVA 0x35857A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-3c5d3f8e4539e524](../../evidence/conditions-sets-023.md#c-3c5d3f8e4539e524) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-339759b930726c8c](../../evidence/parameters-sets-004.md#p-339759b930726c8c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024796

```text
(exec)# do-exec test odb client <number:1..256> table <number:1..65534> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 4 `；EOL ` RVA 0x35857648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-7c978f9c07c92832](../../evidence/conditions-sets-048.md#c-7c978f9c07c92832) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025153

```text
(exec)# do-exec test odb client <number:1..256> table <number:1..65534> notify subscribe add <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 5 `；EOL ` RVA 0x35857D70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-02058b781e1101b0](../../evidence/conditions-sets-001.md#c-02058b781e1101b0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-5f2c68abdefa12c3](../../evidence/state_effects-sets-020.md#s-5f2c68abdefa12c3)

### path-024023

```text
(exec)# do-exec test odb client <number:1..256> table create <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 3 `；EOL ` RVA 0x358572C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-b430db76483bbdf3](../../evidence/conditions-sets-070.md#c-b430db76483bbdf3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021906

```text
(exec)# do-exec test odb client register <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 0 `；EOL ` RVA 0x35856920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Client name。

[条件 C-9d4808203c71352b](../../evidence/conditions-sets-061.md#c-9d4808203c71352b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-13828cb53228f29f](../../evidence/parameters-sets-002.md#p-13828cb53228f29f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021918

```text
(exec)# do-exec test onep cli uninstall <string> <cr>
```

Handler ` RVA 0x13A82E40 `；selector ` 0 `；EOL ` RVA 0x35CAA6E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Configuration Domain。

[条件 C-30650f11735b2424](../../evidence/conditions-sets-019.md#c-30650f11735b2424) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6b00482f66f10d6d](../../evidence/parameters-sets-008.md#p-6b00482f66f10d6d) · [状态效果 S-bbcd05db8db16a32](../../evidence/state_effects-sets-040.md#s-bbcd05db8db16a32)

### path-014352

```text
(exec)# do-exec test onep ctx_reg <cr>
```

Handler ` RVA 0x13A858B0 `；selector ` 0 `；EOL ` RVA 0x35CABFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2e013613ed02bb0c](../../evidence/conditions-sets-018.md#c-2e013613ed02bb0c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eeba3251be42be17](../../evidence/state_effects-sets-050.md#s-eeba3251be42be17)

### path-018374

```text
(exec)# do-exec test onep if_ctx_event enable <cr>
```

Handler ` RVA 0x13A85820 `；selector ` 0 `；EOL ` RVA 0x35CAC308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d26840ca034f356](../../evidence/conditions-sets-042.md#c-6d26840ca034f356) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-75ca3e5e710d061e](../../evidence/state_effects-sets-025.md#s-75ca3e5e710d061e)

### path-018219

```text
(exec)# do-exec test onep internal enable <cr>
```

Handler ` RVA 0x13A82DA0 `；selector ` 0 `；EOL ` RVA 0x35CAA9D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b38550c3604f7a72](../../evidence/state_effects-sets-038.md#s-b38550c3604f7a72)

### path-018273

```text
(exec)# do-exec test onep thrift list <cr>
```

Handler ` RVA 0x13A863B0 `；selector ` 0 `；EOL ` RVA 0x35CAADE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fbe63d357ef87e68](../../evidence/conditions-sets-097.md#c-fbe63d357ef87e68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4e27bc30603a7712](../../evidence/state_effects-sets-017.md#s-4e27bc30603a7712)

### path-018308

```text
(exec)# do-exec test onep version disable <cr>
```

Handler ` RVA 0x13A86260 `；selector ` 0 `；EOL ` RVA 0x35CAB5B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bbcd05db8db16a32](../../evidence/state_effects-sets-040.md#s-bbcd05db8db16a32)

### path-021946

```text
(exec)# do-exec test onep version disable exact <cr>
```

Handler ` RVA 0x13A86210 `；selector ` 0 `；EOL ` RVA 0x35CAB588 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bbcd05db8db16a32](../../evidence/state_effects-sets-040.md#s-bbcd05db8db16a32)

### path-018298

```text
(exec)# do-exec test onep version enable <cr>
```

Handler ` RVA 0x13A862B0 `；selector ` 0 `；EOL ` RVA 0x35CABA80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bbcd05db8db16a32](../../evidence/state_effects-sets-040.md#s-bbcd05db8db16a32)

### path-014335

```text
(exec)# do-exec test onep xdt_buginf <cr>
```

Handler ` RVA 0x13A84B00 `；selector ` 0 `；EOL ` RVA 0x35CABD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f740640b0f81d7ab](../../evidence/conditions-sets-095.md#c-f740640b0f81d7ab) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bbcd05db8db16a32](../../evidence/state_effects-sets-040.md#s-bbcd05db8db16a32)

### path-018014

```text
(exec)# do-exec test opflex agent ha <cr>
```

Handler ` RVA 0xC482E30 `；selector ` 1 `；EOL ` RVA 0x33A939F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024793

```text
(exec)# do-exec test opflex agent service vxlan-evpn create <string> <cr>
```

Handler ` RVA 0xC494C00 `；selector ` 0 `；EOL ` RVA 0x33A97360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tenant name。

[条件 C-9725188d4df45d9f](../../evidence/conditions-sets-058.md#c-9725188d4df45d9f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b42fb32a7d39d38b](../../evidence/parameters-sets-014.md#p-b42fb32a7d39d38b) · [状态效果 S-efa29a1d5a287e8b](../../evidence/state_effects-sets-051.md#s-efa29a1d5a287e8b)

### path-024009

```text
(exec)# do-exec test opflex agent service vxlan-evpn state <cr>
```

Handler ` RVA 0xC494F30 `；selector ` 0 `；EOL ` RVA 0x33A96FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024042

```text
(exec)# do-exec test opssl nonblockingsession server dtls stop <cr>
```

Handler ` RVA 0x12A14A30 `；selector ` 0 `；EOL ` RVA 0x35936140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-222758c3ad39c65b](../../evidence/conditions-sets-013.md#c-222758c3ad39c65b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9b829b362556bbbf](../../evidence/state_effects-sets-033.md#s-9b829b362556bbbf)

### path-013732

```text
(exec)# do-exec test ospf debug <cr>
```

Handler ` RVA 0xFCD52B0 `；selector ` 0 `；EOL ` RVA 0x34894F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023895

```text
(exec)# do-exec test ospf nsr cf error <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 10 `；EOL ` RVA 0x33FC6990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Repeat count。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1e19628e5a2b3740](../../evidence/parameters-sets-003.md#p-1e19628e5a2b3740) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021664

```text
(exec)# do-exec test ospf nsr cf flow-off <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 9 `；EOL ` RVA 0x33FC66A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021635

```text
(exec)# do-exec test ospf nsr cf flow-on <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 8 `；EOL ` RVA 0x33FC6400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023894

```text
(exec)# do-exec test ospf nsr cp clear <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 2 `；EOL ` RVA 0x33FC6FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Opcode。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-588a2cc36056eed0](../../evidence/parameters-sets-007.md#p-588a2cc36056eed0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021738

```text
(exec)# do-exec test ospf nsr cp lsa <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 7 `；EOL ` RVA 0x33FC7F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021660

```text
(exec)# do-exec test ospf nsr cp nop <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 1 `；EOL ` RVA 0x33FC6CA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021703

```text
(exec)# do-exec test ospf nsr cp router-id <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 4 `；EOL ` RVA 0x33FC7530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023909

```text
(exec)# do-exec test ospf nsr cp sync <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 3 `；EOL ` RVA 0x33FC72A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Event。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1dd2c57cd27b0f0d](../../evidence/parameters-sets-003.md#p-1dd2c57cd27b0f0d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023893

```text
(exec)# do-exec test ospf nsr recovery delay <number:0..255> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 11 `；EOL ` RVA 0x33FC82E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Seconds to delay recovery。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-56211fbc98f531aa](../../evidence/parameters-sets-007.md#p-56211fbc98f531aa) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017745

```text
(exec)# do-exec test ospf nsr unsynchronize <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 12 `；EOL ` RVA 0x33FC8580 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014062

```text
(exec)# do-exec test ospfv3 crimson <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 17 `；EOL ` RVA 0x35691980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f557668156498af9](../../evidence/state_effects-sets-052.md#s-f557668156498af9)

### path-012890

```text
(exec)# do-exec test parser afs <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 0 `；EOL ` RVA 0x340E0AD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3fb93dcbb5609e4e](../../evidence/conditions-sets-025.md#c-3fb93dcbb5609e4e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016842

```text
(exec)# do-exec test parser configure buffer <cr>
```

Handler ` RVA 0xDEF9430 `；selector ` 0 `；EOL ` RVA 0x340B00E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-80d5c6ad8e66a9e0](../../evidence/state_effects-sets-027.md#s-80d5c6ad8e66a9e0)

### path-016768

```text
(exec)# do-exec test parser consume-memory <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEF9560 `；selector ` 0 `；EOL ` RVA 0x340ACF20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Memory size。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9fc98b3d0183c115](../../evidence/parameters-sets-012.md#p-9fc98b3d0183c115) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012868

```text
(exec)# do-exec test parser gmd <cr>
```

Handler ` RVA 0xDF333D0 `；selector ` 0 `；EOL ` RVA 0x340AC020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013091

```text
(exec)# do-exec test parser green-fe <cr>
```

Handler ` RVA 0xDF8E5F0 `；selector ` 0 `；EOL ` RVA 0x340AEDA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020834

```text
(exec)# do-exec test parser ngios native-green enable <cr>
```

Handler ` RVA 0xDF8EDC0 `；selector ` 0 `；EOL ` RVA 0x340AE210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d0ab82142fe16b1f](../../evidence/state_effects-sets-044.md#s-d0ab82142fe16b1f)

### path-020846

```text
(exec)# do-exec test parser ngios side-effect per-batch <cr>
```

Handler ` RVA 0xDF8ED00 `；selector ` 0 `；EOL ` RVA 0x340AE5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ac7711c89942f5a8](../../evidence/state_effects-sets-036.md#s-ac7711c89942f5a8)

### path-020855

```text
(exec)# do-exec test parser ngios validation enable <cr>
```

Handler ` RVA 0xDF8EC40 `；selector ` 0 `；EOL ` RVA 0x340AE9C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dceb85114228acd2](../../evidence/state_effects-sets-047.md#s-dceb85114228acd2)

### path-020848

```text
(exec)# do-exec test parser rc errno <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 5 `；EOL ` RVA 0x340ADBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` errno value to be mapped。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-712d36c9f93ef0d8](../../evidence/parameters-sets-009.md#p-712d36c9f93ef0d8) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023319

```text
(exec)# do-exec test parser rc failure <number:11..211> <number:1..2> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 4 `；EOL ` RVA 0x340AD2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PRC error code；` unsigned_number ` PRC failure type。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0d3868e4e55310a0](../../evidence/parameters-sets-001.md#p-0d3868e4e55310a0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016819

```text
(exec)# do-exec test parser rc invalid <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 2 `；EOL ` RVA 0x340AD8B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023324

```text
(exec)# do-exec test parser rc success <number:1..3> <number:1..4> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 3 `；EOL ` RVA 0x340AD630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PRC change type；` unsigned_number ` PRC change mode。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-961119851006963a](../../evidence/parameters-sets-012.md#p-961119851006963a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016794

```text
(exec)# do-exec test parser redirect small <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 4 `；EOL ` RVA 0x340E0E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-401bad26f0222cf5](../../evidence/conditions-sets-025.md#c-401bad26f0222cf5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6dfd3a35793e2fe1](../../evidence/state_effects-sets-023.md#s-6dfd3a35793e2fe1)

### path-016749

```text
(exec)# do-exec test parser session-lock <number:0..1200> <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 1 `；EOL ` RVA 0x340E0238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Config session lock holdtime in seconds。

[条件 C-19519dc36d8d974a](../../evidence/conditions-sets-010.md#c-19519dc36d8d974a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-146602e89f177353](../../evidence/parameters-sets-002.md#p-146602e89f177353) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016762

```text
(exec)# do-exec test parser session-lock exit <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 2 `；EOL ` RVA 0x340E04E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3174b2ac1d6f72c1](../../evidence/conditions-sets-019.md#c-3174b2ac1d6f72c1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

