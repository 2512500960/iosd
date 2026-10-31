# 模式 qosclasspolice

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` qosclasspolice `。

- 根 ` RVA 0x33F62400 `；名称 ` qosclasspolice `；提示符 ` config-pmap-c-police `；parent ` qospolicymapclass `；` mode-0123 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` <?dumper_command_func@5555894bcef8> conform-action <cr> ` → ` <?dumper_command_func@5555894bcef8> violate-action drop <cr> ` | 6 |
