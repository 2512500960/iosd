# 模式 exec

[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)

每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。


| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |
|---|---|---|---|---:|
| 六个基础模式的历史连接 | [baseline-001.txt](baseline-001.txt) | [baseline-001.md](baseline-001.md) | ` aaa tools memleak-detection-start <cr> ` → ` clear ip rtp header-compression <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-002.txt](baseline-002.txt) | [baseline-002.md](baseline-002.md) | ` clear ip rtp header-compression <interface> <cr> ` → ` debug aaa api <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-003.txt](baseline-003.txt) | [baseline-003.md](baseline-003.md) | ` debug aaa api attr <cr> ` → ` debug cpc function-trace <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-004.txt](baseline-004.txt) | [baseline-004.md](baseline-004.md) | ` debug cpc subblock <cr> ` → ` debug dlsw border-peers interface <interface> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-005.txt](baseline-005.txt) | [baseline-005.md](baseline-005.md) | ` debug dmvpn condition <cr> ` → ` debug hw-module all oir message <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-006.txt](baseline-006.txt) | [baseline-006.md](baseline-006.md) | ` debug hw-module all oir plugin <cr> ` → ` debug ip ospf scheduler hello <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-007.txt](baseline-007.txt) | [baseline-007.md](baseline-007.md) | ` debug ip ospf scheduler hello input <cr> ` → ` debug isis * <string> snp-packets <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-008.txt](baseline-008.txt) | [baseline-008.md](baseline-008.md) | ` debug isis * <string> spt dampening <cr> ` → ` debug nat66 all <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-009.txt](baseline-009.txt) | [baseline-009.md](baseline-009.md) | ` debug nat66 info <cr> ` → ` debug platform software ethernet efp configuration <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-010.txt](baseline-010.txt) | [baseline-010.md](baseline-010.md) | ` debug platform software ethernet efp l2tunnel error <cr> ` → ` debug pre error <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-011.txt](baseline-011.txt) | [baseline-011.md](baseline-011.md) | ` debug pre event <cr> ` → ` debug subscriber feature name qos-peruser error <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-012.txt](baseline-012.txt) | [baseline-012.md](baseline-012.md) | ` debug subscriber feature name qos-peruser event <cr> ` → ` do-exec clear aaa local user fail-attempts all <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-013.txt](baseline-013.txt) | [baseline-013.md](baseline-013.md) | ` do-exec clear aaa local user lockout all <cr> ` → ` do-exec clear registry calls <string> <cr> ` | 375 |
| 六个基础模式的历史连接 | [baseline-014.txt](baseline-014.txt) | [baseline-014.md](baseline-014.md) | ` do-exec clear rif-cache <cr> ` → ` do-exec debug cns image connection <cr> ` | 382 |
| 六个基础模式的历史连接 | [baseline-015.txt](baseline-015.txt) | [baseline-015.md](baseline-015.md) | ` do-exec debug cns image error <cr> ` → ` do-exec debug dhcp <cr> ` | 386 |
| 六个基础模式的历史连接 | [baseline-016.txt](baseline-016.txt) | [baseline-016.md](baseline-016.md) | ` do-exec debug dhcp api <cr> ` → ` do-exec debug hqf feature queue-limit error <cr> ` | 393 |
| 六个基础模式的历史连接 | [baseline-017.txt](baseline-017.txt) | [baseline-017.md](baseline-017.md) | ` do-exec debug hqf feature queue-limit event <cr> ` → ` do-exec debug ip ospf fast-reroute ti-lfa spf <cr> ` | 395 |
| 六个基础模式的历史连接 | [baseline-018.txt](baseline-018.txt) | [baseline-018.md](baseline-018.md) | ` do-exec debug ip ospf flex-algo <cr> ` → ` do-exec debug isis microloop <cr> ` | 395 |
| 六个基础模式的历史连接 | [baseline-019.txt](baseline-019.txt) | [baseline-019.md](baseline-019.md) | ` do-exec debug isis mpls traffic-eng advertisements <cr> ` → ` do-exec debug oce packet frr <cr> ` | 394 |
| 六个基础模式的历史连接 | [baseline-020.txt](baseline-020.txt) | [baseline-020.md](baseline-020.md) | ` do-exec debug oce packet gal-check <cr> ` → ` do-exec debug platform software macsec info <cr> ` | 386 |
| 六个基础模式的历史连接 | [baseline-021.txt](baseline-021.txt) | [baseline-021.md](baseline-021.md) | ` do-exec debug platform software macsec none <cr> ` → ` do-exec debug redundancy application group faults DB <cr> ` | 392 |
| 六个基础模式的历史连接 | [baseline-022.txt](baseline-022.txt) | [baseline-022.md](baseline-022.md) | ` do-exec debug redundancy application group faults all <cr> ` → ` do-exec debug tbridge multicast-2 <cr> ` | 392 |
| 六个基础模式的历史连接 | [baseline-023.txt](baseline-023.txt) | [baseline-023.md](baseline-023.md) | ` do-exec debug tbridge packet-0 <cr> ` → ` do-exec pnpa service copy <string> <string> <cr> ` | 372 |
| 六个基础模式的历史连接 | [baseline-024.txt](baseline-024.txt) | [baseline-024.md](baseline-024.md) | ` do-exec pnpa service correlator-check <number:0..1> <cr> ` → ` do-exec show call-home diagnostic-signature statistics <cr> ` | 349 |
| 六个基础模式的历史连接 | [baseline-025.txt](baseline-025.txt) | [baseline-025.md](baseline-025.md) | ` do-exec show call-home diagnostic-signature statistics download <cr> ` → ` do-exec show ethernet cfm traceroute-cache <cr> ` | 385 |
| 六个基础模式的历史连接 | [baseline-026.txt](baseline-026.txt) | [baseline-026.md](baseline-026.md) | ` do-exec show ethernet dot1ad <cr> ` → ` do-exec show ip nbar resources status <cr> ` | 379 |
| 六个基础模式的历史连接 | [baseline-027.txt](baseline-027.txt) | [baseline-027.md](baseline-027.md) | ` do-exec show ip nbar resources status <number:10..86400> <cr> ` → ` do-exec show issu FSM <cr> ` | 382 |
| 六个基础模式的历史连接 | [baseline-028.txt](baseline-028.txt) | [baseline-028.md](baseline-028.md) | ` do-exec show issu FSM <number:1..4294967295> <cr> ` → ` do-exec show platform software shell command package <cr> ` | 380 |
| 六个基础模式的历史连接 | [baseline-029.txt](baseline-029.txt) | [baseline-029.md](baseline-029.md) | ` do-exec show platform software shell command set <cr> ` → ` do-exec show subscriber service <cr> ` | 386 |
| 六个基础模式的历史连接 | [baseline-030.txt](baseline-030.txt) | [baseline-030.md](baseline-030.md) | ` do-exec show subscriber session <cr> ` → ` do-exec terminal no private <cr> ` | 381 |
| 六个基础模式的历史连接 | [baseline-031.txt](baseline-031.txt) | [baseline-031.md](baseline-031.md) | ` do-exec terminal no privilege level <cr> ` → ` do-exec test ip nat show pool <string> <cr> ` | 356 |
| 六个基础模式的历史连接 | [baseline-032.txt](baseline-032.txt) | [baseline-032.md](baseline-032.md) | ` do-exec test ip nat show pool all <cr> ` → ` do-exec test parser session-lock exit <cr> ` | 325 |
| 六个基础模式的历史连接 | [baseline-033.txt](baseline-033.txt) | [baseline-033.md](baseline-033.md) | ` do-exec test parser session-lock lock-break <cr> ` → ` do-exec test tunnel tun-to <number:0..9> feature enable post-encap <cr> ` | 313 |
| 六个基础模式的历史连接 | [baseline-034.txt](baseline-034.txt) | [baseline-034.md](baseline-034.md) | ` do-exec test tunnel tun-to <number:0..9> feature enable pre-decap <cr> ` → ` do-exec undebug cpl ppcp client <cr> ` | 379 |
| 六个基础模式的历史连接 | [baseline-035.txt](baseline-035.txt) | [baseline-035.md](baseline-035.md) | ` do-exec undebug cpl ppcp client class-type <cr> ` → ` do-exec undebug dot1x all <cr> ` | 393 |
| 六个基础模式的历史连接 | [baseline-036.txt](baseline-036.txt) | [baseline-036.md](baseline-036.md) | ` do-exec undebug dot1x errors <cr> ` → ` do-exec undebug if-mgr errors tunnel-ext <cr> ` | 390 |
| 六个基础模式的历史连接 | [baseline-037.txt](baseline-037.txt) | [baseline-037.md](baseline-037.md) | ` do-exec undebug if-mgr errors vlan-ext <cr> ` → ` do-exec undebug ip pim df <cr> ` | 393 |
| 六个基础模式的历史连接 | [baseline-038.txt](baseline-038.txt) | [baseline-038.md](baseline-038.md) | ` do-exec undebug ip pim drlb <cr> ` → ` do-exec undebug kron major <cr> ` | 388 |
| 六个基础模式的历史连接 | [baseline-039.txt](baseline-039.txt) | [baseline-039.md](baseline-039.md) | ` do-exec undebug l2ctrl all <cr> ` → ` do-exec undebug ospfv3 graceful-restart <cr> ` | 398 |
| 六个基础模式的历史连接 | [baseline-040.txt](baseline-040.txt) | [baseline-040.md](baseline-040.md) | ` do-exec undebug ospfv3 ha <cr> ` → ` do-exec undebug platform software nat64 configuration timeout <cr> ` | 382 |
| 六个基础模式的历史连接 | [baseline-041.txt](baseline-041.txt) | [baseline-041.md](baseline-041.md) | ` do-exec undebug platform software nat64 exec <cr> ` → ` do-exec undebug remote-management pnsc info <cr> ` | 391 |
| 六个基础模式的历史连接 | [baseline-042.txt](baseline-042.txt) | [baseline-042.md](baseline-042.md) | ` do-exec undebug remote-management restful-api error <cr> ` → ` do-exec undebug transport port-manager <cr> ` | 393 |
| 六个基础模式的历史连接 | [baseline-043.txt](baseline-043.txt) | [baseline-043.md](baseline-043.md) | ` do-exec undebug transport port-ranges <cr> ` → ` pnpa service discovery bypass-connectivity-check <number:0..1> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-044.txt](baseline-044.txt) | [baseline-044.md](baseline-044.md) | ` pnpa service discovery bypass-disc-summary <number:0..1> <cr> ` → ` show bgp * tags <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-045.txt](baseline-045.txt) | [baseline-045.md](baseline-045.md) | ` show bgp * template peer-policy <cr> ` → ` show cwmp map wanconnectiondevice <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-046.txt](baseline-046.txt) | [baseline-046.md](baseline-046.md) | ` show cwmp map wandevice <cr> ` → ` show format validate <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-047.txt](baseline-047.txt) | [baseline-047.md](baseline-047.md) | ` show fqdn <cr> ` → ` show ip nbar resources status freebucket <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-048.txt](baseline-048.txt) | [baseline-048.md](baseline-048.md) | ` show ip nbar resources status freebucket <number:1..50> <cr> ` → ` show ipv6 mld internal <interface> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-049.txt](baseline-049.txt) | [baseline-049.md](baseline-049.md) | ` show ipv6 mld ssm-map <cr> ` → ` show mfib background <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-050.txt](baseline-050.txt) | [baseline-050.md](baseline-050.md) | ` show mfib broker <?option@55558aa78120> <cr> ` → ` show pm vp <interface> <number:1..4095> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-051.txt](baseline-051.txt) | [baseline-051.md](baseline-051.md) | ` show pnp all-summary <cr> ` → ` show ssm memory chunk variable feature <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-052.txt](baseline-052.txt) | [baseline-052.md](baseline-052.md) | ` show ssm memory chunk variable queue <cr> ` → ` terminal default download <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-053.txt](baseline-053.txt) | [baseline-053.md](baseline-053.md) | ` terminal default editing <cr> ` → ` test cef <?dumper_command_func@555588cac488> table signal-suppression Enable <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-054.txt](baseline-054.txt) | [baseline-054.md](baseline-054.md) | ` test cef <?dumper_command_func@555588cac488> table signal-suppression Enable <cr> ` → ` test ipc watermark callback <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-055.txt](baseline-055.txt) | [baseline-055.md](baseline-055.md) | ` test ipc window-size <number:32..1024> <cr> ` → ` test platform software macsec frame-capture enable direction ingress <interface> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-056.txt](baseline-056.txt) | [baseline-056.md](baseline-056.md) | ` test platform software macsec pattern-delete name <string> <cr> ` → ` undebug aaa sg-server-selection <cr> ` | 396 |
| 六个基础模式的历史连接 | [baseline-057.txt](baseline-057.txt) | [baseline-057.md](baseline-057.md) | ` undebug aaa subscriber profile <cr> ` → ` undebug crypto engine error <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-058.txt](baseline-058.txt) | [baseline-058.md](baseline-058.md) | ` undebug crypto engine packet <cr> ` → ` undebug epm events <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-059.txt](baseline-059.txt) | [baseline-059.md](baseline-059.md) | ` undebug epm events detail <cr> ` → ` undebug ip bgp evi context <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-060.txt](baseline-060.txt) | [baseline-060.md](baseline-060.md) | ` undebug ip bgp gr <cr> ` → ` undebug ip sla trace twamp-light session <number:1..100> <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-061.txt](baseline-061.txt) | [baseline-061.md](baseline-061.md) | ` undebug ip socket <cr> ` → ` undebug management event mib <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-062.txt](baseline-062.txt) | [baseline-062.md](baseline-062.md) | ` undebug management expression evaluator <cr> ` → ` undebug platform software cef fib table <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-063.txt](baseline-063.txt) | [baseline-063.md](baseline-063.md) | ` undebug platform software cef fib table add <cr> ` → ` undebug pnp service image-install <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-064.txt](baseline-064.txt) | [baseline-064.md](baseline-064.md) | ` undebug pnp service interface-info <cr> ` → ` undebug subscriber elog policy-mgr <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-065.txt](baseline-065.txt) | [baseline-065.md](baseline-065.md) | ` undebug subscriber elog session-mgr <cr> ` → ` virtual-service throttle clear <cr> ` | 400 |
| 六个基础模式的历史连接 | [baseline-066.txt](baseline-066.txt) | [baseline-066.md](baseline-066.md) | ` virtual-service throttle disable <cr> ` → ` <number:1..99> <cr> ` | 22 |
