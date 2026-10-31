# iosd 命令文本目录

C8000v IOS XE 26.01.02，样本 MD5 ` 9eccfd46caadfff9c18557e2a446e19b `。本目录将已恢复路径整理成小型 Markdown 文本，点击模式即可在 GitHub 阅读。

**路径记录 98,812 条，涉及 287 个主名称；跨模式合计 21,795 个不同 EOL。**相同命令文本可以对应多个上下文、selector 或终点，各记录保留。另列 [尚缺模式路径的 1,350 个候选](unresolved/README.md)。

## 怎样读一条命令

例如 `(config-router)# priority <number:0..127> <cr>`：提示符标明解析模式，`priority` 是关键词，`<number:0..127>` 表示参数范围，`<cr>` 表示路径到达终止动作。参数记号按实际值替换，`<cr>` 对应回车。`<opaque:…>` 及其他 `<?…>` 表示未解析步骤，其实际输入含义保留未知；动态范围按记录原样展示。

模式页中，**命令文本（txt）**直接列出命令和来源编号；**参数与证据（md）**逐条给出 handler、selector、EOL 和参数提示。条件、状态效果、缺口及注册关系链接到共享参考页。编号可用于定位原 gzip 目录中的 `evidence_id`。先列关键词开头的路径，带分析记号的前缀路径附后，各组按语法排序；每页最多 400 条，并限制 UTF-8 字节数。

这份目录描述特定样本的候选语法与历史连接。当前注册、权限、谓词状态和实际执行分别依赖对应证据。命令是否 documented/undocumented 需要与适用版本文档对照，未逐条作该分类。

## 证据模型

| 模型 | 路径记录 | 含义 |
|---|---:|---|
| baseline | 73,159 | 六个基础模式的历史连接 |
| observed | 9,880 | 补充模式入口与历史连接 |
| conditional | 11,138 | 已捕获槽位上的条件安装 |
| slot-creation | 4,622 | 依赖静态建槽的条件安装 |
| other | 13 | 其他模式的历史连接 |

基础模式和补充模式分开保存。条件安装模型保留注册调用、槽位、创建点、顺序和解析条件；当前生效情况另按运行时状态核对。跨捕获的映像关系通过 MD5/RVA 对齐，历史堆地址保持所属捕获来源。

[条件与字段说明](evidence/README.md) · [版本分析结果](../README.md) · [原始派生目录](../cli/summary.json) · [后续模型统计](../unbound-cli/path-summary.json)

## 按模式阅读

模式名称按采集结果保留，同根别名、父模式和定义候选见各模式页。全局配置从 configure 进入；接口配置从 interface/subinterface 进入；router、bgp-address-family 等为补充子模式入口。

