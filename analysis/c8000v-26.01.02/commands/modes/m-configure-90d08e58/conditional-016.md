# configure · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-006844

```text
(config)# do-exec debug crypto condition local ipv4 <address> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 4 `；EOL ` RVA 0x3689EBC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Local address。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-db40a5676717b582](../../evidence/parameters-sets-017.md#p-db40a5676717b582) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-006789

```text
(config)# do-exec debug crypto condition peer group <string> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 9 `；EOL ` RVA 0x3689D610 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IKE peer's Unity group name string。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c2b98d37fe390749](../../evidence/parameters-sets-015.md#p-c2b98d37fe390749) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-006758

```text
(config)# do-exec debug crypto condition peer hostname <string> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 10 `；EOL ` RVA 0x3689D350 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` FQDN hostname of IKE peer's identity。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a008621ccdb3f5fb](../../evidence/parameters-sets-012.md#p-a008621ccdb3f5fb) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-006638

```text
(config)# do-exec debug crypto condition peer ipv4 <address> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 13 `；EOL ` RVA 0x3689C998 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer IP address。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-41d79f8de98691ce](../../evidence/parameters-sets-006.md#p-41d79f8de98691ce) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-007897

```text
(config)# do-exec debug crypto condition peer subnet <address> <address> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 12 `；EOL ` RVA 0x3689CD68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer subnet address；` address ` Peer subnet mask。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-41b0bd4a6b05c316](../../evidence/parameters-sets-006.md#p-41b0bd4a6b05c316) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-009373

```text
(config)# do-exec debug crypto condition peer subnet <prefix:dynamic> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 12 `；EOL ` RVA 0x3689CD68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-92bff217bb8075a6](../../evidence/conditions-sets-057.md#c-92bff217bb8075a6) · [缺口 G-167e2d4d33095b92](../../evidence/gaps-sets-001.md#g-167e2d4d33095b92) · [参数 P-91682df858ea1713](../../evidence/parameters-sets-011.md#p-91682df858ea1713) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-006734

```text
(config)# do-exec debug crypto condition peer username <string> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 11 `；EOL ` RVA 0x3689D068 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` FQDN username of IKE peer's identity。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-30d0a1f5b0e5fbc5](../../evidence/parameters-sets-004.md#p-30d0a1f5b0e5fbc5) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003257

```text
(config)# do-exec debug crypto condition reset <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 0 `；EOL ` RVA 0x3689FF68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-007883

```text
(config)# do-exec debug crypto condition session range <number:1..100000000> <number:1..100000000> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 19 `；EOL ` RVA 0x3689D9C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session-id range start；` unsigned_number ` Session-id range end。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-98048f5661dfab0a](../../evidence/parameters-sets-012.md#p-98048f5661dfab0a) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-004867

```text
(config)# do-exec debug crypto condition spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 7 `；EOL ` RVA 0x3689DFB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SPI (Security Policy Index) value。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b8ec2162851f1442](../../evidence/parameters-sets-014.md#p-b8ec2162851f1442) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003548

```text
(config)# do-exec debug crypto condition unmatched <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 15 `；EOL ` RVA 0x3689FA78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005387

```text
(config)# do-exec debug crypto condition unmatched engine <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 20 `；EOL ` RVA 0x3689F7A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005483

```text
(config)# do-exec debug crypto condition unmatched ikev2 <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 17 `；EOL ` RVA 0x3689FA50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005291

```text
(config)# do-exec debug crypto condition unmatched ipsec <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 18 `；EOL ` RVA 0x3689F500 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005202

```text
(config)# do-exec debug crypto condition unmatched isakmp <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 16 `；EOL ` RVA 0x3689F258 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005031

```text
(config)# do-exec debug crypto condition username <string> <cr>
```

Handler ` RVA 0x18D8AD00 `；selector ` 3 `；EOL ` RVA 0x3689E878 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Xauth or Pki-aaa username。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6c6ee7261a7b4363](../../evidence/parameters-sets-009.md#p-6c6ee7261a7b4363) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001472

```text
(config)# do-exec debug crypto csi <cr>
```

Handler ` RVA 0xE002120 `；selector ` 38 `；EOL ` RVA 0x368A5DD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003211

