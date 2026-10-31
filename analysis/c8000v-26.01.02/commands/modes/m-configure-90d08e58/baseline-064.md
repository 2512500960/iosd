# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-036402

```text
(config)# do-exec test sw-vlan show data <cr>
```

Handler ` RVA 0x15C8E860 `；selector ` 0 `；EOL ` RVA 0x35DFE5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19d6abbf3e222af0](../../evidence/conditions-sets-010.md#c-19d6abbf3e222af0) · [状态效果 S-4dfd02e3b26d326e](../../evidence/state_effects-sets-017.md#s-4dfd02e3b26d326e)

### path-038118

```text
(config)# do-exec test system secure db <cr>
```

Handler ` RVA 0xE031AB0 `；selector ` 0 `；EOL ` RVA 0x3416FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-63655c1a2ea907be](../../evidence/state_effects-sets-021.md#s-63655c1a2ea907be)

### path-027273

```text
(config)# do-exec test tcp delay <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 2 `；EOL ` RVA 0x33CF79B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-72d8ec7d57fcae0c](../../evidence/conditions-sets-044.md#c-72d8ec7d57fcae0c) · [参数 P-dbbc7c51a2581030](../../evidence/parameters-sets-017.md#p-dbbc7c51a2581030) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027256

```text
(config)# do-exec test tcp drop <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 1 `；EOL ` RVA 0x33CF7978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-2949db2c7841cd4d](../../evidence/conditions-sets-016.md#c-2949db2c7841cd4d) · [参数 P-9905a3044e6cc7c3](../../evidence/parameters-sets-012.md#p-9905a3044e6cc7c3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027286

```text
(config)# do-exec test tcp line <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 0 `；EOL ` RVA 0x33CF7C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-ea17e3fb8c7dd85a](../../evidence/conditions-sets-090.md#c-ea17e3fb8c7dd85a) · [参数 P-168d315b78b62806](../../evidence/parameters-sets-002.md#p-168d315b78b62806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027303

```text
(config)# do-exec test tcp random <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 3 `；EOL ` RVA 0x33CF7EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-dc7084e073e7fd80](../../evidence/conditions-sets-085.md#c-dc7084e073e7fd80) · [参数 P-d316af619bb90043](../../evidence/parameters-sets-016.md#p-d316af619bb90043) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058004

```text
(config)# do-exec test template scope global <string> bind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 0 `；EOL ` RVA 0x33ED94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058010

```text
(config)# do-exec test template scope global <string> unbind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 1 `；EOL ` RVA 0x33ED9780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062621

```text
(config)# do-exec test template scope interface <string> bind dynamic interface <interface> <cr>
```

Handler ` RVA 0xD6D9FC0 `；selector ` 0 `；EOL ` RVA 0x33ED8370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-17d8572c7ad97c55](../../evidence/conditions-sets-009.md#c-17d8572c7ad97c55) · [缺口 G-43f87bfb76bc1d11](../../evidence/gaps-sets-003.md#g-43f87bfb76bc1d11) · [参数 P-ddaa6dab3e069515](../../evidence/parameters-sets-017.md#p-ddaa6dab3e069515) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059855

```text
(config)# do-exec test template scope interface <string> bind static merge interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 2 `；EOL ` RVA 0x33ED86E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059858

```text
(config)# do-exec test template scope interface <string> bind static replace interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 3 `；EOL ` RVA 0x33ED89B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062622

```text
(config)# do-exec test template scope interface <string> unbind dynamic interface <interface> <cr>
```

Handler ` RVA 0xD6D9FC0 `；selector ` 1 `；EOL ` RVA 0x33ED8DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-58392159ab0e3a36](../../evidence/conditions-sets-035.md#c-58392159ab0e3a36) · [缺口 G-4c77652b9cce4e73](../../evidence/gaps-sets-003.md#g-4c77652b9cce4e73) · [参数 P-192ef1b35ceca6e4](../../evidence/parameters-sets-002.md#p-192ef1b35ceca6e4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059371

```text
(config)# do-exec test template scope interface <string> unbind static interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 4 `；EOL ` RVA 0x33ED90F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062534

```text
(config)# do-exec test template scope interface apply common-config interface <interface> <cr>
```

Handler ` RVA 0xD6DAEC0 `；selector ` 1 `；EOL ` RVA 0x33ED7B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b18b5b863a34bc1](../../evidence/conditions-sets-011.md#c-1b18b5b863a34bc1) · [缺口 G-bbb78dbe26e32634](../../evidence/gaps-sets-007.md#g-bbb78dbe26e32634) · [参数 P-09e959048d046c6b](../../evidence/parameters-sets-001.md#p-09e959048d046c6b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054432

```text
(config)# do-exec test template scope interface nvgen interface-global <cr>
```

Handler ` RVA 0xD6DAF30 `；selector ` 0 `；EOL ` RVA 0x33ED7EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030883

```text
(config)# do-exec test tenant-mgr disable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35849178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec2270a6067721e6](../../evidence/conditions-sets-091.md#c-ec2270a6067721e6) · [状态效果 S-c8449321e3014536](../../evidence/state_effects-sets-042.md#s-c8449321e3014536)

### path-030859

```text
(config)# do-exec test tenant-mgr enable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35848EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec2270a6067721e6](../../evidence/conditions-sets-091.md#c-ec2270a6067721e6) · [状态效果 S-1e4f54b43ac170b7](../../evidence/state_effects-sets-007.md#s-1e4f54b43ac170b7)

### path-035501

```text
(config)# do-exec test timer-wheel process create <cr>
```

Handler ` RVA 0xD7AC900 `；selector ` 0 `；EOL ` RVA 0x33EEEF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1597b37888df441b](../../evidence/conditions-sets-009.md#c-1597b37888df441b) · [状态效果 S-dbadb1c192756282](../../evidence/state_effects-sets-046.md#s-dbadb1c192756282)

### path-061290

```text
(config)# do-exec test timer-wheel stop <number:1..9999> <?general_pointer_number_action@5555894433f8> <cr>
```

Handler ` RVA 0xD7AC900 `；selector ` 0 `；EOL ` RVA 0x33EEEF30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PID。

[条件 C-959d20fa63003b58](../../evidence/conditions-sets-058.md#c-959d20fa63003b58) · [缺口 G-95f244cd86b6fb75](../../evidence/gaps-sets-005.md#g-95f244cd86b6fb75) · [参数 P-4260d50421298b7b](../../evidence/parameters-sets-006.md#p-4260d50421298b7b) · [状态效果 S-8797d65fb2cf3ab2](../../evidence/state_effects-sets-029.md#s-8797d65fb2cf3ab2)

### path-029615

```text
(config)# do-exec test topology clients <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 11 `；EOL ` RVA 0x33FE4560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036199

```text
(config)# do-exec test topology create ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 1 `；EOL ` RVA 0x33FE5EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94b8dca91a9ab089](../../evidence/conditions-sets-058.md#c-94b8dca91a9ab089) · [状态效果 S-653644e2f6ca084c](../../evidence/state_effects-sets-022.md#s-653644e2f6ca084c)

### path-036129

```text
(config)# do-exec test topology delete ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 7 `；EOL ` RVA 0x33FE5A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94b8dca91a9ab089](../../evidence/conditions-sets-058.md#c-94b8dca91a9ab089) · [状态效果 S-bdb887f03f7b0218](../../evidence/state_effects-sets-040.md#s-bdb887f03f7b0218)

### path-061900

```text
(config)# do-exec test topology lookup idb <interface> ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 2 `；EOL ` RVA 0x33FE53D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a403964d4305362f](../../evidence/conditions-sets-063.md#c-a403964d4305362f) · [缺口 G-63614d8e2e0732ac](../../evidence/gaps-sets-004.md#g-63614d8e2e0732ac) · [参数 P-4e67ecd43565aeab](../../evidence/parameters-sets-006.md#p-4e67ecd43565aeab) · [状态效果 S-a6a9b93672bb2856](../../evidence/state_effects-sets-035.md#s-a6a9b93672bb2856)

### path-036051

```text
(config)# do-exec test topology lookup ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 2 `；EOL ` RVA 0x33FE53D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-3a7a91298b38de09](../../evidence/state_effects-sets-013.md#s-3a7a91298b38de09)

### path-029757

```text
(config)# do-exec test topology walk <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 14 `；EOL ` RVA 0x33FE4B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcb690536ca205a0](../../evidence/conditions-sets-098.md#c-fcb690536ca205a0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061336

```text
(config)# do-exec test topology walk idb <interface> <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 14 `；EOL ` RVA 0x33FE4B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f74fb73d448a565](../../evidence/conditions-sets-031.md#c-4f74fb73d448a565) · [缺口 G-f5eeebac63c91685](../../evidence/gaps-sets-008.md#g-f5eeebac63c91685) · [参数 P-b112d1001116c0fd](../../evidence/parameters-sets-013.md#p-b112d1001116c0fd) · [状态效果 S-3518b22facbbaabf](../../evidence/state_effects-sets-012.md#s-3518b22facbbaabf)

### path-053066

```text
(config)# do-exec test track map name <string> create <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 1 `；EOL ` RVA 0x34216BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053157

```text
(config)# do-exec test track map name <string> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 5 `；EOL ` RVA 0x34217100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053109

```text
(config)# do-exec test track map name <string> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 2 `；EOL ` RVA 0x34216E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053148

```text
(config)# do-exec test track map num <number:1..32767> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 4 `；EOL ` RVA 0x342176D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053097

```text
(config)# do-exec test track map num <number:1..32767> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 3 `；EOL ` RVA 0x34217430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045386

```text
(config)# do-exec test track service <string> up <cr>
```

Handler ` RVA 0xE14F670 `；selector ` 0 `；EOL ` RVA 0x34216180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked service name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-8b58f3bab75800c0](../../evidence/parameters-sets-011.md#p-8b58f3bab75800c0) · [状态效果 S-0cccb59963e191f8](../../evidence/state_effects-sets-003.md#s-0cccb59963e191f8)

### path-029524

```text
(config)# do-exec test track white-box <cr>
```

Handler ` RVA 0xE14F7A0 `；selector ` 0 `；EOL ` RVA 0x34215DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4fd28978f6871800](../../evidence/conditions-sets-031.md#c-4fd28978f6871800) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062358

```text
(config)# do-exec test trunkgroup <?show_tg_cmd@55558ce57570> preemption-pending flash-override data <number:1..2147483647> <cr>
```

Handler ` RVA 0x1E3C1110 `；selector ` 1 `；EOL ` RVA 0x37903B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Call Reference Id。

[条件 C-bb0e267c34bab18f](../../evidence/conditions-sets-072.md#c-bb0e267c34bab18f) · [缺口 G-3c24b5e558ad4dc0](../../evidence/gaps-sets-003.md#g-3c24b5e558ad4dc0) · [参数 P-accf59baec26636a](../../evidence/parameters-sets-013.md#p-accf59baec26636a) · [状态效果 S-0f7adc8bf22e301a](../../evidence/state_effects-sets-004.md#s-0f7adc8bf22e301a)

### path-061492

```text
(config)# do-exec test trunkgroup <?show_tg_cmd@55558ce57570> set_tgCic <number:1..65535> <cr>
```

Handler ` RVA 0x1E3CF1F0 `；selector ` 0 `；EOL ` RVA 0x379036C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TRUNKGROUP CIC Number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [缺口 G-3c24b5e558ad4dc0](../../evidence/gaps-sets-003.md#g-3c24b5e558ad4dc0) · [参数 P-5cd29f6ad2bad388](../../evidence/parameters-sets-007.md#p-5cd29f6ad2bad388) · [状态效果 S-039a35bce4d28841](../../evidence/state_effects-sets-001.md#s-039a35bce4d28841)

### path-061953

```text
(config)# do-exec test tunnel <interface> config destination dynamic <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 9 `；EOL ` RVA 0x34831460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d39768fe2c143b86](../../evidence/conditions-sets-082.md#c-d39768fe2c143b86) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-21f0dbf54a53faf7](../../evidence/state_effects-sets-008.md#s-21f0dbf54a53faf7)

### path-061957

```text
(config)# do-exec test tunnel <interface> config dst-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 30 `；EOL ` RVA 0x34831828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` tunnel destination port number。

[条件 C-c4daf2de092c24d9](../../evidence/conditions-sets-076.md#c-c4daf2de092c24d9) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-6304a1ea7ef5cef4](../../evidence/parameters-sets-008.md#p-6304a1ea7ef5cef4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061948

```text
(config)# do-exec test tunnel <interface> config source dynamic <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 10 `；EOL ` RVA 0x34830F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a74fc86c0eead44e](../../evidence/conditions-sets-065.md#c-a74fc86c0eead44e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-7293902ea6d80881](../../evidence/state_effects-sets-024.md#s-7293902ea6d80881)

### path-061964

```text
(config)# do-exec test tunnel <interface> config src-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 31 `；EOL ` RVA 0x34831B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel Source port number。

[条件 C-12b73f0333e37816](../../evidence/conditions-sets-007.md#c-12b73f0333e37816) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-1d60903cb544d4d7](../../evidence/parameters-sets-003.md#p-1d60903cb544d4d7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060890

```text
(config)# do-exec test tunnel <interface> decap <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 23 `；EOL ` RVA 0x34833C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061971

```text
(config)# do-exec test tunnel <interface> endpoints add <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 2 `；EOL ` RVA 0x34832038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` overlay ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-f0432e4861384a95](../../evidence/parameters-sets-018.md#p-f0432e4861384a95) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061970

```text
(config)# do-exec test tunnel <interface> endpoints auto-adj-mtu enable <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 6 `；EOL ` RVA 0x348338D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c04a62a5dc9e190](../../evidence/conditions-sets-017.md#c-2c04a62a5dc9e190) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-849d8ba37bb3daef](../../evidence/state_effects-sets-028.md#s-849d8ba37bb3daef)

### path-061952

```text
(config)# do-exec test tunnel <interface> endpoints delete <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 1 `；EOL ` RVA 0x34832738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` overlay ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-f3b06952e2b4f70c](../../evidence/parameters-sets-018.md#p-f3b06952e2b4f70c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062314

```text
(config)# do-exec test tunnel <interface> endpoints find transport <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 0 `；EOL ` RVA 0x34832AD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-078211b1f83acf51](../../evidence/parameters-sets-001.md#p-078211b1f83acf51) · [状态效果 S-2c2b2691e2efbaf7](../../evidence/state_effects-sets-010.md#s-2c2b2691e2efbaf7)

### path-062512

```text
(config)# do-exec test tunnel <interface> endpoints ref transport <address> <number:0..1000000> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 3 `；EOL ` RVA 0x34832F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address；` unsigned_number ` refcount。

[条件 C-d3e077c46cf85569](../../evidence/conditions-sets-082.md#c-d3e077c46cf85569) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-fd86cf69070b5df9](../../evidence/parameters-sets-019.md#p-fd86cf69070b5df9) · [状态效果 S-cb9a7f28f788e17b](../../evidence/state_effects-sets-043.md#s-cb9a7f28f788e17b)

### path-062612

```text
(config)# do-exec test tunnel <interface> endpoints service-policy output <string> <address> add <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 4 `；EOL ` RVA 0x34833348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` QoS policy-map name；` address ` transport ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-7ca721b4af31f699](../../evidence/parameters-sets-010.md#p-7ca721b4af31f699) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062614

```text
(config)# do-exec test tunnel <interface> endpoints service-policy output <string> <address> delete <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 5 `；EOL ` RVA 0x348335F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` QoS policy-map name；` address ` transport ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-7ca721b4af31f699](../../evidence/parameters-sets-010.md#p-7ca721b4af31f699) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062613

```text
(config)# do-exec test tunnel <interface> key add p2mp <number:0..4294967295> <number:0..4294967295> <address> <cr>
```

Handler ` RVA 0xFBC5ED0 `；selector ` 0 `；EOL ` RVA 0x34834150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` receive key；` unsigned_number ` transmit key；` address ` Overlay ipv4 address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-bbb06155c8fdfa8b](../../evidence/parameters-sets-014.md#p-bbb06155c8fdfa8b) · [状态效果 S-1fa1431ea06e349c](../../evidence/state_effects-sets-007.md#s-1fa1431ea06e349c)

### path-062511

```text
(config)# do-exec test tunnel <interface> subblock add endpoint transport <address> <cr>
```

Handler ` RVA 0xFB7BB40 `；selector ` 0 `；EOL ` RVA 0x34826C40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-48d3fa64684472b9](../../evidence/parameters-sets-006.md#p-48d3fa64684472b9) · [状态效果 S-89a3fbeb1d7ef4fa](../../evidence/state_effects-sets-029.md#s-89a3fbeb1d7ef4fa)

### path-061947

```text
(config)# do-exec test tunnel <interface> subblock add interface <cr>
```

Handler ` RVA 0xFB7BB40 `；selector ` 1 `；EOL ` RVA 0x348268E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-de689e9bf2ef222a](../../evidence/state_effects-sets-047.md#s-de689e9bf2ef222a)

### path-061362

```text
(config)# do-exec test tunnel <interface> tos enable <cr>
```

Handler ` RVA 0xFB8F9A0 `；selector ` 0 `；EOL ` RVA 0x34830B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92cbaf4bde04b1fe](../../evidence/conditions-sets-057.md#c-92cbaf4bde04b1fe) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-21b5354fffa8d2b5](../../evidence/state_effects-sets-008.md#s-21b5354fffa8d2b5)

### path-053977

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> add <cr>
```

Handler ` RVA 0xB516500 `；selector ` 0 `；EOL ` RVA 0x33792A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-1bd963aded0ee02e](../../evidence/conditions-sets-011.md#c-1bd963aded0ee02e) · [参数 P-816d5b8c6fbe0a85](../../evidence/parameters-sets-010.md#p-816d5b8c6fbe0a85) · [状态效果 S-2a0f4cf52a2dc8a6](../../evidence/state_effects-sets-009.md#s-2a0f4cf52a2dc8a6)

### path-059261

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> add ipv4 V1 <cr>
```

Handler ` RVA 0xB513640 `；selector ` 0 `；EOL ` RVA 0x33790108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-3f666681904692d3](../../evidence/state_effects-sets-014.md#s-3f666681904692d3)

### path-054098

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> clear <cr>
```

Handler ` RVA 0xB513640 `；selector ` 6 `；EOL ` RVA 0x337916D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-053904

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 1 `；EOL ` RVA 0x33790440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-057821

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> df-bit set <cr>
```

Handler ` RVA 0xB513640 `；selector ` 5 `；EOL ` RVA 0x33791448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-059274

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB513640 `；selector ` 7 `；EOL ` RVA 0x33790AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-059284

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 8 `；EOL ` RVA 0x33790D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-057748

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 2 `；EOL ` RVA 0x33790750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-de0e272fb87adafa](../../evidence/parameters-sets-017.md#p-de0e272fb87adafa) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-062322

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> source-if <interface> <cr>
```

Handler ` RVA 0xB514190 `；selector ` 0 `；EOL ` RVA 0x33792060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-cca7954a511f3c33](../../evidence/conditions-sets-079.md#c-cca7954a511f3c33) · [缺口 G-638bea1b3cb44416](../../evidence/gaps-sets-004.md#g-638bea1b3cb44416) · [参数 P-1400d1d8336b2244](../../evidence/parameters-sets-002.md#p-1400d1d8336b2244) · [状态效果 S-04c7b47b5aceea57](../../evidence/state_effects-sets-001.md#s-04c7b47b5aceea57)

### path-062324

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> unnumbered <interface> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 3 `；EOL ` RVA 0x33791120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-fa05ae8b0c13056f](../../evidence/conditions-sets-097.md#c-fa05ae8b0c13056f) · [缺口 G-4d973959b4f976be](../../evidence/gaps-sets-003.md#g-4d973959b4f976be) · [参数 P-4d4e6c62c08c8969](../../evidence/parameters-sets-006.md#p-4d4e6c62c08c8969) · [状态效果 S-0889414883cef131](../../evidence/state_effects-sets-002.md#s-0889414883cef131)

### path-053910

```text
(config)# do-exec test tunnel Groups wccp <number:0..9> unsource <cr>
```

Handler ` RVA 0xB514190 `；selector ` 0 `；EOL ` RVA 0x33792060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-c2b7d57abb0f4b71](../../evidence/conditions-sets-075.md#c-c2b7d57abb0f4b71) · [参数 P-ccb3e85e97e2dec4](../../evidence/parameters-sets-016.md#p-ccb3e85e97e2dec4) · [状态效果 S-ac9a351aa7fef2c6](../../evidence/state_effects-sets-036.md#s-ac9a351aa7fef2c6)

### path-036765

```text
(config)# do-exec test tunnel tos enable <cr>
```

Handler ` RVA 0xFB8F9A0 `；selector ` 0 `；EOL ` RVA 0x34830B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [状态效果 S-21b5354fffa8d2b5](../../evidence/state_effects-sets-008.md#s-21b5354fffa8d2b5)

### path-059247

```text
(config)# do-exec test tunnel tun-to <number:0..9> add transport ipv4 none <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 1 `；EOL ` RVA 0x33794348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-258c15a8ca3df44c](../../evidence/conditions-sets-015.md#c-258c15a8ca3df44c) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b06694caff1bf183](../../evidence/state_effects-sets-037.md#s-b06694caff1bf183)

### path-046382

```text
(config)# do-exec test tunnel tun-to <number:0..9> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 2 `；EOL ` RVA 0x33794638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054038

```text
(config)# do-exec test tunnel tun-to <number:0..9> display <number:0..160> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 7 `；EOL ` RVA 0x337968F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` unsigned_number ` Indent。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-c32407e8d350360d](../../evidence/parameters-sets-015.md#p-c32407e8d350360d) · [状态效果 S-b3284cd086af616e](../../evidence/state_effects-sets-038.md#s-b3284cd086af616e)

### path-057724

```text
(config)# do-exec test tunnel tun-to <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 13 `；EOL ` RVA 0x33795110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057756

```text
(config)# do-exec test tunnel tun-to <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 14 `；EOL ` RVA 0x337953B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062617

```text
(config)# do-exec test tunnel tun-to <number:0..9> endpoint <address> redirect <interface> disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 16 `；EOL ` RVA 0x33795A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-d92799083c2af1b1](../../evidence/conditions-sets-084.md#c-d92799083c2af1b1) · [缺口 G-aeb93bfcdfaa0a3e](../../evidence/gaps-sets-006.md#g-aeb93bfcdfaa0a3e) · [参数 P-2f3d36d1a44d7406](../../evidence/parameters-sets-004.md#p-2f3d36d1a44d7406) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062615

```text
(config)# do-exec test tunnel tun-to <number:0..9> endpoint <address> redirect <interface> enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 15 `；EOL ` RVA 0x33795760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-d92799083c2af1b1](../../evidence/conditions-sets-084.md#c-d92799083c2af1b1) · [缺口 G-aeb93bfcdfaa0a3e](../../evidence/gaps-sets-006.md#g-aeb93bfcdfaa0a3e) · [参数 P-2f3d36d1a44d7406](../../evidence/parameters-sets-004.md#p-2f3d36d1a44d7406) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057796

```text
(config)# do-exec test tunnel tun-to <number:0..9> feature enable post-encap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 9 `；EOL ` RVA 0x33796C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-844a1914bcd9dd98](../../evidence/state_effects-sets-028.md#s-844a1914bcd9dd98)

### path-057822

```text
(config)# do-exec test tunnel tun-to <number:0..9> feature enable pre-decap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 10 `；EOL ` RVA 0x33796EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-844a1914bcd9dd98](../../evidence/state_effects-sets-028.md#s-844a1914bcd9dd98)

### path-057744

```text
(config)# do-exec test tunnel tun-to <number:0..9> gre key disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 8 `；EOL ` RVA 0x33796538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-d7e21aa8b1845f67](../../evidence/state_effects-sets-046.md#s-d7e21aa8b1845f67)

### path-057716

```text
(config)# do-exec test tunnel tun-to <number:0..9> payload ipv4 enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 11 `；EOL ` RVA 0x33795DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-3e74c4e5aa3d4c6a](../../evidence/conditions-sets-024.md#c-3e74c4e5aa3d4c6a) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b1ddea302eb93eb3](../../evidence/state_effects-sets-038.md#s-b1ddea302eb93eb3)

### path-059265

```text
(config)# do-exec test tunnel tun-to <number:0..9> payload ipv4 mtu default <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 12 `；EOL ` RVA 0x337960C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-3e74c4e5aa3d4c6a](../../evidence/conditions-sets-024.md#c-3e74c4e5aa3d4c6a) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-3d8f37cfd0a1d664](../../evidence/state_effects-sets-013.md#s-3d8f37cfd0a1d664)

### path-053802

```text
(config)# do-exec test tunnel tun-to <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 3 `；EOL ` RVA 0x33794948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-b5fd48203094e8df](../../evidence/parameters-sets-014.md#p-b5fd48203094e8df) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061977

```text
(config)# do-exec test tunnel tun-to <number:0..9> source <interface> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 4 `；EOL ` RVA 0x33794CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-c83fcc08420a6a4b](../../evidence/conditions-sets-077.md#c-c83fcc08420a6a4b) · [缺口 G-e0c458f4d5299bd1](../../evidence/gaps-sets-008.md#g-e0c458f4d5299bd1) · [参数 P-4356715a4b94a73e](../../evidence/parameters-sets-006.md#p-4356715a4b94a73e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031881

```text
(config)# do-exec test uninstall <string> <cr>
```

Handler ` RVA 0x15A6CC70 `；selector ` 0 `；EOL ` RVA 0x35DE37F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-8e5bac707605508a](../../evidence/conditions-sets-055.md#c-8e5bac707605508a) · [参数 P-7b9316c0493b1273](../../evidence/parameters-sets-010.md#p-7b9316c0493b1273) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061325

```text
(config)# do-exec test vlan-autoconfig <interface> <number:1..4096> <number:1..4096> <cr>
```

Handler ` RVA 0x112B7720 `；selector ` 0 `；EOL ` RVA 0x35450498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Begin VLAN；` unsigned_number ` End VLAN。

[条件 C-de6e0d3e140b9d46](../../evidence/conditions-sets-086.md#c-de6e0d3e140b9d46) · [缺口 G-dd7d4d75d0ddffb2](../../evidence/gaps-sets-008.md#g-dd7d4d75d0ddffb2) · [参数 P-0d9c3b97f8d0dcc0](../../evidence/parameters-sets-001.md#p-0d9c3b97f8d0dcc0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053029

```text
(config)# do-exec test vrrs client add <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 9 `；EOL ` RVA 0x342A0CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-c1faf0a01590e7c1](../../evidence/parameters-sets-015.md#p-c1faf0a01590e7c1) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-045476

```text
(config)# do-exec test vrrs client register <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 11 `；EOL ` RVA 0x342A0678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-dfe2be5a59cb5d99](../../evidence/parameters-sets-017.md#p-dfe2be5a59cb5d99) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-053068

```text
(config)# do-exec test vrrs client remove <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 8 `；EOL ` RVA 0x342A0FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-912dcfafa5af0bac](../../evidence/parameters-sets-011.md#p-912dcfafa5af0bac) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-045389

```text
(config)# do-exec test vrrs client unregister <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 10 `；EOL ` RVA 0x342A0988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-e7f6bd64325acaf4](../../evidence/parameters-sets-017.md#p-e7f6bd64325acaf4) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-062495

```text
(config)# do-exec test vrrs pathway name <string> connect <interface> <address> <cr>
```

Handler ` RVA 0x133F9580 `；selector ` 0 `；EOL ` RVA 0x35A8B960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the VRRS tag associated with pathways；` address ` vMAC address。

[条件 C-559ebd8720b6d51c](../../evidence/conditions-sets-034.md#c-559ebd8720b6d51c) · [缺口 G-3287da47fde6f86b](../../evidence/gaps-sets-002.md#g-3287da47fde6f86b) · [参数 P-dd3512a0572d360b](../../evidence/parameters-sets-017.md#p-dd3512a0572d360b) · [状态效果 S-fe392c8dd825631f](../../evidence/state_effects-sets-054.md#s-fe392c8dd825631f)

### path-053366

```text
(config)# do-exec test vrrs pathway name <string> disconnect <cr>
```

Handler ` RVA 0x133F9580 `；selector ` 0 `；EOL ` RVA 0x35A8B960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the VRRS tag associated with pathways。

[条件 C-966f3f4db04d8f90](../../evidence/conditions-sets-058.md#c-966f3f4db04d8f90) · [参数 P-b55499403f5cacac](../../evidence/parameters-sets-014.md#p-b55499403f5cacac) · [状态效果 S-77c0c0d003214a70](../../evidence/state_effects-sets-025.md#s-77c0c0d003214a70)

### path-034169

```text
(config)# do-exec test vrrs plugin server <cr>
```

Handler ` RVA 0xE2FF4F0 `；selector ` 0 `；EOL ` RVA 0x342A69C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1827a8e6f0d8dd8c](../../evidence/conditions-sets-009.md#c-1827a8e6f0d8dd8c) · [状态效果 S-7fa593bdfdc26ef0](../../evidence/state_effects-sets-027.md#s-7fa593bdfdc26ef0)

### path-057319

```text
(config)# do-exec test vrrs server add <string> vip <address> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 7 `；EOL ` RVA 0x342A15D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string；` address ` VRRP group's virtual address。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-1c35fd9c9703b522](../../evidence/parameters-sets-003.md#p-1c35fd9c9703b522) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-045496

```text
(config)# do-exec test vrrs server delete <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 5 `；EOL ` RVA 0x342A1F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-3c862bfbe3046baa](../../evidence/parameters-sets-005.md#p-3c862bfbe3046baa) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-045708

```text
(config)# do-exec test vrrs server update <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 6 `；EOL ` RVA 0x342A1BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-6c0f2e263c8af654](../../evidence/parameters-sets-009.md#p-6c0f2e263c8af654) · [状态效果 S-f60b5bd6425ef7e3](../../evidence/state_effects-sets-052.md#s-f60b5bd6425ef7e3)

### path-053429

```text
(config)# do-exec test wccp ip web-cache assignment hash <cr>
```

Handler ` RVA 0x10AE0FA0 `；selector ` 0 `；EOL ` RVA 0x34CA15E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00a73cc4271e7434](../../evidence/conditions-sets-001.md#c-00a73cc4271e7434) · [状态效果 S-3efc41f98d4f2d6b](../../evidence/state_effects-sets-014.md#s-3efc41f98d4f2d6b)

### path-046066

```text
(config)# do-exec test wccp ip web-cache capabilities <cr>
```

Handler ` RVA 0x10AE0C00 `；selector ` 0 `；EOL ` RVA 0x34CA11B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eebebb687cfef849](../../evidence/conditions-sets-092.md#c-eebebb687cfef849) · [状态效果 S-3905c77d283539e1](../../evidence/state_effects-sets-013.md#s-3905c77d283539e1)

### path-062494

```text
(config)# do-exec test wccp ip web-cache client <address> <interface> add <cr>
```

Handler ` RVA 0x10AE07A0 `；selector ` 1 `；EOL ` RVA 0x34CA07B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Client IPv4 address。

[条件 C-e61124defdbb458f](../../evidence/conditions-sets-089.md#c-e61124defdbb458f) · [缺口 G-406cfbfa190f2d4b](../../evidence/gaps-sets-003.md#g-406cfbfa190f2d4b) · [参数 P-fa6891eb35ef32da](../../evidence/parameters-sets-019.md#p-fa6891eb35ef32da) · [状态效果 S-3905c77d283539e1](../../evidence/state_effects-sets-013.md#s-3905c77d283539e1)

### path-062498

```text
(config)# do-exec test wccp ip web-cache client <address> <interface> remove <cr>
```

Handler ` RVA 0x10AE07A0 `；selector ` 2 `；EOL ` RVA 0x34CA0A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Client IPv4 address。

[条件 C-65eed33a91b8ec78](../../evidence/conditions-sets-039.md#c-65eed33a91b8ec78) · [缺口 G-406cfbfa190f2d4b](../../evidence/gaps-sets-003.md#g-406cfbfa190f2d4b) · [参数 P-fa6891eb35ef32da](../../evidence/parameters-sets-019.md#p-fa6891eb35ef32da) · [状态效果 S-3905c77d283539e1](../../evidence/state_effects-sets-013.md#s-3905c77d283539e1)

### path-059167

```text
(config)# do-exec test wccp ip web-cache service <number:0..255> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10AE0A90 `；selector ` 0 `；EOL ` RVA 0x34CA1C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` WCCP service priority；` unsigned_number ` WCCP service protocol；` unsigned_number ` WCCP service flags。

[条件 C-84c16de96cd6cea1](../../evidence/conditions-sets-051.md#c-84c16de96cd6cea1) · [参数 P-71b77f6b738f2f59](../../evidence/parameters-sets-009.md#p-71b77f6b738f2f59) · [状态效果 S-3905c77d283539e1](../../evidence/state_effects-sets-013.md#s-3905c77d283539e1)

### path-031675

```text
(config)# do-exec test wsma history <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 1 `；EOL ` RVA 0x3463D0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039550

```text
(config)# do-exec test wsma listener <string> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 2 `；EOL ` RVA 0x3463D6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the transport。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9f474f72af6c782b](../../evidence/parameters-sets-012.md#p-9f474f72af6c782b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039609

```text
(config)# do-exec test wsma max-priv-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 4 `；EOL ` RVA 0x3463D960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce max priv or not。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-d3faea102e025dae](../../evidence/parameters-sets-016.md#p-d3faea102e025dae) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031697

```text
(config)# do-exec test wsma summary <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 3 `；EOL ` RVA 0x3463D390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035849

```text
(config)# do-exec test x25 dbit <number:0..1000> <cr>
```

Handler ` RVA 0x1061D5B0 `；selector ` 0 `；EOL ` RVA 0x34BD4DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` D-bit interval (packets)。

[条件 C-4c469b247959c3aa](../../evidence/conditions-sets-030.md#c-4c469b247959c3aa) · [参数 P-f4144dc0d3cc9c91](../../evidence/parameters-sets-018.md#p-f4144dc0d3cc9c91) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036954

```text
(config)# do-exec test xdr create-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7830 `；selector ` 0 `；EOL ` RVA 0x34CFDE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ID of test stream to create。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-d155c8fe88eef6d1](../../evidence/parameters-sets-016.md#p-d155c8fe88eef6d1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036913

```text
(config)# do-exec test xdr destroy-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7890 `；selector ` 0 `；EOL ` RVA 0x34CFDB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ID of test stream to destroy。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-c2413738ef352aaf](../../evidence/parameters-sets-015.md#p-c2413738ef352aaf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030141

```text
(config)# do-exec test xdr disable <cr>
```

Handler ` RVA 0x10C75EA0 `；selector ` 0 `；EOL ` RVA 0x34CF46D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd1bed760fb9c021](../../evidence/conditions-sets-098.md#c-fd1bed760fb9c021) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030142

```text
(config)# do-exec test xdr enable <cr>
```

Handler ` RVA 0x10C75E20 `；selector ` 0 `；EOL ` RVA 0x34CF4988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12dd95f8ed5d6c5f](../../evidence/conditions-sets-007.md#c-12dd95f8ed5d6c5f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062904

```text
(config)# do-exec test xdr fragment <number:1..1000000> to_slots <number:dynamic> High-queue <cr>
```

Handler ` RVA 0x10CA78F0 `；selector ` 0 `；EOL ` RVA 0x34CFEF00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` fragment size (in Bytes)；` unsigned_number_dynamic ` slot numbers (specify 1+ slots)。

[条件 C-def7b035af0c06a3](../../evidence/conditions-sets-086.md#c-def7b035af0c06a3) · [缺口 G-ae5afb2258072387](../../evidence/gaps-sets-006.md#g-ae5afb2258072387) · [参数 P-33a3bcb686fb79b1](../../evidence/parameters-sets-004.md#p-33a3bcb686fb79b1) · [状态效果 S-6926485ac4f2c709](../../evidence/state_effects-sets-022.md#s-6926485ac4f2c709)

### path-054081

```text
(config)# do-exec test xdr fragment <number:1..1000000> to_slots High-queue <cr>
```

Handler ` RVA 0x10CA78F0 `；selector ` 0 `；EOL ` RVA 0x34CFEF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` fragment size (in Bytes)。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-7258ec243930115d](../../evidence/parameters-sets-009.md#p-7258ec243930115d) · [状态效果 S-b8b573fd88dcc9d4](../../evidence/state_effects-sets-039.md#s-b8b573fd88dcc9d4)

### path-062863

```text
(config)# do-exec test xdr join <number:dynamic> to <number:dynamic> <cr>
```

Handler ` RVA 0x10CA7B90 `；selector ` 0 `；EOL ` RVA 0x34CFD4C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Group containing this linecard as a member；` unsigned_number_dynamic ` Group containing this linecard as a member。

[条件 C-98188c9ec089355f](../../evidence/conditions-sets-059.md#c-98188c9ec089355f) · [缺口 G-4ac3da73487c730b](../../evidence/gaps-sets-003.md#g-4ac3da73487c730b) · [参数 P-089665b9a1263322](../../evidence/parameters-sets-001.md#p-089665b9a1263322) · [状态效果 S-ac6943a2568a31d3](../../evidence/state_effects-sets-036.md#s-ac6943a2568a31d3)

### path-053685

```text
(config)# do-exec test xdr ping to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA7E20 `；selector ` 0 `；EOL ` RVA 0x34CFD028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-b75cb2e4c5728f3a](../../evidence/parameters-sets-014.md#p-b75cb2e4c5728f3a) · [状态效果 S-bbd5efe2ca5a5b23](../../evidence/state_effects-sets-040.md#s-bbd5efe2ca5a5b23)

### path-037049

```text
(config)# do-exec test xdr push start <cr>
```

Handler ` RVA 0x10CA7B40 `；selector ` 0 `；EOL ` RVA 0x34CFE3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060056

```text
(config)# do-exec test xdr push stream <number:1..20> count <number:0..200000> to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA75D0 `；selector ` 0 `；EOL ` RVA 0x34CFE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-92fc2dc68416fcec](../../evidence/parameters-sets-011.md#p-92fc2dc68416fcec) · [状态效果 S-1d68986b49386b19](../../evidence/state_effects-sets-007.md#s-1d68986b49386b19)

### path-030434

```text
(config)# do-exec test xdr show-streams <cr>
```

Handler ` RVA 0x10CA76F0 `；selector ` 0 `；EOL ` RVA 0x34CFE0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036884

```text
(config)# do-exec test xdr split allow <cr>
```

Handler ` RVA 0x10CA7D50 `；selector ` 0 `；EOL ` RVA 0x34CFD7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-a1cd72bcf400be6d](../../evidence/state_effects-sets-034.md#s-a1cd72bcf400be6d)

### path-061401

```text
(config)# do-exec test xdr state-change <number:dynamic> up <cr>
```

Handler ` RVA 0x10C913F0 `；selector ` 0 `；EOL ` RVA 0x34CFF320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-09b13b3d0828105a](../../evidence/conditions-sets-004.md#c-09b13b3d0828105a) · [缺口 G-f1c4b55ebaa95cca](../../evidence/gaps-sets-008.md#g-f1c4b55ebaa95cca) · [参数 P-175b50d7b53a64f0](../../evidence/parameters-sets-002.md#p-175b50d7b53a64f0) · [状态效果 S-c08519711428ed4d](../../evidence/state_effects-sets-041.md#s-c08519711428ed4d)

### path-037231

```text
(config)# do-exec test xdr state-change IPC_START_SENDING <cr>
```

Handler ` RVA 0x10C913F0 `；selector ` 0 `；EOL ` RVA 0x34CFF320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef3cee784612cf50](../../evidence/conditions-sets-092.md#c-ef3cee784612cf50) · [状态效果 S-50b03173b77fa3a9](../../evidence/state_effects-sets-018.md#s-50b03173b77fa3a9)

### path-059223

```text
(config)# do-exec test xdr statistics client test-stats-1 create <number:1..1000000> <number:1..6000> <cr>
```

Handler ` RVA 0xB315AB0 `；selector ` 0 `；EOL ` RVA 0x33737890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Num counters for this client；` unsigned_number ` Update interval for this client (s)。

[条件 C-1e4face58ff1c1c7](../../evidence/conditions-sets-012.md#c-1e4face58ff1c1c7) · [参数 P-022205fef7e7929e](../../evidence/parameters-sets-001.md#p-022205fef7e7929e) · [状态效果 S-cd450be2582dc83d](../../evidence/state_effects-sets-043.md#s-cd450be2582dc83d)

### path-053830

```text
(config)# do-exec test xdr statistics client test-stats-1 req-stats <cr>
```

Handler ` RVA 0xB2B2B70 `；selector ` 0 `；EOL ` RVA 0x3372F4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9b6c9b0a0770911](../../evidence/conditions-sets-090.md#c-e9b6c9b0a0770911) · [状态效果 S-34ae1bb6632b76f3](../../evidence/state_effects-sets-012.md#s-34ae1bb6632b76f3)

### path-053872

```text
(config)# do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB3157E0 `；selector ` 0 `；EOL ` RVA 0x33737E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e4face58ff1c1c7](../../evidence/conditions-sets-012.md#c-1e4face58ff1c1c7) · [状态效果 S-b0dd6d7bcfc567ae](../../evidence/state_effects-sets-037.md#s-b0dd6d7bcfc567ae)

### path-053925

```text
(config)# do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB2B2770 `；selector ` 0 `；EOL ` RVA 0x3372FCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9b6c9b0a0770911](../../evidence/conditions-sets-090.md#c-e9b6c9b0a0770911) · [状态效果 S-66df810769cfd174](../../evidence/state_effects-sets-022.md#s-66df810769cfd174)

### path-046415

```text
(config)# do-exec test xdr statistics selftest <number:0..64> <cr>
```

Handler ` RVA 0xB2B3280 `；selector ` 0 `；EOL ` RVA 0x33730148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot_id。

[条件 C-f7aef6601c77bc03](../../evidence/conditions-sets-096.md#c-f7aef6601c77bc03) · [参数 P-a26de8620aef734b](../../evidence/parameters-sets-012.md#p-a26de8620aef734b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027610

```text
(config)# do-exec test xtf-policy-shim <cr>
```

Handler ` RVA 0x128866D0 `；selector ` 0 `；EOL ` RVA 0x358F6488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025726

```text
(config)# do-exec traceroute <cr>
```

Handler ` RVA 0xE00FAA0 `；selector ` 0 `；EOL ` RVA 0x3415C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2d51f748f49cf43](../../evidence/conditions-sets-081.md#c-d2d51f748f49cf43) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060822

```text
(config)# do-exec traceroute <string> source <?match_ipv6_addrinfo_action_nodefault@55558ad60650> <cr>
```

Handler ` RVA 0xE00FAA0 `；selector ` 0 `；EOL ` RVA 0x3415C008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trace route to destination address or hostname。

[条件 C-e8d8848dc70388bb](../../evidence/conditions-sets-090.md#c-e8d8848dc70388bb) · [缺口 G-0915cb0a92ed98fc](../../evidence/gaps-sets-001.md#g-0915cb0a92ed98fc) · [参数 P-21234a974580ed00](../../evidence/parameters-sets-003.md#p-21234a974580ed00) · [状态效果 S-b2c598957daaf8b4](../../evidence/state_effects-sets-038.md#s-b2c598957daaf8b4)

### path-052695

```text
(config)# do-exec traceroute ethernet <address> domain <string> port <cr>
```

Handler ` RVA 0xBD664C0 `；selector ` 0 `；EOL ` RVA 0x338E2680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote Maintenance Point MAC Address；` string ` maintenance domain name。

[条件 C-ea9bd3859077cfe4](../../evidence/conditions-sets-091.md#c-ea9bd3859077cfe4) · [参数 P-938128e39050e564](../../evidence/parameters-sets-011.md#p-938128e39050e564) · [状态效果 S-9e6abbeabde8a718](../../evidence/state_effects-sets-034.md#s-9e6abbeabde8a718)

### path-026017

```text
(config)# do-exec trigger <string> <cr>
```

Handler ` RVA 0xDF79070 `；selector ` 0 `；EOL ` RVA 0x340B8D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trigger identifier for the trigger to be created or executed。

[条件 C-ca1ed1bb35931af0](../../evidence/conditions-sets-078.md#c-ca1ed1bb35931af0) · [参数 P-8105354b13a9d4eb](../../evidence/parameters-sets-010.md#p-8105354b13a9d4eb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026818

```text
(config)# do-exec tunnel <string> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33D2A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Address or hostname of a remote system。

[条件 C-1dfed2db29fc3190](../../evidence/conditions-sets-012.md#c-1dfed2db29fc3190) · [参数 P-4279d2faf8428569](../../evidence/parameters-sets-006.md#p-4279d2faf8428569) · [状态效果 S-800a30ac6a646fa8](../../evidence/state_effects-sets-027.md#s-800a30ac6a646fa8)

### path-028471

```text
(config)# do-exec undebug ACM all <cr>
```

Handler ` RVA 0xDEDBDB0 `；selector ` 0 `；EOL ` RVA 0x34096D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9567263b3223cb8f](../../evidence/state_effects-sets-032.md#s-9567263b3223cb8f)

### path-028412

```text
(config)# do-exec undebug ACM error <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 1 `；EOL ` RVA 0x340967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9567263b3223cb8f](../../evidence/state_effects-sets-032.md#s-9567263b3223cb8f)

### path-028445

```text
(config)# do-exec undebug ACM event <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 0 `；EOL ` RVA 0x34096A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9567263b3223cb8f](../../evidence/state_effects-sets-032.md#s-9567263b3223cb8f)

### path-032980

```text
(config)# do-exec undebug LDAP all <cr>
```

Handler ` RVA 0x11AC30E0 `；selector ` 0 `；EOL ` RVA 0x3560CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-a0440eb8658913a1](../../evidence/state_effects-sets-034.md#s-a0440eb8658913a1)

### path-032942

```text
(config)# do-exec undebug LDAP error <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 1 `；EOL ` RVA 0x3560C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-a0440eb8658913a1](../../evidence/state_effects-sets-034.md#s-a0440eb8658913a1)

### path-032954

```text
(config)# do-exec undebug LDAP event <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 0 `；EOL ` RVA 0x3560C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-a0440eb8658913a1](../../evidence/state_effects-sets-034.md#s-a0440eb8658913a1)

### path-032968

```text
(config)# do-exec undebug LDAP legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3560C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-a0440eb8658913a1](../../evidence/state_effects-sets-034.md#s-a0440eb8658913a1)

### path-032929

```text
(config)# do-exec undebug LDAP packet <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 2 `；EOL ` RVA 0x3560C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-a0440eb8658913a1](../../evidence/state_effects-sets-034.md#s-a0440eb8658913a1)

### path-029106

```text
(config)# do-exec undebug aaa accounting <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 16 `；EOL ` RVA 0x341B80C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029158

```text
(config)# do-exec undebug aaa administrative <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 17 `；EOL ` RVA 0x341B8368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030089

```text
(config)# do-exec undebug aaa api <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 35 `；EOL ` RVA 0x341BC6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036416

```text
(config)# do-exec undebug aaa api attr <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 36 `；EOL ` RVA 0x341BC680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030033

```text
(config)# do-exec undebug aaa attr <cr>
```

Handler ` RVA 0xDD3A410 `；selector ` 26 `；EOL ` RVA 0x341BB120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036173

```text
(config)# do-exec undebug aaa attr add <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 30 `；EOL ` RVA 0x341BABA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036098

```text
(config)# do-exec undebug aaa attr alloc-free <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 31 `；EOL ` RVA 0x341BA900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036014

```text
(config)# do-exec undebug aaa attr error <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 32 `；EOL ` RVA 0x341BA658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-035930

```text
(config)# do-exec undebug aaa attr handle <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 27 `；EOL ` RVA 0x341BA3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036310

```text
(config)# do-exec undebug aaa attr info <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 28 `；EOL ` RVA 0x341BB0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036239

```text
(config)# do-exec undebug aaa attr update <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 29 `；EOL ` RVA 0x341BAE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029027

```text
(config)# do-exec undebug aaa authentication <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 12 `；EOL ` RVA 0x341B7B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029067

```text
(config)# do-exec undebug aaa authorization <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 15 `；EOL ` RVA 0x341B7E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029210

```text
(config)# do-exec undebug aaa boundary <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 56 `；EOL ` RVA 0x341B8610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-034978

```text
(config)# do-exec undebug aaa cache filterserver <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 50 `；EOL ` RVA 0x341B7040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-035023

```text
(config)# do-exec undebug aaa cache group <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 51 `；EOL ` RVA 0x341B72E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029272

```text
(config)# do-exec undebug aaa cca <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 57 `；EOL ` RVA 0x341B88B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029540

```text
(config)# do-exec undebug aaa coa <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 25 `；EOL ` RVA 0x341B98A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030260

```text
(config)# do-exec undebug aaa common-criteria <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 55 `；EOL ` RVA 0x341BD9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-305bd1d1fbc899f1](../../evidence/conditions-sets-019.md#c-305bd1d1fbc899f1) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029894

```text
(config)# do-exec undebug aaa db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 38 `；EOL ` RVA 0x341BBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036523

```text
(config)# do-exec undebug aaa dead-criteria transaction <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 42 `；EOL ` RVA 0x341BD188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030290

```text
(config)# do-exec undebug aaa green <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 69 `；EOL ` RVA 0x341BDC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89fb90ca84e0b9a0](../../evidence/conditions-sets-053.md#c-89fb90ca84e0b9a0) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029985

```text
(config)# do-exec undebug aaa id <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 37 `；EOL ` RVA 0x341BC0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029789

```text
(config)# do-exec undebug aaa ipc <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 33 `；EOL ` RVA 0x341BB628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029695

```text
(config)# do-exec undebug aaa memory <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 13 `；EOL ` RVA 0x341BA0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029346

```text
(config)# do-exec undebug aaa mlist-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 44 `；EOL ` RVA 0x341B8E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030185

```text
(config)# do-exec undebug aaa mlist-state <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 45 `；EOL ` RVA 0x341BD6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029488

```text
(config)# do-exec undebug aaa per-user <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 18 `；EOL ` RVA 0x341B9600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029595

```text
(config)# do-exec undebug aaa pod <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 24 `；EOL ` RVA 0x341B9B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-035056

```text
(config)# do-exec undebug aaa profile db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 52 `；EOL ` RVA 0x341B78E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036470

```text
(config)# do-exec undebug aaa protocol local <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 40 `；EOL ` RVA 0x341BCBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-036533

```text
(config)# do-exec undebug aaa protocol radius <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 41 `；EOL ` RVA 0x341BCE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029642

```text
(config)# do-exec undebug aaa proxy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 23 `；EOL ` RVA 0x341B9DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030291

```text
(config)# do-exec undebug aaa redundancy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 54 `；EOL ` RVA 0x341BDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3604d86012653633](../../evidence/conditions-sets-021.md#c-3604d86012653633) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029433

```text
(config)# do-exec undebug aaa server-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 46 `；EOL ` RVA 0x341B9358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029382

```text
(config)# do-exec undebug aaa sg-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 47 `；EOL ` RVA 0x341B90B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029313

```text
(config)# do-exec undebug aaa sg-server-selection <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 48 `；EOL ` RVA 0x341B8B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-035020

```text
(config)# do-exec undebug aaa subscriber profile <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 53 `；EOL ` RVA 0x341B75E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029843

```text
(config)# do-exec undebug aaa subsys <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 34 `；EOL ` RVA 0x341BB8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-030153

```text
(config)# do-exec undebug aaa testing <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 43 `；EOL ` RVA 0x341BD418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-035021

```text
(config)# do-exec undebug aaa tools memleak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35C0DA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-43c85fe43d6586fc](../../evidence/state_effects-sets-015.md#s-43c85fe43d6586fc)

### path-030022

```text
(config)# do-exec undebug aaa traceback <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 14 `；EOL ` RVA 0x341BC370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-029939

```text
(config)# do-exec undebug aaa userdb <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 39 `；EOL ` RVA 0x341BBE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7fc25652bb29692c](../../evidence/state_effects-sets-027.md#s-7fc25652bb29692c)

### path-027743

```text
(config)# do-exec undebug access-expression <cr>
```

Handler ` RVA 0xF2A3970 `；selector ` 0 `；EOL ` RVA 0x345E4A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fd1c930701bd9956](../../evidence/state_effects-sets-054.md#s-fd1c930701bd9956)

### path-033181

```text
(config)# do-exec undebug access-session all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 4 `；EOL ` RVA 0x33BAEA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-033173

```text
(config)# do-exec undebug access-session detail <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 2 `；EOL ` RVA 0x33BAE7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-033155

```text
(config)# do-exec undebug access-session errors <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 0 `；EOL ` RVA 0x33BAE258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-033166

```text
(config)# do-exec undebug access-session events <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 1 `；EOL ` RVA 0x33BAE500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-042457

```text
(config)# do-exec undebug access-session feature all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 5 `；EOL ` RVA 0x33BAF118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-042657

```text
(config)# do-exec undebug access-session rcl_server all <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 3 `；EOL ` RVA 0x33BAD888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-6b8d7e1b22fef0ee](../../evidence/state_effects-sets-023.md#s-6b8d7e1b22fef0ee)

### path-042634

```text
(config)# do-exec undebug access-session rcl_server detail <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 2 `；EOL ` RVA 0x33BAD5E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-6b8d7e1b22fef0ee](../../evidence/state_effects-sets-023.md#s-6b8d7e1b22fef0ee)

### path-042613

```text
(config)# do-exec undebug access-session rcl_server error <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 0 `；EOL ` RVA 0x33BAD338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-6b8d7e1b22fef0ee](../../evidence/state_effects-sets-023.md#s-6b8d7e1b22fef0ee)

### path-042596

```text
(config)# do-exec undebug access-session rcl_server event <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 1 `；EOL ` RVA 0x33BAD090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-6b8d7e1b22fef0ee](../../evidence/state_effects-sets-023.md#s-6b8d7e1b22fef0ee)

### path-033198

```text
(config)# do-exec undebug access-session sync <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 3 `；EOL ` RVA 0x33BAED38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-8051ba8a3329c81b](../../evidence/state_effects-sets-027.md#s-8051ba8a3329c81b)

### path-038049

```text
(config)# do-exec undebug acl cca error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3447D290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-636fdb83a8c4e643](../../evidence/state_effects-sets-021.md#s-636fdb83a8c4e643)

### path-038085

```text
(config)# do-exec undebug acl cca event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3447D538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-636fdb83a8c4e643](../../evidence/state_effects-sets-021.md#s-636fdb83a8c4e643)

### path-027411

```text
(config)# do-exec undebug adjacency <cr>
```

Handler ` RVA 0xB559CD0 `；selector ` 0 `；EOL ` RVA 0x3379B6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f773847018d57e5e](../../evidence/conditions-sets-096.md#c-f773847018d57e5e) · [状态效果 S-93dc5bb8f94cd207](../../evidence/state_effects-sets-031.md#s-93dc5bb8f94cd207)

### path-030683

```text
(config)# do-exec undebug alg all <cr>
```

Handler ` RVA 0xCD3BF50 `；selector ` 1 `；EOL ` RVA 0x33CD4910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65dc017238348d20](../../evidence/state_effects-sets-022.md#s-65dc017238348d20)

### path-030763

```text
(config)# do-exec undebug alg info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD5108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65dc017238348d20](../../evidence/state_effects-sets-022.md#s-65dc017238348d20)

### path-030743

```text
(config)# do-exec undebug alg trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD4E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65dc017238348d20](../../evidence/state_effects-sets-022.md#s-65dc017238348d20)

### path-030713

```text
(config)# do-exec undebug alg warn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CD4BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65dc017238348d20](../../evidence/state_effects-sets-022.md#s-65dc017238348d20)

### path-026314

```text
(config)# do-exec undebug all <cr>
```

Handler ` RVA 0xE002630 `；selector ` 0 `；EOL ` RVA 0x34121818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-043172

```text
(config)# do-exec undebug alps ascu event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 3 `；EOL ` RVA 0x3541C160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dec29db2ab391490](../../evidence/conditions-sets-086.md#c-dec29db2ab391490) · [状态效果 S-3fc447bfcf04524c](../../evidence/state_effects-sets-014.md#s-3fc447bfcf04524c)

### path-043102

```text
(config)# do-exec undebug alps circuit event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 2 `；EOL ` RVA 0x3541BCD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3cf6eb04f0c32659](../../evidence/state_effects-sets-013.md#s-3cf6eb04f0c32659)

### path-043105

```text
(config)# do-exec undebug alps peer event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 1 `；EOL ` RVA 0x3541B960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-85f719a71135a4cc](../../evidence/state_effects-sets-028.md#s-85f719a71135a4cc)

### path-033515

```text
(config)# do-exec undebug alps snmp <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 4 `；EOL ` RVA 0x3541C6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032734

```text
(config)# do-exec undebug analyze memory-leak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x341F0BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57872e0efd72043a](../../evidence/conditions-sets-034.md#c-57872e0efd72043a) · [状态效果 S-77af2bb29edcddee](../../evidence/state_effects-sets-025.md#s-77af2bb29edcddee)

### path-030277

```text
(config)# do-exec undebug ancp adjacency <cr>
```

Handler ` RVA 0xB258990 `；selector ` 0 `；EOL ` RVA 0x336D7DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-cc5ca44fd2e78ad6](../../evidence/state_effects-sets-043.md#s-cc5ca44fd2e78ad6)

### path-032566

```text
(config)# do-exec undebug application db <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 7 `；EOL ` RVA 0x358DCD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032585

```text
(config)# do-exec undebug application detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 2 `；EOL ` RVA 0x358DD028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032535

```text
(config)# do-exec undebug application event <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 5 `；EOL ` RVA 0x358DC578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032655

```text
(config)# do-exec undebug application ha <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 8 `；EOL ` RVA 0x358DD660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-041549

```text
(config)# do-exec undebug application ha detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 9 `；EOL ` RVA 0x358DD638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-050407

```text
(config)# do-exec undebug application route <address> <address> <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 1 `；EOL ` RVA 0x358DD378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [参数 P-3fadc80999e697ce](../../evidence/parameters-sets-005.md#p-3fadc80999e697ce) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032569

```text
(config)# do-exec undebug application rwatch <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 3 `；EOL ` RVA 0x358DC8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-041400

```text
(config)# do-exec undebug application rwatch rib <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 4 `；EOL ` RVA 0x358DC888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032524

```text
(config)# do-exec undebug application summary <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 6 `；EOL ` RVA 0x358DC2D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-042630

```text
(config)# do-exec undebug archive config differences <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-7dce69e9c756ec80](../../evidence/state_effects-sets-027.md#s-7dce69e9c756ec80)

### path-042671

```text
(config)# do-exec undebug archive config ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-f487d72278db81f1](../../evidence/state_effects-sets-052.md#s-f487d72278db81f1)

### path-042650

```text
(config)# do-exec undebug archive config timestamp <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-0732aa18ba8bba81](../../evidence/state_effects-sets-002.md#s-0732aa18ba8bba81)

### path-051195

```text
(config)# do-exec undebug archive log config persistent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3409A520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3daa5eeb50466169](../../evidence/state_effects-sets-014.md#s-3daa5eeb50466169)

### path-033255

```text
(config)# do-exec undebug archive versioning <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9d9c37cb3c2adf8f](../../evidence/state_effects-sets-033.md#s-9d9c37cb3c2adf8f)

### path-042610

```text
(config)# do-exec undebug archive versioning ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c543ed64e00d1b36](../../evidence/state_effects-sets-042.md#s-c543ed64e00d1b36)

### path-026880

```text
(config)# do-exec undebug arp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDA618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-06f0822d871e3d4a](../../evidence/conditions-sets-003.md#c-06f0822d871e3d4a) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028609

```text
(config)# do-exec undebug arp adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD8580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028650

```text
(config)# do-exec undebug arp application <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD8828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-029029

```text
(config)# do-exec undebug arp database <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33CD9D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028690

```text
(config)# do-exec undebug arp dynamic <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33CD8AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028929

```text
(config)# do-exec undebug arp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x33CD9818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028727

```text
(config)# do-exec undebug arp ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33CD8D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028769

```text
(config)# do-exec undebug arp interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33CD9020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-029161

```text
(config)# do-exec undebug arp retry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33CDA2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-23688e86dcdd4a02](../../evidence/conditions-sets-014.md#c-23688e86dcdd4a02) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028830

```text
(config)# do-exec undebug arp static <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CD92C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028883

```text
(config)# do-exec undebug arp subblocking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33CD9570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-028987

```text
(config)# do-exec undebug arp table <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33CD9AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-029069

```text
(config)# do-exec undebug arp timer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33CDA010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-d2c04f8a5a756b82](../../evidence/state_effects-sets-045.md#s-d2c04f8a5a756b82)

### path-033799

```text
(config)# do-exec undebug aspp event <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 0 `；EOL ` RVA 0x354A3338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-781b102a9daacd58](../../evidence/state_effects-sets-026.md#s-781b102a9daacd58)

### path-033820

```text
(config)# do-exec undebug aspp packet <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 1 `；EOL ` RVA 0x354A3668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-781b102a9daacd58](../../evidence/state_effects-sets-026.md#s-781b102a9daacd58)

### path-032336

```text
(config)# do-exec undebug async async-queue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34935440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-10fa5461f4212f5a](../../evidence/state_effects-sets-004.md#s-10fa5461f4212f5a)

### path-032281

```text
(config)# do-exec undebug async framing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34934C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-10fa5461f4212f5a](../../evidence/state_effects-sets-004.md#s-10fa5461f4212f5a)

### path-032299

```text
(config)# do-exec undebug async packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34934EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-10fa5461f4212f5a](../../evidence/state_effects-sets-004.md#s-10fa5461f4212f5a)

### path-032318

```text
(config)# do-exec undebug async state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34935198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-10fa5461f4212f5a](../../evidence/state_effects-sets-004.md#s-10fa5461f4212f5a)

### path-032140

```text
(config)# do-exec undebug atm ilmi <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 24 `；EOL ` RVA 0x33C52E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3c4f4ee513c9bece](../../evidence/conditions-sets-023.md#c-3c4f4ee513c9bece) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-040614

```text
(config)# do-exec undebug atm ilmi red <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 29 `；EOL ` RVA 0x33C530D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3c4f4ee513c9bece](../../evidence/conditions-sets-023.md#c-3c4f4ee513c9bece) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-027775

```text
(config)# do-exec undebug atomic-config <cr>
```

Handler ` RVA 0x165754F0 `；selector ` 0 `；EOL ` RVA 0x35FA2C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa82dbd4e796703d](../../evidence/conditions-sets-097.md#c-fa82dbd4e796703d) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-032579

```text
(config)# do-exec undebug autoip event <cr>
```

Handler ` RVA 0xB286740 `；selector ` 0 `；EOL ` RVA 0x3372B5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-a345a5824b9d8141](../../evidence/state_effects-sets-035.md#s-a345a5824b9d8141)

### path-026802

```text
(config)# do-exec undebug backup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34481E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5d53e7721f409bab](../../evidence/state_effects-sets-020.md#s-5d53e7721f409bab)

### path-032805

```text
(config)# do-exec undebug beep concurrency <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 3 `；EOL ` RVA 0x3448B2A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16d117361ec8aabf](../../evidence/conditions-sets-009.md#c-16d117361ec8aabf) · [状态效果 S-7da0d8f414e97f1a](../../evidence/state_effects-sets-027.md#s-7da0d8f414e97f1a)

### path-032836

```text
(config)# do-exec undebug beep profile <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 1 `；EOL ` RVA 0x3448B950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16d117361ec8aabf](../../evidence/conditions-sets-009.md#c-16d117361ec8aabf) · [状态效果 S-7da0d8f414e97f1a](../../evidence/state_effects-sets-027.md#s-7da0d8f414e97f1a)

### path-032847

```text
(config)# do-exec undebug beep session <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 2 `；EOL ` RVA 0x3448B5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-565da835f8b1f810](../../evidence/conditions-sets-034.md#c-565da835f8b1f810) · [状态效果 S-7da0d8f414e97f1a](../../evidence/state_effects-sets-027.md#s-7da0d8f414e97f1a)

### path-031361

```text
(config)# do-exec undebug bfd dampening <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 3 `；EOL ` RVA 0x34CAD060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-031433

```text
(config)# do-exec undebug bfd event <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 1 `；EOL ` RVA 0x34CAC8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b465663d70eedbd6](../../evidence/state_effects-sets-038.md#s-b465663d70eedbd6)

### path-031317

```text
(config)# do-exec undebug bfd ha <cr>
```

Handler ` RVA 0x10B663D0 `；selector ` 0 `；EOL ` RVA 0x34CBEF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-aa0a1892d26f1673](../../evidence/state_effects-sets-036.md#s-aa0a1892d26f1673)

### path-031418

```text
(config)# do-exec undebug bfd packet <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 0 `；EOL ` RVA 0x34CAC2A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-48f55cc32ed5baaf](../../evidence/state_effects-sets-016.md#s-48f55cc32ed5baaf)

### path-031336

```text
(config)# do-exec undebug bfd stub <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 2 `；EOL ` RVA 0x34CACDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-039988

```text
(config)# do-exec undebug bgp telemetry enable <cr>
```

Handler ` RVA 0xF047BD0 `；selector ` 1 `；EOL ` RVA 0x344F9690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1c3d05487b88cc4c](../../evidence/state_effects-sets-006.md#s-1c3d05487b88cc4c)

### path-032082

```text
(config)# do-exec undebug bidb errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 67 `；EOL ` RVA 0x33BF93F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5b85ce2fc80644c7](../../evidence/state_effects-sets-020.md#s-5b85ce2fc80644c7)

### path-032071

```text
(config)# do-exec undebug bidb events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 66 `；EOL ` RVA 0x33BF9150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5b85ce2fc80644c7](../../evidence/state_effects-sets-020.md#s-5b85ce2fc80644c7)

### path-032099

```text
(config)# do-exec undebug bidb verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 68 `；EOL ` RVA 0x33BF96A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5b85ce2fc80644c7](../../evidence/state_effects-sets-020.md#s-5b85ce2fc80644c7)

### path-027689

```text
(config)# do-exec undebug bing <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 0 `；EOL ` RVA 0x345DE0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-61fcf183886e570b](../../evidence/state_effects-sets-021.md#s-61fcf183886e570b)

### path-032806

```text
(config)# do-exec undebug bing detail <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 1 `；EOL ` RVA 0x345DE0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-61fcf183886e570b](../../evidence/state_effects-sets-021.md#s-61fcf183886e570b)

### path-037006

```text
(config)# do-exec undebug bridge-domain client api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33950710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-036949

```text
(config)# do-exec undebug bridge-domain client errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33950468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-030427

```text
(config)# do-exec undebug bridge-domain configuration <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x339509A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-030453

```text
(config)# do-exec undebug bridge-domain errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33950C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-030479

```text
(config)# do-exec undebug bridge-domain ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33950EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037308

```text
(config)# do-exec undebug bridge-domain l2fib errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x339522E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7841d41a44c717ef](../../evidence/conditions-sets-047.md#c-7841d41a44c717ef) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037262

```text
(config)# do-exec undebug bridge-domain l2fib events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33952040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7841d41a44c717ef](../../evidence/conditions-sets-047.md#c-7841d41a44c717ef) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-030505

```text
(config)# do-exec undebug bridge-domain linkfault <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x339511A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037269

```text
(config)# do-exec undebug bridge-domain route errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33951798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57507965cb1d4c3b](../../evidence/conditions-sets-034.md#c-57507965cb1d4c3b) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037223

```text
(config)# do-exec undebug bridge-domain route events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x339514F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57507965cb1d4c3b](../../evidence/conditions-sets-034.md#c-57507965cb1d4c3b) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037353

```text
(config)# do-exec undebug bridge-domain route flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33951CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57507965cb1d4c3b](../../evidence/conditions-sets-034.md#c-57507965cb1d4c3b) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-037313

```text
(config)# do-exec undebug bridge-domain route messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33951A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57507965cb1d4c3b](../../evidence/conditions-sets-034.md#c-57507965cb1d4c3b) · [状态效果 S-fe9543181d108db9](../../evidence/state_effects-sets-054.md#s-fe9543181d108db9)

### path-033538

```text
(config)# do-exec undebug bsc diagnostic <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 2 `；EOL ` RVA 0x354B4EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-707b147eefceccb2](../../evidence/state_effects-sets-024.md#s-707b147eefceccb2)

### path-033545

```text
(config)# do-exec undebug bsc event <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 0 `；EOL ` RVA 0x354B51E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-707b147eefceccb2](../../evidence/state_effects-sets-024.md#s-707b147eefceccb2)

### path-033565

```text
(config)# do-exec undebug bsc packet <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 1 `；EOL ` RVA 0x354B5510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-707b147eefceccb2](../../evidence/state_effects-sets-024.md#s-707b147eefceccb2)

### path-033544

```text
(config)# do-exec undebug bstun event <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 1 `；EOL ` RVA 0x354BBF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65300f676791da2e](../../evidence/state_effects-sets-022.md#s-65300f676791da2e)

### path-033564

```text
(config)# do-exec undebug bstun packet <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 2 `；EOL ` RVA 0x354BC278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-65300f676791da2e](../../evidence/state_effects-sets-022.md#s-65300f676791da2e)

### path-027742

```text
(config)# do-exec undebug buffer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x342BC530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9d7cbba43badc4ad](../../evidence/state_effects-sets-033.md#s-9d7cbba43badc4ad)

### path-033301

```text
(config)# do-exec undebug buffer failures <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x342BC508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-9d7cbba43badc4ad](../../evidence/state_effects-sets-033.md#s-9d7cbba43badc4ad)

### path-043446

```text
(config)# do-exec undebug bulkstat client all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 2 `；EOL ` RVA 0x33888E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-043404

```text
(config)# do-exec undebug bulkstat client error <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 0 `；EOL ` RVA 0x33888908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-764bedb6d9457892](../../evidence/state_effects-sets-025.md#s-764bedb6d9457892)

### path-043423

```text
(config)# do-exec undebug bulkstat client info <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 1 `；EOL ` RVA 0x33888BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-96be54cab289208d](../../evidence/state_effects-sets-032.md#s-96be54cab289208d)

### path-043425

```text
(config)# do-exec undebug bulkstat file all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 1 `；EOL ` RVA 0x33888620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-043383

```text
(config)# do-exec undebug bulkstat file error <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 0 `；EOL ` RVA 0x338880B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8b6a4aa638c7caa1](../../evidence/state_effects-sets-030.md#s-8b6a4aa638c7caa1)

### path-043407

```text
(config)# do-exec undebug bulkstat file info <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 1 `；EOL ` RVA 0x33888368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-bb22517fc51d6b72](../../evidence/state_effects-sets-040.md#s-bb22517fc51d6b72)

### path-043489

```text
(config)# do-exec undebug bulkstat processing all <cr>
```

Handler ` RVA 0xBC88F60 `；selector ` 0 `；EOL ` RVA 0x338984B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-043475

```text
(config)# do-exec undebug bulkstat processing error <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 0 `；EOL ` RVA 0x338981F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-dd9a5d71f930cd14](../../evidence/state_effects-sets-047.md#s-dd9a5d71f930cd14)

### path-043459

```text
(config)# do-exec undebug bulkstat processing info <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 1 `；EOL ` RVA 0x33897F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c6b5b34399021e2d](../../evidence/state_effects-sets-042.md#s-c6b5b34399021e2d)

### path-032085

```text
(config)# do-exec undebug caaa accounting <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 4 `；EOL ` RVA 0x33BB3A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032171

```text
(config)# do-exec undebug caaa all <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 0 `；EOL ` RVA 0x33BB4A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032101

```text
(config)# do-exec undebug caaa authentication <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 2 `；EOL ` RVA 0x33BB3D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032116

```text
(config)# do-exec undebug caaa authorization <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 3 `；EOL ` RVA 0x33BB3FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032062

```text
(config)# do-exec undebug caaa command-handler <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 6 `；EOL ` RVA 0x33BB3538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032134

```text
(config)# do-exec undebug caaa error <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 1 `；EOL ` RVA 0x33BB4280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032050

```text
(config)# do-exec undebug caaa ha <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 7 `；EOL ` RVA 0x33BB3290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-032075

```text
(config)# do-exec undebug caaa service <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 5 `；EOL ` RVA 0x33BB37E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-066b93c1d6800060](../../evidence/state_effects-sets-002.md#s-066b93c1d6800060)

### path-041884

```text
(config)# do-exec undebug call filter detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3605B290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-27a9a065fce88407](../../evidence/conditions-sets-016.md#c-27a9a065fce88407) · [状态效果 S-414180bd0a7568ec](../../evidence/state_effects-sets-014.md#s-414180bd0a7568ec)

### path-041853

```text
(config)# do-exec undebug call filter inout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3605AFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-27a9a065fce88407](../../evidence/conditions-sets-016.md#c-27a9a065fce88407) · [状态效果 S-0d3dbf83224d72fa](../../evidence/state_effects-sets-003.md#s-0d3dbf83224d72fa)

### path-033083

```text
(config)# do-exec undebug call-admission elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3408F7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-039cbd13e0172420](../../evidence/state_effects-sets-001.md#s-039cbd13e0172420)

### path-033093

```text
(config)# do-exec undebug call-admission trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3408FA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-039cbd13e0172420](../../evidence/state_effects-sets-001.md#s-039cbd13e0172420)

### path-030481

```text
(config)# do-exec undebug call-home all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 14 `；EOL ` RVA 0x337F5370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-030374

```text
(config)# do-exec undebug call-home detail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 2 `；EOL ` RVA 0x337F48D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037314

```text
(config)# do-exec undebug call-home diagnostic-signature action <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 6 `；EOL ` RVA 0x337F61B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037492

```text
(config)# do-exec undebug call-home diagnostic-signature all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 15 `；EOL ` RVA 0x337F6EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037394

```text
(config)# do-exec undebug call-home diagnostic-signature api <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 8 `；EOL ` RVA 0x337F6700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037420

```text
(config)# do-exec undebug call-home diagnostic-signature cli <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 10 `；EOL ` RVA 0x337F69A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037354

```text
(config)# do-exec undebug call-home diagnostic-signature download <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 7 `；EOL ` RVA 0x337F6458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037452

```text
(config)# do-exec undebug call-home diagnostic-signature error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 9 `；EOL ` RVA 0x337F6C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037270

```text
(config)# do-exec undebug call-home diagnostic-signature event-registration <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 5 `；EOL ` RVA 0x337F5F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037224

```text
(config)# do-exec undebug call-home diagnostic-signature parsing <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 4 `；EOL ` RVA 0x337F5C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ea0e1b024e36b7](../../evidence/conditions-sets-032.md#c-50ea0e1b024e36b7) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-030430

```text
(config)# do-exec undebug call-home error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 1 `；EOL ` RVA 0x337F4E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-030402

```text
(config)# do-exec undebug call-home mail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 3 `；EOL ` RVA 0x337F4B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-030540

```text
(config)# do-exec undebug call-home message-content <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 13 `；EOL ` RVA 0x337F56A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-046574

```text
(config)# do-exec undebug call-home message-content profile <string> <cr>
```

Handler ` RVA 0xB6C71B0 `；selector ` 0 `；EOL ` RVA 0x337F56E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile name。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [参数 P-e516ecaeeb5cb103](../../evidence/parameters-sets-017.md#p-e516ecaeeb5cb103) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037350

```text
(config)# do-exec undebug call-home smart-licensing all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 16 `；EOL ` RVA 0x337F77A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d54572e6bd884bef](../../evidence/conditions-sets-082.md#c-d54572e6bd884bef) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037310

```text
(config)# do-exec undebug call-home smart-licensing error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 12 `；EOL ` RVA 0x337F7500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d54572e6bd884bef](../../evidence/conditions-sets-082.md#c-d54572e6bd884bef) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-037263

```text
(config)# do-exec undebug call-home smart-licensing trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 11 `；EOL ` RVA 0x337F7258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d54572e6bd884bef](../../evidence/conditions-sets-082.md#c-d54572e6bd884bef) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-030457

```text
(config)# do-exec undebug call-home trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 0 `；EOL ` RVA 0x337F50C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-ba80198ecb4fd67e](../../evidence/state_effects-sets-039.md#s-ba80198ecb4fd67e)

### path-027690

```text
(config)# do-exec undebug callback <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346049D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-061da2120956ed28](../../evidence/state_effects-sets-002.md#s-061da2120956ed28)

### path-026579

```text
(config)# do-exec undebug cca <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33EDDF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-45b7c0a522890172](../../evidence/state_effects-sets-015.md#s-45b7c0a522890172)

### path-030944

```text
(config)# do-exec undebug cce cp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x340387A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-51dfa820b316c240](../../evidence/state_effects-sets-018.md#s-51dfa820b316c240)

### path-047154

```text
(config)# do-exec undebug cce cp filter balance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34038DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-51dfa820b316c240](../../evidence/state_effects-sets-018.md#s-51dfa820b316c240)

### path-031061

```text
(config)# do-exec undebug cce cpdp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3403BB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-416e6478c50b84c3](../../evidence/state_effects-sets-014.md#s-416e6478c50b84c3)

### path-038025

```text
(config)# do-exec undebug cce cpdp elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3403BB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-416e6478c50b84c3](../../evidence/state_effects-sets-014.md#s-416e6478c50b84c3)

### path-038040

```text
(config)# do-exec undebug cce cpdp events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3403B698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-416e6478c50b84c3](../../evidence/state_effects-sets-014.md#s-416e6478c50b84c3)

### path-047226

```text
(config)# do-exec undebug cce cpdp events detailed <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3403B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-416e6478c50b84c3](../../evidence/state_effects-sets-014.md#s-416e6478c50b84c3)

### path-031062

```text
(config)# do-exec undebug cce ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CDECF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3e82d595ccf632a3](../../evidence/state_effects-sets-014.md#s-3e82d595ccf632a3)

### path-037982

```text
(config)# do-exec undebug cce ha event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CDEA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3e82d595ccf632a3](../../evidence/state_effects-sets-014.md#s-3e82d595ccf632a3)

### path-038026

```text
(config)# do-exec undebug cce ha issu <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDECC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3e82d595ccf632a3](../../evidence/state_effects-sets-014.md#s-3e82d595ccf632a3)

### path-033010

```text
(config)# do-exec undebug cdapi detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35F0C540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5cf3af454a7a8583](../../evidence/state_effects-sets-020.md#s-5cf3af454a7a8583)

### path-033004

```text
(config)# do-exec undebug cdapi events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35F0C298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5cf3af454a7a8583](../../evidence/state_effects-sets-020.md#s-5cf3af454a7a8583)

### path-030761

```text
(config)# do-exec undebug cdp adjacency <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 2 `；EOL ` RVA 0x33CE0CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030741

```text
(config)# do-exec undebug cdp events <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 1 `；EOL ` RVA 0x33CE0A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030839

```text
(config)# do-exec undebug cdp ilp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CE1760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030777

```text
(config)# do-exec undebug cdp ip <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 3 `；EOL ` RVA 0x33CE0F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030789

```text
(config)# do-exec undebug cdp location-server <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 4 `；EOL ` RVA 0x33CE1210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030710

```text
(config)# do-exec undebug cdp packets <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 0 `；EOL ` RVA 0x33CE0770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-030811

```text
(config)# do-exec undebug cdp test <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 5 `；EOL ` RVA 0x33CE14B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-883105f865e83918](../../evidence/state_effects-sets-029.md#s-883105f865e83918)

### path-037029

```text
(config)# do-exec undebug cef filter fib <cr>
```

Handler ` RVA 0xB384EB0 `；selector ` 0 `；EOL ` RVA 0x337431A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-51ee62ff5f765f62](../../evidence/conditions-sets-032.md#c-51ee62ff5f765f62) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-046703

```text
(config)# do-exec undebug cef filter hardware notifications <cr>
```

Handler ` RVA 0xB4F8820 `；selector ` 0 `；EOL ` RVA 0x33743D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cca6ad8b759bb762](../../evidence/conditions-sets-079.md#c-cca6ad8b759bb762) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-037134

```text
(config)# do-exec undebug cef filter path <cr>
```

Handler ` RVA 0xB422A80 `；selector ` 0 `；EOL ` RVA 0x33742A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4915d83fcdf6de2e](../../evidence/conditions-sets-029.md#c-4915d83fcdf6de2e) · [状态效果 S-a49db99804430429](../../evidence/state_effects-sets-035.md#s-a49db99804430429)

### path-053718

```text
(config)# do-exec undebug cef filter subtree context client <cr>
```

Handler ` RVA 0xB4537D0 `；selector ` 0 `；EOL ` RVA 0x33742120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-acc55370c5145221](../../evidence/conditions-sets-067.md#c-acc55370c5145221) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-037072

```text
(config)# do-exec undebug cef filter table <cr>
```

Handler ` RVA 0xB45B0A0 `；selector ` 0 `；EOL ` RVA 0x33743680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-53243143abe55aa8](../../evidence/conditions-sets-032.md#c-53243143abe55aa8) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-046351

```text
(config)# do-exec undebug cef filter uid key <cr>
```

Handler ` RVA 0xB4B72F0 `；selector ` 0 `；EOL ` RVA 0x337424F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d4d530f8b4438ec7](../../evidence/conditions-sets-082.md#c-d4d530f8b4438ec7) · [状态效果 S-ee724a6b3a43a74c](../../evidence/state_effects-sets-050.md#s-ee724a6b3a43a74c)

### path-037116

```text
(config)# do-exec undebug cef filter vrf <cr>
```

Handler ` RVA 0xB4863B0 `；selector ` 0 `；EOL ` RVA 0x337439F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9354790daf0052d9](../../evidence/conditions-sets-057.md#c-9354790daf0052d9) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-030415

```text
(config)# do-exec undebug cef table <cr>
```

Handler ` RVA 0xB37CB40 `；selector ` 0 `；EOL ` RVA 0x33744360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5834555a1f291788](../../evidence/conditions-sets-035.md#c-5834555a1f291788) · [状态效果 S-88c2a0ead41ad1cb](../../evidence/state_effects-sets-029.md#s-88c2a0ead41ad1cb)

### path-026581

```text
(config)# do-exec undebug cfgdiff <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 1 `；EOL ` RVA 0x34113FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5021ea46ad3bbdfb](../../evidence/state_effects-sets-018.md#s-5021ea46ad3bbdfb)

### path-028488

```text
(config)# do-exec undebug cfgdiff timestamp <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 2 `；EOL ` RVA 0x34113F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5021ea46ad3bbdfb](../../evidence/state_effects-sets-018.md#s-5021ea46ad3bbdfb)

### path-027605

```text
(config)# do-exec undebug cft <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 6 `；EOL ` RVA 0x358FF988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-93c756b1adc42475](../../evidence/conditions-sets-057.md#c-93c756b1adc42475) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031510

```text
(config)# do-exec undebug cft ager <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 4 `；EOL ` RVA 0x358FEEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e2e9d8a63dd0e5d0](../../evidence/conditions-sets-087.md#c-e2e9d8a63dd0e5d0) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031561

```text
(config)# do-exec undebug cft engine <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 0 `；EOL ` RVA 0x358FF410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7013a36ee33f5942](../../evidence/conditions-sets-043.md#c-7013a36ee33f5942) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031584

```text
(config)# do-exec undebug cft fe <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 3 `；EOL ` RVA 0x358FF6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6ad05fd4276aa2b9](../../evidence/conditions-sets-041.md#c-6ad05fd4276aa2b9) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031485

```text
(config)# do-exec undebug cft flow <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 5 `；EOL ` RVA 0x358FEC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3954b649674382f0](../../evidence/conditions-sets-022.md#c-3954b649674382f0) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031604

```text
(config)# do-exec undebug cft l4 <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 2 `；EOL ` RVA 0x358FF960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6ac65320fe7dc72c](../../evidence/conditions-sets-041.md#c-6ac65320fe7dc72c) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-031534

```text
(config)# do-exec undebug cft memory <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 1 `；EOL ` RVA 0x358FF168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4768fa796ff21f35](../../evidence/conditions-sets-028.md#c-4768fa796ff21f35) · [状态效果 S-8e7c7ff71af9e725](../../evidence/state_effects-sets-030.md#s-8e7c7ff71af9e725)

### path-027693

```text
(config)# do-exec undebug chat <cr>
```

Handler ` RVA 0xF2F58D0 `；selector ` 0 `；EOL ` RVA 0x346038B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-6f8e1d8dc9477a2e](../../evidence/state_effects-sets-024.md#s-6f8e1d8dc9477a2e)

### path-029697

```text
(config)# do-exec undebug checkpoint timers <cr>
```

Handler ` RVA 0xCDBA680 `；selector ` 0 `；EOL ` RVA 0x33CECC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-44fec8ec8181353f](../../evidence/state_effects-sets-015.md#s-44fec8ec8181353f)

### path-032439

```text
(config)# do-exec undebug clns cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x34B6DC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-040974

```text
(config)# do-exec undebug clns esis events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x34B6C768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-041017

```text
(config)# do-exec undebug clns esis packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x34B6CA10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032334

```text
(config)# do-exec undebug clns events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34B6CCA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032423

```text
(config)# do-exec undebug clns filters <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x34B6D9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032386

```text
(config)# do-exec undebug clns igrp-adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34B6D4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032350

```text
(config)# do-exec undebug clns igrp-events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34B6CF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032371

```text
(config)# do-exec undebug clns igrp-packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34B6D1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032406

```text
(config)# do-exec undebug clns packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34B6D748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032461

```text
(config)# do-exec undebug clns routing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34B6DF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-15d2f381568a44a6](../../evidence/state_effects-sets-005.md#s-15d2f381568a44a6)

### path-032415

```text
(config)# do-exec undebug cls errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x354C1F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032490

```text
(config)# do-exec undebug cls flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x354C29D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032511

```text
(config)# do-exec undebug cls hpr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x354C2C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032432

```text
(config)# do-exec undebug cls messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x354C21D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032454

```text
(config)# do-exec undebug cls sdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x354C2480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032398

```text
(config)# do-exec undebug cls state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x354C1C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-032473

```text
(config)# do-exec undebug cls vdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x354C2728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8a4a7fae40d936a7](../../evidence/state_effects-sets-029.md#s-8a4a7fae40d936a7)

### path-033489

```text
(config)# do-exec undebug cns aaa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x340E7338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d05c9ba586719651](../../evidence/conditions-sets-080.md#c-d05c9ba586719651) · [状态效果 S-6bc6e8fece1aa3a2](../../evidence/state_effects-sets-023.md#s-6bc6e8fece1aa3a2)

### path-033537

```text
(config)# do-exec undebug cns all <cr>
```

Handler ` RVA 0xDFA8FB0 `；selector ` 0 `；EOL ` RVA 0x340E8680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d05c9ba586719651](../../evidence/conditions-sets-080.md#c-d05c9ba586719651) · [状态效果 S-5784d45d0dd132de](../../evidence/state_effects-sets-019.md#s-5784d45d0dd132de)

### path-033446

```text
(config)# do-exec undebug cns config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460F7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1ac6ab178203f4d2](../../evidence/state_effects-sets-006.md#s-1ac6ab178203f4d2)

### path-043118

```text
(config)# do-exec undebug cns config all <cr>
```

Handler ` RVA 0xF314C20 `；selector ` 0 `；EOL ` RVA 0x3460F518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-043058

```text
(config)# do-exec undebug cns config apply <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3460ED20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-043077

```text
(config)# do-exec undebug cns config decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3460EFC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-043034

```text
(config)# do-exec undebug cns config initial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3460EA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-042978

```text
(config)# do-exec undebug cns config interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x3460E528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-043099

```text
(config)# do-exec undebug cns config messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x3460F270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-051663

```text
(config)# do-exec undebug cns config notify all <cr>
```

Handler ` RVA 0xF32E760 `；selector ` 0 `；EOL ` RVA 0x34611C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051593

```text
(config)# do-exec undebug cns config notify eventing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34610C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051651

```text
(config)# do-exec undebug cns config notify expand <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34611978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051618

```text
(config)# do-exec undebug cns config notify generation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34611180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051641

```text
(config)# do-exec undebug cns config notify modes <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x346116D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051605

```text
(config)# do-exec undebug cns config notify nvgen <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34610ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-051630

```text
(config)# do-exec undebug cns config notify xml <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34611428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-b31ed14c8fc38028](../../evidence/state_effects-sets-038.md#s-b31ed14c8fc38028)

### path-043006

```text
(config)# do-exec undebug cns config partial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3460E7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-042950

```text
(config)# do-exec undebug cns config retrieve <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460E280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-74892d3bb56ba374](../../evidence/state_effects-sets-025.md#s-74892d3bb56ba374)

### path-042955

```text
(config)# do-exec undebug cns event agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34617F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-91fa9663c36656bb](../../evidence/state_effects-sets-031.md#s-91fa9663c36656bb)

### path-043009

```text
(config)# do-exec undebug cns event all <cr>
```

Handler ` RVA 0xF35D580 `；selector ` 0 `；EOL ` RVA 0x346184C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-91fa9663c36656bb](../../evidence/state_effects-sets-031.md#s-91fa9663c36656bb)

### path-042928

```text
(config)# do-exec undebug cns event connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34617CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-91fa9663c36656bb](../../evidence/state_effects-sets-031.md#s-91fa9663c36656bb)

### path-042982

```text
(config)# do-exec undebug cns event subscriber <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34618220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-91fa9663c36656bb](../../evidence/state_effects-sets-031.md#s-91fa9663c36656bb)

### path-042975

```text
(config)# do-exec undebug cns exec agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346198D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-76ac35bbe0fca8a2](../../evidence/state_effects-sets-025.md#s-76ac35bbe0fca8a2)

### path-043056

```text
(config)# do-exec undebug cns exec all <cr>
```

Handler ` RVA 0xF369750 `；selector ` 0 `；EOL ` RVA 0x3461A0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-76ac35bbe0fca8a2](../../evidence/state_effects-sets-025.md#s-76ac35bbe0fca8a2)

### path-043032

```text
(config)# do-exec undebug cns exec decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34619E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-76ac35bbe0fca8a2](../../evidence/state_effects-sets-025.md#s-76ac35bbe0fca8a2)

### path-043004

```text
(config)# do-exec undebug cns exec messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34619B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-76ac35bbe0fca8a2](../../evidence/state_effects-sets-025.md#s-76ac35bbe0fca8a2)

### path-033503

```text
(config)# do-exec undebug cns format <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x340E75F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d05c9ba586719651](../../evidence/conditions-sets-080.md#c-d05c9ba586719651) · [状态效果 S-4d12d5fe5c028a23](../../evidence/state_effects-sets-017.md#s-4d12d5fe5c028a23)

### path-033479

```text
(config)# do-exec undebug cns framework <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x340E7080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d05c9ba586719651](../../evidence/conditions-sets-080.md#c-d05c9ba586719651) · [状态效果 S-a47e91d1d9352a18](../../evidence/state_effects-sets-035.md#s-a47e91d1d9352a18)

### path-033516

```text
(config)# do-exec undebug cns http <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x340E78A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d05c9ba586719651](../../evidence/conditions-sets-080.md#c-d05c9ba586719651) · [状态效果 S-5201d333a4116e35](../../evidence/state_effects-sets-018.md#s-5201d333a4116e35)

### path-043029

```text
(config)# do-exec undebug cns image agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3461CC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c57c99bb95113dc3](../../evidence/state_effects-sets-042.md#s-c57c99bb95113dc3)

### path-043075

```text
(config)# do-exec undebug cns image all <cr>
```

Handler ` RVA 0xF36F680 `；selector ` 0 `；EOL ` RVA 0x3461D1C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c57c99bb95113dc3](../../evidence/state_effects-sets-042.md#s-c57c99bb95113dc3)

### path-043000

```text
(config)# do-exec undebug cns image connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3461C9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c57c99bb95113dc3](../../evidence/state_effects-sets-042.md#s-c57c99bb95113dc3)

### path-043054

```text
(config)# do-exec undebug cns image error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3461CF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-c57c99bb95113dc3](../../evidence/state_effects-sets-042.md#s-c57c99bb95113dc3)

