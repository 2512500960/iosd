# 模式 qosclassmap

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` qosclassmap `。

- 根 ` RVA 0x33F0EFD0 `；名称 ` qosclassmap `；提示符 ` config-cmap `；parent ` configure `；` mode-0119 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match <?sync_force_action@555589463098> access-group <number:1..2799> <cr> ` → ` <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> stack-start <cr> ` | 49 |
| 已捕获槽位上的条件安装 | [conditional-001.txt](conditional-001.txt) | [conditional-001.md](conditional-001.md) | ` <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match cac status admitted <cr> ` → ` <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request protocol-violation <cr> ` | 37 |
