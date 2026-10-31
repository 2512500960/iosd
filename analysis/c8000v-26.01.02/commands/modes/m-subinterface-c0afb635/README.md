# 模式 subinterface

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。


| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 六个基础模式的历史连接 | [baseline-001.txt](baseline-001.txt) | [baseline-001.md](baseline-001.md) | ` aaa connect-info <string> <cr> ` → ` default dot1x default <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-002.txt](baseline-002.txt) | [baseline-002.md](baseline-002.md) | ` default dot1x eap profile <cr> ` → ` default ip pim <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-003.txt](baseline-003.txt) | [baseline-003.md](baseline-003.md) | ` default ip pim bfd <cr> ` → ` default llc2 trej-time <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-004.txt](baseline-004.txt) | [baseline-004.md](baseline-004.md) | ` default llc2 txq-max <cr> ` → ` default tunnel path-mtu-discovery age-timer <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-005.txt](baseline-005.txt) | [baseline-005.md](baseline-005.md) | ` default tunnel path-mtu-discovery min-mtu <cr> ` → ` ip access-group <number:1..199> out <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-006.txt](baseline-006.txt) | [baseline-006.md](baseline-006.md) | ` ip access-group common <number:1..199> <number:1..199> in <cr> ` → ` ipv6 mfib test mask <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-007.txt](baseline-007.txt) | [baseline-007.md](baseline-007.md) | ` ipv6 mfib-cef <cr> ` → ` no alps host-hld <number:1..65535> host-link <number:1..255> ax25 <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-008.txt](baseline-008.txt) | [baseline-008.md](baseline-008.md) | ` no alps n1 <cr> ` → ` no half-duplex test rts <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-009.txt](baseline-009.txt) | [baseline-009.md](baseline-009.md) | ` no half-duplex test transmit <cr> ` → ` no ipv6 nd ra interval <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-010.txt](baseline-010.txt) | [baseline-010.md](baseline-010.md) | ` no ipv6 nd ra lifetime <cr> ` → ` no ppp link trap <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-011.txt](baseline-011.txt) | [baseline-011.md](baseline-011.md) | ` no ppp loopback ignore <cr> ` → ` ppp chap ignoreus <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-012.txt](baseline-012.txt) | [baseline-012.md](baseline-012.md) | ` ppp chap matchnames <cr> ` → ` x25 t23 <number:1..1000> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-013.txt](baseline-013.txt) | [baseline-013.md](baseline-013.md) | ` x25 threshold <number:1..127> <cr> ` → ` yellow alarm detect <cr> ` | 6 |
