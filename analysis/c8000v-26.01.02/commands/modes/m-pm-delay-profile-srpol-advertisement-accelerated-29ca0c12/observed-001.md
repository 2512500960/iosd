# pm-delay-profile-srpol-advertisement-accelerated · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009444

```text
(config-pm-dm-srpol-adv-acc)# default <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-0f69244901bf0145](../../evidence/state_effects-sets-004.md#s-0f69244901bf0145)

### observed_connections-009448

```text
(config-pm-dm-srpol-adv-acc)# default minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-0f69244901bf0145](../../evidence/state_effects-sets-004.md#s-0f69244901bf0145)

### observed_connections-009450

```text
(config-pm-dm-srpol-adv-acc)# default threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-0f69244901bf0145](../../evidence/state_effects-sets-004.md#s-0f69244901bf0145)

### observed_connections-009442

```text
(config-pm-dm-srpol-adv-acc)# exit <cr>
```

Handler ` RVA 0x1ACF94D0 `；selector ` 0 `；EOL ` RVA 0x36DDC1F0 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f77d4a96b1d97ae8](../../evidence/conditions-sets-096.md#c-f77d4a96b1d97ae8)

### observed_connections-009445

```text
(config-pm-dm-srpol-adv-acc)# minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7)

### observed_connections-009443

```text
(config-pm-dm-srpol-adv-acc)# no <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-c0e467049f6d051f](../../evidence/state_effects-sets-041.md#s-c0e467049f6d051f)

### observed_connections-009447

```text
(config-pm-dm-srpol-adv-acc)# no minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-c0e467049f6d051f](../../evidence/state_effects-sets-041.md#s-c0e467049f6d051f)

### observed_connections-009449

```text
(config-pm-dm-srpol-adv-acc)# no threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-c0e467049f6d051f](../../evidence/state_effects-sets-041.md#s-c0e467049f6d051f)

### observed_connections-009446

```text
(config-pm-dm-srpol-adv-acc)# threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48)

### observed_connections-009441

```text
(config-pm-dm-srpol-adv-acc)# <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC19F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

