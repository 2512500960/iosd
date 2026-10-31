# xconnect-if-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004260

```text
(config-if-xconn)# backup delay <number:0..180> <number:0..180> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x36D23290 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable delay；` unsigned_number ` Disable delay。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-65090b6c5e8e749f](../../evidence/conditions-sets-039.md#c-65090b6c5e8e749f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3f85be26346208b0](../../evidence/parameters-sets-005.md#p-3f85be26346208b0) · [状态效果 S-07ff0c5b7dd54059](../../evidence/state_effects-sets-002.md#s-07ff0c5b7dd54059)

### static_slot_creation_candidates-004259

```text
(config-if-xconn)# backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36D22EF0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-198dc284946478ed](../../evidence/conditions-sets-010.md#c-198dc284946478ed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7fb9a7f8ea96b65a](../../evidence/parameters-sets-010.md#p-7fb9a7f8ea96b65a) · [状态效果 S-5f9db177cff5f729](../../evidence/state_effects-sets-021.md#s-5f9db177cff5f729)

### static_slot_creation_candidates-004247

```text
(config-if-xconn)# default <cr>
```

Handler ` RVA 0x1AA09570 `；selector ` 16 `；EOL ` RVA 0x36D33278 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-2a4909d4d24776f4](../../evidence/conditional_registrations-sets-001.md#r-2a4909d4d24776f4) · [条件 C-5decf09dc70e7cdd](../../evidence/conditions-sets-037.md#c-5decf09dc70e7cdd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004255

```text
(config-if-xconn)# default backup delay <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x36D23290 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-4ef0a7d424511818](../../evidence/conditions-sets-031.md#c-4ef0a7d424511818) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004264

```text
(config-if-xconn)# default backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36D22EF0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-198dc284946478ed](../../evidence/conditions-sets-010.md#c-198dc284946478ed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7fb9a7f8ea96b65a](../../evidence/parameters-sets-010.md#p-7fb9a7f8ea96b65a) · [状态效果 S-7e08caf57622da1c](../../evidence/state_effects-sets-027.md#s-7e08caf57622da1c)

### static_slot_creation_candidates-004257

```text
(config-if-xconn)# default match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x36D229A0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-c9ef6c3e50b83ad2](../../evidence/conditions-sets-078.md#c-c9ef6c3e50b83ad2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004249

```text
(config-if-xconn)# default mtu <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36D23AA0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-8de4db8a635b1744](../../evidence/conditions-sets-055.md#c-8de4db8a635b1744) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004253

```text
(config-if-xconn)# default redundancy all-active <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x36D23758 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-a79d378149f4152a](../../evidence/conditions-sets-065.md#c-a79d378149f4152a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004262

```text
(config-if-xconn)# default remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36D22608 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-aa62d0ae4c8b9474](../../evidence/conditions-sets-066.md#c-aa62d0ae4c8b9474) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4c723134247c35fa](../../evidence/state_effects-sets-017.md#s-4c723134247c35fa)

### static_slot_creation_candidates-004250

```text
(config-if-xconn)# match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x36D229A0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-c9ef6c3e50b83ad2](../../evidence/conditions-sets-078.md#c-c9ef6c3e50b83ad2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004265

```text
(config-if-xconn)# mtu <?number_help_func_action@55558c277a78> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36D23AA0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-2c02c9dbc938be1e](../../evidence/conditions-sets-017.md#c-2c02c9dbc938be1e) · [缺口 G-e224fa4ffefb7804](../../evidence/gaps-sets-008.md#g-e224fa4ffefb7804)

### static_slot_creation_candidates-004246

```text
(config-if-xconn)# no <cr>
```

Handler ` RVA 0x1AA09570 `；selector ` 16 `；EOL ` RVA 0x36D33278 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-2a4909d4d24776f4](../../evidence/conditional_registrations-sets-001.md#r-2a4909d4d24776f4) · [条件 C-5decf09dc70e7cdd](../../evidence/conditions-sets-037.md#c-5decf09dc70e7cdd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004254

```text
(config-if-xconn)# no backup delay <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x36D23290 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-fa257d73e422d5af](../../evidence/conditions-sets-097.md#c-fa257d73e422d5af) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004263

```text
(config-if-xconn)# no backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36D22EF0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-198dc284946478ed](../../evidence/conditions-sets-010.md#c-198dc284946478ed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7fb9a7f8ea96b65a](../../evidence/parameters-sets-010.md#p-7fb9a7f8ea96b65a) · [状态效果 S-e6f61270e48bdbc9](../../evidence/state_effects-sets-049.md#s-e6f61270e48bdbc9)

### static_slot_creation_candidates-004256

```text
(config-if-xconn)# no match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x36D229A0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-c9ef6c3e50b83ad2](../../evidence/conditions-sets-078.md#c-c9ef6c3e50b83ad2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004248

```text
(config-if-xconn)# no mtu <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36D23AA0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-72abbf2f8f1348ee](../../evidence/conditions-sets-044.md#c-72abbf2f8f1348ee) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004251

```text
(config-if-xconn)# no redundancy all-active <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x36D23758 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-863a652ad770bcd4](../../evidence/conditions-sets-052.md#c-863a652ad770bcd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004261

```text
(config-if-xconn)# no remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36D22608 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-aa62d0ae4c8b9474](../../evidence/conditions-sets-066.md#c-aa62d0ae4c8b9474) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f5293526a157f50e](../../evidence/state_effects-sets-052.md#s-f5293526a157f50e)

### static_slot_creation_candidates-004252

```text
(config-if-xconn)# redundancy all-active replicate <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x36D23758 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-7744b999bc7b296f](../../evidence/conditions-sets-046.md#c-7744b999bc7b296f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004266

```text
(config-if-xconn)# remote circuit id <number:dynamic> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 7 `；EOL ` RVA 0x36D222B0 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Remote circuit ID。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-f733b672dc5acd68](../../evidence/conditions-sets-095.md#c-f733b672dc5acd68) · [缺口 G-9b09b7abfc5fa2b9](../../evidence/gaps-sets-006.md#g-9b09b7abfc5fa2b9) · [参数 P-8217da1de977b67e](../../evidence/parameters-sets-010.md#p-8217da1de977b67e)

### static_slot_creation_candidates-004258

```text
(config-if-xconn)# remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36D22608 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-01e4814eaccf7149](../../evidence/conditional_registrations-sets-001.md#r-01e4814eaccf7149) · [条件 C-aa62d0ae4c8b9474](../../evidence/conditions-sets-066.md#c-aa62d0ae4c8b9474) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004245

```text
(config-if-xconn)# <cr>
```

Handler ` RVA 0x1AA09570 `；selector ` 16 `；EOL ` RVA 0x36D33278 `。

模式根 ` RVA 0x36D1F948 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a4909d4d24776f4](../../evidence/conditional_registrations-sets-001.md#r-2a4909d4d24776f4) · [条件 C-5decf09dc70e7cdd](../../evidence/conditions-sets-037.md#c-5decf09dc70e7cdd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

