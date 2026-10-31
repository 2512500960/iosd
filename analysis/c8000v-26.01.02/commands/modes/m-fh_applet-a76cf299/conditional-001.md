# fh_applet · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-011122

```text
(config-applet)# event ipsla <cr>
```

Handler ` RVA 0x19345B60 `；selector ` 6 `；EOL ` RVA 0x369A1E58 `。

模式根 ` RVA 0x339A04E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7767ccb5460f0131](../../evidence/conditional_registrations-sets-002.md#r-7767ccb5460f0131) · [条件 C-8d4826d142b4a1d8](../../evidence/conditions-sets-055.md#c-8d4826d142b4a1d8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3fab8a8180bb8ebf](../../evidence/state_effects-sets-014.md#s-3fab8a8180bb8ebf)

### conditional_registration_candidates-011124

```text
(config-applet)# event ipsla maxrun <number:0..31536000> . <?match_subsec_action@55558bef5fb8> <cr>
```

Handler ` RVA 0x19345B60 `；selector ` 6 `；EOL ` RVA 0x369A1E58 `。

模式根 ` RVA 0x339A04E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter seconds\[.milliseconds\] value。

[候选注册 R-7767ccb5460f0131](../../evidence/conditional_registrations-sets-002.md#r-7767ccb5460f0131) · [条件 C-096fc037a3d19d7c](../../evidence/conditions-sets-004.md#c-096fc037a3d19d7c) · [缺口 G-76ebf6ae1711316c](../../evidence/gaps-sets-005.md#g-76ebf6ae1711316c) · [参数 P-0e90623b185e4948](../../evidence/parameters-sets-002.md#p-0e90623b185e4948) · [状态效果 S-9025d641d4d96309](../../evidence/state_effects-sets-031.md#s-9025d641d4d96309)

### conditional_registration_candidates-011123

```text
(config-applet)# no event ipsla <cr>
```

Handler ` RVA 0x19345B60 `；selector ` 6 `；EOL ` RVA 0x369A1E58 `。

模式根 ` RVA 0x339A04E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7767ccb5460f0131](../../evidence/conditional_registrations-sets-002.md#r-7767ccb5460f0131) · [条件 C-4f21b45f5725ce2b](../../evidence/conditions-sets-031.md#c-4f21b45f5725ce2b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5a33fbdcb8188025](../../evidence/state_effects-sets-019.md#s-5a33fbdcb8188025)

