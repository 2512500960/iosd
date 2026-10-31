# pm-delay-profile-srpol-advertisement-periodic · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009224

```text
(config-pm-dm-srpol-adv-per)# default <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ad02189964f42da1](../../evidence/state_effects-sets-037.md#s-ad02189964f42da1)

### observed_connections-009230

```text
(config-pm-dm-srpol-adv-per)# default disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ad02189964f42da1](../../evidence/state_effects-sets-037.md#s-ad02189964f42da1)

### observed_connections-009236

```text
(config-pm-dm-srpol-adv-per)# default interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-ad02189964f42da1](../../evidence/state_effects-sets-037.md#s-ad02189964f42da1)

### observed_connections-009232

```text
(config-pm-dm-srpol-adv-per)# default minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-ad02189964f42da1](../../evidence/state_effects-sets-037.md#s-ad02189964f42da1)

### observed_connections-009234

```text
(config-pm-dm-srpol-adv-per)# default threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-ad02189964f42da1](../../evidence/state_effects-sets-037.md#s-ad02189964f42da1)

### observed_connections-009225

```text
(config-pm-dm-srpol-adv-per)# disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009222

```text
(config-pm-dm-srpol-adv-per)# exit <cr>
```

Handler ` RVA 0x1ACF95B0 `；selector ` 0 `；EOL ` RVA 0x36DDD618 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9558d3c3c3bcb25c](../../evidence/conditions-sets-058.md#c-9558d3c3c3bcb25c)

### observed_connections-009228

```text
(config-pm-dm-srpol-adv-per)# interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d)

### observed_connections-009226

```text
(config-pm-dm-srpol-adv-per)# minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca)

### observed_connections-009223

```text
(config-pm-dm-srpol-adv-per)# no <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a98479ceaa82734e](../../evidence/state_effects-sets-036.md#s-a98479ceaa82734e)

### observed_connections-009229

```text
(config-pm-dm-srpol-adv-per)# no disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a98479ceaa82734e](../../evidence/state_effects-sets-036.md#s-a98479ceaa82734e)

### observed_connections-009235

```text
(config-pm-dm-srpol-adv-per)# no interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-a98479ceaa82734e](../../evidence/state_effects-sets-036.md#s-a98479ceaa82734e)

### observed_connections-009231

```text
(config-pm-dm-srpol-adv-per)# no minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-a98479ceaa82734e](../../evidence/state_effects-sets-036.md#s-a98479ceaa82734e)

### observed_connections-009233

```text
(config-pm-dm-srpol-adv-per)# no threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-a98479ceaa82734e](../../evidence/state_effects-sets-036.md#s-a98479ceaa82734e)

### observed_connections-009227

```text
(config-pm-dm-srpol-adv-per)# threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781)

### observed_connections-009221

```text
(config-pm-dm-srpol-adv-per)# <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

