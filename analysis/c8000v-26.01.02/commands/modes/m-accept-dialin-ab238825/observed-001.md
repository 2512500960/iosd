# accept-dialin · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009616

```text
(config-vpdn-acc-in)# default protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 110 `；EOL ` RVA 0x356DEED8 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a14dff43b9f58b6](../../evidence/conditions-sets-035.md#c-5a14dff43b9f58b6) · [状态效果 S-43dc0f2b2dd374ac](../../evidence/state_effects-sets-015.md#s-43dc0f2b2dd374ac)

### observed_connections-009618

```text
(config-vpdn-acc-in)# default virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 104 `；EOL ` RVA 0x356FCFD0 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1cc7dd3d2e113f0](../../evidence/conditions-sets-075.md#c-c1cc7dd3d2e113f0) · [状态效果 S-43dc0f2b2dd374ac](../../evidence/state_effects-sets-015.md#s-43dc0f2b2dd374ac)

### observed_connections-009612

```text
(config-vpdn-acc-in)# exit <cr>
```

Handler ` RVA 0x11D54850 `；selector ` 0 `；EOL ` RVA 0x356DEC58 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-99c962a1c48e993c](../../evidence/conditions-sets-059.md#c-99c962a1c48e993c)

### observed_connections-009614

```text
(config-vpdn-acc-in)# no protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 110 `；EOL ` RVA 0x356DEED8 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ede61447064ecccc](../../evidence/conditions-sets-092.md#c-ede61447064ecccc) · [状态效果 S-73a1e49f85cfba5f](../../evidence/state_effects-sets-025.md#s-73a1e49f85cfba5f)

### observed_connections-009617

```text
(config-vpdn-acc-in)# no virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 104 `；EOL ` RVA 0x356FCFD0 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1cc7dd3d2e113f0](../../evidence/conditions-sets-075.md#c-c1cc7dd3d2e113f0) · [状态效果 S-73a1e49f85cfba5f](../../evidence/state_effects-sets-025.md#s-73a1e49f85cfba5f)

### observed_connections-009615

```text
(config-vpdn-acc-in)# protocol l2tp <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 110 `；EOL ` RVA 0x356DEED8 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fa282fd2f29764c](../../evidence/conditions-sets-019.md#c-2fa282fd2f29764c) · [状态效果 S-fc106410f129a4da](../../evidence/state_effects-sets-053.md#s-fc106410f129a4da)

### observed_connections-009613

```text
(config-vpdn-acc-in)# virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 104 `；EOL ` RVA 0x356FCFD0 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1cc7dd3d2e113f0](../../evidence/conditions-sets-075.md#c-c1cc7dd3d2e113f0)

### observed_connections-009619

```text
(config-vpdn-acc-in)# virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 104 `；EOL ` RVA 0x356FCFD0 `。

模式根 ` RVA 0x356DE4C0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template interface number。

[条件 C-1290f880f8ea126b](../../evidence/conditions-sets-007.md#c-1290f880f8ea126b) · [缺口 G-2963b6ba951480cd](../../evidence/gaps-sets-002.md#g-2963b6ba951480cd) · [参数 P-7c533f9fe2ed8fee](../../evidence/parameters-sets-010.md#p-7c533f9fe2ed8fee)
