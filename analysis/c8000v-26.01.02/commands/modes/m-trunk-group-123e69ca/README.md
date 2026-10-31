# 模式 trunk-group

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` trunk-group `。

- 根 ` RVA 0x378FC6A0 `；名称 ` trunk-group `；提示符 ` config-trunk-group `；parent ` configure `；` mode-1219 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` capacity trunk-group update interval <number:10..3600> <cr> ` → ` xsvc <cr> ` | 45 |
| 已捕获槽位上的条件安装 | [conditional-001.txt](conditional-001.txt) | [conditional-001.md](conditional-001.md) | ` default lpcor incoming <cr> ` → ` no lpcor outgoing <cr> ` | 6 |
