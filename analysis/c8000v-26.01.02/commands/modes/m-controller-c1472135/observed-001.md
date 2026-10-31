# controller · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-004318

```text
(config-controller)# ais-core-failure <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 31 `；EOL ` RVA 0x35EE5588 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-636f78bcace5cbc8](../../evidence/conditions-sets-039.md#c-636f78bcace5cbc8)

### observed_connections-004321

```text
(config-controller)# ais-core-failure <cr>
```

Handler ` RVA 0x16144750 `；selector ` 129 `；EOL ` RVA 0x35EF1C50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ad0b8092f8973f4](../../evidence/conditions-sets-010.md#c-1ad0b8092f8973f4)

### observed_connections-004317

```text
(config-controller)# ais-shut <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 29 `；EOL ` RVA 0x35EE52A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da59e6784203a6cf](../../evidence/conditions-sets-084.md#c-da59e6784203a6cf)

### observed_connections-004319

```text
(config-controller)# ais-shut <cr>
```

Handler ` RVA 0x16144750 `；selector ` 127 `；EOL ` RVA 0x35EF1968 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c2fd523ac70f579](../../evidence/conditions-sets-011.md#c-1c2fd523ac70f579)

### observed_connections-004546

```text
(config-controller)# alarm-trigger blue <number:0..23> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 120 `；EOL ` RVA 0x378E0D90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of ds0-groups which needed to be triggered。

[条件 C-858d853d8765146a](../../evidence/conditions-sets-052.md#c-858d853d8765146a) · [缺口 G-a545d56b84456547](../../evidence/gaps-sets-006.md#g-a545d56b84456547) · [参数 P-4110b0131776e38a](../../evidence/parameters-sets-005.md#p-4110b0131776e38a) · [状态效果 S-5dbd9e0566162455](../../evidence/state_effects-sets-020.md#s-5dbd9e0566162455)

### observed_connections-004549

```text
(config-controller)# alarm-trigger blue <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 20 `；EOL ` RVA 0x378DCA88 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of ds0-groups which needed to be triggered。

[条件 C-7abe265aeb194d6f](../../evidence/conditions-sets-048.md#c-7abe265aeb194d6f) · [缺口 G-0d745c9fbe510bde](../../evidence/gaps-sets-001.md#g-0d745c9fbe510bde) · [参数 P-6eb1181e83a04ba6](../../evidence/parameters-sets-009.md#p-6eb1181e83a04ba6) · [状态效果 S-0e8bffba720f94c3](../../evidence/state_effects-sets-003.md#s-0e8bffba720f94c3)

### observed_connections-004335

```text
(config-controller)# atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EFA8B8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01c0e98410a8c994](../../evidence/conditions-sets-001.md#c-01c0e98410a8c994)

### observed_connections-004337

```text
(config-controller)# atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EEEF20 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d60cdf224c26dc7](../../evidence/conditions-sets-024.md#c-3d60cdf224c26dc7)

### observed_connections-004471

```text
(config-controller)# attach profile <string> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 4 `；EOL ` RVA 0x35EE6710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-a6735121ef5783a3](../../evidence/conditions-sets-064.md#c-a6735121ef5783a3) · [参数 P-ddd1d2c1f78ae7df](../../evidence/parameters-sets-017.md#p-ddd1d2c1f78ae7df)

### observed_connections-004474

```text
(config-controller)# attach profile <string> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 102 `；EOL ` RVA 0x35EF2E38 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-17dd5fcc7139be00](../../evidence/conditions-sets-009.md#c-17dd5fcc7139be00) · [参数 P-47af0e22bac05b2a](../../evidence/parameters-sets-006.md#p-47af0e22bac05b2a)

### observed_connections-004452

```text
(config-controller)# bert errors <cr>
```

Handler ` RVA 0x16144750 `；selector ` 124 `；EOL ` RVA 0x35EF98A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4d5856133c61593](../../evidence/conditions-sets-076.md#c-c4d5856133c61593) · [状态效果 S-1990f793c9177c64](../../evidence/state_effects-sets-006.md#s-1990f793c9177c64)

### observed_connections-004456

```text
(config-controller)# bert errors <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 26 `；EOL ` RVA 0x35EEE978 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-68b9a41cea803a94](../../evidence/conditions-sets-041.md#c-68b9a41cea803a94) · [状态效果 S-5677b28f08e6bf05](../../evidence/state_effects-sets-019.md#s-5677b28f08e6bf05)

### observed_connections-004564

```text
(config-controller)# bert pattern <?option@55558b441cb0> interval <number:1..14400> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 15 `；EOL ` RVA 0x35EEDB78 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Duration of BERT &lt;1-14400&gt; minutes。

[条件 C-358a69d69f7f4719](../../evidence/conditions-sets-021.md#c-358a69d69f7f4719) · [缺口 G-7725262d1eaa08fd](../../evidence/gaps-sets-005.md#g-7725262d1eaa08fd) · [参数 P-f2c767b1bb846dea](../../evidence/parameters-sets-018.md#p-f2c767b1bb846dea) · [状态效果 S-7dd5e437e89e1282](../../evidence/state_effects-sets-027.md#s-7dd5e437e89e1282)

### observed_connections-004563

```text
(config-controller)# bert pattern <?option@55558b44cc20> interval <number:1..14400> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 109 `；EOL ` RVA 0x35EF8AE8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Duration of BERT &lt;1-14400&gt; minutes。

[条件 C-bef5c18fd3048e59](../../evidence/conditions-sets-074.md#c-bef5c18fd3048e59) · [缺口 G-ccd2ed3e095614a6](../../evidence/gaps-sets-007.md#g-ccd2ed3e095614a6) · [参数 P-2aa886d22fb8647f](../../evidence/parameters-sets-004.md#p-2aa886d22fb8647f) · [状态效果 S-c0aefae42e7ce780](../../evidence/state_effects-sets-041.md#s-c0aefae42e7ce780)

### observed_connections-004328

```text
(config-controller)# bitswap <cr>
```

Handler ` RVA 0x1243D6A0 `；selector ` 0 `；EOL ` RVA 0x3586EEB0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9269b65ddbfa60ae](../../evidence/conditions-sets-056.md#c-9269b65ddbfa60ae)

### observed_connections-004489

```text
(config-controller)# cablelength short 550ft <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 7 `；EOL ` RVA 0x35EE7C98 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be4212fb0a9f4a69](../../evidence/conditions-sets-073.md#c-be4212fb0a9f4a69) · [状态效果 S-bd2e524ee7c92bcb](../../evidence/state_effects-sets-040.md#s-bd2e524ee7c92bcb)

### observed_connections-004545

```text
(config-controller)# cablelength short <?option@55558b43bc20> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 7 `；EOL ` RVA 0x35EE7C98 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6906e758d1e0afca](../../evidence/conditions-sets-041.md#c-6906e758d1e0afca) · [缺口 G-1aabec413a3f120e](../../evidence/gaps-sets-001.md#g-1aabec413a3f120e) · [状态效果 S-34555d179539d65a](../../evidence/state_effects-sets-012.md#s-34555d179539d65a)

### observed_connections-004325

```text
(config-controller)# cas <cr>
```

Handler ` RVA 0x16144750 `；selector ` 128 `；EOL ` RVA 0x35EF2710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1948456dcffdcd3c](../../evidence/conditions-sets-010.md#c-1948456dcffdcd3c)

### observed_connections-004455

```text
(config-controller)# cas-custom <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 21 `；EOL ` RVA 0x378DE5D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-2367ea5a778c5e78](../../evidence/conditions-sets-014.md#c-2367ea5a778c5e78) · [参数 P-82d8522f5b1fba13](../../evidence/parameters-sets-010.md#p-82d8522f5b1fba13)

### observed_connections-004441

```text
(config-controller)# cas-custom <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 115 `；EOL ` RVA 0x378E33F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-db0a8589aa4a7dac](../../evidence/conditions-sets-084.md#c-db0a8589aa4a7dac) · [参数 P-9c3dcfa7df47f226](../../evidence/parameters-sets-012.md#p-9c3dcfa7df47f226)

### observed_connections-004569

```text
(config-controller)# cas-group <number:0..23> timeslots <number:1..24> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DB760 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Channel number；` unsigned_number ` List of timeslots which comprise the cas-group。

[条件 C-303c4ef1a5f5e202](../../evidence/conditions-sets-019.md#c-303c4ef1a5f5e202) · [缺口 G-5d1e79b29365d8cc](../../evidence/gaps-sets-004.md#g-5d1e79b29365d8cc) · [参数 P-67176de5bf674d46](../../evidence/parameters-sets-008.md#p-67176de5bf674d46) · [状态效果 S-b5aa38aab8e97349](../../evidence/state_effects-sets-038.md#s-b5aa38aab8e97349)

### observed_connections-004567

```text
(config-controller)# cas-group <number:0..30> timeslots <number:1..31> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378E18B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Channel number；` unsigned_number ` List of timeslots which comprise the cas-group。

[条件 C-226818b6c8e6ee58](../../evidence/conditions-sets-013.md#c-226818b6c8e6ee58) · [缺口 G-26581e15d473d508](../../evidence/gaps-sets-002.md#g-26581e15d473d508) · [参数 P-e21a485f83fbc7f2](../../evidence/parameters-sets-017.md#p-e21a485f83fbc7f2) · [状态效果 S-5e280e567e44195c](../../evidence/state_effects-sets-020.md#s-5e280e567e44195c)

### observed_connections-004543

```text
(config-controller)# channel-group <number:dynamic> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 8 `；EOL ` RVA 0x35EE87E0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel number。

[条件 C-dc2c7abba4a1c9b3](../../evidence/conditions-sets-085.md#c-dc2c7abba4a1c9b3) · [缺口 G-d22cd93968d6d19f](../../evidence/gaps-sets-007.md#g-d22cd93968d6d19f) · [参数 P-151edb1536bb29d5](../../evidence/parameters-sets-002.md#p-151edb1536bb29d5) · [状态效果 S-fd28b5166f19b7a2](../../evidence/state_effects-sets-054.md#s-fd28b5166f19b7a2)

### observed_connections-004544

```text
(config-controller)# channel-group <number:dynamic> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 107 `；EOL ` RVA 0x35EF53D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel number。

[条件 C-13517ce0ed972e06](../../evidence/conditions-sets-008.md#c-13517ce0ed972e06) · [缺口 G-2e4117a55d280365](../../evidence/gaps-sets-002.md#g-2e4117a55d280365) · [参数 P-b2d157b745ba263f](../../evidence/parameters-sets-014.md#p-b2d157b745ba263f) · [状态效果 S-901c164bedd160c5](../../evidence/state_effects-sets-031.md#s-901c164bedd160c5)

### observed_connections-004485

```text
(config-controller)# clock source internal <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 5 `；EOL ` RVA 0x35EEFE70 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9cf5bb6e75c3f93b](../../evidence/conditions-sets-061.md#c-9cf5bb6e75c3f93b) · [状态效果 S-fee8417b3bdf4661](../../evidence/state_effects-sets-054.md#s-fee8417b3bdf4661)

### observed_connections-004487

```text
(config-controller)# clock source internal <cr>
```

Handler ` RVA 0x16144750 `；selector ` 106 `；EOL ` RVA 0x35EFB408 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65f4fa06367c7dba](../../evidence/conditions-sets-039.md#c-65f4fa06367c7dba) · [状态效果 S-c30a131ec4bd6f7d](../../evidence/state_effects-sets-041.md#s-c30a131ec4bd6f7d)

### observed_connections-004555

```text
(config-controller)# clock source recovered <number:dynamic> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 5 `；EOL ` RVA 0x35EEFE70 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Choose Clock ID &lt;0-X&gt;。

[条件 C-80dc69f478583802](../../evidence/conditions-sets-050.md#c-80dc69f478583802) · [缺口 G-ad6a10f64c82b145](../../evidence/gaps-sets-006.md#g-ad6a10f64c82b145) · [参数 P-243df10cccbb9318](../../evidence/parameters-sets-003.md#p-243df10cccbb9318) · [状态效果 S-3601c4364d9cf4f2](../../evidence/state_effects-sets-012.md#s-3601c4364d9cf4f2)

### observed_connections-004556

```text
(config-controller)# clock source recovered <number:dynamic> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 106 `；EOL ` RVA 0x35EFB408 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` choose a clock ID &lt;0-X&gt;。

[条件 C-475b74fd258abdb7](../../evidence/conditions-sets-028.md#c-475b74fd258abdb7) · [缺口 G-1fedde6295bc6150](../../evidence/gaps-sets-002.md#g-1fedde6295bc6150) · [参数 P-241278314104845c](../../evidence/parameters-sets-003.md#p-241278314104845c) · [状态效果 S-0bd55250493ff54b](../../evidence/state_effects-sets-003.md#s-0bd55250493ff54b)

### observed_connections-004422

```text
(config-controller)# compand a-law <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 13 `；EOL ` RVA 0x35EEB4F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b61a8df1eb377b86](../../evidence/conditions-sets-070.md#c-b61a8df1eb377b86)

### observed_connections-004322

```text
(config-controller)# debug-state-change <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 32 `；EOL ` RVA 0x35EE5FA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4c0805c72ec7c22](../../evidence/conditions-sets-082.md#c-d4c0805c72ec7c22)

### observed_connections-004345

```text
(config-controller)# default ais-core-failure <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 31 `；EOL ` RVA 0x35EE5588 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e88748eb8bd8b81d](../../evidence/conditions-sets-090.md#c-e88748eb8bd8b81d) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004353

```text
(config-controller)# default ais-core-failure <cr>
```

Handler ` RVA 0x16144750 `；selector ` 129 `；EOL ` RVA 0x35EF1C50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf02022253074a69](../../evidence/conditions-sets-080.md#c-cf02022253074a69) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004340

```text
(config-controller)# default ais-shut <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 29 `；EOL ` RVA 0x35EE52A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3016429c41dbc18d](../../evidence/conditions-sets-019.md#c-3016429c41dbc18d) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004346

```text
(config-controller)# default ais-shut <cr>
```

Handler ` RVA 0x16144750 `；selector ` 127 `；EOL ` RVA 0x35EF1968 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4edbf22ffba8230f](../../evidence/conditions-sets-031.md#c-4edbf22ffba8230f) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004439

```text
(config-controller)# default alarm-trigger <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 120 `；EOL ` RVA 0x378E0D90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-991679973daf7e04](../../evidence/conditions-sets-059.md#c-991679973daf7e04) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004453

```text
(config-controller)# default alarm-trigger <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 20 `；EOL ` RVA 0x378DCA88 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-44308c5c4848d554](../../evidence/conditions-sets-027.md#c-44308c5c4848d554) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004443

```text
(config-controller)# default atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EFA8B8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-da12ed887acd775f](../../evidence/conditions-sets-084.md#c-da12ed887acd775f) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004451

```text
(config-controller)# default atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EEEF20 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05a10bd6deb407ec](../../evidence/conditions-sets-003.md#c-05a10bd6deb407ec) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004532

```text
(config-controller)# default attach profile <string> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 4 `；EOL ` RVA 0x35EE6710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-f980853d81713e6b](../../evidence/conditions-sets-096.md#c-f980853d81713e6b) · [参数 P-ddd1d2c1f78ae7df](../../evidence/parameters-sets-017.md#p-ddd1d2c1f78ae7df) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004535

```text
(config-controller)# default attach profile <string> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 102 `；EOL ` RVA 0x35EF2E38 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-eb5afbbe6724c3c1](../../evidence/conditions-sets-091.md#c-eb5afbbe6724c3c1) · [参数 P-47af0e22bac05b2a](../../evidence/parameters-sets-006.md#p-47af0e22bac05b2a) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004431

```text
(config-controller)# default bert <cr>
```

Handler ` RVA 0x16144750 `；selector ` 109 `；EOL ` RVA 0x35EF8AE8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-714387ee9012a11e](../../evidence/conditions-sets-044.md#c-714387ee9012a11e) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004444

```text
(config-controller)# default bert <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 15 `；EOL ` RVA 0x35EEDB78 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b69b0b92553d9f7c](../../evidence/conditions-sets-071.md#c-b69b0b92553d9f7c) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004399

```text
(config-controller)# default bitswap <cr>
```

Handler ` RVA 0x1243D6A0 `；selector ` 0 `；EOL ` RVA 0x3586EEB0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0ef8391a0e674e6c](../../evidence/conditions-sets-006.md#c-0ef8391a0e674e6c) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004537

```text
(config-controller)# default cablelength short 550ft <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 7 `；EOL ` RVA 0x35EE7C98 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87c5b081f9659b25](../../evidence/conditions-sets-053.md#c-87c5b081f9659b25) · [状态效果 S-b585d232f6ad668b](../../evidence/state_effects-sets-038.md#s-b585d232f6ad668b)

### observed_connections-004371

```text
(config-controller)# default cas <cr>
```

Handler ` RVA 0x16144750 `；selector ` 128 `；EOL ` RVA 0x35EF2710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d7071394594c166](../../evidence/conditions-sets-005.md#c-0d7071394594c166) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004523

```text
(config-controller)# default cas-custom <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 21 `；EOL ` RVA 0x378DE5D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-e62576d5914e0586](../../evidence/conditions-sets-089.md#c-e62576d5914e0586) · [参数 P-82d8522f5b1fba13](../../evidence/parameters-sets-010.md#p-82d8522f5b1fba13) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004513

```text
(config-controller)# default cas-custom <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 115 `；EOL ` RVA 0x378E33F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-d5147f654a248436](../../evidence/conditions-sets-082.md#c-d5147f654a248436) · [参数 P-9c3dcfa7df47f226](../../evidence/parameters-sets-012.md#p-9c3dcfa7df47f226) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004521

```text
(config-controller)# default cas-group <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DB760 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-ac75a04427342a01](../../evidence/conditions-sets-067.md#c-ac75a04427342a01) · [参数 P-ff6a65ee5de4a5f9](../../evidence/parameters-sets-019.md#p-ff6a65ee5de4a5f9) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004510

```text
(config-controller)# default cas-group <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378E18B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-2d2924d0252d4900](../../evidence/conditions-sets-018.md#c-2d2924d0252d4900) · [参数 P-d8d70c5e33d1ab95](../../evidence/parameters-sets-016.md#p-d8d70c5e33d1ab95) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004488

```text
(config-controller)# default clock source <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 5 `；EOL ` RVA 0x35EEFE70 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7735de73e07db6ee](../../evidence/conditions-sets-046.md#c-7735de73e07db6ee) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004490

```text
(config-controller)# default clock source <cr>
```

Handler ` RVA 0x16144750 `；selector ` 106 `；EOL ` RVA 0x35EFB408 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce9916a45ce7927c](../../evidence/conditions-sets-080.md#c-ce9916a45ce7927c) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004425

```text
(config-controller)# default compand <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 13 `；EOL ` RVA 0x35EEB4F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66e0d55b4eaea5fe](../../evidence/conditions-sets-040.md#c-66e0d55b4eaea5fe) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004357

```text
(config-controller)# default debug-state-change <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 32 `；EOL ` RVA 0x35EE5FA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f41dfb76e6b3df3](../../evidence/conditions-sets-049.md#c-7f41dfb76e6b3df3) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004349

```text
(config-controller)# default description <cr>
```

Handler ` RVA 0xECFF8D0 `；selector ` 0 `；EOL ` RVA 0x35EF16A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c922f4e9b61aaa77](../../evidence/conditions-sets-077.md#c-c922f4e9b61aaa77) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004423

```text
(config-controller)# default detect <cr>
```

Handler ` RVA 0x16144750 `；selector ` 118 `；EOL ` RVA 0x35EF7320 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e213b83c1aafc70](../../evidence/conditions-sets-006.md#c-0e213b83c1aafc70) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004429

```text
(config-controller)# default detect <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 18 `；EOL ` RVA 0x35EEB890 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-979bf9928589ff81](../../evidence/conditions-sets-059.md#c-979bf9928589ff81) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004383

```text
(config-controller)# default diagnostics <cr>
```

Handler ` RVA 0x1243ED90 `；selector ` 0 `；EOL ` RVA 0x3586E148 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-890c09e15f96b4ff](../../evidence/conditions-sets-053.md#c-890c09e15f96b4ff) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004509

```text
(config-controller)# default ds0-group <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DA330 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Group Number。

[条件 C-4d25bfe4173b4126](../../evidence/conditions-sets-030.md#c-4d25bfe4173b4126) · [参数 P-5aa4943895e5d8af](../../evidence/parameters-sets-007.md#p-5aa4943895e5d8af) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004498

```text
(config-controller)# default ds0-group <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378DE9E0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-d420dd8a2225f4c2](../../evidence/conditions-sets-082.md#c-d420dd8a2225f4c2) · [参数 P-42aac2c29d87f8bf](../../evidence/parameters-sets-006.md#p-42aac2c29d87f8bf) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004482

```text
(config-controller)# default dsl-group auto <cr>
```

Handler ` RVA 0x163D0F00 `；selector ` 1 `；EOL ` RVA 0x35F82518 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c5632c0c9f90d8cf](../../evidence/conditions-sets-076.md#c-c5632c0c9f90d8cf) · [状态效果 S-79346c9cce4892b3](../../evidence/state_effects-sets-026.md#s-79346c9cce4892b3)

### observed_connections-004397

```text
(config-controller)# default fdl <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 14 `；EOL ` RVA 0x35EF07A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b4bb8a67d8c0e5bf](../../evidence/conditions-sets-070.md#c-b4bb8a67d8c0e5bf) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004461

```text
(config-controller)# default firmware phy <cr>
```

Handler ` RVA 0x163CFA90 `；selector ` 0 `；EOL ` RVA 0x35F818E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5d00cd9c6644d3b](../../evidence/conditions-sets-095.md#c-f5d00cd9c6644d3b) · [状态效果 S-35578735af2a144d](../../evidence/state_effects-sets-012.md#s-35578735af2a144d)

### observed_connections-004534

```text
(config-controller)# default firmware phy filename <cr>
```

Handler ` RVA 0x1243EF20 `；selector ` 0 `；EOL ` RVA 0x3586D510 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b9fb88b9472ccd05](../../evidence/conditions-sets-072.md#c-b9fb88b9472ccd05) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004514

```text
(config-controller)# default forward-alarm ais <cr>
```

Handler ` RVA 0x16144750 `；selector ` 125 `；EOL ` RVA 0x35EFAC40 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c02ec290843daa5](../../evidence/conditions-sets-048.md#c-7c02ec290843daa5) · [状态效果 S-62d982072fdb95e2](../../evidence/state_effects-sets-021.md#s-62d982072fdb95e2)

### observed_connections-004517

```text
(config-controller)# default forward-alarm ais <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 27 `；EOL ` RVA 0x35EEF2A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98747ad78dd3d87c](../../evidence/conditions-sets-059.md#c-98747ad78dd3d87c) · [状态效果 S-3b94f4d318abfbe1](../../evidence/state_effects-sets-013.md#s-3b94f4d318abfbe1)

### observed_connections-004432

```text
(config-controller)# default forward-alarms <cr>
```

Handler ` RVA 0x16144750 `；selector ` 119 `；EOL ` RVA 0x35EF87B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25dd27ab5618092c](../../evidence/conditions-sets-015.md#c-25dd27ab5618092c) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004445

```text
(config-controller)# default forward-alarms <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 19 `；EOL ` RVA 0x35EED840 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf43f4f332dcc991](../../evidence/conditions-sets-080.md#c-cf43f4f332dcc991) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004375

```text
(config-controller)# default framing <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 3 `；EOL ` RVA 0x35EE7060 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ef3a56901be2a58](../../evidence/conditions-sets-061.md#c-9ef3a56901be2a58) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004387

```text
(config-controller)# default framing <cr>
```

Handler ` RVA 0x16144750 `；selector ` 104 `；EOL ` RVA 0x35EF3788 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0832eb84d6b1c209](../../evidence/conditions-sets-004.md#c-0832eb84d6b1c209) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004370

```text
(config-controller)# default interface-default-mtu <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 2 `；EOL ` RVA 0x35EE6358 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e659e952492a4509](../../evidence/conditions-sets-089.md#c-e659e952492a4509) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004382

```text
(config-controller)# default interface-default-mtu <cr>
```

Handler ` RVA 0x16144750 `；selector ` 101 `；EOL ` RVA 0x35EF2A80 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2b55d08331262fca](../../evidence/conditions-sets-017.md#c-2b55d08331262fca) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004469

```text
(config-controller)# default line-mode bonding <cr>
```

Handler ` RVA 0x12443B00 `；selector ` 0 `；EOL ` RVA 0x3586CB60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c0ecd63054da5e5](../../evidence/conditions-sets-005.md#c-0c0ecd63054da5e5) · [状态效果 S-05b29d92302ce611](../../evidence/state_effects-sets-002.md#s-05b29d92302ce611)

### observed_connections-004410

```text
(config-controller)# default line-termination <cr>
```

Handler ` RVA 0x16144750 `；selector ` 114 `；EOL ` RVA 0x35EF4F58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6dac15749ed3b80f](../../evidence/conditions-sets-042.md#c-6dac15749ed3b80f) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004405

```text
(config-controller)# default linecode <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 6 `；EOL ` RVA 0x35EEFA60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-749edaae0875507b](../../evidence/conditions-sets-045.md#c-749edaae0875507b) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004406

```text
(config-controller)# default linecode <cr>
```

Handler ` RVA 0x16144750 `；selector ` 105 `；EOL ` RVA 0x35EF4B58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cbb9d0918cd416c3](../../evidence/conditions-sets-078.md#c-cbb9d0918cd416c3) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004446

```text
(config-controller)# default linestate <cr>
```

Handler ` RVA 0x16144750 `；selector ` 122 `；EOL ` RVA 0x35EFA560 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8340887383f92a17](../../evidence/conditions-sets-051.md#c-8340887383f92a17) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004419

```text
(config-controller)# default logging-events <cr>
```

Handler ` RVA 0x16144750 `；selector ` 123 `；EOL ` RVA 0x35EF6BC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5cc852c2e3a8b28](../../evidence/conditions-sets-095.md#c-f5cc852c2e3a8b28) · [状态效果 S-a2a46cc7ae67d14a](../../evidence/state_effects-sets-034.md#s-a2a46cc7ae67d14a)

### observed_connections-004426

```text
(config-controller)# default logging-events <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 25 `；EOL ` RVA 0x35EEB108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3b3d2578c24589](../../evidence/conditions-sets-084.md#c-db3b3d2578c24589) · [状态效果 S-a86bcdd4300a4c65](../../evidence/state_effects-sets-036.md#s-a86bcdd4300a4c65)

### observed_connections-004417

```text
(config-controller)# default loopback <cr>
```

Handler ` RVA 0x16144750 `；selector ` 108 `；EOL ` RVA 0x35EF6020 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-098eb4209615ab4e](../../evidence/conditions-sets-004.md#c-098eb4209615ab4e) · [状态效果 S-d87f6bba98936273](../../evidence/state_effects-sets-046.md#s-d87f6bba98936273)

### observed_connections-004421

```text
(config-controller)# default loopback <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 9 `；EOL ` RVA 0x35EE96F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9287ac3074d0b6a1](../../evidence/conditions-sets-057.md#c-9287ac3074d0b6a1) · [状态效果 S-646be3dde5a00ab8](../../evidence/state_effects-sets-021.md#s-646be3dde5a00ab8)

### observed_connections-004364

```text
(config-controller)# default mode <cr>
```

Handler ` RVA 0x163CEBA0 `；selector ` 0 `；EOL ` RVA 0x35F82110 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7e02985b68045e8](../../evidence/conditions-sets-096.md#c-f7e02985b68045e8) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004475

```text
(config-controller)# default modem <string> <cr>
```

Handler ` RVA 0x1243E380 `；selector ` 0 `；EOL ` RVA 0x3586E480 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` command line string。

[条件 C-c9fd5a6a01c5b4fc](../../evidence/conditions-sets-078.md#c-c9fd5a6a01c5b4fc) · [参数 P-60c5f3f749e58c14](../../evidence/parameters-sets-008.md#p-60c5f3f749e58c14) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004525

```text
(config-controller)# default national reserve <cr>
```

Handler ` RVA 0x16144750 `；selector ` 110 `；EOL ` RVA 0x35EFA058 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1bc87305226a389](../../evidence/conditions-sets-075.md#c-c1bc87305226a389) · [状态效果 S-8a09306497d7ba55](../../evidence/state_effects-sets-029.md#s-8a09306497d7ba55)

### observed_connections-004467

```text
(config-controller)# default operating mode <cr>
```

Handler ` RVA 0x1243CAE0 `；selector ` 0 `；EOL ` RVA 0x3586BFF0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eef1a2450a976622](../../evidence/conditions-sets-092.md#c-eef1a2450a976622) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004454

```text
(config-controller)# default pri-group <cr>
```

Handler ` RVA 0x16144750 `；selector ` 113 `；EOL ` RVA 0x35EF7AC0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ede4fc3ce12012e](../../evidence/conditions-sets-055.md#c-8ede4fc3ce12012e) · [状态效果 S-e4a6d5bdf75a3a68](../../evidence/state_effects-sets-048.md#s-e4a6d5bdf75a3a68)

### observed_connections-004409

```text
(config-controller)# default rem-loop-detect-disable <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 35 `；EOL ` RVA 0x35EE9108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be55ab1ada3000ac](../../evidence/conditions-sets-073.md#c-be55ab1ada3000ac) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004512

```text
(config-controller)# default scrambling cell-payload <cr>
```

Handler ` RVA 0x16144750 `；selector ` 126 `；EOL ` RVA 0x35EFAFC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a81b9a8be14d185d](../../evidence/conditions-sets-065.md#c-a81b9a8be14d185d) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004516

```text
(config-controller)# default scrambling cell-payload <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 28 `；EOL ` RVA 0x35EEF630 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e1ef65672a1090eb](../../evidence/conditions-sets-087.md#c-e1ef65672a1090eb) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004480

```text
(config-controller)# default secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 33 `；EOL ` RVA 0x35EE6BD0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11dfd529cfc0f82c](../../evidence/conditions-sets-007.md#c-11dfd529cfc0f82c) · [状态效果 S-8d1b6ada5e5aed4e](../../evidence/state_effects-sets-030.md#s-8d1b6ada5e5aed4e)

### observed_connections-004483

```text
(config-controller)# default secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x16144750 `；selector ` 130 `；EOL ` RVA 0x35EF32F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e20655dd103d1aa2](../../evidence/conditions-sets-087.md#c-e20655dd103d1aa2) · [状态效果 S-2cef195eda3b9bfd](../../evidence/state_effects-sets-010.md#s-2cef195eda3b9bfd)

### observed_connections-004386

```text
(config-controller)# default service-type <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 23 `；EOL ` RVA 0x35EE7628 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f9d7151f04ccf8cb](../../evidence/conditions-sets-096.md#c-f9d7151f04ccf8cb) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004398

```text
(config-controller)# default service-type <cr>
```

Handler ` RVA 0x16144750 `；selector ` 121 `；EOL ` RVA 0x35EF3CD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-137512c8ce82c9e4](../../evidence/conditions-sets-008.md#c-137512c8ce82c9e4) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004352

```text
(config-controller)# default shutdown <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 1 `；EOL ` RVA 0x35EE5D00 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f41dfb76e6b3df3](../../evidence/conditions-sets-049.md#c-7f41dfb76e6b3df3) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004361

```text
(config-controller)# default shutdown <cr>
```

Handler ` RVA 0x16144750 `；selector ` 103 `；EOL ` RVA 0x35EF23C8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a079454017368a4](../../evidence/conditions-sets-029.md#c-4a079454017368a4) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004388

```text
(config-controller)# default shutdown <cr>
```

Handler ` RVA 0x1243E150 `；selector ` 0 `；EOL ` RVA 0x3586E7A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65a8c7dc0f19d20e](../../evidence/conditions-sets-039.md#c-65a8c7dc0f19d20e) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004527

```text
(config-controller)# default snmp trap link-status <cr>
```

Handler ` RVA 0x104C38D0 `；selector ` 0 `；EOL ` RVA 0x33C3CDD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1d0ecaf09eaa266e](../../evidence/conditions-sets-011.md#c-1d0ecaf09eaa266e) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004395

```text
(config-controller)# default sra <cr>
```

Handler ` RVA 0x1243DA00 `；selector ` 0 `；EOL ` RVA 0x3586EB10 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-762df5077c69f95b](../../evidence/conditions-sets-046.md#c-762df5077c69f95b) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004367

```text
(config-controller)# default sync interval <cr>
```

Handler ` RVA 0x1243DD60 `；selector ` 0 `；EOL ` RVA 0x3586D800 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7cd82133fb300417](../../evidence/conditions-sets-048.md#c-7cd82133fb300417) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004479

```text
(config-controller)# default sync mode <cr>
```

Handler ` RVA 0x1243DED0 `；selector ` 0 `；EOL ` RVA 0x3586DBA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-075bb97754b48490](../../evidence/conditions-sets-003.md#c-075bb97754b48490) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004519

```text
(config-controller)# default tdm-group <number:0..23> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEACA0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-a035a96a6328d879](../../evidence/conditions-sets-062.md#c-a035a96a6328d879) · [参数 P-e50349e291365166](../../evidence/parameters-sets-017.md#p-e50349e291365166) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004506

```text
(config-controller)# default tdm-group <number:0..30> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEB730 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-9c47f2ef74a32c76](../../evidence/conditions-sets-060.md#c-9c47f2ef74a32c76) · [参数 P-df916d37e743465e](../../evidence/parameters-sets-017.md#p-df916d37e743465e) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004363

```text
(config-controller)# default termination <cr>
```

Handler ` RVA 0x163CF330 `；selector ` 0 `；EOL ` RVA 0x35F81D50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-86e2c30b17fd6610](../../evidence/conditions-sets-052.md#c-86e2c30b17fd6610) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004465

```text
(config-controller)# default threshold sd-ber <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 30 `；EOL ` RVA 0x35EE59B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e766d26a4be1c810](../../evidence/conditions-sets-089.md#c-e766d26a4be1c810) · [状态效果 S-526ef1b0b5872b63](../../evidence/state_effects-sets-018.md#s-526ef1b0b5872b63)

### observed_connections-004470

```text
(config-controller)# default threshold sd-ber <cr>
```

Handler ` RVA 0x16144750 `；selector ` 132 `；EOL ` RVA 0x35EF2078 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfdf3f5d2770ea0f](../../evidence/conditions-sets-086.md#c-dfdf3f5d2770ea0f) · [状态效果 S-108c895dcdaf48e3](../../evidence/state_effects-sets-004.md#s-108c895dcdaf48e3)

### observed_connections-004531

```text
(config-controller)# default training log filename <cr>
```

Handler ` RVA 0x1243F600 `；selector ` 0 `；EOL ` RVA 0x3586D0D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab3da90492588462](../../evidence/conditions-sets-066.md#c-ab3da90492588462) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004493

```text
(config-controller)# default vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 34 `；EOL ` RVA 0x35EEAD50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-562a89859fedd101](../../evidence/conditions-sets-034.md#c-562a89859fedd101) · [参数 P-dfdb74fc1c98c978](../../evidence/parameters-sets-017.md#p-dfdb74fc1c98c978) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004494

```text
(config-controller)# default vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 131 `；EOL ` RVA 0x35EF6F90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-d7e214e1e79bf78f](../../evidence/conditions-sets-083.md#c-d7e214e1e79bf78f) · [参数 P-63ccf7b593ace76e](../../evidence/parameters-sets-008.md#p-63ccf7b593ace76e) · [状态效果 S-0ed34d9a5adaf60b](../../evidence/state_effects-sets-004.md#s-0ed34d9a5adaf60b)

### observed_connections-004497

```text
(config-controller)# default yellow generation <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 24 `；EOL ` RVA 0x35EED3E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-51cdb59a02557997](../../evidence/conditions-sets-032.md#c-51cdb59a02557997) · [状态效果 S-dc5529c5712c5e45](../../evidence/state_effects-sets-047.md#s-dc5529c5712c5e45)

### observed_connections-004344

```text
(config-controller)# description <string> <cr>
```

Handler ` RVA 0xECFF8D0 `；selector ` 0 `；EOL ` RVA 0x35EF16A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 240 characters describing this interface。

[条件 C-42f6ce1a05df9d17](../../evidence/conditions-sets-026.md#c-42f6ce1a05df9d17) · [参数 P-2f068efe2ab2b113](../../evidence/parameters-sets-004.md#p-2f068efe2ab2b113)

### observed_connections-004558

```text
(config-controller)# detect v54 channel-group <number:dynamic> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 118 `；EOL ` RVA 0x35EF7320 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` channel-group number。

[条件 C-ba3cd5d9198cd0fb](../../evidence/conditions-sets-072.md#c-ba3cd5d9198cd0fb) · [缺口 G-792f52d07fda286d](../../evidence/gaps-sets-005.md#g-792f52d07fda286d) · [参数 P-274f3f4237fbf31f](../../evidence/parameters-sets-003.md#p-274f3f4237fbf31f)

### observed_connections-004560

```text
(config-controller)# detect v54 channel-group <number:dynamic> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 18 `；EOL ` RVA 0x35EEB890 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` channel-group number。

[条件 C-ce17a6527d1da470](../../evidence/conditions-sets-079.md#c-ce17a6527d1da470) · [缺口 G-c8b54f0b4db1c655](../../evidence/gaps-sets-007.md#g-c8b54f0b4db1c655) · [参数 P-62ade67510479f57](../../evidence/parameters-sets-008.md#p-62ade67510479f57)

### observed_connections-004374

```text
(config-controller)# diagnostics DELT <cr>
```

Handler ` RVA 0x1243ED90 `；selector ` 0 `；EOL ` RVA 0x3586E148 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-955286b51a241784](../../evidence/conditions-sets-058.md#c-955286b51a241784)

### observed_connections-004550

```text
(config-controller)# ds0 busyout <number:1..24> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 16 `；EOL ` RVA 0x378DD220 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of timeslots which needed to be busyout。

[条件 C-379047f33e72fde8](../../evidence/conditions-sets-022.md#c-379047f33e72fde8) · [缺口 G-023a4e9d71454b24](../../evidence/gaps-sets-001.md#g-023a4e9d71454b24) · [参数 P-82270768c5700ca4](../../evidence/parameters-sets-010.md#p-82270768c5700ca4) · [状态效果 S-aa1585d5c9fbd55d](../../evidence/state_effects-sets-036.md#s-aa1585d5c9fbd55d)

### observed_connections-004547

```text
(config-controller)# ds0 busyout <number:1..31> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 117 `；EOL ` RVA 0x378E1528 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of timeslots which needed to be busyout。

[条件 C-518a8cf11bf22c34](../../evidence/conditions-sets-032.md#c-518a8cf11bf22c34) · [缺口 G-05285da24efc8cc1](../../evidence/gaps-sets-001.md#g-05285da24efc8cc1) · [参数 P-17a7e5d9fd7a6926](../../evidence/parameters-sets-002.md#p-17a7e5d9fd7a6926) · [状态效果 S-77b6a52616e43178](../../evidence/state_effects-sets-025.md#s-77b6a52616e43178)

### observed_connections-004568

```text
(config-controller)# ds0-group <number:0..23> timeslots <number:1..24> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DA330 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group Number；` unsigned_number ` List of T1 timeslots。

[条件 C-17447c74171eabea](../../evidence/conditions-sets-009.md#c-17447c74171eabea) · [缺口 G-6fc1175efb94d0d0](../../evidence/gaps-sets-004.md#g-6fc1175efb94d0d0) · [参数 P-2984503ba8a2a2cb](../../evidence/parameters-sets-004.md#p-2984503ba8a2a2cb) · [状态效果 S-08a9ec514d9c3f05](../../evidence/state_effects-sets-002.md#s-08a9ec514d9c3f05)

### observed_connections-004566

```text
(config-controller)# ds0-group <number:0..30> timeslots <number:1..31> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378DE9E0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number；` unsigned_number ` List of timeslots which comprise the ds0-group。

[条件 C-c8aa22d00bd7e3c1](../../evidence/conditions-sets-077.md#c-c8aa22d00bd7e3c1) · [缺口 G-6a62eba247f61d1e](../../evidence/gaps-sets-004.md#g-6a62eba247f61d1e) · [参数 P-1b61f4763a6799de](../../evidence/parameters-sets-003.md#p-1b61f4763a6799de) · [状态效果 S-57bb2ad127e04088](../../evidence/state_effects-sets-019.md#s-57bb2ad127e04088)

### observed_connections-004539

```text
(config-controller)# dsl-group <number:dynamic> <cr>
```

Handler ` RVA 0x163D0F00 `；selector ` 1 `；EOL ` RVA 0x35F82518 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` DSL group number。

[条件 C-beb17224bd40a418](../../evidence/conditions-sets-074.md#c-beb17224bd40a418) · [缺口 G-d4bd20bf5315cca3](../../evidence/gaps-sets-007.md#g-d4bd20bf5315cca3) · [参数 P-0d52c825e0777b8c](../../evidence/parameters-sets-001.md#p-0d52c825e0777b8c)

### observed_connections-004541

```text
(config-controller)# dsl-group <number:dynamic> <cr>
```

Handler ` RVA 0x163D0F00 `；selector ` 2 `；EOL ` RVA 0x35F82AC0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` DSL group number。

[条件 C-7f1d5d8225af2dbc](../../evidence/conditions-sets-049.md#c-7f1d5d8225af2dbc) · [缺口 G-d4bd20bf5315cca3](../../evidence/gaps-sets-007.md#g-d4bd20bf5315cca3) · [参数 P-0d52c825e0777b8c](../../evidence/parameters-sets-001.md#p-0d52c825e0777b8c)

### observed_connections-004385

```text
(config-controller)# dsl-group auto <cr>
```

Handler ` RVA 0x163D0F00 `；selector ` 1 `；EOL ` RVA 0x35F82518 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00b910165542f060](../../evidence/conditions-sets-001.md#c-00b910165542f060) · [状态效果 S-53ac3ad9c032c274](../../evidence/state_effects-sets-018.md#s-53ac3ad9c032c274)

### observed_connections-004316

```text
(config-controller)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x343F7428 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-223cfbc6be0717fd](../../evidence/conditions-sets-013.md#c-223cfbc6be0717fd)

### observed_connections-004392

```text
(config-controller)# fdl att <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 14 `；EOL ` RVA 0x35EF07A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b8f13a21ac60276](../../evidence/conditions-sets-060.md#c-9b8f13a21ac60276) · [状态效果 S-f9d84ebd30b5e8de](../../evidence/state_effects-sets-053.md#s-f9d84ebd30b5e8de)

### observed_connections-004351

```text
(config-controller)# firmware phy <cr>
```

Handler ` RVA 0x163CFA90 `；selector ` 0 `；EOL ` RVA 0x35F818E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6606185ff4000a77](../../evidence/conditions-sets-039.md#c-6606185ff4000a77) · [状态效果 S-24a48960320268ca](../../evidence/state_effects-sets-008.md#s-24a48960320268ca)

### observed_connections-004551

```text
(config-controller)# firmware phy filename <url:dynamic> <cr>
```

Handler ` RVA 0x163CFA90 `；selector ` 0 `；EOL ` RVA 0x35F818E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d6a5566d352d499c](../../evidence/conditions-sets-083.md#c-d6a5566d352d499c) · [缺口 G-07ec2e8b39b7ec9d](../../evidence/gaps-sets-001.md#g-07ec2e8b39b7ec9d) · [参数 P-690f1a5b4d975a3e](../../evidence/parameters-sets-008.md#p-690f1a5b4d975a3e) · [状态效果 S-884f9d20e6806ad7](../../evidence/state_effects-sets-029.md#s-884f9d20e6806ad7)

### observed_connections-004554

```text
(config-controller)# firmware phy filename <url:dynamic> <cr>
```

Handler ` RVA 0x1243EF20 `；selector ` 0 `；EOL ` RVA 0x3586D510 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f63843441ddb4d0](../../evidence/conditions-sets-025.md#c-3f63843441ddb4d0) · [缺口 G-80f92aa856d1fb99](../../evidence/gaps-sets-005.md#g-80f92aa856d1fb99) · [参数 P-31bca40a8071a6b0](../../evidence/parameters-sets-004.md#p-31bca40a8071a6b0)

### observed_connections-004442

```text
(config-controller)# forward-alarm ais <cr>
```

Handler ` RVA 0x16144750 `；selector ` 125 `；EOL ` RVA 0x35EFAC40 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c085d23fed16022b](../../evidence/conditions-sets-074.md#c-c085d23fed16022b) · [状态效果 S-7db5d9e2c91051c7](../../evidence/state_effects-sets-027.md#s-7db5d9e2c91051c7)

### observed_connections-004450

```text
(config-controller)# forward-alarm ais <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 27 `；EOL ` RVA 0x35EEF2A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c60e51b55540b011](../../evidence/conditions-sets-076.md#c-c60e51b55540b011) · [状态效果 S-564365ebac63cb1b](../../evidence/state_effects-sets-019.md#s-564365ebac63cb1b)

### observed_connections-004333

```text
(config-controller)# forward-alarms <cr>
```

Handler ` RVA 0x16144750 `；selector ` 119 `；EOL ` RVA 0x35EF87B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22a93f584c85b38b](../../evidence/conditions-sets-014.md#c-22a93f584c85b38b)

### observed_connections-004336

```text
(config-controller)# forward-alarms <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 19 `；EOL ` RVA 0x35EED840 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-434d7faebac1ec5b](../../evidence/conditions-sets-026.md#c-434d7faebac1ec5b)

### observed_connections-004394

```text
(config-controller)# framing no-crc4 <cr>
```

Handler ` RVA 0x16144750 `；selector ` 104 `；EOL ` RVA 0x35EF3788 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c33a217428f458e2](../../evidence/conditions-sets-075.md#c-c33a217428f458e2) · [状态效果 S-afdc2b82c9c38d1e](../../evidence/state_effects-sets-037.md#s-afdc2b82c9c38d1e)

### observed_connections-004381

```text
(config-controller)# framing unframed <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 3 `；EOL ` RVA 0x35EE7060 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64cd93431b8e05c8](../../evidence/conditions-sets-039.md#c-64cd93431b8e05c8) · [状态效果 S-2aefeb671b1d25b1](../../evidence/state_effects-sets-010.md#s-2aefeb671b1d25b1)

### observed_connections-004540

```text
(config-controller)# interface-default-mtu <number:dynamic> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 2 `；EOL ` RVA 0x35EE6358 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` mtu value。

[条件 C-90e28442bd9015c8](../../evidence/conditions-sets-056.md#c-90e28442bd9015c8) · [缺口 G-a15d985a9abc37fb](../../evidence/gaps-sets-006.md#g-a15d985a9abc37fb) · [参数 P-f18f7486188314d1](../../evidence/parameters-sets-018.md#p-f18f7486188314d1)

### observed_connections-004542

```text
(config-controller)# interface-default-mtu <number:dynamic> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 101 `；EOL ` RVA 0x35EF2A80 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` mtu value。

[条件 C-d89b1c81d3d4157d](../../evidence/conditions-sets-083.md#c-d89b1c81d3d4157d) · [缺口 G-3691f0cec679f947](../../evidence/gaps-sets-002.md#g-3691f0cec679f947) · [参数 P-1ed4b94af781fd7a](../../evidence/parameters-sets-003.md#p-1ed4b94af781fd7a)

### observed_connections-004359

```text
(config-controller)# line-mode bonding <cr>
```

Handler ` RVA 0x12443B00 `；selector ` 0 `；EOL ` RVA 0x3586CB60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85d06705ff0bc988](../../evidence/conditions-sets-052.md#c-85d06705ff0bc988) · [状态效果 S-975341ce7538804b](../../evidence/state_effects-sets-032.md#s-975341ce7538804b)

### observed_connections-004408

```text
(config-controller)# line-termination 75-ohm <cr>
```

Handler ` RVA 0x16144750 `；selector ` 114 `；EOL ` RVA 0x35EF4F58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec0470999756491e](../../evidence/conditions-sets-091.md#c-ec0470999756491e) · [状态效果 S-8c9df5b3aa736152](../../evidence/state_effects-sets-030.md#s-8c9df5b3aa736152)

### observed_connections-004402

```text
(config-controller)# linecode ami <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 6 `；EOL ` RVA 0x35EEFA60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3afff1869d2586e9](../../evidence/conditions-sets-023.md#c-3afff1869d2586e9) · [状态效果 S-8fb9deb123ac6dc2](../../evidence/state_effects-sets-030.md#s-8fb9deb123ac6dc2)

### observed_connections-004403

```text
(config-controller)# linecode ami <cr>
```

Handler ` RVA 0x16144750 `；selector ` 105 `；EOL ` RVA 0x35EF4B58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-77b9c9c5d908d172](../../evidence/conditions-sets-047.md#c-77b9c9c5d908d172) · [状态效果 S-2de4b03468eca0f8](../../evidence/state_effects-sets-010.md#s-2de4b03468eca0f8)

### observed_connections-004502

```text
(config-controller)# linestate debounce <number:1..1000> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 122 `；EOL ` RVA 0x35EFA560 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Range between 1 and thousand millisecs。

[条件 C-ad7535998ec7be9e](../../evidence/conditions-sets-067.md#c-ad7535998ec7be9e) · [参数 P-e3b32731695f272f](../../evidence/parameters-sets-017.md#p-e3b32731695f272f)

### observed_connections-004330

```text
(config-controller)# logging-events <cr>
```

Handler ` RVA 0x16144750 `；selector ` 123 `；EOL ` RVA 0x35EF6BC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-206f28112125edf4](../../evidence/conditions-sets-013.md#c-206f28112125edf4) · [状态效果 S-ae1ca923b294be2f](../../evidence/state_effects-sets-037.md#s-ae1ca923b294be2f)

### observed_connections-004331

```text
(config-controller)# logging-events <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 25 `；EOL ` RVA 0x35EEB108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9f8cdfb0cc401d1](../../evidence/conditions-sets-066.md#c-a9f8cdfb0cc401d1) · [状态效果 S-4b9481bf901286a7](../../evidence/state_effects-sets-017.md#s-4b9481bf901286a7)

### observed_connections-004332

```text
(config-controller)# loopback <cr>
```

Handler ` RVA 0x16144750 `；selector ` 108 `；EOL ` RVA 0x35EF6020 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-573385b36e30068c](../../evidence/conditions-sets-034.md#c-573385b36e30068c) · [状态效果 S-a3da8258161f75bf](../../evidence/state_effects-sets-035.md#s-a3da8258161f75bf)

### observed_connections-004334

```text
(config-controller)# loopback <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 9 `；EOL ` RVA 0x35EE96F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfc1895b94ac6038](../../evidence/conditions-sets-080.md#c-cfc1895b94ac6038) · [状态效果 S-6543cee07ea03eef](../../evidence/state_effects-sets-022.md#s-6543cee07ea03eef)

### observed_connections-004559

```text
(config-controller)# loopback local timeslots <number:1..24> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 9 `；EOL ` RVA 0x35EE96F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of timeslots which comprise the DS0 loop。

[条件 C-e35cd63156166da2](../../evidence/conditions-sets-088.md#c-e35cd63156166da2) · [缺口 G-3b47caebf9337444](../../evidence/gaps-sets-003.md#g-3b47caebf9337444) · [参数 P-5f859ab68e6038b4](../../evidence/parameters-sets-008.md#p-5f859ab68e6038b4) · [状态效果 S-47e33da05f0a162e](../../evidence/state_effects-sets-016.md#s-47e33da05f0a162e)

### observed_connections-004557

```text
(config-controller)# loopback local timeslots <number:1..31> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 108 `；EOL ` RVA 0x35EF6020 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of timeslots which comprise the DS0 loop。

[条件 C-785d01e76518d9a0](../../evidence/conditions-sets-047.md#c-785d01e76518d9a0) · [缺口 G-dfd5b313aaac5b56](../../evidence/gaps-sets-008.md#g-dfd5b313aaac5b56) · [参数 P-8f81df8ce89317e4](../../evidence/parameters-sets-011.md#p-8f81df8ce89317e4) · [状态效果 S-effc813d3b3323e3](../../evidence/state_effects-sets-051.md#s-effc813d3b3323e3)

### observed_connections-004360

```text
(config-controller)# mode efm <cr>
```

Handler ` RVA 0x163CEBA0 `；selector ` 0 `；EOL ` RVA 0x35F82110 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08526493bdfc5bcf](../../evidence/conditions-sets-004.md#c-08526493bdfc5bcf) · [状态效果 S-fcd9db2f95c0fe3d](../../evidence/state_effects-sets-054.md#s-fcd9db2f95c0fe3d)

### observed_connections-004369

```text
(config-controller)# modem <string> <cr>
```

Handler ` RVA 0x1243E380 `；selector ` 0 `；EOL ` RVA 0x3586E480 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` command line string。

[条件 C-0c0ad5bf5e2cf003](../../evidence/conditions-sets-005.md#c-0c0ad5bf5e2cf003) · [参数 P-60c5f3f749e58c14](../../evidence/parameters-sets-008.md#p-60c5f3f749e58c14)

### observed_connections-004538

```text
(config-controller)# national reserve <number:0..1> <number:0..1> <number:0..1> <number:0..1> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 110 `；EOL ` RVA 0x35EFA058 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of International bit.；` unsigned_number ` Value of Sa4 bit.；` unsigned_number ` Value of Sa5 bit.；` unsigned_number ` Value of Sa6 bit.；` unsigned_number ` Value of Sa7 bit.；` unsigned_number ` Value of Sa8 bit.。

[条件 C-7556c93a04294151](../../evidence/conditions-sets-046.md#c-7556c93a04294151) · [参数 P-914e8e2a1f673381](../../evidence/parameters-sets-011.md#p-914e8e2a1f673381) · [状态效果 S-01914912a9ba8bce](../../evidence/state_effects-sets-001.md#s-01914912a9ba8bce)

### observed_connections-004341

```text
(config-controller)# no ais-core-failure <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 31 `；EOL ` RVA 0x35EE5588 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7899693bc4117431](../../evidence/conditions-sets-047.md#c-7899693bc4117431) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004348

```text
(config-controller)# no ais-core-failure <cr>
```

Handler ` RVA 0x16144750 `；selector ` 129 `；EOL ` RVA 0x35EF1C50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e2ab5919008fd3e](../../evidence/conditions-sets-043.md#c-6e2ab5919008fd3e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004339

```text
(config-controller)# no ais-shut <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 29 `；EOL ` RVA 0x35EE52A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-00331dde37fc21b8](../../evidence/conditions-sets-001.md#c-00331dde37fc21b8) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004342

```text
(config-controller)# no ais-shut <cr>
```

Handler ` RVA 0x16144750 `；selector ` 127 `；EOL ` RVA 0x35EF1968 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-279c82f39592685c](../../evidence/conditions-sets-016.md#c-279c82f39592685c) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004433

```text
(config-controller)# no alarm-trigger <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 120 `；EOL ` RVA 0x378E0D90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-95e8d93976b329c5](../../evidence/conditions-sets-058.md#c-95e8d93976b329c5) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004447

```text
(config-controller)# no alarm-trigger <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 20 `；EOL ` RVA 0x378DCA88 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-40ca52ff7e122fb9](../../evidence/conditions-sets-025.md#c-40ca52ff7e122fb9) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004434

```text
(config-controller)# no atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EFA8B8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-55b67533121fd2df](../../evidence/conditions-sets-034.md#c-55b67533121fd2df) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004438

```text
(config-controller)# no atm <cr>
```

Handler ` RVA 0x16144620 `；selector ` 0 `；EOL ` RVA 0x35EEEF20 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-00fbe09800a90cd0](../../evidence/conditions-sets-001.md#c-00fbe09800a90cd0) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004529

```text
(config-controller)# no attach profile <string> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 4 `；EOL ` RVA 0x35EE6710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-ec3cda1ed59693f2](../../evidence/conditions-sets-091.md#c-ec3cda1ed59693f2) · [参数 P-ddd1d2c1f78ae7df](../../evidence/parameters-sets-017.md#p-ddd1d2c1f78ae7df) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004533

```text
(config-controller)# no attach profile <string> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 102 `；EOL ` RVA 0x35EF2E38 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Alarm profile name。

[条件 C-b344db1881b07d2f](../../evidence/conditions-sets-069.md#c-b344db1881b07d2f) · [参数 P-47af0e22bac05b2a](../../evidence/parameters-sets-006.md#p-47af0e22bac05b2a) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004428

```text
(config-controller)# no bert <cr>
```

Handler ` RVA 0x16144750 `；selector ` 109 `；EOL ` RVA 0x35EF8AE8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8bfe6f51b6ab96c0](../../evidence/conditions-sets-054.md#c-8bfe6f51b6ab96c0) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004435

```text
(config-controller)# no bert <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 15 `；EOL ` RVA 0x35EEDB78 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9d42410b90c8697f](../../evidence/conditions-sets-061.md#c-9d42410b90c8697f) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004391

```text
(config-controller)# no bitswap <cr>
```

Handler ` RVA 0x1243D6A0 `；selector ` 0 `；EOL ` RVA 0x3586EEB0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-11b60ec87ff285e9](../../evidence/conditions-sets-007.md#c-11b60ec87ff285e9) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004536

```text
(config-controller)# no cablelength short 550ft <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 7 `；EOL ` RVA 0x35EE7C98 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6eadcf539e3c6c8d](../../evidence/conditions-sets-043.md#c-6eadcf539e3c6c8d) · [状态效果 S-512cb84b176dcd45](../../evidence/state_effects-sets-018.md#s-512cb84b176dcd45)

### observed_connections-004366

```text
(config-controller)# no cas <cr>
```

Handler ` RVA 0x16144750 `；selector ` 128 `；EOL ` RVA 0x35EF2710 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c190c0d5b2099614](../../evidence/conditions-sets-075.md#c-c190c0d5b2099614) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004518

```text
(config-controller)# no cas-custom <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 21 `；EOL ` RVA 0x378DE5D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-96b7b7a14f574780](../../evidence/conditions-sets-058.md#c-96b7b7a14f574780) · [参数 P-82d8522f5b1fba13](../../evidence/parameters-sets-010.md#p-82d8522f5b1fba13) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004504

```text
(config-controller)# no cas-custom <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 115 `；EOL ` RVA 0x378E33F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-1bad10afeed2b0e6](../../evidence/conditions-sets-011.md#c-1bad10afeed2b0e6) · [参数 P-9c3dcfa7df47f226](../../evidence/parameters-sets-012.md#p-9c3dcfa7df47f226) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004515

```text
(config-controller)# no cas-group <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DB760 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-80de18cc1ea32e67](../../evidence/conditions-sets-050.md#c-80de18cc1ea32e67) · [参数 P-ff6a65ee5de4a5f9](../../evidence/parameters-sets-019.md#p-ff6a65ee5de4a5f9) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004501

```text
(config-controller)# no cas-group <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378E18B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Channel number。

[条件 C-8bc029fb3395c82a](../../evidence/conditions-sets-054.md#c-8bc029fb3395c82a) · [参数 P-d8d70c5e33d1ab95](../../evidence/parameters-sets-016.md#p-d8d70c5e33d1ab95) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004484

```text
(config-controller)# no clock source <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 5 `；EOL ` RVA 0x35EEFE70 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-747d5e0d57c114f4](../../evidence/conditions-sets-045.md#c-747d5e0d57c114f4) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004486

```text
(config-controller)# no clock source <cr>
```

Handler ` RVA 0x16144750 `；selector ` 106 `；EOL ` RVA 0x35EFB408 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7f53c295fe17e90f](../../evidence/conditions-sets-049.md#c-7f53c295fe17e90f) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004418

```text
(config-controller)# no compand <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 13 `；EOL ` RVA 0x35EEB4F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c75fed3dd56c5230](../../evidence/conditions-sets-077.md#c-c75fed3dd56c5230) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004350

```text
(config-controller)# no debug-state-change <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 32 `；EOL ` RVA 0x35EE5FA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bd68e3ac3f60b70](../../evidence/conditions-sets-060.md#c-9bd68e3ac3f60b70) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004343

```text
(config-controller)# no description <cr>
```

Handler ` RVA 0xECFF8D0 `；selector ` 0 `；EOL ` RVA 0x35EF16A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb89bc86acbc8898](../../evidence/conditions-sets-097.md#c-fb89bc86acbc8898) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004416

```text
(config-controller)# no detect <cr>
```

Handler ` RVA 0x16144750 `；selector ` 118 `；EOL ` RVA 0x35EF7320 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18f042ec779b0ed5](../../evidence/conditions-sets-010.md#c-18f042ec779b0ed5) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004424

```text
(config-controller)# no detect <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 18 `；EOL ` RVA 0x35EEB890 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3051921207d05b72](../../evidence/conditions-sets-019.md#c-3051921207d05b72) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004373

```text
(config-controller)# no diagnostics <cr>
```

Handler ` RVA 0x1243ED90 `；selector ` 0 `；EOL ` RVA 0x3586E148 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0fd7743a49d1538f](../../evidence/conditions-sets-006.md#c-0fd7743a49d1538f) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004500

```text
(config-controller)# no ds0-group <number:0..23> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 11 `；EOL ` RVA 0x378DA330 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Group Number。

[条件 C-f435fd77532d66e1](../../evidence/conditions-sets-094.md#c-f435fd77532d66e1) · [参数 P-5aa4943895e5d8af](../../evidence/parameters-sets-007.md#p-5aa4943895e5d8af) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004496

```text
(config-controller)# no ds0-group <number:0..30> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 111 `；EOL ` RVA 0x378DE9E0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-ce62c485a34c635c](../../evidence/conditions-sets-079.md#c-ce62c485a34c635c) · [参数 P-42aac2c29d87f8bf](../../evidence/parameters-sets-006.md#p-42aac2c29d87f8bf) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004478

```text
(config-controller)# no dsl-group auto <cr>
```

Handler ` RVA 0x163D0F00 `；selector ` 1 `；EOL ` RVA 0x35F82518 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-691768d4f1403faa](../../evidence/conditions-sets-041.md#c-691768d4f1403faa) · [状态效果 S-a26162ab56925b95](../../evidence/state_effects-sets-034.md#s-a26162ab56925b95)

### observed_connections-004389

```text
(config-controller)# no fdl <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 14 `；EOL ` RVA 0x35EF07A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-00d36500a174886b](../../evidence/conditions-sets-001.md#c-00d36500a174886b) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004457

```text
(config-controller)# no firmware phy <cr>
```

Handler ` RVA 0x163CFA90 `；selector ` 0 `；EOL ` RVA 0x35F818E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-753b6ba3a30aa0e1](../../evidence/conditions-sets-045.md#c-753b6ba3a30aa0e1) · [状态效果 S-d7a74abd5c47ec6d](../../evidence/state_effects-sets-046.md#s-d7a74abd5c47ec6d)

### observed_connections-004530

```text
(config-controller)# no firmware phy filename <cr>
```

Handler ` RVA 0x1243EF20 `；selector ` 0 `；EOL ` RVA 0x3586D510 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4c82a63944f46155](../../evidence/conditions-sets-030.md#c-4c82a63944f46155) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004505

```text
(config-controller)# no forward-alarm ais <cr>
```

Handler ` RVA 0x16144750 `；selector ` 125 `；EOL ` RVA 0x35EFAC40 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1d256da6841bfeea](../../evidence/conditions-sets-011.md#c-1d256da6841bfeea) · [状态效果 S-c57a886f218d9156](../../evidence/state_effects-sets-042.md#s-c57a886f218d9156)

### observed_connections-004508

```text
(config-controller)# no forward-alarm ais <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 27 `；EOL ` RVA 0x35EEF2A8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-77fbade9d523c536](../../evidence/conditions-sets-047.md#c-77fbade9d523c536) · [状态效果 S-f3e70fa23d239702](../../evidence/state_effects-sets-052.md#s-f3e70fa23d239702)

### observed_connections-004430

```text
(config-controller)# no forward-alarms <cr>
```

Handler ` RVA 0x16144750 `；selector ` 119 `；EOL ` RVA 0x35EF87B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fd4e55eae9165443](../../evidence/conditions-sets-098.md#c-fd4e55eae9165443) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004436

```text
(config-controller)# no forward-alarms <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 19 `；EOL ` RVA 0x35EED840 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-115bafc48623c5bb](../../evidence/conditions-sets-007.md#c-115bafc48623c5bb) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004368

```text
(config-controller)# no framing <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 3 `；EOL ` RVA 0x35EE7060 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1a9cd1bc725d3cb](../../evidence/conditions-sets-087.md#c-e1a9cd1bc725d3cb) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004377

```text
(config-controller)# no framing <cr>
```

Handler ` RVA 0x16144750 `；selector ` 104 `；EOL ` RVA 0x35EF3788 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a80eb4017168be74](../../evidence/conditions-sets-065.md#c-a80eb4017168be74) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004365

```text
(config-controller)# no interface-default-mtu <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 2 `；EOL ` RVA 0x35EE6358 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73e1ead25defc720](../../evidence/conditions-sets-045.md#c-73e1ead25defc720) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004372

```text
(config-controller)# no interface-default-mtu <cr>
```

Handler ` RVA 0x16144750 `；selector ` 101 `；EOL ` RVA 0x35EF2A80 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6f166b83b120f613](../../evidence/conditions-sets-043.md#c-6f166b83b120f613) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004463

```text
(config-controller)# no line-mode bonding <cr>
```

Handler ` RVA 0x12443B00 `；selector ` 0 `；EOL ` RVA 0x3586CB60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc5c06b7a3774a87](../../evidence/conditions-sets-073.md#c-bc5c06b7a3774a87) · [状态效果 S-5d5bdb3ab05bd698](../../evidence/state_effects-sets-020.md#s-5d5bdb3ab05bd698)

### observed_connections-004407

```text
(config-controller)# no line-termination <cr>
```

Handler ` RVA 0x16144750 `；selector ` 114 `；EOL ` RVA 0x35EF4F58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7831b05d3c44ab40](../../evidence/conditions-sets-047.md#c-7831b05d3c44ab40) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004400

```text
(config-controller)# no linecode <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 6 `；EOL ` RVA 0x35EEFA60 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f15a7da15da32e23](../../evidence/conditions-sets-093.md#c-f15a7da15da32e23) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004401

```text
(config-controller)# no linecode <cr>
```

Handler ` RVA 0x16144750 `；selector ` 105 `；EOL ` RVA 0x35EF4B58 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-522f43ba291fbccf](../../evidence/conditions-sets-032.md#c-522f43ba291fbccf) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004437

```text
(config-controller)# no linestate <cr>
```

Handler ` RVA 0x16144750 `；selector ` 122 `；EOL ` RVA 0x35EFA560 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5518325e806af233](../../evidence/conditions-sets-033.md#c-5518325e806af233) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004414

```text
(config-controller)# no logging-events <cr>
```

Handler ` RVA 0x16144750 `；selector ` 123 `；EOL ` RVA 0x35EF6BC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4d41edd7586ad401](../../evidence/conditions-sets-030.md#c-4d41edd7586ad401) · [状态效果 S-189c20f7236fa0b9](../../evidence/state_effects-sets-006.md#s-189c20f7236fa0b9)

### observed_connections-004420

```text
(config-controller)# no logging-events <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 25 `；EOL ` RVA 0x35EEB108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-693ce1ad68d849ac](../../evidence/conditions-sets-041.md#c-693ce1ad68d849ac) · [状态效果 S-63db30da16bfbc92](../../evidence/state_effects-sets-021.md#s-63db30da16bfbc92)

### observed_connections-004411

```text
(config-controller)# no loopback <cr>
```

Handler ` RVA 0x16144750 `；selector ` 108 `；EOL ` RVA 0x35EF6020 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-344e8d67501841ef](../../evidence/conditions-sets-020.md#c-344e8d67501841ef) · [状态效果 S-a579d432e33074a3](../../evidence/state_effects-sets-035.md#s-a579d432e33074a3)

### observed_connections-004415

```text
(config-controller)# no loopback <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 9 `；EOL ` RVA 0x35EE96F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5e8f1046eace43af](../../evidence/conditions-sets-037.md#c-5e8f1046eace43af) · [状态效果 S-70805a2055b79546](../../evidence/state_effects-sets-024.md#s-70805a2055b79546)

### observed_connections-004358

```text
(config-controller)# no mode <cr>
```

Handler ` RVA 0x163CEBA0 `；selector ` 0 `；EOL ` RVA 0x35F82110 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-46eeea068aa3b034](../../evidence/conditions-sets-028.md#c-46eeea068aa3b034) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004472

```text
(config-controller)# no modem <string> <cr>
```

Handler ` RVA 0x1243E380 `；selector ` 0 `；EOL ` RVA 0x3586E480 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` command line string。

[条件 C-6c20bcb438ff4390](../../evidence/conditions-sets-042.md#c-6c20bcb438ff4390) · [参数 P-60c5f3f749e58c14](../../evidence/parameters-sets-008.md#p-60c5f3f749e58c14) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004522

```text
(config-controller)# no national reserve <cr>
```

Handler ` RVA 0x16144750 `；selector ` 110 `；EOL ` RVA 0x35EFA058 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b94a3a115f90b2d0](../../evidence/conditions-sets-072.md#c-b94a3a115f90b2d0) · [状态效果 S-f1e06f37e3091ccd](../../evidence/state_effects-sets-051.md#s-f1e06f37e3091ccd)

### observed_connections-004459

```text
(config-controller)# no operating mode <cr>
```

Handler ` RVA 0x1243CAE0 `；selector ` 0 `；EOL ` RVA 0x3586BFF0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3b141cab4f7a6bdb](../../evidence/conditions-sets-023.md#c-3b141cab4f7a6bdb) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004448

```text
(config-controller)# no pri-group <cr>
```

Handler ` RVA 0x16144750 `；selector ` 113 `；EOL ` RVA 0x35EF7AC0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50c0246e7083a1b2](../../evidence/conditions-sets-032.md#c-50c0246e7083a1b2) · [状态效果 S-3af6ba82df808245](../../evidence/state_effects-sets-013.md#s-3af6ba82df808245)

### observed_connections-004404

```text
(config-controller)# no rem-loop-detect-disable <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 35 `；EOL ` RVA 0x35EE9108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d9a36a244a0bc456](../../evidence/conditions-sets-084.md#c-d9a36a244a0bc456) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004503

```text
(config-controller)# no scrambling cell-payload <cr>
```

Handler ` RVA 0x16144750 `；selector ` 126 `；EOL ` RVA 0x35EFAFC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbd35ef0395fa72e](../../evidence/conditions-sets-097.md#c-fbd35ef0395fa72e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004507

```text
(config-controller)# no scrambling cell-payload <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 28 `；EOL ` RVA 0x35EEF630 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c28b89a6ee5d97f5](../../evidence/conditions-sets-075.md#c-c28b89a6ee5d97f5) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004477

```text
(config-controller)# no secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 33 `；EOL ` RVA 0x35EE6BD0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3ba6c6ed735d50ca](../../evidence/conditions-sets-023.md#c-3ba6c6ed735d50ca) · [状态效果 S-168f6d3b5ce6e45d](../../evidence/state_effects-sets-005.md#s-168f6d3b5ce6e45d)

### observed_connections-004481

```text
(config-controller)# no secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x16144750 `；selector ` 130 `；EOL ` RVA 0x35EF32F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-86039fb273d4ab4c](../../evidence/conditions-sets-052.md#c-86039fb273d4ab4c) · [状态效果 S-abcaef2a82775d5b](../../evidence/state_effects-sets-036.md#s-abcaef2a82775d5b)

### observed_connections-004376

```text
(config-controller)# no service-type <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 23 `；EOL ` RVA 0x35EE7628 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fac98e7023d3bd0b](../../evidence/conditions-sets-097.md#c-fac98e7023d3bd0b) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004390

```text
(config-controller)# no service-type <cr>
```

Handler ` RVA 0x16144750 `；selector ` 121 `；EOL ` RVA 0x35EF3CD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d789c0d7e70b5745](../../evidence/conditions-sets-083.md#c-d789c0d7e70b5745) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004347

```text
(config-controller)# no shutdown <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 1 `；EOL ` RVA 0x35EE5D00 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bd68e3ac3f60b70](../../evidence/conditions-sets-060.md#c-9bd68e3ac3f60b70) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004354

```text
(config-controller)# no shutdown <cr>
```

Handler ` RVA 0x16144750 `；selector ` 103 `；EOL ` RVA 0x35EF23C8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-62f3e864f3667d84](../../evidence/conditions-sets-038.md#c-62f3e864f3667d84) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004378

```text
(config-controller)# no shutdown <cr>
```

Handler ` RVA 0x1243E150 `；selector ` 0 `；EOL ` RVA 0x3586E7A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8c6e6997a5b25dc9](../../evidence/conditions-sets-054.md#c-8c6e6997a5b25dc9) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004526

```text
(config-controller)# no snmp trap link-status <cr>
```

Handler ` RVA 0x104C38D0 `；selector ` 0 `；EOL ` RVA 0x33C3CDD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0b774d9730335ec5](../../evidence/conditions-sets-005.md#c-0b774d9730335ec5) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004384

```text
(config-controller)# no sra <cr>
```

Handler ` RVA 0x1243DA00 `；selector ` 0 `；EOL ` RVA 0x3586EB10 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b3d9ad954cad07b4](../../evidence/conditions-sets-070.md#c-b3d9ad954cad07b4) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004362

```text
(config-controller)# no sync interval <cr>
```

Handler ` RVA 0x1243DD60 `；selector ` 0 `；EOL ` RVA 0x3586D800 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-72eadb4540858989](../../evidence/conditions-sets-044.md#c-72eadb4540858989) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004473

```text
(config-controller)# no sync mode <cr>
```

Handler ` RVA 0x1243DED0 `；selector ` 0 `；EOL ` RVA 0x3586DBA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9860c510b99a7750](../../evidence/conditions-sets-059.md#c-9860c510b99a7750) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004511

```text
(config-controller)# no tdm-group <number:0..23> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEACA0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-bedb8b6144f6dfa6](../../evidence/conditions-sets-074.md#c-bedb8b6144f6dfa6) · [参数 P-e50349e291365166](../../evidence/parameters-sets-017.md#p-e50349e291365166) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004499

```text
(config-controller)# no tdm-group <number:0..30> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEB730 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-1db9bc69d31bfeac](../../evidence/conditions-sets-012.md#c-1db9bc69d31bfeac) · [参数 P-df916d37e743465e](../../evidence/parameters-sets-017.md#p-df916d37e743465e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004355

```text
(config-controller)# no termination <cr>
```

Handler ` RVA 0x163CF330 `；selector ` 0 `；EOL ` RVA 0x35F81D50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a2dff136252c0f2e](../../evidence/conditions-sets-063.md#c-a2dff136252c0f2e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004458

```text
(config-controller)# no threshold sd-ber <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 30 `；EOL ` RVA 0x35EE59B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0d62da890984011](../../evidence/conditions-sets-062.md#c-a0d62da890984011) · [状态效果 S-dd99ae3199d3a807](../../evidence/state_effects-sets-047.md#s-dd99ae3199d3a807)

### observed_connections-004466

```text
(config-controller)# no threshold sd-ber <cr>
```

Handler ` RVA 0x16144750 `；selector ` 132 `；EOL ` RVA 0x35EF2078 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0727d35dc8b13c71](../../evidence/conditions-sets-003.md#c-0727d35dc8b13c71) · [状态效果 S-50c143e0e41747c8](../../evidence/state_effects-sets-018.md#s-50c143e0e41747c8)

### observed_connections-004528

```text
(config-controller)# no training log filename <cr>
```

Handler ` RVA 0x1243F600 `；selector ` 0 `；EOL ` RVA 0x3586D0D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-707bb6985695b45e](../../evidence/conditions-sets-043.md#c-707bb6985695b45e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004491

```text
(config-controller)# no vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 34 `；EOL ` RVA 0x35EEAD50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-a550407e523f20eb](../../evidence/conditions-sets-064.md#c-a550407e523f20eb) · [参数 P-dfdb74fc1c98c978](../../evidence/parameters-sets-017.md#p-dfdb74fc1c98c978) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004492

```text
(config-controller)# no vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 131 `；EOL ` RVA 0x35EF6F90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-836918535831e637](../../evidence/conditions-sets-051.md#c-836918535831e637) · [参数 P-63ccf7b593ace76e](../../evidence/parameters-sets-008.md#p-63ccf7b593ace76e) · [状态效果 S-604c9247ea5040d1](../../evidence/state_effects-sets-021.md#s-604c9247ea5040d1)

### observed_connections-004495

```text
(config-controller)# no yellow generation <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 24 `；EOL ` RVA 0x35EED3E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-08ca3bccaadab50a](../../evidence/conditions-sets-004.md#c-08ca3bccaadab50a) · [状态效果 S-5cc4013cc1891c1a](../../evidence/state_effects-sets-020.md#s-5cc4013cc1891c1a)

### observed_connections-004464

```text
(config-controller)# operating mode adsl1 <cr>
```

Handler ` RVA 0x1243CAE0 `；selector ` 0 `；EOL ` RVA 0x3586BFF0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f289ad124fe3e19c](../../evidence/conditions-sets-094.md#c-f289ad124fe3e19c) · [状态效果 S-b668ace663a1384b](../../evidence/state_effects-sets-039.md#s-b668ace663a1384b)

### observed_connections-004552

```text
(config-controller)# operating mode auto <?option@55558adc3330> <cr>
```

Handler ` RVA 0x1243CAE0 `；selector ` 0 `；EOL ` RVA 0x3586BFF0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bd7cc6b4aecd666](../../evidence/conditions-sets-054.md#c-8bd7cc6b4aecd666) · [缺口 G-78beda0d5aed6dbf](../../evidence/gaps-sets-005.md#g-78beda0d5aed6dbf) · [状态效果 S-e5627c2aa65788f5](../../evidence/state_effects-sets-048.md#s-e5627c2aa65788f5)

### observed_connections-004338

```text
(config-controller)# pri-group <cr>
```

Handler ` RVA 0x16144750 `；selector ` 113 `；EOL ` RVA 0x35EF7AC0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b73921bb4c846f52](../../evidence/conditions-sets-071.md#c-b73921bb4c846f52) · [状态效果 S-dee198c06cb1f289](../../evidence/state_effects-sets-047.md#s-dee198c06cb1f289)

### observed_connections-004565

```text
(config-controller)# pri-group <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 10 `；EOL ` RVA 0x35EEC770 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e3a221571bb7becb](../../evidence/conditions-sets-088.md#c-e3a221571bb7becb) · [缺口 G-53aeba5fe5cb8ff4](../../evidence/gaps-sets-003.md#g-53aeba5fe5cb8ff4) · [状态效果 S-1fad0f51afd2107f](../../evidence/state_effects-sets-007.md#s-1fad0f51afd2107f)

### observed_connections-004548

```text
(config-controller)# pri-group timeslots <number:1..31> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 113 `；EOL ` RVA 0x35EF7AC0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` List of timeslots which comprise the pri-group。

[条件 C-b73921bb4c846f52](../../evidence/conditions-sets-071.md#c-b73921bb4c846f52) · [缺口 G-9ed658790dd953b0](../../evidence/gaps-sets-006.md#g-9ed658790dd953b0) · [参数 P-b5801a6fec76268c](../../evidence/parameters-sets-014.md#p-b5801a6fec76268c) · [状态效果 S-ab5be1ef127acbec](../../evidence/state_effects-sets-036.md#s-ab5be1ef127acbec)

### observed_connections-004329

```text
(config-controller)# rem-loop-detect-disable <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 35 `；EOL ` RVA 0x35EE9108 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b272bdf9062ef98](../../evidence/conditions-sets-041.md#c-6b272bdf9062ef98)

### observed_connections-004440

```text
(config-controller)# scrambling cell-payload <cr>
```

Handler ` RVA 0x16144750 `；selector ` 126 `；EOL ` RVA 0x35EFAFC8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45f6e3be6d9e909b](../../evidence/conditions-sets-027.md#c-45f6e3be6d9e909b)

### observed_connections-004449

```text
(config-controller)# scrambling cell-payload <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 28 `；EOL ` RVA 0x35EEF630 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c40360437498853](../../evidence/conditions-sets-023.md#c-3c40360437498853)

### observed_connections-004379

```text
(config-controller)# secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 33 `；EOL ` RVA 0x35EE6BD0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72f1506475042b15](../../evidence/conditions-sets-044.md#c-72f1506475042b15) · [状态效果 S-f465e27a22f6f5df](../../evidence/state_effects-sets-052.md#s-f465e27a22f6f5df)

### observed_connections-004393

```text
(config-controller)# secondary-admin-state maintenance <cr>
```

Handler ` RVA 0x16144750 `；selector ` 130 `；EOL ` RVA 0x35EF32F8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7742068ce07c3d45](../../evidence/conditions-sets-046.md#c-7742068ce07c3d45) · [状态效果 S-1355c436b92e14ca](../../evidence/state_effects-sets-005.md#s-1355c436b92e14ca)

### observed_connections-004396

```text
(config-controller)# service-type cas-data <cr>
```

Handler ` RVA 0x16144750 `；selector ` 121 `；EOL ` RVA 0x35EF3CD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b396276e5f27fcd9](../../evidence/conditions-sets-069.md#c-b396276e5f27fcd9) · [状态效果 S-ca76aa3ca2cda7a1](../../evidence/state_effects-sets-043.md#s-ca76aa3ca2cda7a1)

### observed_connections-004380

```text
(config-controller)# service-type ccs-voice <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 23 `；EOL ` RVA 0x35EE7628 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c015aafce41eccf](../../evidence/conditions-sets-060.md#c-9c015aafce41eccf) · [状态效果 S-c18b09a0fcfbbf5c](../../evidence/state_effects-sets-041.md#s-c18b09a0fcfbbf5c)

### observed_connections-004320

```text
(config-controller)# shutdown <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 1 `；EOL ` RVA 0x35EE5D00 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4c0805c72ec7c22](../../evidence/conditions-sets-082.md#c-d4c0805c72ec7c22)

### observed_connections-004323

```text
(config-controller)# shutdown <cr>
```

Handler ` RVA 0x16144750 `；selector ` 103 `；EOL ` RVA 0x35EF23C8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c57c8253a34c801d](../../evidence/conditions-sets-076.md#c-c57c8253a34c801d)

### observed_connections-004326

```text
(config-controller)# shutdown <cr>
```

Handler ` RVA 0x1243E150 `；selector ` 0 `；EOL ` RVA 0x3586E7A0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2dd210f3a0318c56](../../evidence/conditions-sets-018.md#c-2dd210f3a0318c56)

### observed_connections-004460

```text
(config-controller)# snmp trap link-status <cr>
```

Handler ` RVA 0x104C38D0 `；selector ` 0 `；EOL ` RVA 0x33C3CDD8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f6532b9581deb8a](../../evidence/conditions-sets-049.md#c-7f6532b9581deb8a)

### observed_connections-004327

```text
(config-controller)# sra <cr>
```

Handler ` RVA 0x1243DA00 `；selector ` 0 `；EOL ` RVA 0x3586EB10 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49e1caa40b775f6d](../../evidence/conditions-sets-029.md#c-49e1caa40b775f6d)

### observed_connections-004324

```text
(config-controller)# sync interval <number:0..360> <cr>
```

Handler ` RVA 0x1243DD60 `；selector ` 0 `；EOL ` RVA 0x3586D800 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-c4c8a900e9b98ddf](../../evidence/conditions-sets-076.md#c-c4c8a900e9b98ddf) · [参数 P-e43ec81869910bdd](../../evidence/parameters-sets-017.md#p-e43ec81869910bdd)

### observed_connections-004476

```text
(config-controller)# sync mode none <cr>
```

Handler ` RVA 0x1243DED0 `；selector ` 0 `；EOL ` RVA 0x3586DBA8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c972fe47427d19d](../../evidence/conditions-sets-036.md#c-5c972fe47427d19d) · [状态效果 S-4e8702aee72c2e3f](../../evidence/state_effects-sets-017.md#s-4e8702aee72c2e3f)

### observed_connections-004562

```text
(config-controller)# tdm-group <number:0..23> timeslots <number:1..24> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEACA0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TDM group ID；` unsigned_number ` List of timeslots which comprise the tdm-group。

[条件 C-f490a1d2c76323ff](../../evidence/conditions-sets-094.md#c-f490a1d2c76323ff) · [缺口 G-a8cb946f1eac6762](../../evidence/gaps-sets-006.md#g-a8cb946f1eac6762) · [参数 P-8c1cae165c27c507](../../evidence/parameters-sets-011.md#p-8c1cae165c27c507) · [状态效果 S-5eeb455473ba0f5c](../../evidence/state_effects-sets-020.md#s-5eeb455473ba0f5c)

### observed_connections-004524

```text
(config-controller)# tdm-group <number:0..23> unstructured <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEACA0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-4011a4eab205c9be](../../evidence/conditions-sets-025.md#c-4011a4eab205c9be) · [参数 P-e50349e291365166](../../evidence/parameters-sets-017.md#p-e50349e291365166) · [状态效果 S-f812488bc1f1a349](../../evidence/state_effects-sets-053.md#s-f812488bc1f1a349)

### observed_connections-004561

```text
(config-controller)# tdm-group <number:0..30> timeslots <number:1..31> <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEB730 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TDM group ID；` unsigned_number ` List of timeslots which comprise the tdm-group。

[条件 C-aa4eb5b58a9ef6be](../../evidence/conditions-sets-066.md#c-aa4eb5b58a9ef6be) · [缺口 G-6bab6655a91e0007](../../evidence/gaps-sets-004.md#g-6bab6655a91e0007) · [参数 P-29e6541b2922b39d](../../evidence/parameters-sets-004.md#p-29e6541b2922b39d) · [状态效果 S-0e8a7be44bdfcb62](../../evidence/state_effects-sets-003.md#s-0e8a7be44bdfcb62)

### observed_connections-004520

```text
(config-controller)# tdm-group <number:0..30> unstructured <cr>
```

Handler ` RVA 0x15B0D370 `；selector ` 0 `；EOL ` RVA 0x35DEB730 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TDM group ID。

[条件 C-305ab7d69c60f669](../../evidence/conditions-sets-019.md#c-305ab7d69c60f669) · [参数 P-df916d37e743465e](../../evidence/parameters-sets-017.md#p-df916d37e743465e) · [状态效果 S-7bed552c2bcf9b03](../../evidence/state_effects-sets-026.md#s-7bed552c2bcf9b03)

### observed_connections-004356

```text
(config-controller)# termination co <cr>
```

Handler ` RVA 0x163CF330 `；selector ` 0 `；EOL ` RVA 0x35F81D50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-852c25b28632ec6c](../../evidence/conditions-sets-052.md#c-852c25b28632ec6c) · [状态效果 S-3665804418c7917c](../../evidence/state_effects-sets-012.md#s-3665804418c7917c)

### observed_connections-004468

```text
(config-controller)# threshold sd-ber <number:5..8> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 132 `；EOL ` RVA 0x35EF2078 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bit error rate (10 to the minus n)。

[条件 C-1af8a6867a0fc5a6](../../evidence/conditions-sets-011.md#c-1af8a6867a0fc5a6) · [参数 P-5fe2fc290a30b51a](../../evidence/parameters-sets-008.md#p-5fe2fc290a30b51a) · [状态效果 S-065b869904985839](../../evidence/state_effects-sets-002.md#s-065b869904985839)

### observed_connections-004462

```text
(config-controller)# threshold sd-ber <number:5..9> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 30 `；EOL ` RVA 0x35EE59B0 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bit error rate (10 to the minus n)。

[条件 C-dbdfc7949578cbbf](../../evidence/conditions-sets-085.md#c-dbdfc7949578cbbf) · [参数 P-24345e2aff198261](../../evidence/parameters-sets-003.md#p-24345e2aff198261) · [状态效果 S-99f1eee723f0e9f0](../../evidence/state_effects-sets-033.md#s-99f1eee723f0e9f0)

### observed_connections-004553

```text
(config-controller)# training log filename <url:dynamic> <cr>
```

Handler ` RVA 0x1243F600 `；selector ` 0 `；EOL ` RVA 0x3586D0D8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30a97441076e11f5](../../evidence/conditions-sets-019.md#c-30a97441076e11f5) · [缺口 G-e09ea19681bdefaa](../../evidence/gaps-sets-008.md#g-e09ea19681bdefaa) · [参数 P-967add3d731f95d4](../../evidence/parameters-sets-012.md#p-967add3d731f95d4)

### observed_connections-004412

```text
(config-controller)# vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 34 `；EOL ` RVA 0x35EEAD50 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-307c4744b9cc806e](../../evidence/conditions-sets-019.md#c-307c4744b9cc806e) · [参数 P-dfdb74fc1c98c978](../../evidence/parameters-sets-017.md#p-dfdb74fc1c98c978)

### observed_connections-004413

```text
(config-controller)# vcat-group <number:1..255> <cr>
```

Handler ` RVA 0x16144750 `；selector ` 131 `；EOL ` RVA 0x35EF6F90 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VCAT group number。

[条件 C-5a321b8388b2a363](../../evidence/conditions-sets-035.md#c-5a321b8388b2a363) · [参数 P-63ccf7b593ace76e](../../evidence/parameters-sets-008.md#p-63ccf7b593ace76e)

### observed_connections-004427

```text
(config-controller)# yellow generation <cr>
```

Handler ` RVA 0x1614D120 `；selector ` 24 `；EOL ` RVA 0x35EED3E8 `。

模式根 ` RVA 0x343F6430 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e5a6f5d1a5b60b0](../../evidence/conditions-sets-024.md#c-3e5a6f5d1a5b60b0) · [状态效果 S-da6e152ea68b9d09](../../evidence/state_effects-sets-046.md#s-da6e152ea68b9d09)

