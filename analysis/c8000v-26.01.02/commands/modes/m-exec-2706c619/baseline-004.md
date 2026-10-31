# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-001795

```text
(exec)# debug cpc subblock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34CC7E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-50a4c8db0c6b1973](../../evidence/state_effects-sets-018.md#s-50a4c8db0c6b1973)

### path-000384

```text
(exec)# debug cpl <cr>
```

Handler ` RVA 0xD8B5AB0 `；selector ` 3 `；EOL ` RVA 0x33F3EC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-6d90ba689eafa21e](../../evidence/state_effects-sets-023.md#s-6d90ba689eafa21e)

### path-003117

```text
(exec)# debug cpl cap-xos <cr>
```

Handler ` RVA 0xD8B6630 `；selector ` 13 `；EOL ` RVA 0x33F2FD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-abb53aa46136a842](../../evidence/state_effects-sets-036.md#s-abb53aa46136a842)

### path-003275

```text
(exec)# debug cpl classification <cr>
```

Handler ` RVA 0xD8B64E0 `；selector ` 78 `；EOL ` RVA 0x33F3E9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-de248899a6f21017](../../evidence/state_effects-sets-047.md#s-de248899a6f21017)

### path-007219

```text
(exec)# debug cpl classification client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 80 `；EOL ` RVA 0x33F3E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-de248899a6f21017](../../evidence/state_effects-sets-047.md#s-de248899a6f21017)

### path-007229

```text
(exec)# debug cpl classification dp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 81 `；EOL ` RVA 0x33F3E738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-de248899a6f21017](../../evidence/state_effects-sets-047.md#s-de248899a6f21017)

### path-007205

```text
(exec)# debug cpl classification infra <cr>
```

Handler ` RVA 0xE002120 `；selector ` 79 `；EOL ` RVA 0x33F3E1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-de248899a6f21017](../../evidence/state_effects-sets-047.md#s-de248899a6f21017)

### path-011897

```text
(exec)# debug cpl concurrency delay acquire <number:0..300> <number:1..10000> <cr>
```

Handler ` RVA 0xD8B8BD0 `；selector ` 0 `；EOL ` RVA 0x33F2F750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds；` unsigned_number ` Process ID to apply delay to。

[条件 C-2710c788e027d32d](../../evidence/conditions-sets-015.md#c-2710c788e027d32d) · [参数 P-84d2a1b37008e964](../../evidence/parameters-sets-010.md#p-84d2a1b37008e964) · [状态效果 S-3d56e8c3d1536d23](../../evidence/state_effects-sets-013.md#s-3d56e8c3d1536d23)

### path-007133

```text
(exec)# debug cpl concurrency history <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33F2EE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-da7c5e195240afb3](../../evidence/state_effects-sets-046.md#s-da7c5e195240afb3)

### path-007159

```text
(exec)# debug cpl concurrency lock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33F2F380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-da7c5e195240afb3](../../evidence/state_effects-sets-046.md#s-da7c5e195240afb3)

### path-009999

```text
(exec)# debug cpl concurrency pid <number:1..10000> <cr>
```

Handler ` RVA 0xD8B8C70 `；selector ` 0 `；EOL ` RVA 0x33F2FAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Process ID。

[条件 C-8064308058171e8d](../../evidence/conditions-sets-050.md#c-8064308058171e8d) · [参数 P-df7cdec8dcffcaec](../../evidence/parameters-sets-017.md#p-df7cdec8dcffcaec) · [状态效果 S-da7c5e195240afb3](../../evidence/state_effects-sets-046.md#s-da7c5e195240afb3)

### path-007147

```text
(exec)# debug cpl concurrency trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33F2F0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-da7c5e195240afb3](../../evidence/state_effects-sets-046.md#s-da7c5e195240afb3)

### path-003207

```text
(exec)# debug cpl filtering <cr>
```

Handler ` RVA 0xE002120 `；selector ` 77 `；EOL ` RVA 0x33F3DEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-402f18a871f8762c](../../evidence/state_effects-sets-014.md#s-402f18a871f8762c)

### path-007178

```text
(exec)# debug cpl function <string> <cr>
```

Handler ` RVA 0xD8B8B50 `；selector ` 0 `；EOL ` RVA 0x33F305E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` function name。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [参数 P-1f5cf5dd81e42be8](../../evidence/parameters-sets-003.md#p-1f5cf5dd81e42be8) · [状态效果 S-abb53aa46136a842](../../evidence/state_effects-sets-036.md#s-abb53aa46136a842)

### path-003061

```text
(exec)# debug cpl inline <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33F28180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ff0a52f6dd0177ed](../../evidence/state_effects-sets-054.md#s-ff0a52f6dd0177ed)

### path-003141

```text
(exec)# debug cpl pol-shim <cr>
```

Handler ` RVA 0xD8B65D0 `；selector ` 12 `；EOL ` RVA 0x33F30028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-abb53aa46136a842](../../evidence/state_effects-sets-036.md#s-abb53aa46136a842)

### path-003364

```text
(exec)# debug cpl ppcp <cr>
```

Handler ` RVA 0xD8B5E60 `；selector ` 4 `；EOL ` RVA 0x33F3DB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007200

```text
(exec)# debug cpl ppcp bind <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x33F30E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007295

```text
(exec)# debug cpl ppcp client <cr>
```

Handler ` RVA 0xD8B6440 `；selector ` 18 `；EOL ` RVA 0x33F326C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010055

```text
(exec)# debug cpl ppcp client class-type <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x33F31ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010036

```text
(exec)# debug cpl ppcp client classification <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x33F316D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010043

```text
(exec)# debug cpl ppcp client distribution <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x33F31980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010018

```text
(exec)# debug cpl ppcp client feature <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x33F31188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010065

```text
(exec)# debug cpl ppcp client filter-type <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x33F32178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010072

```text
(exec)# debug cpl ppcp client legacy-platform <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x33F32420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010049

```text
(exec)# debug cpl ppcp client policy-type <cr>
```

Handler ` RVA 0xE002120 `；selector ` 23 `；EOL ` RVA 0x33F31C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010028

```text
(exec)# debug cpl ppcp client target <cr>
```

Handler ` RVA 0xE002120 `；selector ` 20 `；EOL ` RVA 0x33F31430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007283

```text
(exec)# debug cpl ppcp database <cr>
```

Handler ` RVA 0xD8B6690 `；selector ` 74 `；EOL ` RVA 0x33F3C5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010064

```text
(exec)# debug cpl ppcp database runtime <cr>
```

Handler ` RVA 0xE002120 `；selector ` 76 `；EOL ` RVA 0x33F3C340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010054

```text
(exec)# debug cpl ppcp database template <cr>
```

Handler ` RVA 0xE002120 `；selector ` 75 `；EOL ` RVA 0x33F3C098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007341

```text
(exec)# debug cpl ppcp event <cr>
```

Handler ` RVA 0xD8B6A20 `；selector ` 34 `；EOL ` RVA 0x33F3A210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010095

```text
(exec)# debug cpl ppcp event action <cr>
```

Handler ` RVA 0xD8B6F20 `；selector ` 45 `；EOL ` RVA 0x33F36AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011470

```text
(exec)# debug cpl ppcp event action add <cr>
```

Handler ` RVA 0xD8B8350 `；selector ` 46 `；EOL ` RVA 0x33F362B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011477

```text
(exec)# debug cpl ppcp event action delete <cr>
```

Handler ` RVA 0xD8B8150 `；selector ` 48 `；EOL ` RVA 0x33F36808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011474

```text
(exec)# debug cpl ppcp event action modify <cr>
```

Handler ` RVA 0xD8B8250 `；selector ` 47 `；EOL ` RVA 0x33F36560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010108

```text
(exec)# debug cpl ppcp event attribute <cr>
```

Handler ` RVA 0xD8B6DA0 `；selector ` 55 `；EOL ` RVA 0x33F383D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011478

```text
(exec)# debug cpl ppcp event attribute add <cr>
```

Handler ` RVA 0xD8B7C50 `；selector ` 56 `；EOL ` RVA 0x33F37E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011483

```text
(exec)# debug cpl ppcp event attribute delete <cr>
```

Handler ` RVA 0xD8B7B50 `；selector ` 57 `；EOL ` RVA 0x33F38130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010101

```text
(exec)# debug cpl ppcp event child-policy <cr>
```

Handler ` RVA 0xD8B6E20 `；selector ` 52 `；EOL ` RVA 0x33F37B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011475

```text
(exec)# debug cpl ppcp event child-policy add <cr>
```

Handler ` RVA 0xD8B7E50 `；selector ` 53 `；EOL ` RVA 0x33F37628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011479

```text
(exec)# debug cpl ppcp event child-policy delete <cr>
```

Handler ` RVA 0xD8B7D50 `；selector ` 54 `；EOL ` RVA 0x33F378D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010094

```text
(exec)# debug cpl ppcp event class-to-policy <cr>
```

Handler ` RVA 0xD8B6EA0 `；selector ` 49 `；EOL ` RVA 0x33F37318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011473

```text
(exec)# debug cpl ppcp event class-to-policy add <cr>
```

Handler ` RVA 0xD8B8050 `；selector ` 50 `；EOL ` RVA 0x33F36DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011476

```text
(exec)# debug cpl ppcp event class-to-policy delete <cr>
```

Handler ` RVA 0xD8B7F50 `；selector ` 51 `；EOL ` RVA 0x33F37070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010083

```text
(exec)# debug cpl ppcp event classmap <cr>
```

Handler ` RVA 0xD8B70B0 `；selector ` 35 `；EOL ` RVA 0x33F34EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011460

```text
(exec)# debug cpl ppcp event classmap add <cr>
```

Handler ` RVA 0xD8B8A50 `；selector ` 36 `；EOL ` RVA 0x33F346E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011464

```text
(exec)# debug cpl ppcp event classmap delete <cr>
```

Handler ` RVA 0xD8B8950 `；selector ` 37 `；EOL ` RVA 0x33F34990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011468

```text
(exec)# debug cpl ppcp event classmap logicalop <cr>
```

Handler ` RVA 0xD8B8850 `；selector ` 38 `；EOL ` RVA 0x33F34C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010086

```text
(exec)# debug cpl ppcp event filter <cr>
```

Handler ` RVA 0xD8B6FB0 `；selector ` 42 `；EOL ` RVA 0x33F35FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011465

```text
(exec)# debug cpl ppcp event filter add <cr>
```

Handler ` RVA 0xD8B8550 `；selector ` 43 `；EOL ` RVA 0x33F35A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011472

```text
(exec)# debug cpl ppcp event filter delete <cr>
```

Handler ` RVA 0xD8B8450 `；selector ` 44 `；EOL ` RVA 0x33F35D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010113

```text
(exec)# debug cpl ppcp event parameter-map <cr>
```

Handler ` RVA 0xD8B6D20 `；selector ` 58 `；EOL ` RVA 0x33F38C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011482

```text
(exec)# debug cpl ppcp event parameter-map add <cr>
```

Handler ` RVA 0xD8B7A50 `；selector ` 59 `；EOL ` RVA 0x33F386E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011487

```text
(exec)# debug cpl ppcp event parameter-map delete <cr>
```

Handler ` RVA 0xD8B7950 `；selector ` 60 `；EOL ` RVA 0x33F38990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010082

```text
(exec)# debug cpl ppcp event policymap <cr>
```

Handler ` RVA 0xD8B7030 `；selector ` 39 `；EOL ` RVA 0x33F35748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011462

```text
(exec)# debug cpl ppcp event policymap add <cr>
```

Handler ` RVA 0xD8B8750 `；selector ` 40 `；EOL ` RVA 0x33F351F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011467

```text
(exec)# debug cpl ppcp event policymap delete <cr>
```

Handler ` RVA 0xD8B8650 `；selector ` 41 `；EOL ` RVA 0x33F354A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010142

```text
(exec)# debug cpl ppcp event service-policy <cr>
```

Handler ` RVA 0xD8B6C70 `；selector ` 61 `；EOL ` RVA 0x33F39F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011511

```text
(exec)# debug cpl ppcp event service-policy activate <cr>
```

Handler ` RVA 0xD8B7350 `；selector ` 67 `；EOL ` RVA 0x33F39C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011486

```text
(exec)# debug cpl ppcp event service-policy install <cr>
```

Handler ` RVA 0xD8B7850 `；selector ` 62 `；EOL ` RVA 0x33F38F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011500

```text
(exec)# debug cpl ppcp event service-policy notify <cr>
```

Handler ` RVA 0xD8B7550 `；selector ` 65 `；EOL ` RVA 0x33F39740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011490

```text
(exec)# debug cpl ppcp event service-policy remove <cr>
```

Handler ` RVA 0xD8B7750 `；selector ` 63 `；EOL ` RVA 0x33F391F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011507

```text
(exec)# debug cpl ppcp event service-policy suspend <cr>
```

Handler ` RVA 0xD8B7450 `；selector ` 66 `；EOL ` RVA 0x33F399E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011495

```text
(exec)# debug cpl ppcp event service-policy update <cr>
```

Handler ` RVA 0xD8B7650 `；selector ` 64 `；EOL ` RVA 0x33F39498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011904

```text
(exec)# debug cpl ppcp event test client <number:0..7> <cr>
```

Handler ` RVA 0xD8B7200 `；selector ` 0 `；EOL ` RVA 0x33F33E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [参数 P-2c6ea141e3b82d7f](../../evidence/parameters-sets-004.md#p-2c6ea141e3b82d7f) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011906

```text
(exec)# debug cpl ppcp event test dbtype <number:0..1> <cr>
```

Handler ` RVA 0xD8B7270 `；selector ` 0 `；EOL ` RVA 0x33F34148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DBtype。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [参数 P-595d57db6988d233](../../evidence/parameters-sets-007.md#p-595d57db6988d233) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011902

```text
(exec)# debug cpl ppcp event test event <number:0..40> <cr>
```

Handler ` RVA 0xD8B72E0 `；selector ` 0 `；EOL ` RVA 0x33F33B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Event。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [参数 P-6f4791417319f946](../../evidence/parameters-sets-009.md#p-6f4791417319f946) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011469

```text
(exec)# debug cpl ppcp event test start <cr>
```

Handler ` RVA 0xD8BA7A0 `；selector ` 0 `；EOL ` RVA 0x33F343D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007328

```text
(exec)# debug cpl ppcp flow <cr>
```

Handler ` RVA 0xD8B63D0 `；selector ` 5 `；EOL ` RVA 0x33F3D8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010092

```text
(exec)# debug cpl ppcp flow db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33F3D640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010089

```text
(exec)# debug cpl ppcp flow prov <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33F3D398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007190

```text
(exec)# debug cpl ppcp infra <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x33F30BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007231

```text
(exec)# debug cpl ppcp ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x33F33788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007305

```text
(exec)# debug cpl ppcp level <cr>
```

Handler ` RVA 0xD8B6700 `；selector ` 68 `；EOL ` RVA 0x33F3BD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010073

```text
(exec)# debug cpl ppcp level brief <cr>
```

Handler ` RVA 0xD8B68C0 `；selector ` 71 `；EOL ` RVA 0x33F3B088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcb629a2e98ba93e](../../evidence/conditions-sets-098.md#c-fcb629a2e98ba93e) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010074

```text
(exec)# debug cpl ppcp level brief <cr>
```

Handler ` RVA 0xD8B7140 `；selector ` 71 `；EOL ` RVA 0x33F3B308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4fd4ce8630bb223](../../evidence/conditions-sets-070.md#c-b4fd4ce8630bb223) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010057

```text
(exec)# debug cpl ppcp level error <cr>
```

Handler ` RVA 0xD8B69B0 `；selector ` 69 `；EOL ` RVA 0x33F3A5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-919b506689a3a35a](../../evidence/conditions-sets-056.md#c-919b506689a3a35a) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010058

```text
(exec)# debug cpl ppcp level error <cr>
```

Handler ` RVA 0xD8B7140 `；selector ` 69 `；EOL ` RVA 0x33F3A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5581541575af0de8](../../evidence/conditions-sets-034.md#c-5581541575af0de8) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010079

```text
(exec)# debug cpl ppcp level normal <cr>
```

Handler ` RVA 0xD8B6830 `；selector ` 72 `；EOL ` RVA 0x33F3B5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e51a72961d9c16c](../../evidence/conditions-sets-055.md#c-8e51a72961d9c16c) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010080

```text
(exec)# debug cpl ppcp level normal <cr>
```

Handler ` RVA 0xD8B7140 `；selector ` 72 `；EOL ` RVA 0x33F3B858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71d295a07bc0f35a](../../evidence/conditions-sets-044.md#c-71d295a07bc0f35a) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010077

```text
(exec)# debug cpl ppcp level verbose <cr>
```

Handler ` RVA 0xD8B67A0 `；selector ` 73 `；EOL ` RVA 0x33F3BAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010066

```text
(exec)# debug cpl ppcp level warning <cr>
```

Handler ` RVA 0xD8B6940 `；selector ` 70 `；EOL ` RVA 0x33F3AB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-59f1db94572788a6](../../evidence/conditions-sets-035.md#c-59f1db94572788a6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010067

```text
(exec)# debug cpl ppcp level warning <cr>
```

Handler ` RVA 0xD8B7140 `；selector ` 70 `；EOL ` RVA 0x33F3ADB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b17cb75a3a10da69](../../evidence/conditions-sets-069.md#c-b17cb75a3a10da69) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007291

```text
(exec)# debug cpl ppcp ras-dbg <cr>
```

Handler ` RVA 0xD8B62D0 `；selector ` 8 `；EOL ` RVA 0x33F3D088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007272

```text
(exec)# debug cpl ppcp ras-fc <cr>
```

Handler ` RVA 0xD8B6280 `；selector ` 11 `；EOL ` RVA 0x33F3CB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007261

```text
(exec)# debug cpl ppcp ras-feature <cr>
```

Handler ` RVA 0xD8B61D0 `；selector ` 9 `；EOL ` RVA 0x33F3C890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007281

```text
(exec)# debug cpl ppcp ras-tc <cr>
```

Handler ` RVA 0xD8B6230 `；selector ` 10 `；EOL ` RVA 0x33F3CDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007245

```text
(exec)# debug cpl ppcp stats <cr>
```

Handler ` RVA 0xD8B6560 `；selector ` 29 `；EOL ` RVA 0x33F334E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010038

```text
(exec)# debug cpl ppcp stats ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 30 `；EOL ` RVA 0x33F32AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011456

```text
(exec)# debug cpl ppcp stats ipc ms <cr>
```

Handler ` RVA 0xE002120 `；selector ` 31 `；EOL ` RVA 0x33F32A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-010045

```text
(exec)# debug cpl ppcp stats update <cr>
```

Handler ` RVA 0xE002120 `；selector ` 32 `；EOL ` RVA 0x33F33010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-011458

```text
(exec)# debug cpl ppcp stats update ms <cr>
```

Handler ` RVA 0xE002120 `；selector ` 33 `；EOL ` RVA 0x33F32FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-192d3cf17f1b0fcb](../../evidence/state_effects-sets-006.md#s-192d3cf17f1b0fcb)

### path-007124

```text
(exec)# debug cpl provisioning api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33F597A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007187

```text
(exec)# debug cpl provisioning cce_dp_stubs <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33F5A790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c32c46cbd69e148](../../evidence/conditions-sets-030.md#c-4c32c46cbd69e148) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007180

```text
(exec)# debug cpl provisioning cce_for_test <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33F5A4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce1d6b7abf9ab6ca](../../evidence/conditions-sets-079.md#c-ce1d6b7abf9ab6ca) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007151

```text
(exec)# debug cpl provisioning db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33F59CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007162

```text
(exec)# debug cpl provisioning errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33F59F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007193

```text
(exec)# debug cpl provisioning non_nvgen_client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33F5AA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbd55ab6908bace3](../../evidence/conditions-sets-097.md#c-fbd55ab6908bace3) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007172

```text
(exec)# debug cpl provisioning test <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33F5A240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07500cea0dff8837](../../evidence/conditions-sets-003.md#c-07500cea0dff8837) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007139

```text
(exec)# debug cpl provisioning ttc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33F59A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-a3839071ac07bc7a](../../evidence/state_effects-sets-035.md#s-a3839071ac07bc7a)

### path-007183

```text
(exec)# debug cpl show detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 83 `；EOL ` RVA 0x33F308C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-abb53aa46136a842](../../evidence/state_effects-sets-036.md#s-abb53aa46136a842)

### path-003156

```text
(exec)# debug cpl vrf-target <cr>
```

Handler ` RVA 0xE002120 `；selector ` 84 `；EOL ` RVA 0x33F302D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-abb53aa46136a842](../../evidence/state_effects-sets-036.md#s-abb53aa46136a842)

### path-000408

```text
(exec)# debug crm <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 9 `；EOL ` RVA 0x37908458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-003409

```text
(exec)# debug crm all <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 10 `；EOL ` RVA 0x379081B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-003376

```text
(exec)# debug crm detail <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 2 `；EOL ` RVA 0x37906EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-003424

```text
(exec)# debug crm error <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 8 `；EOL ` RVA 0x37907A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-007369

```text
(exec)# debug crm error call <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 4 `；EOL ` RVA 0x37907528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-010119

```text
(exec)# debug crm error call informational <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 5 `；EOL ` RVA 0x37907500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-007374

```text
(exec)# debug crm error software <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 6 `；EOL ` RVA 0x37907A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-010126

```text
(exec)# debug crm error software informational <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 7 `；EOL ` RVA 0x37907A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-003386

```text
(exec)# debug crm function <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 3 `；EOL ` RVA 0x37907188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-003366

```text
(exec)# debug crm inout <cr>
```

Handler ` RVA 0x1E3CB320 `；selector ` 1 `；EOL ` RVA 0x37906C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-007427

```text
(exec)# debug crypto autovpn error <cr>
```

Handler ` RVA 0x165EC580 `；selector ` 1 `；EOL ` RVA 0x35FA61F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-1db99faf3406fb2b](../../evidence/state_effects-sets-007.md#s-1db99faf3406fb2b)

### path-007438

```text
(exec)# debug crypto autovpn events <cr>
```

Handler ` RVA 0x165EC580 `；selector ` 3 `；EOL ` RVA 0x35FA6498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-1db99faf3406fb2b](../../evidence/state_effects-sets-007.md#s-1db99faf3406fb2b)

### path-007444

```text
(exec)# debug crypto autovpn info <cr>
```

Handler ` RVA 0x165EC580 `；selector ` 2 `；EOL ` RVA 0x35FA6740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-1db99faf3406fb2b](../../evidence/state_effects-sets-007.md#s-1db99faf3406fb2b)

### path-007454

```text
(exec)# debug crypto autovpn verbose <cr>
```

Handler ` RVA 0x165EC580 `；selector ` 0 `；EOL ` RVA 0x35FA69E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-1db99faf3406fb2b](../../evidence/state_effects-sets-007.md#s-1db99faf3406fb2b)

### path-003475

```text
(exec)# debug crypto ber <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35750638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-003441

```text
(exec)# debug crypto engine <cr>
```

Handler ` RVA 0x120EBFB0 `；selector ` 0 `；EOL ` RVA 0x357962D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d72ae9f556f1d24a](../../evidence/conditions-sets-083.md#c-d72ae9f556f1d24a) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-010157

```text
(exec)# debug crypto engine accelerator control <cr>
```

Handler ` RVA 0x120CC450 `；selector ` 8 `；EOL ` RVA 0x3578E990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-011524

```text
(exec)# debug crypto engine accelerator control detail <cr>
```

Handler ` RVA 0x120CC530 `；selector ` 10 `；EOL ` RVA 0x3578E968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-011526

```text
(exec)# debug crypto engine accelerator control error <cr>
```

Handler ` RVA 0x120CC600 `；selector ` 12 `；EOL ` RVA 0x3578E450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-012058

```text
(exec)# debug crypto engine accelerator control error mask <number:0..4294967295> <cr>
```

Handler ` RVA 0x120CC670 `；selector ` 12 `；EOL ` RVA 0x3578E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` error mask。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [参数 P-e711b105fa994be6](../../evidence/parameters-sets-017.md#p-e711b105fa994be6) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-010168

```text
(exec)# debug crypto engine accelerator packet <cr>
```

Handler ` RVA 0x120CC4C0 `；selector ` 9 `；EOL ` RVA 0x3578FA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-011534

```text
(exec)# debug crypto engine accelerator packet detail <cr>
```

Handler ` RVA 0x120CC590 `；selector ` 11 `；EOL ` RVA 0x3578F4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-011529

```text
(exec)# debug crypto engine accelerator packet error <cr>
```

Handler ` RVA 0x120CC700 `；selector ` 13 `；EOL ` RVA 0x3578EF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-012059

```text
(exec)# debug crypto engine accelerator packet error mask <number:0..4294967295> <cr>
```

Handler ` RVA 0x120CC780 `；selector ` 13 `；EOL ` RVA 0x3578EF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` error mask。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [参数 P-0cf189e08b6c5053](../../evidence/parameters-sets-001.md#p-0cf189e08b6c5053) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-012139

```text
(exec)# debug crypto engine accelerator packet number <number:0..32767> length <number:0..32767> <cr>
```

Handler ` RVA 0x120CC820 `；selector ` 14 `；EOL ` RVA 0x3578F5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number limit；` unsigned_number ` packet length。

[条件 C-45462f8c9c854791](../../evidence/conditions-sets-027.md#c-45462f8c9c854791) · [参数 P-991e4c7ff6c5f7c9](../../evidence/parameters-sets-012.md#p-991e4c7ff6c5f7c9) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-007362

```text
(exec)# debug crypto engine error <cr>
```

Handler ` RVA 0x120EBFB0 `；selector ` 1 `；EOL ` RVA 0x35795AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d72ae9f556f1d24a](../../evidence/conditions-sets-083.md#c-d72ae9f556f1d24a) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-007383

```text
(exec)# debug crypto engine packet <cr>
```

Handler ` RVA 0x120EBFB0 `；selector ` 2 `；EOL ` RVA 0x35795DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d72ae9f556f1d24a](../../evidence/conditions-sets-083.md#c-d72ae9f556f1d24a) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-010133

```text
(exec)# debug crypto engine packet detail <cr>
```

Handler ` RVA 0x120EBFB0 `；selector ` 3 `；EOL ` RVA 0x35795D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d72ae9f556f1d24a](../../evidence/conditions-sets-083.md#c-d72ae9f556f1d24a) · [状态效果 S-fa3e8580ce89a2b8](../../evidence/state_effects-sets-053.md#s-fa3e8580ce89a2b8)

### path-010193

```text
(exec)# debug crypto engine vpn_hw all <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 0 `；EOL ` RVA 0x35791350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-e55ed4a297a37126](../../evidence/state_effects-sets-048.md#s-e55ed4a297a37126)

### path-010188

```text
(exec)# debug crypto engine vpn_hw buffer <cr>
```

Handler ` RVA 0x120CC040 `；selector ` 0 `；EOL ` RVA 0x35791098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-ce14bd564a47f9ea](../../evidence/state_effects-sets-044.md#s-ce14bd564a47f9ea)

### path-010174

```text
(exec)# debug crypto engine vpn_hw error <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 6 `；EOL ` RVA 0x35790B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-c3f675a8ca56c893](../../evidence/state_effects-sets-041.md#s-c3f675a8ca56c893)

### path-010156

```text
(exec)# debug crypto engine vpn_hw high <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 5 `；EOL ` RVA 0x35790300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-383a4ba5c62f346d](../../evidence/state_effects-sets-012.md#s-383a4ba5c62f346d)

### path-010166

```text
(exec)# debug crypto engine vpn_hw low <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 3 `；EOL ` RVA 0x35790870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-8930de2137a9b506](../../evidence/state_effects-sets-029.md#s-8930de2137a9b506)

### path-010159

```text
(exec)# debug crypto engine vpn_hw medium <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 4 `；EOL ` RVA 0x357905B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-e1533174e57fe5c6](../../evidence/state_effects-sets-048.md#s-e1533174e57fe5c6)

### path-010153

```text
(exec)# debug crypto engine vpn_hw normal <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 2 `；EOL ` RVA 0x35790048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-56505828c487b0c7](../../evidence/state_effects-sets-019.md#s-56505828c487b0c7)

### path-010150

```text
(exec)# debug crypto engine vpn_hw packet <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 7 `；EOL ` RVA 0x3578FD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-0361f111d3ac3f5b](../../evidence/state_effects-sets-001.md#s-0361f111d3ac3f5b)

### path-010182

```text
(exec)# debug crypto engine vpn_hw stat <cr>
```

Handler ` RVA 0x120CAE90 `；selector ` 1 `；EOL ` RVA 0x35790DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2006de76d733f35e](../../evidence/conditions-sets-012.md#c-2006de76d733f35e) · [状态效果 S-96a62d24d31d59cf](../../evidence/state_effects-sets-032.md#s-96a62d24d31d59cf)

### path-003482

```text
(exec)# debug crypto est-client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35A764F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-34ce8d7b25dcd112](../../evidence/state_effects-sets-012.md#s-34ce8d7b25dcd112)

### path-007445

```text
(exec)# debug crypto pki API <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3575B380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007470

```text
(exec)# debug crypto pki callbacks <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3575BB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007429

```text
(exec)# debug crypto pki messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3575AB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007455

```text
(exec)# debug crypto pki scep <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x3575B628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007450

```text
(exec)# debug crypto pki server <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33871B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-010163

```text
(exec)# debug crypto pki server performance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33871B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007449

```text
(exec)# debug crypto pki transactions <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3575AEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-010162

```text
(exec)# debug crypto pki transactions performance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x3575AE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-007464

```text
(exec)# debug crypto pki validation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x3575B8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-003445

```text
(exec)# debug crypto socket <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x35444AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6705272aaecdbda](../../evidence/conditions-sets-076.md#c-c6705272aaecdbda) · [状态效果 S-5dce66fac8d91968](../../evidence/state_effects-sets-020.md#s-5dce66fac8d91968)

### path-003481

```text
(exec)# debug crypto verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x357508E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-707aa3a79303a770](../../evidence/state_effects-sets-024.md#s-707aa3a79303a770)

### path-003495

```text
(exec)# debug crypto wui <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x359E42C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1069c5604f3222c0](../../evidence/conditions-sets-007.md#c-1069c5604f3222c0) · [状态效果 S-1d7451d52253c597](../../evidence/state_effects-sets-007.md#s-1d7451d52253c597)

### path-000318

```text
(exec)# debug cts <cr>
```

Handler ` RVA 0x1300DA00 `；selector ` 1 `；EOL ` RVA 0x35A0FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d8d19433e2cb2c4](../../evidence/conditions-sets-049.md#c-7d8d19433e2cb2c4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002118

```text
(exec)# debug cts aaa <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 8 `；EOL ` RVA 0x35A06D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a18b00846fae765](../../evidence/conditions-sets-029.md#c-4a18b00846fae765) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002398

```text
(exec)# debug cts all <cr>
```

Handler ` RVA 0x1300D8E0 `；selector ` 1 `；EOL ` RVA 0x35A0F788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d8d19433e2cb2c4](../../evidence/conditions-sets-049.md#c-7d8d19433e2cb2c4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005885

```text
(exec)# debug cts authentication details <cr>
```

Handler ` RVA 0x1300D2A0 `；selector ` 1 `；EOL ` RVA 0x35A03888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ea2556a53cce53f](../../evidence/conditions-sets-006.md#c-0ea2556a53cce53f) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005857

```text
(exec)# debug cts authentication events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 2 `；EOL ` RVA 0x35A035E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ea2556a53cce53f](../../evidence/conditions-sets-006.md#c-0ea2556a53cce53f) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009325

```text
(exec)# debug cts authorization aaa critical <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 2 `；EOL ` RVA 0x35A062B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009262

```text
(exec)# debug cts authorization aaa debug <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 7 `；EOL ` RVA 0x35A05568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009344

```text
(exec)# debug cts authorization aaa emergency <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 0 `；EOL ` RVA 0x35A06558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009309

```text
(exec)# debug cts authorization aaa error <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 3 `；EOL ` RVA 0x35A06008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009272

```text
(exec)# debug cts authorization aaa info <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 6 `；EOL ` RVA 0x35A05810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009285

```text
(exec)# debug cts authorization aaa notice <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 5 `；EOL ` RVA 0x35A05AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009249

```text
(exec)# debug cts authorization aaa verbose <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 8 `；EOL ` RVA 0x35A052C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-009299

```text
(exec)# debug cts authorization aaa warning <cr>
```

Handler ` RVA 0x1300DC80 `；selector ` 4 `；EOL ` RVA 0x35A05D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4195cf8fd0fb48cb](../../evidence/conditions-sets-026.md#c-4195cf8fd0fb48cb) · [状态效果 S-50cfad3dd67e0557](../../evidence/state_effects-sets-018.md#s-50cfad3dd67e0557)

### path-002269

```text
(exec)# debug cts cache <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 1 `；EOL ` RVA 0x35A09BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1cec47299e55bd1](../../evidence/conditions-sets-087.md#c-e1cec47299e55bd1) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006279

```text
(exec)# debug cts coa events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 43 `；EOL ` RVA 0x35A0C9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78b07c32b5b7a4ed](../../evidence/conditions-sets-047.md#c-78b07c32b5b7a4ed) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006311

```text
(exec)# debug cts critical-authentication error <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 45 `；EOL ` RVA 0x35A0CF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8aa41c8f0701afe8](../../evidence/conditions-sets-054.md#c-8aa41c8f0701afe8) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006274

```text
(exec)# debug cts critical-authentication event <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 44 `；EOL ` RVA 0x35A0CCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8aa41c8f0701afe8](../../evidence/conditions-sets-054.md#c-8aa41c8f0701afe8) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006053

```text
(exec)# debug cts dp Info <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 20 `；EOL ` RVA 0x35A084C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec1ad82c5e50c6c6](../../evidence/conditions-sets-091.md#c-ec1ad82c5e50c6c6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006084

```text
(exec)# debug cts dp errors <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 19 `；EOL ` RVA 0x35A08770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec1ad82c5e50c6c6](../../evidence/conditions-sets-091.md#c-ec1ad82c5e50c6c6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006108

```text
(exec)# debug cts dp packets <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 18 `；EOL ` RVA 0x35A08A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec1ad82c5e50c6c6](../../evidence/conditions-sets-091.md#c-ec1ad82c5e50c6c6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002202

```text
(exec)# debug cts environment-data <cr>
```

Handler ` RVA 0x1300D640 `；selector ` 53 `；EOL ` RVA 0x35A04BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005878

```text
(exec)# debug cts environment-data aaa <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 9 `；EOL ` RVA 0x35A03BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006020

```text
(exec)# debug cts environment-data default-epg <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 52 `；EOL ` RVA 0x35A04910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005992

```text
(exec)# debug cts environment-data default-sg <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 51 `；EOL ` RVA 0x35A04668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005905

```text
(exec)# debug cts environment-data events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 10 `；EOL ` RVA 0x35A03E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005965

```text
(exec)# debug cts environment-data platform <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 50 `；EOL ` RVA 0x35A043C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005937

```text
(exec)# debug cts environment-data sg-epg <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 49 `；EOL ` RVA 0x35A04118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99e0dd925733284](../../evidence/conditions-sets-084.md#c-d99e0dd925733284) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002038

```text
(exec)# debug cts error <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 0 `；EOL ` RVA 0x35A03290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fdab3ab31b92922c](../../evidence/conditions-sets-098.md#c-fdab3ab31b92922c) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006006

```text
(exec)# debug cts fips events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 15 `；EOL ` RVA 0x35A078F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61d6808e9097642a](../../evidence/conditions-sets-038.md#c-61d6808e9097642a) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006240

```text
(exec)# debug cts ha config <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 36 `；EOL ` RVA 0x35A0B268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006391

```text
(exec)# debug cts ha core <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 35 `；EOL ` RVA 0x35A0C0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009496

```text
(exec)# debug cts ha core bindings <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 42 `；EOL ` RVA 0x35A0C3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-011234

```text
(exec)# debug cts ha core bindings events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 41 `；EOL ` RVA 0x35A0C108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009457

```text
(exec)# debug cts ha core environment-data <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 38 `；EOL ` RVA 0x35A0B860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-011211

```text
(exec)# debug cts ha core environment-data events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 37 `；EOL ` RVA 0x35A0B5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009475

```text
(exec)# debug cts ha core policy <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 40 `；EOL ` RVA 0x35A0BE08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-011224

```text
(exec)# debug cts ha core policy events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 39 `；EOL ` RVA 0x35A0BB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006208

```text
(exec)# debug cts ha infra <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 34 `；EOL ` RVA 0x35A0AFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56c2cc026ecf6651](../../evidence/conditions-sets-034.md#c-56c2cc026ecf6651) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006058

```text
(exec)# debug cts ifc cache <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 16 `；EOL ` RVA 0x35A07ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b956aaf494b43788](../../evidence/conditions-sets-072.md#c-b956aaf494b43788) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006031

```text
(exec)# debug cts ifc events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 14 `；EOL ` RVA 0x35A07C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b956aaf494b43788](../../evidence/conditions-sets-072.md#c-b956aaf494b43788) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006086

```text
(exec)# debug cts ifc snmp <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 17 `；EOL ` RVA 0x35A08178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b956aaf494b43788](../../evidence/conditions-sets-072.md#c-b956aaf494b43788) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002244

```text
(exec)# debug cts layer3-trustsec <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 26 `；EOL ` RVA 0x35A098D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b3cd6942896333f](../../evidence/conditions-sets-011.md#c-1b3cd6942896333f) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-001999

```text
(exec)# debug cts odm <cr>
```

Handler ` RVA 0x1300D1C0 `；selector ` 54 `；EOL ` RVA 0x35A02CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-10af947d6be6b473](../../evidence/conditions-sets-007.md#c-10af947d6be6b473) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006442

```text
(exec)# debug cts policy-server all <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 56 `；EOL ` RVA 0x35A0F498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009488

```text
(exec)# debug cts policy-server http all <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 62 `；EOL ` RVA 0x35A0E130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009438

```text
(exec)# debug cts policy-server http error <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 60 `；EOL ` RVA 0x35A0DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009463

```text
(exec)# debug cts policy-server http events <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 61 `；EOL ` RVA 0x35A0DE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009508

```text
(exec)# debug cts policy-server json all <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 59 `；EOL ` RVA 0x35A0E990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009459

```text
(exec)# debug cts policy-server json error <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 57 `；EOL ` RVA 0x35A0E440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009487

```text
(exec)# debug cts policy-server json events <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 58 `；EOL ` RVA 0x35A0E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009533

```text
(exec)# debug cts policy-server selection all <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 65 `；EOL ` RVA 0x35A0F1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009483

```text
(exec)# debug cts policy-server selection error <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 63 `；EOL ` RVA 0x35A0ECA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-009507

```text
(exec)# debug cts policy-server selection events <cr>
```

Handler ` RVA 0x1300EFB0 `；selector ` 64 `；EOL ` RVA 0x35A0EF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8cbb873905b8b92](../../evidence/conditions-sets-090.md#c-e8cbb873905b8b92) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006102

```text
(exec)# debug cts provisioning events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 23 `；EOL ` RVA 0x35A09350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46bf9e85d5e4955d](../../evidence/conditions-sets-028.md#c-46bf9e85d5e4955d) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006131

```text
(exec)# debug cts provisioning packets <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 24 `；EOL ` RVA 0x35A095F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46bf9e85d5e4955d](../../evidence/conditions-sets-028.md#c-46bf9e85d5e4955d) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006374

```text
(exec)# debug cts rcl-server all <cr>
```

Handler ` RVA 0x1300EEC0 `；selector ` 48 `；EOL ` RVA 0x35A0D828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2452875f981d4bd6](../../evidence/conditions-sets-014.md#c-2452875f981d4bd6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006335

```text
(exec)# debug cts rcl-server errors <cr>
```

Handler ` RVA 0x1300EEC0 `；selector ` 47 `；EOL ` RVA 0x35A0D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2452875f981d4bd6](../../evidence/conditions-sets-014.md#c-2452875f981d4bd6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006307

```text
(exec)# debug cts rcl-server events <cr>
```

Handler ` RVA 0x1300EEC0 `；selector ` 46 `；EOL ` RVA 0x35A0D2D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2452875f981d4bd6](../../evidence/conditions-sets-014.md#c-2452875f981d4bd6) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006081

```text
(exec)# debug cts relay event <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 21 `；EOL ` RVA 0x35A08D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3386c5bd42d8f997](../../evidence/conditions-sets-020.md#c-3386c5bd42d8f997) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006106

```text
(exec)# debug cts relay pak <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 22 `；EOL ` RVA 0x35A09010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3386c5bd42d8f997](../../evidence/conditions-sets-020.md#c-3386c5bd42d8f997) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-005983

```text
(exec)# debug cts sap events <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 11 `；EOL ` RVA 0x35A07050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2cad383b2f7662b](../../evidence/conditions-sets-081.md#c-d2cad383b2f7662b) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006011

```text
(exec)# debug cts sap packets <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 12 `；EOL ` RVA 0x35A072F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2cad383b2f7662b](../../evidence/conditions-sets-081.md#c-d2cad383b2f7662b) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006037

```text
(exec)# debug cts sap pakdump <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 13 `；EOL ` RVA 0x35A075A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2cad383b2f7662b](../../evidence/conditions-sets-081.md#c-d2cad383b2f7662b) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002080

```text
(exec)# debug cts server-list <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 7 `；EOL ` RVA 0x35A04ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1bcde8be35ccc165](../../evidence/conditions-sets-011.md#c-1bcde8be35ccc165) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-002016

```text
(exec)# debug cts sgacl-db <cr>
```

Handler ` RVA 0x1300D0E0 `；selector ` 55 `；EOL ` RVA 0x35A02FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-222d0ca3f6d0a2f9](../../evidence/conditions-sets-013.md#c-222d0ca3f6d0a2f9) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-001980

```text
(exec)# debug cts states <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 25 `；EOL ` RVA 0x35A029D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58f1412dc394f230](../../evidence/conditions-sets-035.md#c-58f1412dc394f230) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006212

```text
(exec)# debug cts sxp conn <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 29 `；EOL ` RVA 0x35A0A1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006340

```text
(exec)# debug cts sxp error <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 32 `；EOL ` RVA 0x35A0AC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006313

```text
(exec)# debug cts sxp filter <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 33 `；EOL ` RVA 0x35A0A9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006181

```text
(exec)# debug cts sxp internal <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 28 `；EOL ` RVA 0x35A09F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006283

```text
(exec)# debug cts sxp mdb <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 31 `；EOL ` RVA 0x35A0A700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-006244

```text
(exec)# debug cts sxp message <cr>
```

Handler ` RVA 0x1300DB10 `；selector ` 30 `；EOL ` RVA 0x35A0A458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-771cdb2e931906a4](../../evidence/conditions-sets-046.md#c-771cdb2e931906a4) · [状态效果 S-f1b8cb393aa26015](../../evidence/state_effects-sets-051.md#s-f1b8cb393aa26015)

### path-000083

```text
(exec)# debug custom-queue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3419AFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-34f19ce6aed53806](../../evidence/state_effects-sets-012.md#s-34f19ce6aed53806)

### path-000451

```text
(exec)# debug cwan <cr>
```

Handler ` RVA 0xE002120 `；selector ` 74 `；EOL ` RVA 0x34035538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003772

```text
(exec)# debug cwan alarm <cr>
```

Handler ` RVA 0xE002120 `；selector ` 71 `；EOL ` RVA 0x340331D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003888

```text
(exec)# debug cwan atom <cr>
```

Handler ` RVA 0xE002120 `；selector ` 77 `；EOL ` RVA 0x34034D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007745

```text
(exec)# debug cwan atom cf <cr>
```

Handler ` RVA 0xE002120 `；selector ` 84 `；EOL ` RVA 0x340347D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007712

```text
(exec)# debug cwan atom circuit-idx <cr>
```

Handler ` RVA 0xE002120 `；selector ` 82 `；EOL ` RVA 0x34034280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007679

```text
(exec)# debug cwan atom entry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 81 `；EOL ` RVA 0x34033A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007729

```text
(exec)# debug cwan atom ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 83 `；EOL ` RVA 0x34034528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007768

```text
(exec)# debug cwan atom issu <cr>
```

Handler ` RVA 0xE002120 `；selector ` 86 `；EOL ` RVA 0x34034D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007698

```text
(exec)# debug cwan atom msg <cr>
```

Handler ` RVA 0xE002120 `；selector ` 80 `；EOL ` RVA 0x34033FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007756

```text
(exec)# debug cwan atom rf <cr>
```

Handler ` RVA 0xE002120 `；selector ` 85 `；EOL ` RVA 0x34034A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007687

```text
(exec)# debug cwan atom stats <cr>
```

Handler ` RVA 0xE002120 `；selector ` 79 `；EOL ` RVA 0x34033D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003784

```text
(exec)# debug cwan bridge <cr>
```

Handler ` RVA 0xE002120 `；selector ` 72 `；EOL ` RVA 0x34033480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007639

```text
(exec)# debug cwan choc-dsx resets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 70 `；EOL ` RVA 0x34032730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007624

```text
(exec)# debug cwan choc-dsx semaphore <cr>
```

Handler ` RVA 0xE002120 `；selector ` 66 `；EOL ` RVA 0x34032488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003662

```text
(exec)# debug cwan choc-error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x34029518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003671

```text
(exec)# debug cwan choc-event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x340297C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007655

```text
(exec)# debug cwan chocx config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 33 `；EOL ` RVA 0x34031C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007612

```text
(exec)# debug cwan chocx error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x34031410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007641

```text
(exec)# debug cwan chocx events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 30 `；EOL ` RVA 0x34031960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007673

```text
(exec)# debug cwan chocx love-letters <cr>
```

Handler ` RVA 0xE002120 `；selector ` 31 `；EOL ` RVA 0x34032158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007667

```text
(exec)# debug cwan chocx mib <cr>
```

Handler ` RVA 0xE002120 `；selector ` 32 `；EOL ` RVA 0x34031EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007626

```text
(exec)# debug cwan chocx state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 29 `；EOL ` RVA 0x340316B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003652

```text
(exec)# debug cwan cmd-retry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34029270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003646

```text
(exec)# debug cwan cmd-timeout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34028FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003789

```text
(exec)# debug cwan ct3 <cr>
```

Handler ` RVA 0xE002120 `；selector ` 16 `；EOL ` RVA 0x3402B038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007658

```text
(exec)# debug cwan ct3 config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 23 `；EOL ` RVA 0x3402B010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007598

```text
(exec)# debug cwan ct3 error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x3402A2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007586

```text
(exec)# debug cwan ct3 event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x3402A020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007618

```text
(exec)# debug cwan ct3 loveletter <cr>
```

Handler ` RVA 0xE002120 `；selector ` 20 `；EOL ` RVA 0x3402A818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007632

```text
(exec)# debug cwan ct3 mib <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x3402AAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007610

```text
(exec)# debug cwan ct3 state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x3402A570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007645

```text
(exec)# debug cwan ct3 stats <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x3402AD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003613

```text
(exec)# debug cwan dss <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x340287D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007671

```text
(exec)# debug cwan hw-module queue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 73 `；EOL ` RVA 0x34033790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003586

```text
(exec)# debug cwan icc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x34027D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003593

```text
(exec)# debug cwan ifcom <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x34027FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007695

```text
(exec)# debug cwan ifmgr error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 76 `；EOL ` RVA 0x34035578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007709

```text
(exec)# debug cwan ifmgr trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 75 `；EOL ` RVA 0x34035820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003576

```text
(exec)# debug cwan interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x34027A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003818

```text
(exec)# debug cwan localsw <cr>
```

Handler ` RVA 0xE002120 `；selector ` 78 `；EOL ` RVA 0x34035268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003599

```text
(exec)# debug cwan logger <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x34028280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003607

```text
(exec)# debug cwan love <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x34028528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003788

```text
(exec)# debug cwan ltl <cr>
```

Handler ` RVA 0xE002120 `；selector ` 69 `；EOL ` RVA 0x34032D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007651

```text
(exec)# debug cwan ltl plat-idx <cr>
```

Handler ` RVA 0xE002120 `；selector ` 67 `；EOL ` RVA 0x34032CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007635

```text
(exec)# debug cwan ltl skip-sp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 68 `；EOL ` RVA 0x34032A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003624

```text
(exec)# debug cwan oir <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34028A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003634

```text
(exec)# debug cwan pc-lb <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34028D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003857

```text
(exec)# debug cwan redundancy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 36 `；EOL ` RVA 0x34030380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010248

```text
(exec)# debug cwan redundancy aps all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 65 `；EOL ` RVA 0x3402B620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010258

```text
(exec)# debug cwan redundancy aps bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 63 `；EOL ` RVA 0x3402BB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010253

```text
(exec)# debug cwan redundancy aps incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 64 `；EOL ` RVA 0x3402B8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010280

```text
(exec)# debug cwan redundancy ccb all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 46 `；EOL ` RVA 0x3402EB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010292

```text
(exec)# debug cwan redundancy ccb bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 44 `；EOL ` RVA 0x3402F058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010288

```text
(exec)# debug cwan redundancy ccb incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 45 `；EOL ` RVA 0x3402EDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007690

```text
(exec)# debug cwan redundancy channelized-vc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 40 `；EOL ` RVA 0x3402FB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007714

```text
(exec)# debug cwan redundancy deferred <cr>
```

Handler ` RVA 0xE002120 `；selector ` 38 `；EOL ` RVA 0x340300B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010266

```text
(exec)# debug cwan redundancy if-config all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 55 `；EOL ` RVA 0x3402D1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010278

```text
(exec)# debug cwan redundancy if-config bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 53 `；EOL ` RVA 0x3402D738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010273

```text
(exec)# debug cwan redundancy if-config incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 54 `；EOL ` RVA 0x3402D490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010272

```text
(exec)# debug cwan redundancy if-event all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 52 `；EOL ` RVA 0x3402DA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010283

```text
(exec)# debug cwan redundancy if-event bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 50 `；EOL ` RVA 0x3402DF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010277

```text
(exec)# debug cwan redundancy if-event incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 51 `；EOL ` RVA 0x3402DCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010276

```text
(exec)# debug cwan redundancy if-index all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 49 `；EOL ` RVA 0x3402E2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010289

```text
(exec)# debug cwan redundancy if-index bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 47 `；EOL ` RVA 0x3402E7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010281

```text
(exec)# debug cwan redundancy if-index incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 48 `；EOL ` RVA 0x3402E550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007731

```text
(exec)# debug cwan redundancy reload <cr>
```

Handler ` RVA 0xE002120 `；selector ` 37 `；EOL ` RVA 0x34030358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010286

```text
(exec)# debug cwan redundancy slot-info all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 43 `；EOL ` RVA 0x3402F368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010297

```text
(exec)# debug cwan redundancy slot-info bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 41 `；EOL ` RVA 0x3402F8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010291

```text
(exec)# debug cwan redundancy slot-info incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 42 `；EOL ` RVA 0x3402F610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007617

```text
(exec)# debug cwan redundancy spa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 59 `；EOL ` RVA 0x3402C678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010252

```text
(exec)# debug cwan redundancy srp all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 62 `；EOL ` RVA 0x3402BE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010263

```text
(exec)# debug cwan redundancy srp bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 60 `；EOL ` RVA 0x3402C3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010257

```text
(exec)# debug cwan redundancy srp incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 61 `；EOL ` RVA 0x3402C128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007700

```text
(exec)# debug cwan redundancy switchover <cr>
```

Handler ` RVA 0xE002120 `；selector ` 39 `；EOL ` RVA 0x3402FE08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010260

```text
(exec)# debug cwan redundancy vlan all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 58 `；EOL ` RVA 0x3402C988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010274

```text
(exec)# debug cwan redundancy vlan bulk <cr>
```

Handler ` RVA 0xE002120 `；selector ` 56 `；EOL ` RVA 0x3402CED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-010267

```text
(exec)# debug cwan redundancy vlan incr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 57 `；EOL ` RVA 0x3402CC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003558

```text
(exec)# debug cwan set <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x34027538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003566

```text
(exec)# debug cwan single-spa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x340277E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003683

```text
(exec)# debug cwan srp-error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 34 `；EOL ` RVA 0x34029A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003692

```text
(exec)# debug cwan srp-event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 35 `；EOL ` RVA 0x34029D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-003763

```text
(exec)# debug cwan t3e3 <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x34030EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007614

```text
(exec)# debug cwan t3e3 error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x34030BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007604

```text
(exec)# debug cwan t3e3 event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x34030948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-007628

```text
(exec)# debug cwan t3e3 state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x34030E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-215bdc125765249a](../../evidence/state_effects-sets-008.md#s-215bdc125765249a)

### path-002974

```text
(exec)# debug cwmp all <cr>
```

Handler ` RVA 0x16474040 `；selector ` 111 `；EOL ` RVA 0x35F8DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d36b24f02e63ae6f](../../evidence/state_effects-sets-045.md#s-d36b24f02e63ae6f)

### path-002937

```text
(exec)# debug cwmp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35F8D778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d36b24f02e63ae6f](../../evidence/state_effects-sets-045.md#s-d36b24f02e63ae6f)

### path-002947

```text
(exec)# debug cwmp profile <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35F8D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d36b24f02e63ae6f](../../evidence/state_effects-sets-045.md#s-d36b24f02e63ae6f)

### path-007030

```text
(exec)# debug cwmp profile error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35F8D280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d36b24f02e63ae6f](../../evidence/state_effects-sets-045.md#s-d36b24f02e63ae6f)

### path-002954

```text
(exec)# debug cwmp trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35F8DA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d36b24f02e63ae6f](../../evidence/state_effects-sets-045.md#s-d36b24f02e63ae6f)

### path-000687

```text
(exec)# debug dampening all <cr>
```

Handler ` RVA 0xE47A6F0 `；selector ` 1 `；EOL ` RVA 0x342C40A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d9230bed9d7a0b35](../../evidence/state_effects-sets-046.md#s-d9230bed9d7a0b35)

### path-000673

```text
(exec)# debug dampening interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x342C3E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-d9230bed9d7a0b35](../../evidence/state_effects-sets-046.md#s-d9230bed9d7a0b35)

### path-003537

```text
(exec)# debug data-descriptor entry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33E7E818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3a75e784f12e95c](../../evidence/conditions-sets-082.md#c-d3a75e784f12e95c) · [状态效果 S-200892efd0c2a43b](../../evidence/state_effects-sets-007.md#s-200892efd0c2a43b)

### path-003527

```text
(exec)# debug data-descriptor node <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33E7E570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3a75e784f12e95c](../../evidence/conditions-sets-082.md#c-d3a75e784f12e95c) · [状态效果 S-200892efd0c2a43b](../../evidence/state_effects-sets-007.md#s-200892efd0c2a43b)

### path-003543

```text
(exec)# debug data-descriptor other <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33E7EAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3a75e784f12e95c](../../evidence/conditions-sets-082.md#c-d3a75e784f12e95c) · [状态效果 S-200892efd0c2a43b](../../evidence/state_effects-sets-007.md#s-200892efd0c2a43b)

### path-007430

```text
(exec)# debug dcm core all <cr>
```

Handler ` RVA 0xBCC13D0 `；selector ` 0 `；EOL ` RVA 0x3389DEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-007406

```text
(exec)# debug dcm core error <cr>
```

Handler ` RVA 0xBCC1550 `；selector ` 0 `；EOL ` RVA 0x3389D940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-6b31bbdf8f393f31](../../evidence/state_effects-sets-023.md#s-6b31bbdf8f393f31)

### path-007417

```text
(exec)# debug dcm core info <cr>
```

Handler ` RVA 0xBCC1550 `；selector ` 1 `；EOL ` RVA 0x3389DBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-2b4f3fa964b83f80](../../evidence/state_effects-sets-010.md#s-2b4f3fa964b83f80)

### path-010192

```text
(exec)# debug dcm provider cmd error <cr>
```

Handler ` RVA 0xBC536A0 `；selector ` 5 `；EOL ` RVA 0x3387E6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c0e0d3021b4a4a09](../../evidence/state_effects-sets-041.md#s-c0e0d3021b4a4a09)

### path-010185

```text
(exec)# debug dcm provider cmd info <cr>
```

Handler ` RVA 0xBC536A0 `；selector ` 4 `；EOL ` RVA 0x3387E3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-6e7250f737cc65e3](../../evidence/state_effects-sets-023.md#s-6e7250f737cc65e3)

### path-010186

```text
(exec)# debug dcm provider expression error <cr>
```

Handler ` RVA 0xBCC5D90 `；selector ` 3 `；EOL ` RVA 0x338A1AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-988a1805b3e17cb3](../../evidence/state_effects-sets-032.md#s-988a1805b3e17cb3)

### path-010179

```text
(exec)# debug dcm provider expression info <cr>
```

Handler ` RVA 0xBCC5D90 `；selector ` 2 `；EOL ` RVA 0x338A1840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-99d2928e2d340a51](../../evidence/state_effects-sets-033.md#s-99d2928e2d340a51)

### path-010180

```text
(exec)# debug dcm provider snmp error <cr>
```

Handler ` RVA 0xBC4E190 `；selector ` 1 `；EOL ` RVA 0x3387DE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e85b75a7b133499e](../../evidence/state_effects-sets-049.md#s-e85b75a7b133499e)

### path-010170

```text
(exec)# debug dcm provider snmp info <cr>
```

Handler ` RVA 0xBC4E190 `；selector ` 0 `；EOL ` RVA 0x3387DB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-26a76da58ada31c4](../../evidence/state_effects-sets-009.md#s-26a76da58ada31c4)

### path-010165

```text
(exec)# debug dcm services client all <cr>
```

Handler ` RVA 0xBCC13D0 `；selector ` 1 `；EOL ` RVA 0x3389EDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011538

```text
(exec)# debug dcm services client any-ipc error <cr>
```

Handler ` RVA 0xBCC16D0 `；selector ` 3 `；EOL ` RVA 0x3389EB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4059651a6a84d6e7](../../evidence/state_effects-sets-014.md#s-4059651a6a84d6e7)

### path-011531

```text
(exec)# debug dcm services client any-ipc info <cr>
```

Handler ` RVA 0xBCC16D0 `；selector ` 2 `；EOL ` RVA 0x3389E868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-628aab7326a260f2](../../evidence/state_effects-sets-021.md#s-628aab7326a260f2)

### path-011532

```text
(exec)# debug dcm services client api-infra error <cr>
```

Handler ` RVA 0xBCC1610 `；selector ` 1 `；EOL ` RVA 0x3389E550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4b8d689101474831](../../evidence/state_effects-sets-017.md#s-4b8d689101474831)

### path-011527

```text
(exec)# debug dcm services client api-infra info <cr>
```

Handler ` RVA 0xBCC1610 `；selector ` 0 `；EOL ` RVA 0x3389E298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-081a92f823600f25](../../evidence/state_effects-sets-002.md#s-081a92f823600f25)

### path-010173

```text
(exec)# debug dcm services core all <cr>
```

Handler ` RVA 0xBCC13D0 `；selector ` 3 `；EOL ` RVA 0x3389FC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011542

```text
(exec)# debug dcm services core any-ipc error <cr>
```

Handler ` RVA 0xBCC18F0 `；selector ` 3 `；EOL ` RVA 0x3389F9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-43628fc2cec104e6](../../evidence/state_effects-sets-015.md#s-43628fc2cec104e6)

### path-011536

```text
(exec)# debug dcm services core any-ipc info <cr>
```

Handler ` RVA 0xBCC18F0 `；selector ` 2 `；EOL ` RVA 0x3389F718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-5a85106f69e18616](../../evidence/state_effects-sets-019.md#s-5a85106f69e18616)

### path-011537

```text
(exec)# debug dcm services core api-infra error <cr>
```

Handler ` RVA 0xBCC17E0 `；selector ` 1 `；EOL ` RVA 0x3389F400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-42fca87ef48d53c8](../../evidence/state_effects-sets-015.md#s-42fca87ef48d53c8)

### path-011530

```text
(exec)# debug dcm services core api-infra info <cr>
```

Handler ` RVA 0xBCC17E0 `；selector ` 0 `；EOL ` RVA 0x3389F148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-71a20563c8e89f7d](../../evidence/state_effects-sets-024.md#s-71a20563c8e89f7d)

### path-010181

```text
(exec)# debug dcm services provider all <cr>
```

Handler ` RVA 0xBCC13D0 `；selector ` 2 `；EOL ` RVA 0x338A0B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011544

```text
(exec)# debug dcm services provider any-ipc error <cr>
```

Handler ` RVA 0xBCC1B10 `；selector ` 3 `；EOL ` RVA 0x338A0858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-36bbd4ee57e08725](../../evidence/state_effects-sets-012.md#s-36bbd4ee57e08725)

### path-011540

```text
(exec)# debug dcm services provider any-ipc info <cr>
```

Handler ` RVA 0xBCC1B10 `；selector ` 2 `；EOL ` RVA 0x338A05A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9d6535cec7b1077d](../../evidence/state_effects-sets-033.md#s-9d6535cec7b1077d)

### path-011541

```text
(exec)# debug dcm services provider api-infra error <cr>
```

Handler ` RVA 0xBCC1A00 `；selector ` 1 `；EOL ` RVA 0x338A0288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-5a4050ebc121cb0b](../../evidence/state_effects-sets-019.md#s-5a4050ebc121cb0b)

### path-011535

```text
(exec)# debug dcm services provider api-infra info <cr>
```

Handler ` RVA 0xBCC1A00 `；selector ` 0 `；EOL ` RVA 0x3389FFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e111a420b9b5a123](../../evidence/state_effects-sets-048.md#s-e111a420b9b5a123)

### path-025386

```text
(exec)# debug device-tracking bdid <number:dynamic> <cr>
```

Handler ` RVA 0x13686180 `；selector ` 0 `；EOL ` RVA 0x35BD6378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-c09b5466d89b7044](../../evidence/conditions-sets-074.md#c-c09b5466d89b7044) · [缺口 G-0d33b0da8cb21275](../../evidence/gaps-sets-001.md#g-0d33b0da8cb21275) · [参数 P-c89f532bd0e3ec01](../../evidence/parameters-sets-015.md#p-c89f532bd0e3ec01) · [状态效果 S-8f767e74aff22f6f](../../evidence/state_effects-sets-030.md#s-8f767e74aff22f6f)

### path-000411

```text
(exec)# debug dhcp <cr>
```

Handler ` RVA 0xF46A1F0 `；selector ` 0 `；EOL ` RVA 0x34650F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0ae564f8db124224](../../evidence/state_effects-sets-003.md#s-0ae564f8db124224)

### path-003419

```text
(exec)# debug dhcp api <cr>
```

Handler ` RVA 0xF46A1F0 `；selector ` 3 `；EOL ` RVA 0x346511E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a6a8680c4a935e2](../../evidence/conditions-sets-004.md#c-0a6a8680c4a935e2) · [状态效果 S-ce1850348540569d](../../evidence/state_effects-sets-044.md#s-ce1850348540569d)

### path-003429

```text
(exec)# debug dhcp oper <cr>
```

Handler ` RVA 0xF46A1F0 `；selector ` 4 `；EOL ` RVA 0x346514A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8b2dc7934140cc80](../../evidence/state_effects-sets-030.md#s-8b2dc7934140cc80)

### path-003414

```text
(exec)# debug dhcp redundancy <cr>
```

Handler ` RVA 0xF46A1F0 `；selector ` 1 `；EOL ` RVA 0x34650A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e839a2f6b26a66eb](../../evidence/state_effects-sets-049.md#s-e839a2f6b26a66eb)

### path-007353

```text
(exec)# debug dhcp redundancy packet <cr>
```

Handler ` RVA 0xF46A1F0 `；selector ` 2 `；EOL ` RVA 0x34650A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58609f5aad95ff72](../../evidence/conditions-sets-035.md#c-58609f5aad95ff72) · [状态效果 S-9087f1199ac77bd1](../../evidence/state_effects-sets-031.md#s-9087f1199ac77bd1)

### path-003713

```text
(exec)# debug diagnostic all <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 7 `；EOL ` RVA 0x343B8608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003637

```text
(exec)# debug diagnostic engineer <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 6 `；EOL ` RVA 0x343B7370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003666

```text
(exec)# debug diagnostic error <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 4 `；EOL ` RVA 0x343B7B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003656

```text
(exec)# debug diagnostic gods_error <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 2 `；EOL ` RVA 0x343B78C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003704

```text
(exec)# debug diagnostic gods_message <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 0 `；EOL ` RVA 0x343B8360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003690

```text
(exec)# debug diagnostic message <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 1 `；EOL ` RVA 0x343B80B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003648

```text
(exec)# debug diagnostic packet <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 3 `；EOL ` RVA 0x343B7618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-003681

```text
(exec)# debug diagnostic pointer <cr>
```

Handler ` RVA 0xEB64BA0 `；selector ` 5 `；EOL ` RVA 0x343B7E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c281ae1e92659dbd](../../evidence/state_effects-sets-041.md#s-c281ae1e92659dbd)

### path-000180

```text
(exec)# debug dialer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34666300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000837

```text
(exec)# debug dialer cef <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34665858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000863

```text
(exec)# debug dialer detailed <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34665B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000898

```text
(exec)# debug dialer forwarding <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x34666058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000880

```text
(exec)# debug dialer holdq <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34665DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000760

```text
(exec)# debug dialer map <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34665058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000786

```text
(exec)# debug dialer packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34665300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-000807

```text
(exec)# debug dialer temporary <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x346655A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0136c4f797370350](../../evidence/state_effects-sets-001.md#s-0136c4f797370350)

### path-004154

```text
(exec)# debug diameter all <cr>
```

Handler ` RVA 0xBD08DD0 `；selector ` 0 `；EOL ` RVA 0x338ACE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-004110

```text
(exec)# debug diameter connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x338AAFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-004101

```text
(exec)# debug diameter dcca <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x338AAD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-004132

```text
(exec)# debug diameter error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x338ABDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-004144

```text
(exec)# debug diameter event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x338AC088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-004093

```text
(exec)# debug diameter failover <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x338AAA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007954

```text
(exec)# debug diameter fsm error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x338AB8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007960

```text
(exec)# debug diameter fsm event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x338ABB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007983

```text
(exec)# debug diameter gx database <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x338ACB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007978

```text
(exec)# debug diameter gx error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x338AC8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007968

```text
(exec)# debug diameter gx event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x338AC398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007974

```text
(exec)# debug diameter gx fsm <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x338AC640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007948

```text
(exec)# debug diameter packet error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x338AB2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007956

```text
(exec)# debug diameter packet event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x338AB5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a08d5f33d5d9e72](../../evidence/conditions-sets-047.md#c-7a08d5f33d5d9e72) · [状态效果 S-fb5cb45a296c7eac](../../evidence/state_effects-sets-053.md#s-fb5cb45a296c7eac)

### path-007318

```text
(exec)# debug dlep client error <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 11 `；EOL ` RVA 0x35A5D818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007335

```text
(exec)# debug dlep client infrastructure <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 13 `；EOL ` RVA 0x35A5E420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-010111

```text
(exec)# debug dlep client packet detail <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 9 `；EOL ` RVA 0x35A5DDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-010102

```text
(exec)# debug dlep client packet dump <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 8 `；EOL ` RVA 0x35A5DB28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-022952

```text
(exec)# debug dlep client packet interface <interface> <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 23 `；EOL ` RVA 0x35A5E138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c0218ec52fec43c](../../evidence/conditions-sets-005.md#c-0c0218ec52fec43c) · [缺口 G-583d0c8b50d680c1](../../evidence/gaps-sets-004.md#g-583d0c8b50d680c1) · [参数 P-0909769f12fb8b07](../../evidence/parameters-sets-001.md#p-0909769f12fb8b07) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007307

```text
(exec)# debug dlep client state <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 12 `；EOL ` RVA 0x35A5D570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007315

```text
(exec)# debug dlep neighbor all <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 15 `；EOL ` RVA 0x35A5E738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007347

```text
(exec)# debug dlep neighbor error <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 16 `；EOL ` RVA 0x35A5EF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007375

```text
(exec)# debug dlep neighbor infrastructure <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 19 `；EOL ` RVA 0x35A5F4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-010121

```text
(exec)# debug dlep neighbor infrastructure detail <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 20 `；EOL ` RVA 0x35A5F218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-010127

```text
(exec)# debug dlep neighbor infrastructure error <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 21 `；EOL ` RVA 0x35A5F4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007334

```text
(exec)# debug dlep neighbor metrics <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 18 `；EOL ` RVA 0x35A5EC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007325

```text
(exec)# debug dlep neighbor state <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 17 `；EOL ` RVA 0x35A5E9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-003348

```text
(exec)# debug dlep server <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 1 `；EOL ` RVA 0x35A5CAD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007285

```text
(exec)# debug dlep server detail <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 2 `；EOL ` RVA 0x35A5CAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-003369

```text
(exec)# debug dlep snmp <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 22 `；EOL ` RVA 0x35A5FA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-003357

```text
(exec)# debug dlep timer <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 3 `；EOL ` RVA 0x35A5D038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-007297

```text
(exec)# debug dlep timer detail <cr>
```

Handler ` RVA 0x132D0A00 `；selector ` 4 `；EOL ` RVA 0x35A5D010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b94ef4b20df056a7](../../evidence/state_effects-sets-039.md#s-b94ef4b20df056a7)

### path-000466

```text
(exec)# debug dlsw <cr>
```

Handler ` RVA 0x114211D0 `；selector ` 0 `；EOL ` RVA 0x354C9530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a3549815296d282f](../../evidence/conditions-sets-063.md#c-a3549815296d282f) · [状态效果 S-ad567520ca650190](../../evidence/state_effects-sets-037.md#s-ad567520ca650190)

### path-020457

```text
(exec)# debug dlsw border-peers interface <interface> <cr>
```

Handler ` RVA 0x114211D0 `；selector ` 0 `；EOL ` RVA 0x354C9530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a3c7223677e0c497](../../evidence/conditions-sets-063.md#c-a3c7223677e0c497) · [缺口 G-7d04d815c99eab3f](../../evidence/gaps-sets-005.md#g-7d04d815c99eab3f) · [参数 P-9af3c5e44d4af141](../../evidence/parameters-sets-012.md#p-9af3c5e44d4af141) · [状态效果 S-f5b9b2de5a84fb22](../../evidence/state_effects-sets-052.md#s-f5b9b2de5a84fb22)
