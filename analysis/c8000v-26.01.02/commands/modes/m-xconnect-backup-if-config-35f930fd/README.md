# 模式 xconnect-backup-if-config

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` xconnect-backup-connect-config `, ` xconnect-backup-if-config `, ` xconnect-backup-subif-config `, ` xconnect-cem-backup-config `, ` xconnect-cem-data-backup-config `, ` xconnect-cem-sig-backup-config `, ` xconnect-dlci-backup-config `, ` xconnect-pvc-backup-config `, ` xconnect-pvp-backup-config `, ` xconnect-vc-backup-config `。

- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-backup-if-config `；提示符 ` config-if-xconn-backup `；parent ` xconnect-if-config `；` mode-0796 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-backup-subif-config `；提示符 ` config-subif-xconn-backup `；parent ` xconnect-subif-config `；` mode-0797 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-backup-connect-config `；提示符 ` config-connection-backup `；parent ` config-connection `；` mode-0798 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-dlci-backup-config `；提示符 ` cfg-fr-dlci-xconn-bkup `；parent ` xconnect-dlci-config `；` mode-0799 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-pvp-backup-config `；提示符 ` cfg-if-atm-l2trans-pvp-xconn-bkup `；parent ` xconnect-pvp-config `；` mode-0800 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-pvc-backup-config `；提示符 ` cfg-if-atm-l2trans-pvc-xconn-bkup `；parent ` xconnect-pvc-config `；` mode-0801 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-vc-backup-config `；提示符 ` cfg-if-ether-vc-xconn-bkup `；parent ` xconnect-vc-config `；` mode-0802 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-cem-backup-config `；提示符 ` cfg-if-cem-xconn-bkup `；parent ` xconnect-cem-config `；` mode-0803 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-cem-data-backup-config `；提示符 ` cfg-if-cem-data-xconn-bkup `；parent ` xconnect-cem-data-config `；` mode-0804 `。
- 根 ` RVA 0x36D248F8 `；名称 ` xconnect-cem-sig-backup-config `；提示符 ` cfg-if-cem-data-xconn-bkup `；parent ` xconnect-cem-sig-config `；` mode-0805 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 依赖静态建槽的条件安装 | [slot-creation-001.txt](slot-creation-001.txt) | [slot-creation-001.md](slot-creation-001.md) | ` default mpls control-word <cr> ` → ` no mpls label <cr> ` | 6 |
