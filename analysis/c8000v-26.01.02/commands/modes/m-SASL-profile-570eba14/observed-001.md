# SASL-profile · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009258

```text
(config-SASL-profile)# client user <string> password <string> <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 3 `；EOL ` RVA 0x34B18348 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` client's username；` string ` client's password。

[参数 P-5cb3b74c1744e9ba](../../evidence/parameters-sets-007.md#p-5cb3b74c1744e9ba)

### observed_connections-009253

```text
(config-SASL-profile)# exit <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 5 `；EOL ` RVA 0x34B18A70 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9130ede38d08c95e](../../evidence/conditions-sets-056.md#c-9130ede38d08c95e)

### observed_connections-009255

```text
(config-SASL-profile)# mechanism anonymous <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 1 `；EOL ` RVA 0x34B17F88 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009254

```text
(config-SASL-profile)# mechanism digest-md5 <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 2 `；EOL ` RVA 0x34B17CE0 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009260

```text
(config-SASL-profile)# no client user <string> password <string> <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 3 `；EOL ` RVA 0x34B18348 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` client's username；` string ` client's password。

[参数 P-5cb3b74c1744e9ba](../../evidence/parameters-sets-007.md#p-5cb3b74c1744e9ba) · [状态效果 S-2c811a6f897809e6](../../evidence/state_effects-sets-010.md#s-2c811a6f897809e6)

### observed_connections-009257

```text
(config-SASL-profile)# no mechanism anonymous <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 1 `；EOL ` RVA 0x34B17F88 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-2c811a6f897809e6](../../evidence/state_effects-sets-010.md#s-2c811a6f897809e6)

### observed_connections-009256

```text
(config-SASL-profile)# no mechanism digest-md5 <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 2 `；EOL ` RVA 0x34B17CE0 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-2c811a6f897809e6](../../evidence/state_effects-sets-010.md#s-2c811a6f897809e6)

### observed_connections-009261

```text
(config-SASL-profile)# no server user <string> password <string> <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 4 `；EOL ` RVA 0x34B186E0 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` server's username；` string ` server's password。

[参数 P-b9fac7940f20025a](../../evidence/parameters-sets-014.md#p-b9fac7940f20025a) · [状态效果 S-2c811a6f897809e6](../../evidence/state_effects-sets-010.md#s-2c811a6f897809e6)

### observed_connections-009259

```text
(config-SASL-profile)# server user <string> password <string> <cr>
```

Handler ` RVA 0x103E3B20 `；selector ` 4 `；EOL ` RVA 0x34B186E0 `。

模式根 ` RVA 0x34B14948 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` server's username；` string ` server's password。

[参数 P-b9fac7940f20025a](../../evidence/parameters-sets-014.md#p-b9fac7940f20025a)
