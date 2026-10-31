# 模式 l2sdwan-inst

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` l2sdwan-inst `。

- 根 ` RVA 0x36125028 `；名称 ` l2sdwan-inst `；提示符 ` config-l2sdwan-sdi `；parent ` configure `；` mode-0487 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 依赖静态建槽的条件安装 | [slot-creation-001.txt](slot-creation-001.txt) | [slot-creation-001.md](slot-creation-001.md) | ` active-election wait-time <number:1..3600> <cr> ` → ` redundancy all-active <cr> ` | 15 |