| 模式主名称 | 路径记录 |
|---|---:|
| [ANCP](modes/m-ANCP-f32ba368/README.md) | 56 |
| [Ingress-class-map](modes/m-Ingress-class-map-f35db1b4/README.md) | 7 |
| [NHRP-address-family](modes/m-NHRP-address-family-12e89c67/README.md) | 3 |
| [OFA-config](modes/m-OFA-config-32d2e568/README.md) | 3 |
| [SASL-profile](modes/m-SASL-profile-570eba14/README.md) | 9 |
| [accept-dialin](modes/m-accept-dialin-ab238825/README.md) | 8 |
| [accept-dialout](modes/m-accept-dialout-251c60ef/README.md) | 7 |
| [action-submode](modes/m-action-submode-b922053f/README.md) | 1 |
| [address-family](modes/m-address-family-0a372808/README.md) | 671 |
| [application-redundancy-group](modes/m-application-redundancy-group-a09c4cd8/README.md) | 9 |
| [archive](modes/m-archive-0eb3e36b/README.md) | 22 |
| [atm-bm-config](modes/m-atm-bm-config-64219875/README.md) | 75 |
| [atm-bundle-config](modes/m-atm-bundle-config-5d155f46/README.md) | 36 |
| [atm-l2trans-pvc-config](modes/m-atm-l2trans-pvc-config-958f9195/README.md) | 74 |
| [atm-l2trans-pvp-config](modes/m-atm-l2trans-pvp-config-0f0716d8/README.md) | 33 |
| [atm-pvc-range-config](modes/m-atm-pvc-range-config-14d63f0a/README.md) | 90 |
| [atm-range-pvc-config](modes/m-atm-range-pvc-config-c60db53a/README.md) | 80 |
| [atm-svc-bm-config](modes/m-atm-svc-bm-config-704f80ff/README.md) | 75 |
| [atm-svc-bundle-config](modes/m-atm-svc-bundle-config-c37bc051/README.md) | 36 |
| [atm-vc-config](modes/m-atm-vc-config-1bb5bc15/README.md) | 146 |
| [attribute-map](modes/m-attribute-map-1142971d/README.md) | 2 |
| [bba-group](modes/m-bba-group-5c196578/README.md) | 113 |
| [bdomain-efp-mode](modes/m-bdomain-efp-mode-aa663db6/README.md) | 4 |
| [bdomain-glob-mode](modes/m-bdomain-glob-mode-fb6b7763/README.md) | 102 |
| [bgp-address-family](modes/m-bgp-address-family-2cd4dac2/README.md) | 521 |
| [call-filter-matchlist](modes/m-call-filter-matchlist-6483f36e/README.md) | 91 |
| [call-home](modes/m-call-home-daef59b8/README.md) | 11 |
| [casa-config](modes/m-casa-config-60940651/README.md) | 3 |
| [casa-config-wc](modes/m-casa-config-wc-5f02170c/README.md) | 3 |
| [cascustom](modes/m-cascustom-bb9a7f05/README.md) | 9 |
| [cent_domain](modes/m-cent_domain-5bb5bff5/README.md) | 9 |
| [cent_domain_vrf](modes/m-cent_domain_vrf-b09eeb99/README.md) | 4 |
| [cfg-af-topo](modes/m-cfg-af-topo-dd4e02f7/README.md) | 38 |
| [cm-ac](modes/m-cm-ac-9220565a/README.md) | 19 |
| [conf-dia-attr-list](modes/m-conf-dia-attr-list-2f428040/README.md) | 4 |
| [conf-dia-peer](modes/m-conf-dia-peer-4d9609ba/README.md) | 18 |
| [conf-ldap-server](modes/m-conf-ldap-server-ab3d9ed7/README.md) | 35 |
| [conf-rad-server](modes/m-conf-rad-server-bb9b8270/README.md) | 30 |
| [config-l2tp-class](modes/m-config-l2tp-class-d4a72454/README.md) | 55 |
| [config-mac-tunnel-service-instance](modes/m-config-mac-tunnel-service-instance-46cbc7ca/README.md) | 54 |
| [config-onep-mode](modes/m-config-onep-mode-e5da3290/README.md) | 25 |
| [config-onep-tls-mode](modes/m-config-onep-tls-mode-f4f9bc30/README.md) | 6 |
| [config-service-instance](modes/m-config-service-instance-13049fcf/README.md) | 128 |
| [config-st-pw-oam-class](modes/m-config-st-pw-oam-class-684c9002/README.md) | 15 |
| [config-x25-huntgroup](modes/m-config-x25-huntgroup-92ae324a/README.md) | 5 |
| [configure](modes/m-configure-90d08e58/README.md) | 50,163 |
| [conn](modes/m-conn-08041276/README.md) | 7 |
| [control-plane](modes/m-control-plane-96826665/README.md) | 6 |
| [controller](modes/m-controller-c1472135/README.md) | 263 |
| [crypto-gkm-group](modes/m-crypto-gkm-group-b5803929/README.md) | 3 |
| [crypto-map](modes/m-crypto-map-620bfeea/README.md) | 42 |
| [custom](modes/m-custom-6cdfd271/README.md) | 17 |
| [dapr_instance](modes/m-dapr_instance-f1cbe837/README.md) | 4 |
| [decnet-map](modes/m-decnet-map-4ad25cbe/README.md) | 1 |
| [delay-profile-ep-liveness](modes/m-delay-profile-ep-liveness-0f3f17d1/README.md) | 7 |
| [delay-profile-probe-protocol](modes/m-delay-profile-probe-protocol-2dd33a28/README.md) | 10 |
| [delay-profile-srpol-liveness](modes/m-delay-profile-srpol-liveness-e87d5acf/README.md) | 1 |
| [delay-profile-srpol-probe-protocol](modes/m-delay-profile-srpol-probe-protocol-3d18a4ed/README.md) | 1 |
| [delay-profile-srpol-probe-sweep](modes/m-delay-profile-srpol-probe-sweep-6aa5fc4f/README.md) | 1 |
| [dfp-submode](modes/m-dfp-submode-2fd565c6/README.md) | 3 |
| [eap-mprofile-mode](modes/m-eap-mprofile-mode-e8a4562d/README.md) | 24 |
| [ecfm](modes/m-ecfm-c6e24847/README.md) | 22 |
| [ecfm_ll_efp](modes/m-ecfm_ll_efp-7c83b2f3/README.md) | 7 |
| [ecfm_mep_efp](modes/m-ecfm_mep_efp-711388c7/README.md) | 25 |
| [ecfm_mep_int](modes/m-ecfm_mep_int-7c9d9611/README.md) | 22 |
| [ecfm_srv](modes/m-ecfm_srv-73339513/README.md) | 64 |
| [eigrp_af_classic_submode](modes/m-eigrp_af_classic_submode-bcfc4990/README.md) | 119 |
| [eigrp_af_intf_submode](modes/m-eigrp_af_intf_submode-895669fa/README.md) | 58 |
| [eigrp_af_intf_vnet_submode](modes/m-eigrp_af_intf_vnet_submode-3f1cfe8a/README.md) | 54 |
| [eigrp_af_submode](modes/m-eigrp_af_submode-8dd006d5/README.md) | 130 |
| [eigrp_af_topo_submode](modes/m-eigrp_af_topo_submode-4f051837/README.md) | 96 |
| [eigrp_sf_intf_submode](modes/m-eigrp_sf_intf_submode-7a4f0463/README.md) | 35 |
| [eigrp_sf_submode](modes/m-eigrp_sf_submode-6bc7152d/README.md) | 52 |
| [eigrp_sf_topo_submode](modes/m-eigrp_sf_topo_submode-0292057f/README.md) | 25 |
| [eigrp_topo_intf_submode](modes/m-eigrp_topo_intf_submode-019693e4/README.md) | 44 |
| [ether_cfm_ais](modes/m-ether_cfm_ais-ef4179ce/README.md) | 10 |
| [ether_cfm_lck](modes/m-ether_cfm_lck-8150de5b/README.md) | 10 |
| [ethernet-evc-config](modes/m-ethernet-evc-config-e4149402/README.md) | 9 |
| [ethernet-mac-tunnel-config](modes/m-ethernet-mac-tunnel-config-a74afa80/README.md) | 49 |
| [ethernet-mac-tunnel-engine-config](modes/m-ethernet-mac-tunnel-engine-config-ab59c4b8/README.md) | 7 |
| [event-submode](modes/m-event-submode-d60ea7aa/README.md) | 1 |
| [evpn](modes/m-evpn-a0f8fa23/README.md) | 79 |
| [evpn-all-active-mh](modes/m-evpn-all-active-mh-cb82f6f5/README.md) | 4 |
| [evpn-es](modes/m-evpn-es-0ad74155/README.md) | 14 |
| [evpn-evi](modes/m-evpn-evi-56856196/README.md) | 41 |
| [evpn-prof](modes/m-evpn-prof-cf67cd49/README.md) | 47 |
| [evpn-vpws](modes/m-evpn-vpws-8a8e9ce1/README.md) | 14 |
| [exec](modes/m-exec-2706c619/README.md) | 25,423 |
| [fh_applet](modes/m-fh_applet-a76cf299/README.md) | 101 |
| [fh_applet_trigger](modes/m-fh_applet_trigger-b5a6a1a2/README.md) | 5 |
| [filter](modes/m-filter-dfc3376b/README.md) | 7 |
| [filter-submode](modes/m-filter-submode-ce08a189/README.md) | 3 |
| [fr-fr](modes/m-fr-fr-6c76bcf6/README.md) | 7 |
| [fr-pw](modes/m-fr-pw-9021af84/README.md) | 11 |
| [funi-vc-config](modes/m-funi-vc-config-db54f585/README.md) | 108 |
| [global-template](modes/m-global-template-9abcea90/README.md) | 7 |
| [grp-policy-transport](modes/m-grp-policy-transport-a6954aa7/README.md) | 2 |
| [if-evpn-es](modes/m-if-evpn-es-555c40d4/README.md) | 14 |
| [if-topo](modes/m-if-topo-4aa8ef12/README.md) | 25 |
| [if-vnet](modes/m-if-vnet-40a8a87e/README.md) | 24 |
| [inlineservicepolicy](modes/m-inlineservicepolicy-251a56e7/README.md) | 2 |
| [interchassis](modes/m-interchassis-436875dc/README.md) | 8 |
| [interface](modes/m-interface-c796d37c/README.md) | 5,709 |
| [interface-delay](modes/m-interface-delay-17f5d4da/README.md) | 10 |
| [interface-dlci](modes/m-interface-dlci-2fbf63a9/README.md) | 19 |
| [interface-loss](modes/m-interface-loss-2f749c78/README.md) | 8 |
| [ip-sla](modes/m-ip-sla-681e88b6/README.md) | 62 |
| [ip-sla-am-grp](modes/m-ip-sla-am-grp-fedb349f/README.md) | 5 |
| [ip-subscriber](modes/m-ip-subscriber-10ff46ad/README.md) | 7 |
| [ipsub-server-list](modes/m-ipsub-server-list-fd741cd9/README.md) | 5 |
| [ipv6-pmipv6-access-nwk-id](modes/m-ipv6-pmipv6-access-nwk-id-dcfdb34c/README.md) | 2 |
| [ipv6-pmipv6-domain](modes/m-ipv6-pmipv6-domain-a4487686/README.md) | 3 |
| [ipv6-pmipv6-domain-lma](modes/m-ipv6-pmipv6-domain-lma-7d31be3d/README.md) | 2 |
| [ipv6-pmipv6-domain-mag](modes/m-ipv6-pmipv6-domain-mag-d60ada2e/README.md) | 2 |
| [ipv6-pmipv6-domain-mn](modes/m-ipv6-pmipv6-domain-mn-ae3233d9/README.md) | 3 |
| [ipv6-pmipv6-domain-mobile-map](modes/m-ipv6-pmipv6-domain-mobile-map-34a74b37/README.md) | 2 |
| [ipv6-pmipv6-lma](modes/m-ipv6-pmipv6-lma-6eef0a97/README.md) | 3 |
| [ipv6-pmipv6-lma-cust](modes/m-ipv6-pmipv6-lma-cust-0ed64891/README.md) | 3 |
| [ipv6-pmipv6-lma-cust-network](modes/m-ipv6-pmipv6-lma-cust-network-eeba7bae/README.md) | 2 |
| [ipv6-pmipv6-lma-cust-tpt](modes/m-ipv6-pmipv6-lma-cust-tpt-bfb67917/README.md) | 2 |
| [ipv6-pmipv6-lma-haccess-bw-ratio-svc](modes/m-ipv6-pmipv6-lma-haccess-bw-ratio-svc-65744573/README.md) | 2 |
| [ipv6-pmipv6-lma-haccess-mag-bw-ratio-svc](modes/m-ipv6-pmipv6-lma-haccess-mag-bw-ratio-svc-770712b3/README.md) | 2 |
| [ipv6-pmipv6-lma-haccess-profile-def-svc](modes/m-ipv6-pmipv6-lma-haccess-profile-def-svc-f4799889/README.md) | 2 |
| [ipv6-pmipv6-lma-haccess-svc](modes/m-ipv6-pmipv6-lma-haccess-svc-fb61a404/README.md) | 2 |
| [ipv6-pmipv6-lma-network](modes/m-ipv6-pmipv6-lma-network-1254af3a/README.md) | 2 |
| [ipv6-pmipv6-lma-role](modes/m-ipv6-pmipv6-lma-role-f16f03ce/README.md) | 2 |
| [ipv6-pmipv6-lma-svc](modes/m-ipv6-pmipv6-lma-svc-5abf1e49/README.md) | 2 |
| [ipv6-pmipv6-mag](modes/m-ipv6-pmipv6-mag-dfd25e2e/README.md) | 3 |
| [ipv6-pmipv6-mag-addr-dyn](modes/m-ipv6-pmipv6-mag-addr-dyn-9ca22c42/README.md) | 2 |
| [ipv6-pmipv6-mag-haccess-bw-ratio-svc](modes/m-ipv6-pmipv6-mag-haccess-bw-ratio-svc-81691b9b/README.md) | 2 |
| [ipv6-pmipv6-mag-haccess-profile-def-svc](modes/m-ipv6-pmipv6-mag-haccess-profile-def-svc-dcb69d99/README.md) | 2 |
| [ipv6-pmipv6-mag-haccess-svc](modes/m-ipv6-pmipv6-mag-haccess-svc-07019b6f/README.md) | 2 |
| [ipv6-pmipv6-mag-intf](modes/m-ipv6-pmipv6-mag-intf-8f527f7c/README.md) | 2 |
| [ipv6-pmipv6-mag-lma](modes/m-ipv6-pmipv6-mag-lma-080e8233/README.md) | 3 |
| [ipv6-pmipv6-mag-logicalmn](modes/m-ipv6-pmipv6-mag-logicalmn-39198f24/README.md) | 3 |
| [ipv6-pmipv6-mag-mn](modes/m-ipv6-pmipv6-mag-mn-7d13cf78/README.md) | 2 |
| [ipv6-pmipv6-mag-svc](modes/m-ipv6-pmipv6-mag-svc-c48ae637/README.md) | 3 |
| [ipv6-router](modes/m-ipv6-router-e883dca7/README.md) | 399 |
| [ipv6-router-address-family](modes/m-ipv6-router-address-family-ee9f5a29/README.md) | 50 |
| [ipv6acl](modes/m-ipv6acl-0bb7e0fb/README.md) | 6 |
| [ipv6fqdnacl](modes/m-ipv6fqdnacl-b180c794/README.md) | 6 |
| [ipv6rbacl](modes/m-ipv6rbacl-cf277c38/README.md) | 6 |
| [irec-agent](modes/m-irec-agent-3e34933c/README.md) | 3 |
| [isis-flex-algo](modes/m-isis-flex-algo-4717ce4b/README.md) | 21 |
| [isis-flood-speed](modes/m-isis-flood-speed-ba7168ee/README.md) | 9 |
| [isis-rtr-affinity](modes/m-isis-rtr-affinity-081f936f/README.md) | 9 |
| [key-chain-macsec](modes/m-key-chain-macsec-a92c8650/README.md) | 4 |
| [l2](modes/m-l2-8a1cee43/README.md) | 31 |
| [l2-pw-rtg](modes/m-l2-pw-rtg-fc98c74d/README.md) | 6 |
| [l2-vfi-neighbor](modes/m-l2-vfi-neighbor-40b80069/README.md) | 9 |
| [l2-vfi-neighbor-interface](modes/m-l2-vfi-neighbor-interface-06b8eae0/README.md) | 7 |
| [l2sdwan](modes/m-l2sdwan-ad53b317/README.md) | 12 |
| [l2sdwan-inst](modes/m-l2sdwan-inst-bbbfa096/README.md) | 15 |
| [l2vpn](modes/m-l2vpn-4db84069/README.md) | 21 |
| [l2vpn-vfi](modes/m-l2vpn-vfi-ae27da1b/README.md) | 30 |
| [l2vpn-vfi-autodiscovery](modes/m-l2vpn-vfi-autodiscovery-615df852/README.md) | 11 |
| [l2vpn-xc](modes/m-l2vpn-xc-f2fee72c/README.md) | 30 |
| [line](modes/m-line-38a9c1e7/README.md) | 298 |
| [lsp-attribute-list](modes/m-lsp-attribute-list-4e893b31/README.md) | 2 |
| [lw-vlan-range](modes/m-lw-vlan-range-cbba4a20/README.md) | 6 |
| [main-cpu](modes/m-main-cpu-5ff857c2/README.md) | 18 |
| [map-class](modes/m-map-class-42c54aad/README.md) | 172 |
| [map-list](modes/m-map-list-bed565af/README.md) | 2 |
| [mcsa](modes/m-mcsa-222a11bc/README.md) | 2 |
| [mka-policy](modes/m-mka-policy-483a7e22/README.md) | 1 |
| [mmon_action_react](modes/m-mmon_action_react-9cd6ce3e/README.md) | 2 |
| [mobile-networks](modes/m-mobile-networks-e4d08875/README.md) | 3 |
| [mode-0006](modes/m-mode-0006-46a5d823/README.md) | 6 |
| [mode-0007](modes/m-mode-0007-b106e8cd/README.md) | 46 |
| [mon-sess-type-capture](modes/m-mon-sess-type-capture-2737e3bf/README.md) | 1 |
| [mon-sess-type-erspan-dst](modes/m-mon-sess-type-erspan-dst-32770e27/README.md) | 2 |
| [mon-sess-type-erspan-src](modes/m-mon-sess-type-erspan-src-1be4b843/README.md) | 3 |
| [mon-sess-type-local](modes/m-mon-sess-type-local-653229f2/README.md) | 1 |
| [mon-sess-type-rspan-src](modes/m-mon-sess-type-rspan-src-20420bb2/README.md) | 1 |
| [mpls-label-stack](modes/m-mpls-label-stack-318edafe/README.md) | 3 |
| [null-interface](modes/m-null-interface-332801b4/README.md) | 11 |
| [oam](modes/m-oam-33c35f04/README.md) | 16 |
| [otv_site](modes/m-otv_site-c94df10e/README.md) | 39 |
| [parameter-submode](modes/m-parameter-submode-84c6c217/README.md) | 42 |
| [parameter_map_cfg](modes/m-parameter_map_cfg-eec5c9c0/README.md) | 270 |
| [pcm-cap-profile](modes/m-pcm-cap-profile-0b9e586a/README.md) | 4 |
| [performance-measurement](modes/m-performance-measurement-2c347aee/README.md) | 320 |
| [pm-delay-ep-profile-advertisement](modes/m-pm-delay-ep-profile-advertisement-cbadce4f/README.md) | 40 |
| [pm-delay-profile](modes/m-pm-delay-profile-e3bc644d/README.md) | 55 |
| [pm-delay-profile-advertisement](modes/m-pm-delay-profile-advertisement-16c622b1/README.md) | 28 |
| [pm-delay-profile-advertisement-accelerated](modes/m-pm-delay-profile-advertisement-accelerated-5495afd6/README.md) | 1 |
| [pm-delay-profile-advertisement-periodic](modes/m-pm-delay-profile-advertisement-periodic-ab34b30d/README.md) | 1 |
| [pm-delay-profile-ep](modes/m-pm-delay-profile-ep-476543f7/README.md) | 73 |
| [pm-delay-profile-ep-advertisement-accelerated](modes/m-pm-delay-profile-ep-advertisement-accelerated-a73a70a8/README.md) | 10 |
| [pm-delay-profile-ep-advertisement-periodic](modes/m-pm-delay-profile-ep-advertisement-periodic-72dde305/README.md) | 16 |
| [pm-delay-profile-ep-advertisement-thcheck](modes/m-pm-delay-profile-ep-advertisement-thcheck-797671d6/README.md) | 13 |
| [pm-delay-profile-ep-probe](modes/m-pm-delay-profile-ep-probe-38ea7ecd/README.md) | 25 |
| [pm-delay-profile-probe](modes/m-pm-delay-profile-probe-0897b6a9/README.md) | 25 |
| [pm-delay-profile-srpol](modes/m-pm-delay-profile-srpol-beb0e976/README.md) | 88 |
| [pm-delay-profile-srpol-advertisement-accelerated](modes/m-pm-delay-profile-srpol-advertisement-accelerated-29ca0c12/README.md) | 10 |
| [pm-delay-profile-srpol-advertisement-periodic](modes/m-pm-delay-profile-srpol-advertisement-periodic-e8cb93e6/README.md) | 16 |
| [pm-delay-profile-srpol-advertisement-thcheck](modes/m-pm-delay-profile-srpol-advertisement-thcheck-92d422a4/README.md) | 13 |
| [pm-delay-profile-srpol-probe](modes/m-pm-delay-profile-srpol-probe-d6f50436/README.md) | 1 |
| [pm-delay-srpol-profile-advertisement](modes/m-pm-delay-srpol-profile-advertisement-625c8f25/README.md) | 40 |
| [pm-endpoint](modes/m-pm-endpoint-c14f4462/README.md) | 31 |
| [pm-endpoint-delaymeasurement](modes/m-pm-endpoint-delaymeasurement-978d9f17/README.md) | 7 |
| [pm-endpoint-seglist](modes/m-pm-endpoint-seglist-d2402cb2/README.md) | 10 |
| [pm-interface](modes/m-pm-interface-4865a539/README.md) | 23 |
| [pm-loss-profile-intf](modes/m-pm-loss-profile-intf-1be21e0a/README.md) | 38 |
| [pm-loss-profile-intf-adv](modes/m-pm-loss-profile-intf-adv-d36372a7/README.md) | 16 |
| [pm-loss-profile-intf-adv-ac](modes/m-pm-loss-profile-intf-adv-ac-1d1f75ea/README.md) | 5 |
| [pm-loss-profile-intf-adv-per](modes/m-pm-loss-profile-intf-adv-per-30f9a134/README.md) | 9 |
| [pm-loss-profile-intf-probe](modes/m-pm-loss-profile-intf-probe-4e32ace5/README.md) | 20 |
| [pm-loss-profile-intf-probe-clr](modes/m-pm-loss-profile-intf-probe-clr-0254a063/README.md) | 14 |
| [pm-loss-profile-intf-probe-clr-type-single](modes/m-pm-loss-profile-intf-probe-clr-type-single-df934c4a/README.md) | 8 |
| [pm-sdlm](modes/m-pm-sdlm-4d696f8e/README.md) | 13 |
| [pm-sdlm-loss](modes/m-pm-sdlm-loss-de26c09f/README.md) | 10 |
| [pm-sdlm-loss-unauth](modes/m-pm-sdlm-loss-unauth-61ce0e14/README.md) | 7 |
| [pm-twamp](modes/m-pm-twamp-32a17b27/README.md) | 13 |
| [pm-twamp-delay](modes/m-pm-twamp-delay-74cd0cbe/README.md) | 10 |
| [pm-twamp-delay-unauth](modes/m-pm-twamp-delay-unauth-e898f16a/README.md) | 7 |
| [policymap-service](modes/m-policymap-service-b6e31109/README.md) | 81 |
| [policymap-service-classmap](modes/m-policymap-service-classmap-98dfbdda/README.md) | 31 |
| [policymap-service-default-classmap](modes/m-policymap-service-default-classmap-706c2003/README.md) | 4 |
| [pseudo_info](modes/m-pseudo_info-219d18a7/README.md) | 10 |
| [pseudowire-class](modes/m-pseudowire-class-aea7375d/README.md) | 84 |
| [pw-tlv-template](modes/m-pw-tlv-template-d04a9299/README.md) | 4 |
| [qosclassmap](modes/m-qosclassmap-9dc7f2ac/README.md) | 86 |
| [qosclasspolice](modes/m-qosclasspolice-fdc8f081/README.md) | 6 |
| [qospolicymap](modes/m-qospolicymap-06d6ac83/README.md) | 13 |
| [qospolicymapclass](modes/m-qospolicymapclass-697f460e/README.md) | 130 |
| [redundancy](modes/m-redundancy-a9be4c13/README.md) | 35 |
| [request-dialin](modes/m-request-dialin-cd098a6f/README.md) | 19 |
| [request-dialout](modes/m-request-dialout-b45cd64d/README.md) | 14 |
| [route-map](modes/m-route-map-04f77102/README.md) | 158 |
| [router](modes/m-router-74c95604/README.md) | 1,096 |
| [router-af-topology](modes/m-router-af-topology-e915b2b8/README.md) | 226 |
| [router_eigrp_classic](modes/m-router_eigrp_classic-444b3718/README.md) | 116 |
| [router_eigrp_named](modes/m-router_eigrp_named-87f38a91/README.md) | 12 |
| [sbc-dbe](modes/m-sbc-dbe-35e92f90/README.md) | 32 |
| [scope](modes/m-scope-5f161c91/README.md) | 439 |
| [scope-address-family](modes/m-scope-address-family-786d9363/README.md) | 489 |
| [scope-address-family-topology](modes/m-scope-address-family-topology-94138291/README.md) | 466 |
| [sd-service](modes/m-sd-service-2bdd706e/README.md) | 5 |
| [sd-service-controller](modes/m-sd-service-controller-cf88f5eb/README.md) | 25 |
| [service-group-glob-mode](modes/m-service-group-glob-mode-864e13fb/README.md) | 10 |
| [sg-l4redirect-group](modes/m-sg-l4redirect-group-c479ed0d/README.md) | 4 |
| [sitemgr](modes/m-sitemgr-c20b8093/README.md) | 6 |
| [sitemgr_vrf](modes/m-sitemgr_vrf-ea3ca5cb/README.md) | 4 |
| [srmpls](modes/m-srmpls-e73a549a/README.md) | 14 |
| [srmpls-attr](modes/m-srmpls-attr-c5b09720/README.md) | 1 |
| [srmpls-attr-af](modes/m-srmpls-attr-af-bca1d028/README.md) | 6 |
| [srmpls-conn](modes/m-srmpls-conn-540d3b5b/README.md) | 2 |
| [srmpls-conn-af](modes/m-srmpls-conn-af-67b01a3e/README.md) | 1 |
| [srmpls-conn-af-algo](modes/m-srmpls-conn-af-algo-60518abe/README.md) | 1 |
| [srmpls-mapserver](modes/m-srmpls-mapserver-47a0f2f0/README.md) | 3 |
| [srmpls-mapserver-sidmap](modes/m-srmpls-mapserver-sidmap-5ebd5c25/README.md) | 2 |
| [srmpls-mapserver-sidmap-af](modes/m-srmpls-mapserver-sidmap-af-2f027d8d/README.md) | 1 |
| [srmpls-mapserver-sidmap-af-algo](modes/m-srmpls-mapserver-sidmap-af-algo-49fc01bd/README.md) | 1 |
| [srte](modes/m-srte-01f2971a/README.md) | 31 |
| [srte-if](modes/m-srte-if-49d3db06/README.md) | 3 |
| [srte-on-demand-color](modes/m-srte-on-demand-color-45fbacb4/README.md) | 9 |
| [srte-policy](modes/m-srte-policy-46627b13/README.md) | 12 |
| [srv6](modes/m-srv6-95c4483f/README.md) | 15 |
| [subinterface](modes/m-subinterface-c0afb635/README.md) | 4,806 |
| [subscriber-policy](modes/m-subscriber-policy-49c21f8d/README.md) | 19 |
| [suppservice](modes/m-suppservice-9b41b390/README.md) | 5 |
| [suppsrvcvp](modes/m-suppsrvcvp-2f09d3ac/README.md) | 16 |
| [template](modes/m-template-5cde0f12/README.md) | 81 |
| [template-peer-policy](modes/m-template-peer-policy-0f8f7dfa/README.md) | 244 |
| [template_pw](modes/m-template_pw-e109e707/README.md) | 86 |
| [top-af-base](modes/m-top-af-base-e2c66282/README.md) | 17 |
| [tp](modes/m-tp-3abd8072/README.md) | 42 |
| [transport-map](modes/m-transport-map-a904f8a4/README.md) | 22 |
| [trunk-group](modes/m-trunk-group-123e69ca/README.md) | 51 |
| [uc_wsapi_mode](modes/m-uc_wsapi_mode-27bb5080/README.md) | 12 |
| [vc-class](modes/m-vc-class-a14c5713/README.md) | 199 |
| [voice-gateway](modes/m-voice-gateway-e8a48ebe/README.md) | 3 |
| [voice-service](modes/m-voice-service-0163eaf8/README.md) | 13 |
| [voice-service-h323](modes/m-voice-service-h323-1d6d6ae8/README.md) | 3 |
| [voiceport](modes/m-voiceport-69ab91e3/README.md) | 21 |
| [voipdialpeer](modes/m-voipdialpeer-edf8789d/README.md) | 54 |
| [vpdn-group](modes/m-vpdn-group-05ad554b/README.md) | 223 |
| [vpdn-template](modes/m-vpdn-template-f9d9925b/README.md) | 211 |
| [vrf](modes/m-vrf-a8c71d68/README.md) | 141 |
| [vrf-af](modes/m-vrf-af-63b78877/README.md) | 121 |
| [vrf-af-topology](modes/m-vrf-af-topology-9a8fdacd/README.md) | 59 |
| [x25-profile](modes/m-x25-profile-d6fa00c0/README.md) | 1 |
| [xconnect-backup-if-config](modes/m-xconnect-backup-if-config-35f930fd/README.md) | 6 |
| [xconnect-if-config](modes/m-xconnect-if-config-c7edbf23/README.md) | 22 |
| [xml-app](modes/m-xml-app-0d8b45a1/README.md) | 4 |
| [xml-transport](modes/m-xml-transport-d9a0d5df/README.md) | 1 |

## 来源与重建

输入文件与输出文本的 SHA256 记录在 [manifest.json](manifest.json)。生成器保留每条来源编号，分页和参考 ID 由内容确定。仓库根目录运行：

```text
python tools/export_cli_textbook.py --version analysis/c8000v-26.01.02 --output analysis/c8000v-26.01.02/commands
```

当前路径图仍有未知动作、缺页及尚未关联的片段。节点图继续保存其他未选为代表路径的写法；此处按已导出的见证列出命令。
