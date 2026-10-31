# transport-map · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009022

```text
(config-tmap)# authentication-retries <number:0..5> <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 0 `；EOL ` RVA 0x340057B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of authentication retries。

[条件 C-429aa08736cc9f21](../../evidence/conditions-sets-026.md#c-429aa08736cc9f21) · [参数 P-997051eb68bec6a0](../../evidence/parameters-sets-012.md#p-997051eb68bec6a0)

### observed_connections-009035

```text
(config-tmap)# banner wait <string> <cr>
```

Handler ` RVA 0xDBDC680 `；selector ` 0 `；EOL ` RVA 0x34006320 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` c message-text c, where 'c' is a delimiting character。

[条件 C-b6df59723d85a0a6](../../evidence/conditions-sets-071.md#c-b6df59723d85a0a6) · [参数 P-8d369e9b628e4872](../../evidence/parameters-sets-011.md#p-8d369e9b628e4872) · [状态效果 S-8bb368608a687634](../../evidence/state_effects-sets-030.md#s-8bb368608a687634)

### observed_connections-009039

```text
(config-tmap)# connection wait none <cr>
```

Handler ` RVA 0xDBDC840 `；selector ` 0 `；EOL ` RVA 0x340066D8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93cddf057872517f](../../evidence/conditions-sets-057.md#c-93cddf057872517f) · [状态效果 S-71b97208dcc39e7d](../../evidence/state_effects-sets-024.md#s-71b97208dcc39e7d)

### observed_connections-009028

```text
(config-tmap)# default authentication-retries <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 0 `；EOL ` RVA 0x340057B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49a1337ead6fe8b3](../../evidence/conditions-sets-029.md#c-49a1337ead6fe8b3) · [状态效果 S-9b71a1773158540a](../../evidence/state_effects-sets-033.md#s-9b71a1773158540a)

### observed_connections-009037

```text
(config-tmap)# default banner wait <cr>
```

Handler ` RVA 0xDBDC680 `；selector ` 0 `；EOL ` RVA 0x34006320 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-304e95b2cd66f82b](../../evidence/conditions-sets-019.md#c-304e95b2cd66f82b) · [状态效果 S-2c4e583e24495cde](../../evidence/state_effects-sets-010.md#s-2c4e583e24495cde)

### observed_connections-009041

```text
(config-tmap)# default connection wait none <cr>
```

Handler ` RVA 0xDBDC840 `；selector ` 0 `；EOL ` RVA 0x340066D8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93cddf057872517f](../../evidence/conditions-sets-057.md#c-93cddf057872517f) · [状态效果 S-7fd6ccd6ba672947](../../evidence/state_effects-sets-027.md#s-7fd6ccd6ba672947)

### observed_connections-009038

```text
(config-tmap)# default rsa keypair-name <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 1 `；EOL ` RVA 0x34005DD0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7b66075165280d6b](../../evidence/conditions-sets-048.md#c-7b66075165280d6b) · [状态效果 S-9b71a1773158540a](../../evidence/state_effects-sets-033.md#s-9b71a1773158540a)

### observed_connections-009032

```text
(config-tmap)# default secure-server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 1 `；EOL ` RVA 0x340054B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1544633820c5b34b](../../evidence/conditions-sets-008.md#c-1544633820c5b34b) · [状态效果 S-9b71a1773158540a](../../evidence/state_effects-sets-033.md#s-9b71a1773158540a)

### observed_connections-009030

```text
(config-tmap)# default server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 0 `；EOL ` RVA 0x340051C8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6da1e37abc3dc7dc](../../evidence/conditions-sets-042.md#c-6da1e37abc3dc7dc) · [状态效果 S-9b71a1773158540a](../../evidence/state_effects-sets-033.md#s-9b71a1773158540a)

### observed_connections-009025

```text
(config-tmap)# default time-out <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 2 `；EOL ` RVA 0x34005748 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2342338bdecea811](../../evidence/conditions-sets-014.md#c-2342338bdecea811) · [状态效果 S-9b71a1773158540a](../../evidence/state_effects-sets-033.md#s-9b71a1773158540a)

### observed_connections-009026

```text
(config-tmap)# no authentication-retries <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 0 `；EOL ` RVA 0x340057B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49a1337ead6fe8b3](../../evidence/conditions-sets-029.md#c-49a1337ead6fe8b3) · [状态效果 S-38195c368e0c530b](../../evidence/state_effects-sets-012.md#s-38195c368e0c530b)

### observed_connections-009033

```text
(config-tmap)# no banner wait <cr>
```

Handler ` RVA 0xDBDC680 `；selector ` 0 `；EOL ` RVA 0x34006320 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-da997f6bca8f5157](../../evidence/conditions-sets-084.md#c-da997f6bca8f5157) · [状态效果 S-26a64e3a0dad93af](../../evidence/state_effects-sets-009.md#s-26a64e3a0dad93af)

### observed_connections-009040

```text
(config-tmap)# no connection wait none <cr>
```

Handler ` RVA 0xDBDC840 `；selector ` 0 `；EOL ` RVA 0x340066D8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-93cddf057872517f](../../evidence/conditions-sets-057.md#c-93cddf057872517f) · [状态效果 S-a7dd15bd74eb760c](../../evidence/state_effects-sets-035.md#s-a7dd15bd74eb760c)

### observed_connections-009034

```text
(config-tmap)# no rsa keypair-name <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 1 `；EOL ` RVA 0x34005DD0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e77fc9d0fa2ccf09](../../evidence/conditions-sets-089.md#c-e77fc9d0fa2ccf09) · [状态效果 S-38195c368e0c530b](../../evidence/state_effects-sets-012.md#s-38195c368e0c530b)

### observed_connections-009031

```text
(config-tmap)# no secure-server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 1 `；EOL ` RVA 0x340054B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1544633820c5b34b](../../evidence/conditions-sets-008.md#c-1544633820c5b34b) · [状态效果 S-38195c368e0c530b](../../evidence/state_effects-sets-012.md#s-38195c368e0c530b)

### observed_connections-009029

```text
(config-tmap)# no server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 0 `；EOL ` RVA 0x340051C8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6da1e37abc3dc7dc](../../evidence/conditions-sets-042.md#c-6da1e37abc3dc7dc) · [状态效果 S-38195c368e0c530b](../../evidence/state_effects-sets-012.md#s-38195c368e0c530b)

### observed_connections-009024

```text
(config-tmap)# no time-out <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 2 `；EOL ` RVA 0x34005748 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2342338bdecea811](../../evidence/conditions-sets-014.md#c-2342338bdecea811) · [状态效果 S-38195c368e0c530b](../../evidence/state_effects-sets-012.md#s-38195c368e0c530b)

### observed_connections-009036

```text
(config-tmap)# rsa keypair-name <string> <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 1 `；EOL ` RVA 0x34005DD0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` RSA key-pair name。

[条件 C-9c6304c5e38a258c](../../evidence/conditions-sets-060.md#c-9c6304c5e38a258c) · [参数 P-079429935fcc08f2](../../evidence/parameters-sets-001.md#p-079429935fcc08f2)

### observed_connections-009027

```text
(config-tmap)# secure-server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 1 `；EOL ` RVA 0x340054B0 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1544633820c5b34b](../../evidence/conditions-sets-008.md#c-1544633820c5b34b)

### observed_connections-009023

```text
(config-tmap)# server <cr>
```

Handler ` RVA 0xDBDC390 `；selector ` 0 `；EOL ` RVA 0x340051C8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6da1e37abc3dc7dc](../../evidence/conditions-sets-042.md#c-6da1e37abc3dc7dc)

### observed_connections-009021

```text
(config-tmap)# time-out <number:1..120> <cr>
```

Handler ` RVA 0xDBDBED0 `；selector ` 2 `；EOL ` RVA 0x34005748 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SSH time-out interval (secs)。

[条件 C-60a4f59adca72680](../../evidence/conditions-sets-038.md#c-60a4f59adca72680) · [参数 P-10ad8dab258d0550](../../evidence/parameters-sets-002.md#p-10ad8dab258d0550)

### observed_connections-009042

```text
(config-tmap)# transport interface GigabitEthernet <number:0..0> <cr>
```

Handler ` RVA 0xDBDC9A0 `；selector ` 0 `；EOL ` RVA 0x34006AB8 `。

模式根 ` RVA 0x340032C8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` GigabitEthernet interface number。

[条件 C-b45db15832225708](../../evidence/conditions-sets-070.md#c-b45db15832225708) · [缺口 G-65bcc2b9ceb047f4](../../evidence/gaps-sets-004.md#g-65bcc2b9ceb047f4) · [参数 P-9c3be231d9a10b68](../../evidence/parameters-sets-012.md#p-9c3be231d9a10b68) · [状态效果 S-5a0ed14dc2fbfcd1](../../evidence/state_effects-sets-019.md#s-5a0ed14dc2fbfcd1)

