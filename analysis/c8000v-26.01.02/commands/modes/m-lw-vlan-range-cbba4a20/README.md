# 模式 lw-vlan-range

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。

同根名称候选：` lw-vlan-id `, ` lw-vlan-range `。

- 根 ` RVA 0x356D3600 `；名称 ` lw-vlan-range `；提示符 ` config-if-vlan-range `；parent ` interface `；` mode-0343 `。
- 根 ` RVA 0x356D3600 `；名称 ` lw-vlan-id `；提示符 ` config-if-vlan-id `；parent ` interface `；` mode-0344 `。

| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 补充模式入口与历史连接 | [observed-001.txt](observed-001.txt) | [observed-001.md](observed-001.md) | ` default exit-vlan-config <cr> ` → ` pppoe enable group global <cr> ` | 6 |
