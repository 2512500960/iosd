# 模式 xconnect-if-config

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` xconnect-cem-config `, ` xconnect-cem-data-config `, ` xconnect-cem-sig-config `, ` xconnect-conn-config `, ` xconnect-dlci-config `, ` xconnect-if-config `, ` xconnect-pvc-config `, ` xconnect-pvp-config `, ` xconnect-subif-config `, ` xconnect-vc-config `。

- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-if-config `；提示符 ` config-if-xconn `；parent ` interface `；` mode-0786 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-subif-config `；提示符 ` config-subif-xconn `；parent ` subinterface `；` mode-0787 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-conn-config `；提示符 ` config-xconn `；parent ` fr-pw `；` mode-0788 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-dlci-config `；提示符 ` config-fr-dlci-xconn `；parent ` interface-dlci `；` mode-0789 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-pvc-config `；提示符 ` cfg-if-atm-l2trans-pvc-xconn `；parent ` atm-l2trans-pvc-config `；` mode-0790 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-pvp-config `；提示符 ` cfg-if-atm-l2trans-pvp-xconn `；parent ` atm-l2trans-pvp-config `；` mode-0791 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-cem-config `；提示符 ` cfg-if-cem-xconn `；parent ` cem `；` mode-0792 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-cem-data-config `；提示符 ` cfg-if-cem-data-xconn `；parent ` config-if-cem-data `；` mode-0793 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-cem-sig-config `；提示符 ` cfg-if-cem-sig-xconn `；parent ` config-if-cem-sig `；` mode-0794 `。
- 根 ` RVA 0x36D1F948 `；名称 ` xconnect-vc-config `；提示符 ` cfg-if-ether-vc-xconn `；parent ` config-service-instance `；` mode-0795 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 依赖静态建槽的条件安装 | [slot-creation-001.txt](slot-creation-001.txt) | [slot-creation-001.md](slot-creation-001.md) | ` backup delay <number:0..180> <number:0..180> <cr> ` → ` <cr> ` | 22 |
