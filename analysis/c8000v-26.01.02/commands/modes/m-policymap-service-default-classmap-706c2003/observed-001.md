# policymap-service-default-classmap · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009746

```text
(config-service-policymap-class-traffic)# default drop <cr>
```

Handler ` RVA 0x10A652A0 `；selector ` 10 `；EOL ` RVA 0x34C279F0 `。

模式根 ` RVA 0x34C82FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d54ed8ba1a65d5ec](../../evidence/state_effects-sets-045.md#s-d54ed8ba1a65d5ec)

### observed_connections-009744

```text
(config-service-policymap-class-traffic)# drop <cr>
```

Handler ` RVA 0x10A652A0 `；selector ` 10 `；EOL ` RVA 0x34C279F0 `。

模式根 ` RVA 0x34C82FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009743

```text
(config-service-policymap-class-traffic)# exit <cr>
```

Handler ` RVA 0x10A64810 `；selector ` 0 `；EOL ` RVA 0x34C83578 `。

模式根 ` RVA 0x34C82FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-585eb9e5874907f1](../../evidence/conditions-sets-035.md#c-585eb9e5874907f1)

### observed_connections-009745

```text
(config-service-policymap-class-traffic)# no drop <cr>
```

Handler ` RVA 0x10A652A0 `；selector ` 10 `；EOL ` RVA 0x34C279F0 `。

模式根 ` RVA 0x34C82FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-9a5485522d9fa88d](../../evidence/state_effects-sets-033.md#s-9a5485522d9fa88d)

