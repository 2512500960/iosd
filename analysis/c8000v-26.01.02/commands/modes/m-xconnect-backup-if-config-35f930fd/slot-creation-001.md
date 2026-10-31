# xconnect-backup-if-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004571

```text
(config-if-xconn-backup)# default mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D24DD0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-3ea983a54335ecf5](../../evidence/conditions-sets-024.md#c-3ea983a54335ecf5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d5474d37ff166e81](../../evidence/state_effects-sets-045.md#s-d5474d37ff166e81)

### static_slot_creation_candidates-004570

```text
(config-if-xconn-backup)# default mpls label <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D24AC0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-82d006c038eea8a7](../../evidence/conditions-sets-051.md#c-82d006c038eea8a7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d5474d37ff166e81](../../evidence/state_effects-sets-045.md#s-d5474d37ff166e81)

### static_slot_creation_candidates-004567

```text
(config-if-xconn-backup)# mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D24DD0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-3ea983a54335ecf5](../../evidence/conditions-sets-024.md#c-3ea983a54335ecf5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004572

```text
(config-if-xconn-backup)# mpls label <number:dynamic> <number:16..1048575> <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D24AC0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Local pseudowire label；` unsigned_number ` Remote pseudowire label。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-54bba53eb02aa656](../../evidence/conditions-sets-033.md#c-54bba53eb02aa656) · [缺口 G-ed095ffedbfc3b89](../../evidence/gaps-sets-008.md#g-ed095ffedbfc3b89) · [参数 P-4b6d2a28825be053](../../evidence/parameters-sets-006.md#p-4b6d2a28825be053)

### static_slot_creation_candidates-004569

```text
(config-if-xconn-backup)# no mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D24DD0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-3ea983a54335ecf5](../../evidence/conditions-sets-024.md#c-3ea983a54335ecf5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fa4497db6d7d7a30](../../evidence/state_effects-sets-053.md#s-fa4497db6d7d7a30)

### static_slot_creation_candidates-004568

```text
(config-if-xconn-backup)# no mpls label <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D24AC0 `。

模式根 ` RVA 0x36D248F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-74437f40f53fca5d](../../evidence/conditional_registrations-sets-002.md#r-74437f40f53fca5d) · [条件 C-81f667fb959f6a8a](../../evidence/conditions-sets-050.md#c-81f667fb959f6a8a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fa4497db6d7d7a30](../../evidence/state_effects-sets-053.md#s-fa4497db6d7d7a30)