```text
(config)# do-exec debug crypto csi error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 37 `；EOL ` RVA 0x368A5DB0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-009263

```text
(config)# do-exec debug crypto gkm all-features packet <cr>
```

Handler ` RVA 0x190E1EC0 `；selector ` 0 `；EOL ` RVA 0x36953550 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-07ece13f7103ebf4](../../evidence/gaps-sets-001.md#g-07ece13f7103ebf4) · [状态效果 S-b0483f960ecddb9a](../../evidence/state_effects-sets-037.md#s-b0483f960ecddb9a)

### conditional_registration_candidates-006833

```text
(config)# do-exec debug crypto gkm condition group <string> <cr>
```

Handler ` RVA 0x190E16F0 `；selector ` 2 `；EOL ` RVA 0x369540D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-aa1bab655a1ef0db](../../evidence/parameters-sets-013.md#p-aa1bab655a1ef0db) · [状态效果 S-b810c84f1e796c45](../../evidence/state_effects-sets-039.md#s-b810c84f1e796c45)

### conditional_registration_candidates-004928

```text
(config)# do-exec debug crypto gkm condition reset <cr>
```

Handler ` RVA 0x190E16F0 `；selector ` 0 `；EOL ` RVA 0x36953D50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-004868

```text
(config)# do-exec debug crypto gkm condition unmatched <cr>
```

Handler ` RVA 0x190E16F0 `；selector ` 1 `；EOL ` RVA 0x36953AA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-009365

```text
(config)# do-exec debug crypto gkm gm all-features packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 13 `；EOL ` RVA 0x36951878 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-09e636bc5e6bc39e](../../evidence/gaps-sets-001.md#g-09e636bc5e6bc39e) · [状态效果 S-72bbbede6173ab62](../../evidence/state_effects-sets-024.md#s-72bbbede6173ab62)

### conditional_registration_candidates-009394

```text
(config)# do-exec debug crypto gkm gm infrastructure packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 7 `；EOL ` RVA 0x36952F50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-9f5a7994b7f66a3d](../../evidence/gaps-sets-006.md#g-9f5a7994b7f66a3d) · [状态效果 S-f675c5361c1854d3](../../evidence/state_effects-sets-052.md#s-f675c5361c1854d3)

### conditional_registration_candidates-009374

```text
(config)# do-exec debug crypto gkm gm registration packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 8 `；EOL ` RVA 0x36951E38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-fa2eda22a6457a35](../../evidence/gaps-sets-009.md#g-fa2eda22a6457a35) · [状态效果 S-6e4c966e0b8b9142](../../evidence/state_effects-sets-023.md#s-6e4c966e0b8b9142)

### conditional_registration_candidates-009383

```text
(config)# do-exec debug crypto gkm gm rekey packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 9 `；EOL ` RVA 0x369523F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-fdda93acd087dddc](../../evidence/gaps-sets-009.md#g-fdda93acd087dddc) · [状态效果 S-bf08091a4322a432](../../evidence/state_effects-sets-040.md#s-bf08091a4322a432)

### conditional_registration_candidates-009389

```text
(config)# do-exec debug crypto gkm gm replay packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 10 `；EOL ` RVA 0x369529B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-6fcfc08d7e7cd1f1](../../evidence/gaps-sets-004.md#g-6fcfc08d7e7cd1f1) · [状态效果 S-30069546c4cb43e0](../../evidence/state_effects-sets-011.md#s-30069546c4cb43e0)

### conditional_registration_candidates-009362

```text
(config)# do-exec debug crypto gkm ks all-features packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 12 `；EOL ` RVA 0x3694F4B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-049ed347831ca19c](../../evidence/gaps-sets-001.md#g-049ed347831ca19c) · [状态效果 S-dd2aed17e625716a](../../evidence/state_effects-sets-047.md#s-dd2aed17e625716a)

### conditional_registration_candidates-009366

```text
(config)# do-exec debug crypto gkm ks coop packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 2 `；EOL ` RVA 0x3694FA70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-efc38d1c307fe606](../../evidence/gaps-sets-008.md#g-efc38d1c307fe606) · [状态效果 S-20373c2df57eaa02](../../evidence/state_effects-sets-007.md#s-20373c2df57eaa02)

### conditional_registration_candidates-009395

```text
(config)# do-exec debug crypto gkm ks infrastructure packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 1 `；EOL ` RVA 0x36951208 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-f4c85cb50a24474a](../../evidence/gaps-sets-008.md#g-f4c85cb50a24474a) · [状态效果 S-30b70eb690148f56](../../evidence/state_effects-sets-011.md#s-30b70eb690148f56)

### conditional_registration_candidates-009375

```text
(config)# do-exec debug crypto gkm ks registration packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 3 `；EOL ` RVA 0x369500F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-d9b91610ba39ccca](../../evidence/gaps-sets-008.md#g-d9b91610ba39ccca) · [状态效果 S-4c65dd891a4a2018](../../evidence/state_effects-sets-017.md#s-4c65dd891a4a2018)

### conditional_registration_candidates-009384

```text
(config)# do-exec debug crypto gkm ks rekey packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 4 `；EOL ` RVA 0x369506B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-2e34d55640f72ffc](../../evidence/gaps-sets-002.md#g-2e34d55640f72ffc) · [状态效果 S-1128e7e1aba640d3](../../evidence/state_effects-sets-004.md#s-1128e7e1aba640d3)

### conditional_registration_candidates-009390

```text
(config)# do-exec debug crypto gkm ks replay packet <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 5 `；EOL ` RVA 0x36950C70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-337b99e65d22dfef](../../evidence/gaps-sets-002.md#g-337b99e65d22dfef) · [状态效果 S-3cb8b9c8091007d1](../../evidence/state_effects-sets-013.md#s-3cb8b9c8091007d1)

### conditional_registration_candidates-002747

```text
(config)# do-exec debug crypto gkm performance <cr>
```

Handler ` RVA 0x190E1AB0 `；selector ` 14 `；EOL ` RVA 0x36954560 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-3407257be2e97c89](../../evidence/conditional_registrations-sets-001.md#r-3407257be2e97c89) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001242

```text
(config)# do-exec debug crypto ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x368A4AB0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001365

```text
(config)# do-exec debug crypto ikev2 <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 1 `；EOL ` RVA 0x36913900 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002904

```text
(config)# do-exec debug crypto ikev2 data <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 7 `；EOL ` RVA 0x368EA028 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-ab615ae1de2b51cb](../../evidence/conditions-sets-066.md#c-ab615ae1de2b51cb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002662

```text
(config)# do-exec debug crypto ikev2 error <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 0 `；EOL ` RVA 0x368E9830 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002742

```text
(config)# do-exec debug crypto ikev2 internal <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 4 `；EOL ` RVA 0x368E9AD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002682

```text
(config)# do-exec debug crypto ikev2 packet <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 2 `；EOL ` RVA 0x368E9360 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-004824

```text
(config)# do-exec debug crypto ikev2 packet hexdump <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 3 `；EOL ` RVA 0x368E9338 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002511

```text
(config)# do-exec debug crypto ikev2 performance <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 6 `；EOL ` RVA 0x368E9028 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-002823

```text
(config)# do-exec debug crypto ikev2 trace <cr>
```

Handler ` RVA 0x18E988B0 `；selector ` 5 `；EOL ` RVA 0x368E9D80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c1b22c80e1efce17](../../evidence/conditional_registrations-sets-002.md#r-c1b22c80e1efce17) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ab2786c9773cca1](../../evidence/state_effects-sets-013.md#s-3ab2786c9773cca1)

### conditional_registration_candidates-001339

```text
(config)# do-exec debug crypto interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x368A5000 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001412

```text
(config)# do-exec debug crypto ipsec <cr>
```

Handler ` RVA 0x1127D8D0 `；selector ` 16 `；EOL ` RVA 0x368B7E38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002557

```text
(config)# do-exec debug crypto ipsec error <cr>
```

Handler ` RVA 0x1127D8D0 `；selector ` 17 `；EOL ` RVA 0x368A26F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003194

```text
(config)# do-exec debug crypto ipsec ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 29 `；EOL ` RVA 0x368A3798 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005085

```text
(config)# do-exec debug crypto ipsec ha detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 30 `；EOL ` RVA 0x368A34C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005148

```text
(config)# do-exec debug crypto ipsec ha update <cr>
```

Handler ` RVA 0xE002120 `；selector ` 31 `；EOL ` RVA 0x368A3770 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002635

```text
(config)# do-exec debug crypto ipsec hw-request <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x368A2998 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002717

```text
(config)# do-exec debug crypto ipsec message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x368A2C40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005026

```text
(config)# do-exec debug crypto ipsec metadata sgt <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x368A31F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002801

```text
(config)# do-exec debug crypto ipsec states <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x368A2EE8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002697

```text
(config)# do-exec debug crypto ipv6 ipsec <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x368A42C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002783

```text
(config)# do-exec debug crypto ipv6 packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x368A4570 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001487

```text
(config)# do-exec debug crypto isakmp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x368A1E98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002661

```text
(config)# do-exec debug crypto isakmp aaa <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 7 `；EOL ` RVA 0x368A0B68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002510

```text
(config)# do-exec debug crypto isakmp detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x368A0618 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002991

```text
(config)# do-exec debug crypto isakmp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x368A1678 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003361

```text
(config)# do-exec debug crypto isakmp ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x368A1F00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005275

```text
(config)# do-exec debug crypto isakmp ha detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x368A1ED8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-004977

```text
(config)# do-exec debug crypto isakmp kmi <number:1..50> <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 5 `；EOL ` RVA 0x368A0EA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum number of kmi messages to be stored。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-eb1bb18cb1ed23ea](../../evidence/conditions-sets-091.md#c-eb1bb18cb1ed23ea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-959395f9dc6eb734](../../evidence/parameters-sets-011.md#p-959395f9dc6eb734) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002584

```text
(config)# do-exec debug crypto isakmp packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x368A08C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002903

```text
(config)# do-exec debug crypto isakmp performance <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 6 `；EOL ` RVA 0x368A13D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003166

```text
(config)# do-exec debug crypto isakmp qos <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 8 `；EOL ` RVA 0x368A1BC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003078

```text
(config)# do-exec debug crypto isakmp session <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 11 `；EOL ` RVA 0x368A1920 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002822

```text
(config)# do-exec debug crypto isakmp stats <cr>
```

Handler ` RVA 0x1127D7B0 `；selector ` 4 `；EOL ` RVA 0x368A1128 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001288

```text
(config)# do-exec debug crypto kmi <cr>
```

Handler ` RVA 0xE002120 `；selector ` 32 `；EOL ` RVA 0x368A4D58 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002627

```text
(config)# do-exec debug crypto mib detail <cr>
```

Handler ` RVA 0x1127D940 `；selector ` 23 `；EOL ` RVA 0x368A3D20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002709

```text
(config)# do-exec debug crypto mib error <cr>
```

Handler ` RVA 0x1127D990 `；selector ` 22 `；EOL ` RVA 0x368A3FC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001480

```text
(config)# do-exec debug crypto rmal <cr>
```

Handler ` RVA 0xE002120 `；selector ` 33 `；EOL ` RVA 0x368A55E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003350

```text
(config)# do-exec debug crypto rmal datahandler <cr>
```

Handler ` RVA 0xE002120 `；selector ` 35 `；EOL ` RVA 0x368A5648 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-005258

```text
(config)# do-exec debug crypto rmal datahandler error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 36 `；EOL ` RVA 0x368A5620 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-003118

```text
(config)# do-exec debug crypto rmal error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 34 `；EOL ` RVA 0x368A5310 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-001213

```text
(config)# do-exec debug crypto routing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x368A4808 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8460910f52c066](../../evidence/conditional_registrations-sets-001.md#r-4d8460910f52c066) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c822539275957cc](../../evidence/state_effects-sets-033.md#s-9c822539275957cc)

### conditional_registration_candidates-002824

```text
(config)# do-exec debug crypto skip-client debug <cr>
```

Handler ` RVA 0x19292D90 `；selector ` 0 `；EOL ` RVA 0x36984D08 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a22a82a85e3c8fc8](../../evidence/conditional_registrations-sets-002.md#r-a22a82a85e3c8fc8) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f1457ca96a6efaca](../../evidence/state_effects-sets-051.md#s-f1457ca96a6efaca)

### conditional_registration_candidates-002664

```text
(config)# do-exec debug crypto skip-client error <cr>
```

Handler ` RVA 0x19292D90 `；selector ` 2 `；EOL ` RVA 0x369847B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a22a82a85e3c8fc8](../../evidence/conditional_registrations-sets-002.md#r-a22a82a85e3c8fc8) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f1457ca96a6efaca](../../evidence/state_effects-sets-051.md#s-f1457ca96a6efaca)

### conditional_registration_candidates-002744

```text
(config)# do-exec debug crypto skip-client event <cr>
```

Handler ` RVA 0x19292D90 `；selector ` 3 `；EOL ` RVA 0x36984A60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a22a82a85e3c8fc8](../../evidence/conditional_registrations-sets-002.md#r-a22a82a85e3c8fc8) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f1457ca96a6efaca](../../evidence/state_effects-sets-051.md#s-f1457ca96a6efaca)

### conditional_registration_candidates-002586

```text
(config)# do-exec debug crypto skip-client feature-flow <cr>
```

Handler ` RVA 0x19292D90 `；selector ` 1 `；EOL ` RVA 0x36984510 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a22a82a85e3c8fc8](../../evidence/conditional_registrations-sets-002.md#r-a22a82a85e3c8fc8) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f1457ca96a6efaca](../../evidence/state_effects-sets-051.md#s-f1457ca96a6efaca)

### conditional_registration_candidates-001732

```text
(config)# do-exec debug crypto ssl <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 0 `；EOL ` RVA 0x377B22A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-11fa77197ba55a33](../../evidence/conditions-sets-007.md#c-11fa77197ba55a33) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-002905

```text
(config)# do-exec debug crypto ssl aaa <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 9 `；EOL ` RVA 0x377ADE40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003671

```text
(config)# do-exec debug crypto ssl acl <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 31 `；EOL ` RVA 0x377B0500 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005039

```text
(config)# do-exec debug crypto ssl aggr-auth message <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 7 `；EOL ` RVA 0x377ADBA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-004968

```text
(config)# do-exec debug crypto ssl aggr-auth packets <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 6 `；EOL ` RVA 0x377AD900 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-007895

```text
(config)# do-exec debug crypto ssl condition client ipv4 <address> <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 18 `；EOL ` RVA 0x377AC640 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP Address。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e2e375461937563a](../../evidence/parameters-sets-017.md#p-e2e375461937563a) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-007916

```text
(config)# do-exec debug crypto ssl condition client username <string> <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 19 `；EOL ` RVA 0x377AC900 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Username of the Client Session。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-d52ccfc58257b4f7](../../evidence/parameters-sets-016.md#p-d52ccfc58257b4f7) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003915

```text
(config)# do-exec debug crypto ssl count <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 32 `；EOL ` RVA 0x377B1248 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003880

```text
(config)# do-exec debug crypto ssl data <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 33 `；EOL ` RVA 0x377B0FA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-002992

```text
(config)# do-exec debug crypto ssl dns <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 8 `；EOL ` RVA 0x377AE0E8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-004034

```text
(config)# do-exec debug crypto ssl dtls <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 37 `；EOL ` RVA 0x377B1AD0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005986

```text
(config)# do-exec debug crypto ssl dtls errors <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 38 `；EOL ` RVA 0x377B1558 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-006023

```text
(config)# do-exec debug crypto ssl dtls events <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 39 `；EOL ` RVA 0x377B1800 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-006054

```text
(config)# do-exec debug crypto ssl dtls packets <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 40 `；EOL ` RVA 0x377B1AA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003255

```text
(config)# do-exec debug crypto ssl dump <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 12 `；EOL ` RVA 0x377AE9E8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003533

```text
(config)# do-exec debug crypto ssl emweb <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 21 `；EOL ` RVA 0x377AF828 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005444

```text
(config)# do-exec debug crypto ssl emweb state <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 22 `；EOL ` RVA 0x377AF800 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005068

```text
(config)# do-exec debug crypto ssl entry <string> <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 1 `；EOL ` RVA 0x377ACD30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto SSL Context Name。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8ebcd5b1b2169ffb](../../evidence/parameters-sets-011.md#p-8ebcd5b1b2169ffb) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-009495

```text
(config)# do-exec debug crypto ssl entry <string> source <address> <?ipmask_action@55558cd00d80> <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 1 `；EOL ` RVA 0x377ACD30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Crypto SSL Context Name；` address ` Source IP address。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2fdf8197c1a0ede9](../../evidence/conditions-sets-019.md#c-2fdf8197c1a0ede9) · [缺口 G-6853f4c1b5f8723a](../../evidence/gaps-sets-004.md#g-6853f4c1b5f8723a) · [参数 P-3064534f73328a6f](../../evidence/parameters-sets-004.md#p-3064534f73328a6f) · [状态效果 S-c0c89fe9c69ccb90](../../evidence/state_effects-sets-041.md#s-c0c89fe9c69ccb90)

### conditional_registration_candidates-003009

```text
(config)# do-exec debug crypto ssl http <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 3 `；EOL ` RVA 0x377AD5E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-004911

```text
(config)# do-exec debug crypto ssl http authentication <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 4 `；EOL ` RVA 0x377AD090 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-004978

```text
(config)# do-exec debug crypto ssl http trace <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 5 `；EOL ` RVA 0x377AD338 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003836

```text
(config)# do-exec debug crypto ssl hw-api <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 20 `；EOL ` RVA 0x377B0CF8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003999

```text
(config)# do-exec debug crypto ssl license <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 36 `；EOL ` RVA 0x377B1FF8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2a7ce1189399e89f](../../evidence/conditions-sets-017.md#c-2a7ce1189399e89f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003601

```text
(config)# do-exec debug crypto ssl package <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 27 `；EOL ` RVA 0x377B0258 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003274

```text
(config)# do-exec debug crypto ssl sdps <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 11 `；EOL ` RVA 0x377AE728 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003617

```text
(config)# do-exec debug crypto ssl sock <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 25 `；EOL ` RVA 0x377AFD88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005538

```text
(config)# do-exec debug crypto ssl sock flow <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 24 `；EOL ` RVA 0x377AFD60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003733

```text
(config)# do-exec debug crypto ssl timer <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 30 `；EOL ` RVA 0x377B07A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003693

```text
(config)# do-exec debug crypto ssl tunnel <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 13 `；EOL ` RVA 0x377AF2B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2b0d0de78b36d48d](../../evidence/conditions-sets-017.md#c-2b0d0de78b36d48d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005547

```text
(config)# do-exec debug crypto ssl tunnel errors <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 15 `；EOL ` RVA 0x377AEFE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2b0d0de78b36d48d](../../evidence/conditions-sets-017.md#c-2b0d0de78b36d48d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005443

```text
(config)# do-exec debug crypto ssl tunnel events <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 14 `；EOL ` RVA 0x377AED38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2b0d0de78b36d48d](../../evidence/conditions-sets-017.md#c-2b0d0de78b36d48d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-005644

```text
(config)# do-exec debug crypto ssl tunnel packets <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 16 `；EOL ` RVA 0x377AF288 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-2b0d0de78b36d48d](../../evidence/conditions-sets-017.md#c-2b0d0de78b36d48d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003784

```text
(config)# do-exec debug crypto ssl url-disp <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 34 `；EOL ` RVA 0x377B0A50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-746bff4701ccb1b7](../../evidence/conditions-sets-045.md#c-746bff4701ccb1b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-003187

```text
(config)# do-exec debug crypto ssl webservice <cr>
```

Handler ` RVA 0x1DA4B210 `；selector ` 2 `；EOL ` RVA 0x377AE3F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-83614dde5f1e1b76](../../evidence/conditional_registrations-sets-002.md#r-83614dde5f1e1b76) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75369a0bdcfa479f](../../evidence/state_effects-sets-025.md#s-75369a0bdcfa479f)

### conditional_registration_candidates-002663

```text
(config)# do-exec debug crypto tls-tunnel error <cr>
```

Handler ` RVA 0x1926D190 `；selector ` 2 `；EOL ` RVA 0x3697E668 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bde9862cce8cd534](../../evidence/conditional_registrations-sets-002.md#r-bde9862cce8cd534) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-733ad9011634de0f](../../evidence/state_effects-sets-024.md#s-733ad9011634de0f)

### conditional_registration_candidates-002743

```text
(config)# do-exec debug crypto tls-tunnel event <cr>
```

Handler ` RVA 0x1926D190 `；selector ` 3 `；EOL ` RVA 0x3697E910 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bde9862cce8cd534](../../evidence/conditional_registrations-sets-002.md#r-bde9862cce8cd534) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-733ad9011634de0f](../../evidence/state_effects-sets-024.md#s-733ad9011634de0f)

### conditional_registration_candidates-002585

```text
(config)# do-exec debug crypto tls-tunnel feature-flow <cr>
```

Handler ` RVA 0x1926D190 `；selector ` 1 `；EOL ` RVA 0x3697E3C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bde9862cce8cd534](../../evidence/conditional_registrations-sets-002.md#r-bde9862cce8cd534) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-733ad9011634de0f](../../evidence/state_effects-sets-024.md#s-733ad9011634de0f)

### conditional_registration_candidates-000336

```text
(config)# do-exec debug ctl-client <cr>
```

Handler ` RVA 0x1DE084E0 `；selector ` 0 `；EOL ` RVA 0x37868A68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7841db52cdb67c44](../../evidence/conditional_registrations-sets-002.md#r-7841db52cdb67c44) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000938

```text
(config)# do-exec debug dapr packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36E54550 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fe7b06be8c5aee61](../../evidence/state_effects-sets-054.md#s-fe7b06be8c5aee61)

### conditional_registration_candidates-002123

```text
(config)# do-exec debug dapr packet detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x36E54280 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fe7b06be8c5aee61](../../evidence/state_effects-sets-054.md#s-fe7b06be8c5aee61)

### conditional_registration_candidates-002195

```text
(config)# do-exec debug dapr packet dump <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x36E54528 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fe7b06be8c5aee61](../../evidence/state_effects-sets-054.md#s-fe7b06be8c5aee61)

### conditional_registration_candidates-002049

```text
(config)# do-exec debug dapr packet error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x36E53FD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fe7b06be8c5aee61](../../evidence/state_effects-sets-054.md#s-fe7b06be8c5aee61)

### conditional_registration_candidates-000871

```text
(config)# do-exec debug dapr socket <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36E53A88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7fdcb7c1e7600833](../../evidence/state_effects-sets-027.md#s-7fdcb7c1e7600833)

### conditional_registration_candidates-002061

```text
(config)# do-exec debug dapr socket detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36E53A60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7fdcb7c1e7600833](../../evidence/state_effects-sets-027.md#s-7fdcb7c1e7600833)

### conditional_registration_candidates-001985

```text
(config)# do-exec debug dapr socket error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x36E537B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1feafcaea4039f40](../../evidence/conditional_registrations-sets-001.md#r-1feafcaea4039f40) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7fdcb7c1e7600833](../../evidence/state_effects-sets-027.md#s-7fdcb7c1e7600833)

### conditional_registration_candidates-000813

```text
(config)# do-exec debug decnet adjacencies <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x36E88DA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bc51f3778dac33ea](../../evidence/conditional_registrations-sets-002.md#r-bc51f3778dac33ea) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e592067aaf9dd8](../../evidence/state_effects-sets-032.md#s-94e592067aaf9dd8)

### conditional_registration_candidates-000767

```text
(config)# do-exec debug decnet connects <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36E88AF8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bc51f3778dac33ea](../../evidence/conditional_registrations-sets-002.md#r-bc51f3778dac33ea) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e592067aaf9dd8](../../evidence/state_effects-sets-032.md#s-94e592067aaf9dd8)

### conditional_registration_candidates-000855

```text
(config)# do-exec debug decnet events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36E89048 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bc51f3778dac33ea](../../evidence/conditional_registrations-sets-002.md#r-bc51f3778dac33ea) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e592067aaf9dd8](../../evidence/state_effects-sets-032.md#s-94e592067aaf9dd8)

### conditional_registration_candidates-000896

```text
(config)# do-exec debug decnet packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36E892F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bc51f3778dac33ea](../../evidence/conditional_registrations-sets-002.md#r-bc51f3778dac33ea) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e592067aaf9dd8](../../evidence/state_effects-sets-032.md#s-94e592067aaf9dd8)

### conditional_registration_candidates-000929

```text
(config)# do-exec debug decnet routing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36E89598 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-bc51f3778dac33ea](../../evidence/conditional_registrations-sets-002.md#r-bc51f3778dac33ea) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e592067aaf9dd8](../../evidence/state_effects-sets-032.md#s-94e592067aaf9dd8)

### conditional_registration_candidates-000925

```text
(config)# do-exec debug dialog-manager all <cr>
```

Handler ` RVA 0x17C7C490 `；selector ` 0 `；EOL ` RVA 0x3662C3D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-416025ee1fef2d36](../../evidence/conditional_registrations-sets-001.md#r-416025ee1fef2d36) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c937b7baf0370f15](../../evidence/state_effects-sets-043.md#s-c937b7baf0370f15)

### conditional_registration_candidates-000756

```text
(config)# do-exec debug dialog-manager errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3662B938 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-416025ee1fef2d36](../../evidence/conditional_registrations-sets-001.md#r-416025ee1fef2d36) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c937b7baf0370f15](../../evidence/state_effects-sets-043.md#s-c937b7baf0370f15)

### conditional_registration_candidates-000804

```text
(config)# do-exec debug dialog-manager events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3662BBE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-416025ee1fef2d36](../../evidence/conditional_registrations-sets-001.md#r-416025ee1fef2d36) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c937b7baf0370f15](../../evidence/state_effects-sets-043.md#s-c937b7baf0370f15)

### conditional_registration_candidates-000889

```text
(config)# do-exec debug dialog-manager info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3662C130 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-416025ee1fef2d36](../../evidence/conditional_registrations-sets-001.md#r-416025ee1fef2d36) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c937b7baf0370f15](../../evidence/state_effects-sets-043.md#s-c937b7baf0370f15)

### conditional_registration_candidates-000845

```text
(config)# do-exec debug dialog-manager xml <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3662BE88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-416025ee1fef2d36](../../evidence/conditional_registrations-sets-001.md#r-416025ee1fef2d36) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c937b7baf0370f15](../../evidence/state_effects-sets-043.md#s-c937b7baf0370f15)

### conditional_registration_candidates-000332

```text
(config)# do-exec debug dialpeer <cr>
```

Handler ` RVA 0x1BB3B000 `；selector ` 0 `；EOL ` RVA 0x36FAE1B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ec60c45fc50a5d4e](../../evidence/conditional_registrations-sets-003.md#r-ec60c45fc50a5d4e) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b8cd96781a4486f8](../../evidence/state_effects-sets-039.md#s-b8cd96781a4486f8)

### conditional_registration_candidates-000807

```text
(config)# do-exec debug domain all <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 0 `；EOL ` RVA 0x36662600 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c11c5396043d963a](../../evidence/conditional_registrations-sets-002.md#r-c11c5396043d963a) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-90eeeec895496875](../../evidence/state_effects-sets-031.md#s-90eeeec895496875)

### conditional_registration_candidates-000864

```text
(config)# do-exec debug ephone error <cr>
```

Handler ` RVA 0x177CE1A0 `；selector ` 0 `；EOL ` RVA 0x36485580 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-490025ec0a11b499](../../evidence/conditional_registrations-sets-001.md#r-490025ec0a11b499) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f98ee1d417606173](../../evidence/state_effects-sets-053.md#s-f98ee1d417606173)

### conditional_registration_candidates-000754

```text
(config)# do-exec debug ephone hfs <cr>
```

Handler ` RVA 0x1773DAA0 `；selector ` 0 `；EOL ` RVA 0x36485238 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-490025ec0a11b499](../../evidence/conditional_registrations-sets-001.md#r-490025ec0a11b499) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000815

```text
(config)# do-exec debug eta error <cr>
```

Handler ` RVA 0x1D972950 `；selector ` 0 `；EOL ` RVA 0x37796F48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7aa4fc94fb523248](../../evidence/conditional_registrations-sets-002.md#r-7aa4fc94fb523248) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000857

```text
(config)# do-exec debug eta event <cr>
```

Handler ` RVA 0x1D972950 `；selector ` 1 `；EOL ` RVA 0x377971F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7aa4fc94fb523248](../../evidence/conditional_registrations-sets-002.md#r-7aa4fc94fb523248) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000898

```text
(config)# do-exec debug eta message <cr>
```

Handler ` RVA 0x1D972950 `；selector ` 2 `；EOL ` RVA 0x37797498 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7aa4fc94fb523248](../../evidence/conditional_registrations-sets-002.md#r-7aa4fc94fb523248) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-004754

```text
(config)# do-exec debug event manager detector ipsla <cr>
```

Handler ` RVA 0x110705A0 `；selector ` 48 `；EOL ` RVA 0x369A1860 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-165d508a2253e78d](../../evidence/conditional_registrations-sets-001.md#r-165d508a2253e78d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-34ad5f68815c5669](../../evidence/state_effects-sets-012.md#s-34ad5f68815c5669)

### conditional_registration_candidates-001018

```text
(config)# do-exec debug evpn all <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 9 `；EOL ` RVA 0x36027B00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000883

```text
(config)# do-exec debug evpn database <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 1 `；EOL ` RVA 0x36026DB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000919

```text
(config)# do-exec debug evpn dm <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 3 `；EOL ` RVA 0x36027060 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000798

```text
(config)# do-exec debug evpn error <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 8 `；EOL ` RVA 0x36026868 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000951

```text
(config)# do-exec debug evpn ha <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 4 `；EOL ` RVA 0x36027308 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-001002

```text
(config)# do-exec debug evpn mlrib <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 6 `；EOL ` RVA 0x36027858 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000839

```text
(config)# do-exec debug evpn pd <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 2 `；EOL ` RVA 0x36026B10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-000979

```text
(config)# do-exec debug evpn rwatch <cr>
```

Handler ` RVA 0x1692DE10 `；selector ` 5 `；EOL ` RVA 0x360275B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d2534e7aaef75215](../../evidence/conditional_registrations-sets-002.md#r-d2534e7aaef75215) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-035b6874b8925619](../../evidence/state_effects-sets-001.md#s-035b6874b8925619)

### conditional_registration_candidates-004434

```text
(config)# do-exec debug fax relay t30 all-level-1 <cr>
```

Handler ` RVA 0x1BD19870 `；selector ` 3 `；EOL ` RVA 0x36FE9170 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-847a09c42887719a](../../evidence/conditional_registrations-sets-002.md#r-847a09c42887719a) · [条件 C-df4bcc8f86371bf7](../../evidence/conditions-sets-086.md#c-df4bcc8f86371bf7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98e15b393d424dec](../../evidence/state_effects-sets-032.md#s-98e15b393d424dec)

### conditional_registration_candidates-006520

```text
(config)# do-exec debug fax relay t30 called-number <string> <cr>
```

Handler ` RVA 0x1BD19870 `；selector ` 0 `；EOL ` RVA 0x36FE9768 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Called number。

[候选注册 R-847a09c42887719a](../../evidence/conditional_registrations-sets-002.md#r-847a09c42887719a) · [条件 C-82a45f9fcaa26bc4](../../evidence/conditions-sets-051.md#c-82a45f9fcaa26bc4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-ac37ee3ca01231b8](../../evidence/parameters-sets-013.md#p-ac37ee3ca01231b8) · [状态效果 S-98e15b393d424dec](../../evidence/state_effects-sets-032.md#s-98e15b393d424dec)

### conditional_registration_candidates-006487

```text
(config)# do-exec debug fax relay t30 calling-number <string> <cr>
```

Handler ` RVA 0x1BD19870 `；selector ` 1 `；EOL ` RVA 0x36FE9480 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Calling number。

[候选注册 R-847a09c42887719a](../../evidence/conditional_registrations-sets-002.md#r-847a09c42887719a) · [条件 C-277ebf7744955b47](../../evidence/conditions-sets-015.md#c-277ebf7744955b47) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6a5bbca5e09a0f9b](../../evidence/parameters-sets-008.md#p-6a5bbca5e09a0f9b) · [状态效果 S-98e15b393d424dec](../../evidence/state_effects-sets-032.md#s-98e15b393d424dec)

### conditional_registration_candidates-004433

```text
(config)# do-exec debug fax relay t30 level-2 <cr>
```

Handler ` RVA 0x1BD19870 `；selector ` 4 `；EOL ` RVA 0x36FE8EA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-847a09c42887719a](../../evidence/conditional_registrations-sets-002.md#r-847a09c42887719a) · [条件 C-44a39982af35ad1a](../../evidence/conditions-sets-027.md#c-44a39982af35ad1a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98e15b393d424dec](../../evidence/state_effects-sets-032.md#s-98e15b393d424dec)

### conditional_registration_candidates-002259

```text
(config)# do-exec debug flow file-export all <cr>
```

Handler ` RVA 0x1AF00870 `；selector ` 2 `；EOL ` RVA 0x36E72270 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-82ee525c0649cbd0](../../evidence/conditional_registrations-sets-002.md#r-82ee525c0649cbd0) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c479a457fd80690c](../../evidence/state_effects-sets-042.md#s-c479a457fd80690c)

### conditional_registration_candidates-002184

```text
(config)# do-exec debug flow file-export error <cr>
```

Handler ` RVA 0x1AF00870 `；selector ` 1 `；EOL ` RVA 0x36E71FC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-82ee525c0649cbd0](../../evidence/conditional_registrations-sets-002.md#r-82ee525c0649cbd0) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c479a457fd80690c](../../evidence/state_effects-sets-042.md#s-c479a457fd80690c)

### conditional_registration_candidates-002113

```text
(config)# do-exec debug flow file-export event <cr>
```

Handler ` RVA 0x1AF00870 `；selector ` 0 `；EOL ` RVA 0x36E71D20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-82ee525c0649cbd0](../../evidence/conditional_registrations-sets-002.md#r-82ee525c0649cbd0) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c479a457fd80690c](../../evidence/state_effects-sets-042.md#s-c479a457fd80690c)

### conditional_registration_candidates-000882

```text
(config)# do-exec debug flow-sampler class-based <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34CE23A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb76084354400ae3](../../evidence/conditional_registrations-sets-002.md#r-cb76084354400ae3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-80b2ba7e41d7d38c](../../evidence/state_effects-sets-027.md#s-80b2ba7e41d7d38c)

### conditional_registration_candidates-000750

```text
(config)# do-exec debug flow-sampler events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34CE1B80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb76084354400ae3](../../evidence/conditional_registrations-sets-002.md#r-cb76084354400ae3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-17633b96eee5bdf6](../../evidence/state_effects-sets-005.md#s-17633b96eee5bdf6)

### conditional_registration_candidates-000796

```text
(config)# do-exec debug flow-sampler ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34CE1E38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb76084354400ae3](../../evidence/conditional_registrations-sets-002.md#r-cb76084354400ae3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e2806bfc1cc8da54](../../evidence/state_effects-sets-048.md#s-e2806bfc1cc8da54)

### conditional_registration_candidates-000837

```text
(config)# do-exec debug flow-sampler match <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34CE20F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb76084354400ae3](../../evidence/conditional_registrations-sets-002.md#r-cb76084354400ae3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-43159ac5eb17dbed](../../evidence/state_effects-sets-015.md#s-43159ac5eb17dbed)

### conditional_registration_candidates-003678

```text
(config)# do-exec debug frame-relay adjacency vc-bundle <cr>
```

Handler ` RVA 0xF6061A0 `；selector ` 29 `；EOL ` RVA 0x369AFDC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-3c4d7d9649132f47](../../evidence/conditional_registrations-sets-001.md#r-3c4d7d9649132f47) · [条件 C-b67119319eb7db9c](../../evidence/conditions-sets-071.md#c-b67119319eb7db9c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3afb1ed43610ab65](../../evidence/state_effects-sets-013.md#s-3afb1ed43610ab65)

### conditional_registration_candidates-001537

```text
(config)# do-exec debug frame-relay pseudowire <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x369A53B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-70ae95f06196bcdf](../../evidence/conditional_registrations-sets-001.md#r-70ae95f06196bcdf) · [条件 C-b67119319eb7db9c](../../evidence/conditions-sets-071.md#c-b67119319eb7db9c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3afb1ed43610ab65](../../evidence/state_effects-sets-013.md#s-3afb1ed43610ab65)

### conditional_registration_candidates-003608

```text
(config)# do-exec debug frame-relay vc-bundle detail <cr>
```

Handler ` RVA 0xF6061A0 `；selector ` 31 `；EOL ` RVA 0x369AFAB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e1dfffff90dffbf6](../../evidence/conditional_registrations-sets-002.md#r-e1dfffff90dffbf6) · [条件 C-b67119319eb7db9c](../../evidence/conditions-sets-071.md#c-b67119319eb7db9c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3afb1ed43610ab65](../../evidence/state_effects-sets-013.md#s-3afb1ed43610ab65)

### conditional_registration_candidates-003524

```text
(config)# do-exec debug frame-relay vc-bundle state-change <cr>
```

Handler ` RVA 0xF6061A0 `；selector ` 30 `；EOL ` RVA 0x369AF7F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e1dfffff90dffbf6](../../evidence/conditional_registrations-sets-002.md#r-e1dfffff90dffbf6) · [条件 C-b67119319eb7db9c](../../evidence/conditions-sets-071.md#c-b67119319eb7db9c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3afb1ed43610ab65](../../evidence/state_effects-sets-013.md#s-3afb1ed43610ab65)

### conditional_registration_candidates-000761

```text
(config)# do-exec debug frr-manager api <cr>
```

Handler ` RVA 0x196002B0 `；selector ` 1 `；EOL ` RVA 0x36A37998 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-13ce7d60ae09af1d](../../evidence/conditional_registrations-sets-001.md#r-13ce7d60ae09af1d) · [条件 C-2f4a3ce9c7e99321](../../evidence/conditions-sets-019.md#c-2f4a3ce9c7e99321) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000850

```text
(config)# do-exec debug frr-manager errors <cr>
```

Handler ` RVA 0x196002B0 `；selector ` 2 `；EOL ` RVA 0x36A37EE8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-13ce7d60ae09af1d](../../evidence/conditional_registrations-sets-001.md#r-13ce7d60ae09af1d) · [条件 C-86ea3767013d9556](../../evidence/conditions-sets-052.md#c-86ea3767013d9556) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-000810

```text
(config)# do-exec debug frr-manager events <cr>
```

Handler ` RVA 0x196002B0 `；selector ` 0 `；EOL ` RVA 0x36A37C40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-13ce7d60ae09af1d](../../evidence/conditional_registrations-sets-001.md#r-13ce7d60ae09af1d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d989cbbce10de27e](../../evidence/state_effects-sets-046.md#s-d989cbbce10de27e)

### conditional_registration_candidates-001021

```text
(config)# do-exec debug funi api <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 6 `；EOL ` RVA 0x369BECA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-001042

```text
(config)# do-exec debug funi counters <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 12 `；EOL ` RVA 0x369BEF50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-000849

```text
(config)# do-exec debug funi errors <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 7 `；EOL ` RVA 0x369BD9E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-001007

```text
(config)# do-exec debug funi events <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 3 `；EOL ` RVA 0x369BEA00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-000927

```text
(config)# do-exec debug funi gdb-enable <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 39 `；EOL ` RVA 0x369BE208 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-000984

```text
(config)# do-exec debug funi lfi <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 17 `；EOL ` RVA 0x369BE758 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-002176

```text
(config)# do-exec debug funi memory-alloc show <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 38 `；EOL ` RVA 0x369BDCF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c97b993a2271b896](../../evidence/state_effects-sets-043.md#s-c97b993a2271b896)

### conditional_registration_candidates-000958

```text
(config)# do-exec debug funi multiuser <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 4 `；EOL ` RVA 0x369BE4B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-001219

```text
(config)# do-exec debug funi oam <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 8 `；EOL ` RVA 0x369BF600 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-002832

```text
(config)# do-exec debug funi oam cc <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 14 `；EOL ` RVA 0x369BF928 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-009388

```text
(config)# do-exec debug funi oam cc interface <interface> <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 14 `；EOL ` RVA 0x369BF928 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-d777f8b19702c5ef](../../evidence/conditions-sets-083.md#c-d777f8b19702c5ef) · [缺口 G-49f1a24a44c4241d](../../evidence/gaps-sets-003.md#g-49f1a24a44c4241d) · [参数 P-b68f2075437cc89d](../../evidence/parameters-sets-014.md#p-b68f2075437cc89d) · [状态效果 S-0efda481d4a8694f](../../evidence/state_effects-sets-004.md#s-0efda481d4a8694f)

### conditional_registration_candidates-009266

```text
(config)# do-exec debug funi oam interface <interface> <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 8 `；EOL ` RVA 0x369BF600 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-6b44d60617b093b1](../../evidence/conditions-sets-041.md#c-6b44d60617b093b1) · [缺口 G-5874c1dede80b2d6](../../evidence/gaps-sets-004.md#g-5874c1dede80b2d6) · [参数 P-d0db8cfa376c316b](../../evidence/parameters-sets-016.md#p-d0db8cfa376c316b) · [状态效果 S-f84df7af69acadc9](../../evidence/state_effects-sets-053.md#s-f84df7af69acadc9)

### conditional_registration_candidates-000904

```text
(config)# do-exec debug funi packet <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 2 `；EOL ` RVA 0x369BD610 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-009233

```text
(config)# do-exec debug funi packet interface <interface> <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 2 `；EOL ` RVA 0x369BD610 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-ce8ab0637d95a8fe](../../evidence/conditions-sets-080.md#c-ce8ab0637d95a8fe) · [缺口 G-1151ff88feb6e3ba](../../evidence/gaps-sets-001.md#g-1151ff88feb6e3ba) · [参数 P-e4db58faff148aee](../../evidence/parameters-sets-017.md#p-e4db58faff148aee) · [状态效果 S-4cef592bb3a118be](../../evidence/state_effects-sets-017.md#s-4cef592bb3a118be)

### conditional_registration_candidates-001094

```text
(config)# do-exec debug funi state <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 5 `；EOL ` RVA 0x369BF1F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-001173

```text
(config)# do-exec debug funi xdr <cr>
```

Handler ` RVA 0xEC4A9B0 `；selector ` 13 `；EOL ` RVA 0x369BFCB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-00d0f93b92658b57](../../evidence/conditional_registrations-sets-001.md#r-00d0f93b92658b57) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-881496f3b191f961](../../evidence/state_effects-sets-029.md#s-881496f3b191f961)

### conditional_registration_candidates-002535

```text
(config)# do-exec debug group-policy traffic-steering all <cr>
```

Handler ` RVA 0x13063580 `；selector ` 8 `；EOL ` RVA 0x35A3E048 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d84d14fc0d1066ba](../../evidence/state_effects-sets-046.md#s-d84d14fc0d1066ba)

### conditional_registration_candidates-002494

```text
(config)# do-exec debug group-policy traffic-steering odm <cr>
```

Handler ` RVA 0x13063580 `；selector ` 8 `；EOL ` RVA 0x35A3C7C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a6f390f340b771e6](../../evidence/state_effects-sets-035.md#s-a6f390f340b771e6)

### conditional_registration_candidates-004760

```text
(config)# do-exec debug group-policy traffic-steering provisioning critical <cr>
```

Handler ` RVA 0x13063580 `；selector ` 2 `；EOL ` RVA 0x35A3D7B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004472

```text
(config)# do-exec debug group-policy traffic-steering provisioning debug <cr>
```

Handler ` RVA 0x13063580 `；selector ` 7 `；EOL ` RVA 0x35A3CA68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004806

```text
(config)# do-exec debug group-policy traffic-steering provisioning emergency <cr>
```

Handler ` RVA 0x13063580 `；selector ` 0 `；EOL ` RVA 0x35A3DA58 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004712

```text
(config)# do-exec debug group-policy traffic-steering provisioning error <cr>
```

Handler ` RVA 0x13063580 `；selector ` 3 `；EOL ` RVA 0x35A3D508 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004535

```text
(config)# do-exec debug group-policy traffic-steering provisioning info <cr>
```

Handler ` RVA 0x13063580 `；selector ` 6 `；EOL ` RVA 0x35A3CD10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004596

```text
(config)# do-exec debug group-policy traffic-steering provisioning notice <cr>
```

Handler ` RVA 0x13063580 `；selector ` 5 `；EOL ` RVA 0x35A3CFB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-004655

```text
(config)# do-exec debug group-policy traffic-steering provisioning warning <cr>
```

Handler ` RVA 0x13063580 `；selector ` 4 `；EOL ` RVA 0x35A3D260 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-a94714f01202f87e](../../evidence/conditional_registrations-sets-002.md#r-a94714f01202f87e) · [条件 C-6cc4295bb6f539ca](../../evidence/conditions-sets-042.md#c-6cc4295bb6f539ca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a3b8a1852f6a2ad](../../evidence/state_effects-sets-029.md#s-8a3b8a1852f6a2ad)

### conditional_registration_candidates-002878

```text
(config)# do-exec debug gtp all detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 57 `；EOL ` RVA 0x36CF59F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002701

```text
(config)# do-exec debug gtp all error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 55 `；EOL ` RVA 0x36CF54A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002787

```text
(config)# do-exec debug gtp all event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 56 `；EOL ` RVA 0x36CF5748 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-003062

```text
(config)# do-exec debug gtp all function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 59 `；EOL ` RVA 0x36CF5F40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002972

```text
(config)# do-exec debug gtp all message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 58 `；EOL ` RVA 0x36CF5C98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001309

```text
(config)# do-exec debug gtp audit <cr>
```

Handler ` RVA 0xE002120 `；selector ` 68 `；EOL ` RVA 0x36CF3F30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002740

```text
(config)# do-exec debug gtp audit detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 42 `；EOL ` RVA 0x36CF39B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002583

```text
(config)# do-exec debug gtp audit error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 40 `；EOL ` RVA 0x36CF3468 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002659

```text
(config)# do-exec debug gtp audit event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 41 `；EOL ` RVA 0x36CF3710 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002902

```text
(config)# do-exec debug gtp audit function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 44 `；EOL ` RVA 0x36CF3F08 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002821

```text
(config)# do-exec debug gtp audit message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 43 `；EOL ` RVA 0x36CF3C60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001102

```text
(config)# do-exec debug gtp dns <cr>
```

Handler ` RVA 0xE002120 `；selector ` 63 `；EOL ` RVA 0x36CEEE40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002425

```text
(config)# do-exec debug gtp dns detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x36CEE8C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002312

```text
(config)# do-exec debug gtp dns error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x36CEE378 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002374

```text
(config)# do-exec debug gtp dns event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 16 `；EOL ` RVA 0x36CEE620 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002523

```text
(config)# do-exec debug gtp dns function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x36CEEE18 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002474

```text
(config)# do-exec debug gtp dns message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x36CEEB70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-000971

```text
(config)# do-exec debug gtp ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 70 `；EOL ` RVA 0x36CEAD90 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002194

```text
(config)# do-exec debug gtp ha detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 52 `；EOL ` RVA 0x36CEAAC0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002048

```text
(config)# do-exec debug gtp ha error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 50 `；EOL ` RVA 0x36CEA570 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002122

```text
(config)# do-exec debug gtp ha event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 51 `；EOL ` RVA 0x36CEA818 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002269

```text
(config)# do-exec debug gtp ha function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 54 `；EOL ` RVA 0x36CEAD68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001188

```text
(config)# do-exec debug gtp internal <cr>
```

Handler ` RVA 0xE002120 `；selector ` 65 `；EOL ` RVA 0x36CF0EA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002520

```text
(config)# do-exec debug gtp internal detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x36CF0928 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002417

```text
(config)# do-exec debug gtp internal error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x36CF03D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002470

```text
(config)# do-exec debug gtp internal event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x36CF0680 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002670

```text
(config)# do-exec debug gtp internal function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 29 `；EOL ` RVA 0x36CF0E78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002594

```text
(config)# do-exec debug gtp internal message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x36CF0BD0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001014

```text
(config)# do-exec debug gtp io <cr>
```

Handler ` RVA 0xE002120 `；selector ` 60 `；EOL ` RVA 0x36CEBDB0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002260

```text
(config)# do-exec debug gtp io detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x36CEB838 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002114

```text
(config)# do-exec debug gtp io error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36CEB2E8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002185

```text
(config)# do-exec debug gtp io event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36CEB590 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002381

```text
(config)# do-exec debug gtp io function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36CEBD88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002327

```text
(config)# do-exec debug gtp io message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36CEBAE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001144

```text
(config)# do-exec debug gtp mcsa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 64 `；EOL ` RVA 0x36CEFE70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002471

```text
(config)# do-exec debug gtp mcsa detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x36CEF8F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002367

```text
(config)# do-exec debug gtp mcsa error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 20 `；EOL ` RVA 0x36CEF3A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002422

```text
(config)# do-exec debug gtp mcsa event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x36CEF650 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002595

```text
(config)# do-exec debug gtp mcsa function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x36CEFE48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002521

```text
(config)# do-exec debug gtp mcsa message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 23 `；EOL ` RVA 0x36CEFBA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001032

```text
(config)# do-exec debug gtp path <cr>
```

Handler ` RVA 0xE002120 `；selector ` 61 `；EOL ` RVA 0x36CECDE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002324

```text
(config)# do-exec debug gtp path detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x36CEC868 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002177

```text
(config)# do-exec debug gtp path error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x36CEC318 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002255

```text
(config)# do-exec debug gtp path event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x36CEC5C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002430

```text
(config)# do-exec debug gtp path function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x36CECDB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002379

```text
(config)# do-exec debug gtp path message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x36CECB10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001054

```text
(config)# do-exec debug gtp pdp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 62 `；EOL ` RVA 0x36CEDE10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002376

```text
(config)# do-exec debug gtp pdp detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x36CED898 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002247

```text
(config)# do-exec debug gtp pdp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x36CED348 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002315

```text
(config)# do-exec debug gtp pdp event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x36CED5F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002475

```text
(config)# do-exec debug gtp pdp function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x36CEDDE8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002427

```text
(config)# do-exec debug gtp pdp message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x36CEDB40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001364

```text
(config)# do-exec debug gtp protocol <cr>
```

Handler ` RVA 0xE002120 `；selector ` 69 `；EOL ` RVA 0x36CF4F60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002797

```text
(config)# do-exec debug gtp protocol detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 47 `；EOL ` RVA 0x36CF49E8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002629

```text
(config)# do-exec debug gtp protocol error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 45 `；EOL ` RVA 0x36CF4498 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002712

```text
(config)# do-exec debug gtp protocol event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 46 `；EOL ` RVA 0x36CF4740 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002977

```text
(config)# do-exec debug gtp protocol function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 49 `；EOL ` RVA 0x36CF4F38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002887

```text
(config)# do-exec debug gtp protocol message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 48 `；EOL ` RVA 0x36CF4C90 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001255

```text
(config)# do-exec debug gtp timer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 67 `；EOL ` RVA 0x36CF2F00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002665

```text
(config)# do-exec debug gtp timer detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 37 `；EOL ` RVA 0x36CF2988 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002512

```text
(config)# do-exec debug gtp timer error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 35 `；EOL ` RVA 0x36CF2438 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002587

```text
(config)# do-exec debug gtp timer event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 36 `；EOL ` RVA 0x36CF26E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002825

```text
(config)# do-exec debug gtp timer function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 39 `；EOL ` RVA 0x36CF2ED8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002745

```text
(config)# do-exec debug gtp timer message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 38 `；EOL ` RVA 0x36CF2C30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-001222

```text
(config)# do-exec debug gtp tunnel <cr>
```

Handler ` RVA 0xE002120 `；selector ` 66 `；EOL ` RVA 0x36CF1ED0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002592

```text
(config)# do-exec debug gtp tunnel detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 32 `；EOL ` RVA 0x36CF1958 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002468

```text
(config)# do-exec debug gtp tunnel error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 30 `；EOL ` RVA 0x36CF1408 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002516

```text
(config)# do-exec debug gtp tunnel event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 31 `；EOL ` RVA 0x36CF16B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002748

```text
(config)# do-exec debug gtp tunnel function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 34 `；EOL ` RVA 0x36CF1EA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002669

```text
(config)# do-exec debug gtp tunnel message <cr>
```

Handler ` RVA 0xE002120 `；selector ` 33 `；EOL ` RVA 0x36CF1C00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-2a1ef3aba6b8be4d](../../evidence/conditional_registrations-sets-001.md#r-2a1ef3aba6b8be4d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2ea0ca631f73efe](../../evidence/state_effects-sets-041.md#s-c2ea0ca631f73efe)

### conditional_registration_candidates-002482

```text
(config)# do-exec debug http client all <cr>
```

Handler ` RVA 0x169B50B0 `；selector ` 1 `；EOL ` RVA 0x3606AB00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c9e87c8b3476b808](../../evidence/state_effects-sets-043.md#s-c9e87c8b3476b808)

### conditional_registration_candidates-002334

```text
(config)# do-exec debug http client api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3606A2D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ccba1a393782cb85](../../evidence/state_effects-sets-043.md#s-ccba1a393782cb85)

### conditional_registration_candidates-002439

```text
(config)# do-exec debug http client background <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x3606A848 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7125915a12b09937](../../evidence/state_effects-sets-024.md#s-7125915a12b09937)

### conditional_registration_candidates-002202

```text
(config)# do-exec debug http client cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36069D68 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-97e25c39bd2c8791](../../evidence/state_effects-sets-032.md#s-97e25c39bd2c8791)

### conditional_registration_candidates-002057

```text
(config)# do-exec debug http client cookie <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x360697F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3dc1504312515be0](../../evidence/state_effects-sets-014.md#s-3dc1504312515be0)

### conditional_registration_candidates-002389

```text
(config)# do-exec debug http client error <cr>
```

Handler ` RVA 0x169B5280 `；selector ` 5 `；EOL ` RVA 0x3606A590 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7d8c11f58d57d805](../../evidence/state_effects-sets-027.md#s-7d8c11f58d57d805)

### conditional_registration_candidates-001981

```text
(config)# do-exec debug http client main <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36069540 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f66adb1d413c60e6](../../evidence/state_effects-sets-052.md#s-f66adb1d413c60e6)

### conditional_registration_candidates-002274

```text
(config)# do-exec debug http client msg <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3606A020 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ba765d696e02d79](../../evidence/state_effects-sets-013.md#s-3ba765d696e02d79)

### conditional_registration_candidates-002127

```text
(config)# do-exec debug http client socket <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36069AB0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-c91ed7d76e01b682](../../evidence/conditional_registrations-sets-002.md#r-c91ed7d76e01b682) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bd04013ce8599ddf](../../evidence/state_effects-sets-040.md#s-bd04013ce8599ddf)

### conditional_registration_candidates-002698

```text
(config)# do-exec debug ip flow cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34CCCEA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ffea0b91f053c9b1](../../evidence/conditional_registrations-sets-003.md#r-ffea0b91f053c9b1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb67572cfd9d3a3a](../../evidence/state_effects-sets-040.md#s-bb67572cfd9d3a3a)

### conditional_registration_candidates-002784

```text
(config)# do-exec debug ip flow export <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34CCD160 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ffea0b91f053c9b1](../../evidence/conditional_registrations-sets-003.md#r-ffea0b91f053c9b1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a4a3989d2a1cbae0](../../evidence/state_effects-sets-035.md#s-a4a3989d2a1cbae0)

### conditional_registration_candidates-002875

```text
(config)# do-exec debug ip flow ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34CCD418 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ffea0b91f053c9b1](../../evidence/conditional_registrations-sets-003.md#r-ffea0b91f053c9b1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-445ec3bf530467cb](../../evidence/state_effects-sets-015.md#s-445ec3bf530467cb)

### conditional_registration_candidates-002969

```text
(config)# do-exec debug ip flow mp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34CCD6D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ffea0b91f053c9b1](../../evidence/conditional_registrations-sets-003.md#r-ffea0b91f053c9b1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c17f64c1f4c96a35](../../evidence/state_effects-sets-041.md#s-c17f64c1f4c96a35)

### conditional_registration_candidates-003060

```text
(config)# do-exec debug ip flow non-forwarded <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34CCD988 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ffea0b91f053c9b1](../../evidence/conditional_registrations-sets-003.md#r-ffea0b91f053c9b1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4623821782e6b500](../../evidence/state_effects-sets-015.md#s-4623821782e6b500)

### conditional_registration_candidates-003244

```text
(config)# do-exec debug ip inspect acl-bypass <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 0 `；EOL ` RVA 0x360706F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-004162

```text
(config)# do-exec debug ip inspect aol-msgr <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 25 `；EOL ` RVA 0x36074958 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003832

```text
(config)# do-exec debug ip inspect cuseeme <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 21 `；EOL ` RVA 0x36071C30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003150

```text
(config)# do-exec debug ip inspect detailed <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 6 `；EOL ` RVA 0x36070448 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003943

```text
(config)# do-exec debug ip inspect dns <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 34 `；EOL ` RVA 0x36072428 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-002699

```text
(config)# do-exec debug ip inspect events <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 1 `；EOL ` RVA 0x3606F700 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003338

```text
(config)# do-exec debug ip inspect ftp-cmd <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 9 `；EOL ` RVA 0x36070998 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003428

```text
(config)# do-exec debug ip inspect ftp-token <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 10 `；EOL ` RVA 0x36070C40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-002785

```text
(config)# do-exec debug ip inspect function-trace <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 2 `；EOL ` RVA 0x3606F9A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-003913

```text
(config)# do-exec debug ip inspect h323 <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 14 `；EOL ` RVA 0x36072180 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-004049

```text
(config)# do-exec debug ip inspect http <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 22 `；EOL ` RVA 0x36072EC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)

### conditional_registration_candidates-004172

```text
(config)# do-exec debug ip inspect icmp <cr>
```

Handler ` RVA 0x16A406F0 `；selector ` 33 `；EOL ` RVA 0x36074EA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-d83eb23f15e32891](../../evidence/conditional_registrations-sets-002.md#r-d83eb23f15e32891) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-59cc36ee30303f60](../../evidence/state_effects-sets-019.md#s-59cc36ee30303f60)
