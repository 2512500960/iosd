# 模式 fh_applet

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` fh_applet `。

- 根 ` RVA 0x339A04E0 `；名称 ` fh_applet `；提示符 ` config-applet `；parent ` configure `；` mode-0042 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` action <string> add <string> <string> <cr> ` → ` trigger period <number:0..4294967295> . <?match_subsec_action@555588f04c88> <cr> ` | 98 |
| 已捕获槽位上的条件安装 | [conditional-001.txt](conditional-001.txt) | [conditional-001.md](conditional-001.md) | ` event ipsla <cr> ` → ` no event ipsla <cr> ` | 3 |
