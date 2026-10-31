# 模式 router

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` router `。

- 根 ` RVA 0x3422CD00 `；名称 ` router `；提示符 ` config-router `；parent ` configure `；` mode-0163 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` address-family <?option@5555897b9978> <cr> ` → ` default redistribute maximum-prefix <cr> ` | 400 |
| 补充模式入口与历史连接 | [observed-002.txt](observed-002.txt) | [observed-002.md](observed-002.md) | ` default router-id <cr> ` → ` no limit retransmissions <cr> ` | 393 |
| 补充模式入口与历史连接 | [observed-003.txt](observed-003.txt) | [observed-003.md](observed-003.md) | ` no limit retransmissions <cr> ` → ` vrf <string> <cr> ` | 211 |
| 已捕获槽位上的条件安装 | [conditional-001.txt](conditional-001.txt) | [conditional-001.md](conditional-001.md) | ` affinity-map <cr> ` → ` timers manet ackwait <number:0..10000> <cr> ` | 92 |
