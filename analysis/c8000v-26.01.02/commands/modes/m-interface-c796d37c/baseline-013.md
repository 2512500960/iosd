# interface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-063359

```text
(config-if)# x25 threshold <number:1..127> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 9 `；EOL ` RVA 0x34BBA218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Packets。

[条件 C-1d3bdd9adaa3e492](../../evidence/conditions-sets-011.md#c-1d3bdd9adaa3e492) · [参数 P-6f12d7fd73d879be](../../evidence/parameters-sets-009.md#p-6f12d7fd73d879be)

### path-063906

```text
(config-if)# x25 use-source-address <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 6 `；EOL ` RVA 0x34BB9F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-064575

```text
(config-if)# x25 version 1980 <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 0 `；EOL ` RVA 0x34BB4370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-260afe87aea98fb7](../../evidence/conditions-sets-015.md#c-260afe87aea98fb7) · [状态效果 S-d7974cc7f1290103](../../evidence/state_effects-sets-046.md#s-d7974cc7f1290103)

### path-067772

```text
(config-if)# x25 win <number:dynamic> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 17 `；EOL ` RVA 0x34BB75B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Packets。

[条件 C-5e43946619aa80b3](../../evidence/conditions-sets-037.md#c-5e43946619aa80b3) · [缺口 G-fcbb09300e55c0e0](../../evidence/gaps-sets-009.md#g-fcbb09300e55c0e0) · [参数 P-ef52c9a3124b87d0](../../evidence/parameters-sets-018.md#p-ef52c9a3124b87d0)

### path-067775

```text
(config-if)# x25 wout <number:dynamic> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 18 `；EOL ` RVA 0x34BB7900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Packets。

[条件 C-c7f211aae473a5ae](../../evidence/conditions-sets-077.md#c-c7f211aae473a5ae) · [缺口 G-c365e2c332ad1326](../../evidence/gaps-sets-007.md#g-c365e2c332ad1326) · [参数 P-4ae5bdc653f2d730](../../evidence/parameters-sets-006.md#p-4ae5bdc653f2d730)

### path-064345

```text
(config-if)# yellow alarm detect <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 11 `；EOL ` RVA 0x34410A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-edb68e002ca02f11](../../evidence/conditions-sets-092.md#c-edb68e002ca02f11)
