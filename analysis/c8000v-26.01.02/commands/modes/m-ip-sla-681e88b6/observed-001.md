# ip-sla · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008137

```text
(config-ip-sla)# default dhcp <address> <cr>
```

Handler ` RVA 0x1033EEF0 `；selector ` 0 `；EOL ` RVA 0x34ACE630 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-503eb6417936fac8](../../evidence/conditions-sets-031.md#c-503eb6417936fac8) · [参数 P-aa64406e14251c78](../../evidence/parameters-sets-013.md#p-aa64406e14251c78) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008161

```text
(config-ip-sla)# default dns <string> name-server <address> <cr>
```

Handler ` RVA 0x103463F0 `；selector ` 0 `；EOL ` RVA 0x34AD1B80 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Target IP Address or Hostname；` address ` IP Address or hostname, broadcast disallowed。

[条件 C-0175cb35d7de23e7](../../evidence/conditions-sets-001.md#c-0175cb35d7de23e7) · [参数 P-d65af0d4f5782976](../../evidence/parameters-sets-016.md#p-d65af0d4f5782976) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008169

```text
(config-ip-sla)# default ethernet echo mpid <number:1..8191> domain <string> port <cr>
```

Handler ` RVA 0x103BFAB0 `；selector ` 0 `；EOL ` RVA 0x34B09210 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` MPID Value；` string ` Domain Name Value。

[条件 C-a842a3ecd4b8af0d](../../evidence/conditions-sets-065.md#c-a842a3ecd4b8af0d) · [参数 P-82dbc4e4fa687da8](../../evidence/parameters-sets-010.md#p-82dbc4e4fa687da8) · [状态效果 S-a852e9ce79df6687](../../evidence/state_effects-sets-036.md#s-a852e9ce79df6687)

### observed_connections-008172

```text
(config-ip-sla)# default ethernet y1731 loss LMM domain <string> evc <string> cos <number:0..8> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBF22AE0 `；selector ` 0 `；EOL ` RVA 0x339492C8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Specify the Ethernet OAM domain；` string ` Specify the EVC Identifier value；` unsigned_number ` Specify CoS value；` unsigned_number ` Local MPID value。

[条件 C-d383bcc1fce23fd6](../../evidence/conditions-sets-082.md#c-d383bcc1fce23fd6) · [参数 P-251f54c5cc49e492](../../evidence/parameters-sets-003.md#p-251f54c5cc49e492) · [状态效果 S-b87f1779243aded4](../../evidence/state_effects-sets-039.md#s-b87f1779243aded4)

### observed_connections-008154

```text
(config-ip-sla)# default ftp get <string> <cr>
```

Handler ` RVA 0x10349660 `；selector ` 0 `；EOL ` RVA 0x34AD54D0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` URL。

[参数 P-e4f860d26f1f0682](../../evidence/parameters-sets-017.md#p-e4f860d26f1f0682) · [状态效果 S-ec77ecbdcb06dd75](../../evidence/state_effects-sets-050.md#s-ec77ecbdcb06dd75)

### observed_connections-008159

```text
(config-ip-sla)# default http get <string> <cr>
```

Handler ` RVA 0x103556C0 `；selector ` 0 `；EOL ` RVA 0x34AD9518 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` URL。

[参数 P-4a31766bc00269e0](../../evidence/parameters-sets-006.md#p-4a31766bc00269e0) · [状态效果 S-a7eea0f572c0492f](../../evidence/state_effects-sets-035.md#s-a7eea0f572c0492f)

### observed_connections-008163

```text
(config-ip-sla)# default http secure get <string> <cr>
```

Handler ` RVA 0x10356950 `；selector ` 0 `；EOL ` RVA 0x34ADE158 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` URL。

[参数 P-b07fc3c17177576d](../../evidence/parameters-sets-013.md#p-b07fc3c17177576d) · [状态效果 S-0686aa3bd5d3e535](../../evidence/state_effects-sets-002.md#s-0686aa3bd5d3e535)

### observed_connections-008135

```text
(config-ip-sla)# default icmp-echo <string> <cr>
```

Handler ` RVA 0x10323F60 `；selector ` 0 `；EOL ` RVA 0x34ABBBC0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname。

[条件 C-6950fe074e277131](../../evidence/conditions-sets-041.md#c-6950fe074e277131) · [参数 P-43ee110e18ba5b5c](../../evidence/parameters-sets-006.md#p-43ee110e18ba5b5c) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008139

```text
(config-ip-sla)# default icmp-jitter <string> <cr>
```

Handler ` RVA 0x103398F0 `；selector ` 0 `；EOL ` RVA 0x34ACABF0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Destination IP address or hostname, broadcase disallowed。

[条件 C-dc64891f6d76f6ea](../../evidence/conditions-sets-085.md#c-dc64891f6d76f6ea) · [参数 P-8337543a0b28ae56](../../evidence/parameters-sets-010.md#p-8337543a0b28ae56) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008142

```text
(config-ip-sla)# default path-echo <address> <cr>
```

Handler ` RVA 0x10328A80 `；selector ` 0 `；EOL ` RVA 0x34AC0F70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-f3a822bfafba8f74](../../evidence/conditions-sets-094.md#c-f3a822bfafba8f74) · [参数 P-e66f9e849f86d530](../../evidence/parameters-sets-017.md#p-e66f9e849f86d530) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008146

```text
(config-ip-sla)# default path-jitter <address> <cr>
```

Handler ` RVA 0x103309C0 `；selector ` 0 `；EOL ` RVA 0x34AC66E8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination IP address or Hostname, broadcast disallowed。

[条件 C-2d4e907038c36765](../../evidence/conditions-sets-018.md#c-2d4e907038c36765) · [参数 P-085dc3cbd199fb4f](../../evidence/parameters-sets-001.md#p-085dc3cbd199fb4f) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008152

```text
(config-ip-sla)# default tcp-connect <string> <number:0..65535> <cr>
```

Handler ` RVA 0x1031CBD0 `；selector ` 0 `；EOL ` RVA 0x34AB6848 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-e0d565ca29b0ad05](../../evidence/conditions-sets-087.md#c-e0d565ca29b0ad05) · [参数 P-dd92460a3990b114](../../evidence/parameters-sets-017.md#p-dd92460a3990b114) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008149

```text
(config-ip-sla)# default udp-echo <string> <number:0..65535> <cr>
```

Handler ` RVA 0x10301F90 `；selector ` 0 `；EOL ` RVA 0x34AA8398 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-52b9773d953e4722](../../evidence/conditions-sets-032.md#c-52b9773d953e4722) · [参数 P-f2b22b697bde1bff](../../evidence/parameters-sets-018.md#p-f2b22b697bde1bff) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008166

```text
(config-ip-sla)# default udp-jitter <address> <number:0..65535> endpoint-list <string> <cr>
```

Handler ` RVA 0x1036DDD0 `；selector ` 0 `；EOL ` RVA 0x34AE6E70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination IP address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535；` string ` Endpoint list name。

[条件 C-ea48371454793884](../../evidence/conditions-sets-090.md#c-ea48371454793884) · [参数 P-c147bd872e9c33ba](../../evidence/parameters-sets-015.md#p-c147bd872e9c33ba) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008156

```text
(config-ip-sla)# default udp-jitter <string> <number:1..65535> <cr>
```

Handler ` RVA 0x10307C70 `；selector ` 0 `；EOL ` RVA 0x34AAE428 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Destination IP/IPv6 address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535。

[条件 C-b7ea163e5ed8c4dc](../../evidence/conditions-sets-071.md#c-b7ea163e5ed8c4dc) · [参数 P-70adabcddc7d4553](../../evidence/parameters-sets-009.md#p-70adabcddc7d4553) · [状态效果 S-dfc87ad96272bec4](../../evidence/state_effects-sets-047.md#s-dfc87ad96272bec4)

### observed_connections-008173

```text
(config-ip-sla)# dhcp <?ipv4orv6_addr_action@55558a022588> <cr>
```

Handler ` RVA 0x1033EEF0 `；selector ` 0 `；EOL ` RVA 0x34ACE630 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d5df8f4998fe0b64](../../evidence/conditions-sets-083.md#c-d5df8f4998fe0b64) · [缺口 G-46439d5c4ea2d13d](../../evidence/gaps-sets-003.md#g-46439d5c4ea2d13d)

### observed_connections-008129

```text
(config-ip-sla)# dhcp <address> <cr>
```

Handler ` RVA 0x1033EEF0 `；selector ` 0 `；EOL ` RVA 0x34ACE630 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-503eb6417936fac8](../../evidence/conditions-sets-031.md#c-503eb6417936fac8) · [参数 P-aa64406e14251c78](../../evidence/parameters-sets-013.md#p-aa64406e14251c78)

### observed_connections-008180

```text
(config-ip-sla)# dns <string> name-server <?ipv4orv6_addr_action@55558a025908> <cr>
```

Handler ` RVA 0x103463F0 `；selector ` 0 `；EOL ` RVA 0x34AD1B80 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Target IP Address or Hostname。

[条件 C-74816f8d6eb41364](../../evidence/conditions-sets-045.md#c-74816f8d6eb41364) · [缺口 G-8eb4dea1ea6fd0db](../../evidence/gaps-sets-005.md#g-8eb4dea1ea6fd0db) · [参数 P-ce0a20c935cd49b9](../../evidence/parameters-sets-016.md#p-ce0a20c935cd49b9)

### observed_connections-008155

```text
(config-ip-sla)# dns <string> name-server <address> <cr>
```

Handler ` RVA 0x103463F0 `；selector ` 0 `；EOL ` RVA 0x34AD1B80 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Target IP Address or Hostname；` address ` IP Address or hostname, broadcast disallowed。

[条件 C-0175cb35d7de23e7](../../evidence/conditions-sets-001.md#c-0175cb35d7de23e7) · [参数 P-d65af0d4f5782976](../../evidence/parameters-sets-016.md#p-d65af0d4f5782976)

### observed_connections-008184

```text
(config-ip-sla)# ethernet echo mpid <number:1..8191> domain <string> evc <string> <cr>
```

Handler ` RVA 0x103BFAB0 `；selector ` 0 `；EOL ` RVA 0x34B09210 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MPID Value；` string ` Domain Name Value；` string ` EVC ID Value。

[条件 C-e778224e4e23250a](../../evidence/conditions-sets-089.md#c-e778224e4e23250a) · [缺口 G-c32764b789e90aa3](../../evidence/gaps-sets-007.md#g-c32764b789e90aa3) · [参数 P-1b259c37858d7ea0](../../evidence/parameters-sets-003.md#p-1b259c37858d7ea0) · [状态效果 S-977d5d9c31955309](../../evidence/state_effects-sets-032.md#s-977d5d9c31955309)

### observed_connections-008167

```text
(config-ip-sla)# ethernet echo mpid <number:1..8191> domain <string> port <cr>
```

Handler ` RVA 0x103BFAB0 `；selector ` 0 `；EOL ` RVA 0x34B09210 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MPID Value；` string ` Domain Name Value。

[条件 C-a842a3ecd4b8af0d](../../evidence/conditions-sets-065.md#c-a842a3ecd4b8af0d) · [参数 P-82dbc4e4fa687da8](../../evidence/parameters-sets-010.md#p-82dbc4e4fa687da8) · [状态效果 S-9d8d1e0aef0b0d8c](../../evidence/state_effects-sets-033.md#s-9d8d1e0aef0b0d8c)

### observed_connections-008185

```text
(config-ip-sla)# ethernet y1731 delay 1DM domain <string> evc <string> cos <number:0..8> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBF1ED70 `；selector ` 0 `；EOL ` RVA 0x33944318 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the Ethernet OAM domain；` string ` Specify the EVC Identifier value；` unsigned_number ` Specify CoS value；` unsigned_number ` Local MPID value。

[条件 C-725897126540d296](../../evidence/conditions-sets-044.md#c-725897126540d296) · [缺口 G-b2a035f066e96a1b](../../evidence/gaps-sets-006.md#g-b2a035f066e96a1b) · [参数 P-c569f54359bc7425](../../evidence/parameters-sets-015.md#p-c569f54359bc7425) · [状态效果 S-e8560a2e4245d3d4](../../evidence/state_effects-sets-049.md#s-e8560a2e4245d3d4)

### observed_connections-008170

```text
(config-ip-sla)# ethernet y1731 loss LMM domain <string> evc <string> cos <number:0..8> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBF22AE0 `；selector ` 0 `；EOL ` RVA 0x339492C8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the Ethernet OAM domain；` string ` Specify the EVC Identifier value；` unsigned_number ` Specify CoS value；` unsigned_number ` Local MPID value。

[条件 C-d383bcc1fce23fd6](../../evidence/conditions-sets-082.md#c-d383bcc1fce23fd6) · [参数 P-251f54c5cc49e492](../../evidence/parameters-sets-003.md#p-251f54c5cc49e492) · [状态效果 S-0dbbea9d28b38ab9](../../evidence/state_effects-sets-003.md#s-0dbbea9d28b38ab9)

### observed_connections-008186

```text
(config-ip-sla)# ethernet y1731 loss SLM domain <string> evc <string> cos <number:0..8> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBF22AE0 `；selector ` 0 `；EOL ` RVA 0x339492C8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the Ethernet OAM domain；` string ` Specify the EVC Identifier value；` unsigned_number ` Specify CoS value；` unsigned_number ` Local MPID value。

[条件 C-0cf7efb148c0a28e](../../evidence/conditions-sets-005.md#c-0cf7efb148c0a28e) · [缺口 G-8bdbda3dca885664](../../evidence/gaps-sets-005.md#g-8bdbda3dca885664) · [参数 P-251f54c5cc49e492](../../evidence/parameters-sets-003.md#p-251f54c5cc49e492) · [状态效果 S-7631574899d34ba9](../../evidence/state_effects-sets-025.md#s-7631574899d34ba9)

### observed_connections-008143

```text
(config-ip-sla)# ftp get <string> <cr>
```

Handler ` RVA 0x10349660 `；selector ` 0 `；EOL ` RVA 0x34AD54D0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL。

[参数 P-e4f860d26f1f0682](../../evidence/parameters-sets-017.md#p-e4f860d26f1f0682) · [状态效果 S-bdbf38a6c251ba05](../../evidence/state_effects-sets-040.md#s-bdbf38a6c251ba05)

### observed_connections-008147

```text
(config-ip-sla)# http get <string> <cr>
```

Handler ` RVA 0x103556C0 `；selector ` 0 `；EOL ` RVA 0x34AD9518 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL。

[参数 P-4a31766bc00269e0](../../evidence/parameters-sets-006.md#p-4a31766bc00269e0) · [状态效果 S-d6bb2c42c9ab4fba](../../evidence/state_effects-sets-046.md#s-d6bb2c42c9ab4fba)

### observed_connections-008182

```text
(config-ip-sla)# http get <string> name-server <?ipv4orv6_addr_action@55558a02cf70> <cr>
```

Handler ` RVA 0x103556C0 `；selector ` 0 `；EOL ` RVA 0x34AD9518 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` URL。

[条件 C-d9b57056a72ffa12](../../evidence/conditions-sets-084.md#c-d9b57056a72ffa12) · [缺口 G-277d978bf78007e7](../../evidence/gaps-sets-002.md#g-277d978bf78007e7) · [参数 P-4a31766bc00269e0](../../evidence/parameters-sets-006.md#p-4a31766bc00269e0) · [状态效果 S-7d9c85292197877a](../../evidence/state_effects-sets-027.md#s-7d9c85292197877a)

### observed_connections-008157

```text
(config-ip-sla)# http secure get <string> <cr>
```

Handler ` RVA 0x10356950 `；selector ` 0 `；EOL ` RVA 0x34ADE158 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL。

[参数 P-b07fc3c17177576d](../../evidence/parameters-sets-013.md#p-b07fc3c17177576d) · [状态效果 S-96394d157e48dd45](../../evidence/state_effects-sets-032.md#s-96394d157e48dd45)

### observed_connections-008183

```text
(config-ip-sla)# http secure get <string> source-interface <interface> <cr>
```

Handler ` RVA 0x10356950 `；selector ` 0 `；EOL ` RVA 0x34ADE158 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` URL。

[条件 C-d261256b429ba8cb](../../evidence/conditions-sets-081.md#c-d261256b429ba8cb) · [缺口 G-6b08c59b4f2084c5](../../evidence/gaps-sets-004.md#g-6b08c59b4f2084c5) · [参数 P-d802dc6222fe5d2d](../../evidence/parameters-sets-016.md#p-d802dc6222fe5d2d) · [状态效果 S-96394d157e48dd45](../../evidence/state_effects-sets-032.md#s-96394d157e48dd45)

### observed_connections-008174

```text
(config-ip-sla)# icmp-echo <?ipv4orv6_addr_action@55558a010058> <cr>
```

Handler ` RVA 0x10323F60 `；selector ` 0 `；EOL ` RVA 0x34ABBBC0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f96186a244c6f6e](../../evidence/conditions-sets-037.md#c-5f96186a244c6f6e) · [缺口 G-444168110a42cc1d](../../evidence/gaps-sets-003.md#g-444168110a42cc1d)

### observed_connections-008128

```text
(config-ip-sla)# icmp-echo <string> <cr>
```

Handler ` RVA 0x10323F60 `；selector ` 0 `；EOL ` RVA 0x34ABBBC0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname。

[条件 C-6950fe074e277131](../../evidence/conditions-sets-041.md#c-6950fe074e277131) · [参数 P-43ee110e18ba5b5c](../../evidence/parameters-sets-006.md#p-43ee110e18ba5b5c)

### observed_connections-008130

```text
(config-ip-sla)# icmp-jitter <string> <cr>
```

Handler ` RVA 0x103398F0 `；selector ` 0 `；EOL ` RVA 0x34ACABF0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination IP address or hostname, broadcase disallowed。

[条件 C-dc64891f6d76f6ea](../../evidence/conditions-sets-085.md#c-dc64891f6d76f6ea) · [参数 P-8337543a0b28ae56](../../evidence/parameters-sets-010.md#p-8337543a0b28ae56)

### observed_connections-008134

```text
(config-ip-sla)# no dhcp <address> <cr>
```

Handler ` RVA 0x1033EEF0 `；selector ` 0 `；EOL ` RVA 0x34ACE630 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-503eb6417936fac8](../../evidence/conditions-sets-031.md#c-503eb6417936fac8) · [参数 P-aa64406e14251c78](../../evidence/parameters-sets-013.md#p-aa64406e14251c78) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008160

```text
(config-ip-sla)# no dns <string> name-server <address> <cr>
```

Handler ` RVA 0x103463F0 `；selector ` 0 `；EOL ` RVA 0x34AD1B80 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Target IP Address or Hostname；` address ` IP Address or hostname, broadcast disallowed。

[条件 C-0175cb35d7de23e7](../../evidence/conditions-sets-001.md#c-0175cb35d7de23e7) · [参数 P-d65af0d4f5782976](../../evidence/parameters-sets-016.md#p-d65af0d4f5782976) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008168

```text
(config-ip-sla)# no ethernet echo mpid <number:1..8191> domain <string> port <cr>
```

Handler ` RVA 0x103BFAB0 `；selector ` 0 `；EOL ` RVA 0x34B09210 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` MPID Value；` string ` Domain Name Value。

[条件 C-a842a3ecd4b8af0d](../../evidence/conditions-sets-065.md#c-a842a3ecd4b8af0d) · [参数 P-82dbc4e4fa687da8](../../evidence/parameters-sets-010.md#p-82dbc4e4fa687da8) · [状态效果 S-6ebe7b73bd17af35](../../evidence/state_effects-sets-024.md#s-6ebe7b73bd17af35)

### observed_connections-008171

```text
(config-ip-sla)# no ethernet y1731 loss LMM domain <string> evc <string> cos <number:0..8> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBF22AE0 `；selector ` 0 `；EOL ` RVA 0x339492C8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the Ethernet OAM domain；` string ` Specify the EVC Identifier value；` unsigned_number ` Specify CoS value；` unsigned_number ` Local MPID value。

[条件 C-d383bcc1fce23fd6](../../evidence/conditions-sets-082.md#c-d383bcc1fce23fd6) · [参数 P-251f54c5cc49e492](../../evidence/parameters-sets-003.md#p-251f54c5cc49e492) · [状态效果 S-29f55cdeb0ef03f9](../../evidence/state_effects-sets-009.md#s-29f55cdeb0ef03f9)

### observed_connections-008151

```text
(config-ip-sla)# no ftp get <string> <cr>
```

Handler ` RVA 0x10349660 `；selector ` 0 `；EOL ` RVA 0x34AD54D0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL。

[参数 P-e4f860d26f1f0682](../../evidence/parameters-sets-017.md#p-e4f860d26f1f0682) · [状态效果 S-68a383970db93063](../../evidence/state_effects-sets-022.md#s-68a383970db93063)

### observed_connections-008158

```text
(config-ip-sla)# no http get <string> <cr>
```

Handler ` RVA 0x103556C0 `；selector ` 0 `；EOL ` RVA 0x34AD9518 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL。

[参数 P-4a31766bc00269e0](../../evidence/parameters-sets-006.md#p-4a31766bc00269e0) · [状态效果 S-e37b21fe53637b9d](../../evidence/state_effects-sets-048.md#s-e37b21fe53637b9d)

### observed_connections-008162

```text
(config-ip-sla)# no http secure get <string> <cr>
```

Handler ` RVA 0x10356950 `；selector ` 0 `；EOL ` RVA 0x34ADE158 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL。

[参数 P-b07fc3c17177576d](../../evidence/parameters-sets-013.md#p-b07fc3c17177576d) · [状态效果 S-41412dd58ddd9fe2](../../evidence/state_effects-sets-014.md#s-41412dd58ddd9fe2)

### observed_connections-008133

```text
(config-ip-sla)# no icmp-echo <string> <cr>
```

Handler ` RVA 0x10323F60 `；selector ` 0 `；EOL ` RVA 0x34ABBBC0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname。

[条件 C-6950fe074e277131](../../evidence/conditions-sets-041.md#c-6950fe074e277131) · [参数 P-43ee110e18ba5b5c](../../evidence/parameters-sets-006.md#p-43ee110e18ba5b5c) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008138

```text
(config-ip-sla)# no icmp-jitter <string> <cr>
```

Handler ` RVA 0x103398F0 `；selector ` 0 `；EOL ` RVA 0x34ACABF0 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Destination IP address or hostname, broadcase disallowed。

[条件 C-dc64891f6d76f6ea](../../evidence/conditions-sets-085.md#c-dc64891f6d76f6ea) · [参数 P-8337543a0b28ae56](../../evidence/parameters-sets-010.md#p-8337543a0b28ae56) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008140

```text
(config-ip-sla)# no path-echo <address> <cr>
```

Handler ` RVA 0x10328A80 `；selector ` 0 `；EOL ` RVA 0x34AC0F70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-f3a822bfafba8f74](../../evidence/conditions-sets-094.md#c-f3a822bfafba8f74) · [参数 P-e66f9e849f86d530](../../evidence/parameters-sets-017.md#p-e66f9e849f86d530) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008145

```text
(config-ip-sla)# no path-jitter <address> <cr>
```

Handler ` RVA 0x103309C0 `；selector ` 0 `；EOL ` RVA 0x34AC66E8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination IP address or Hostname, broadcast disallowed。

[条件 C-2d4e907038c36765](../../evidence/conditions-sets-018.md#c-2d4e907038c36765) · [参数 P-085dc3cbd199fb4f](../../evidence/parameters-sets-001.md#p-085dc3cbd199fb4f) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008150

```text
(config-ip-sla)# no tcp-connect <string> <number:0..65535> <cr>
```

Handler ` RVA 0x1031CBD0 `；selector ` 0 `；EOL ` RVA 0x34AB6848 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-e0d565ca29b0ad05](../../evidence/conditions-sets-087.md#c-e0d565ca29b0ad05) · [参数 P-dd92460a3990b114](../../evidence/parameters-sets-017.md#p-dd92460a3990b114) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008148

```text
(config-ip-sla)# no udp-echo <string> <number:0..65535> <cr>
```

Handler ` RVA 0x10301F90 `；selector ` 0 `；EOL ` RVA 0x34AA8398 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-52b9773d953e4722](../../evidence/conditions-sets-032.md#c-52b9773d953e4722) · [参数 P-f2b22b697bde1bff](../../evidence/parameters-sets-018.md#p-f2b22b697bde1bff) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008165

```text
(config-ip-sla)# no udp-jitter <address> <number:0..65535> endpoint-list <string> <cr>
```

Handler ` RVA 0x1036DDD0 `；selector ` 0 `；EOL ` RVA 0x34AE6E70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination IP address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535；` string ` Endpoint list name。

[条件 C-ea48371454793884](../../evidence/conditions-sets-090.md#c-ea48371454793884) · [参数 P-c147bd872e9c33ba](../../evidence/parameters-sets-015.md#p-c147bd872e9c33ba) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008153

```text
(config-ip-sla)# no udp-jitter <string> <number:1..65535> <cr>
```

Handler ` RVA 0x10307C70 `；selector ` 0 `；EOL ` RVA 0x34AAE428 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Destination IP/IPv6 address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535。

[条件 C-b7ea163e5ed8c4dc](../../evidence/conditions-sets-071.md#c-b7ea163e5ed8c4dc) · [参数 P-70adabcddc7d4553](../../evidence/parameters-sets-009.md#p-70adabcddc7d4553) · [状态效果 S-6f8d10e4532c09bb](../../evidence/state_effects-sets-024.md#s-6f8d10e4532c09bb)

### observed_connections-008175

```text
(config-ip-sla)# path-echo <?ipv4orv6_addr_action@55558a014ec8> <cr>
```

Handler ` RVA 0x10328A80 `；selector ` 0 `；EOL ` RVA 0x34AC0F70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54ee1f1ba3f04524](../../evidence/conditions-sets-033.md#c-54ee1f1ba3f04524) · [缺口 G-c5841029aa3ea9c3](../../evidence/gaps-sets-007.md#g-c5841029aa3ea9c3)

### observed_connections-008131

```text
(config-ip-sla)# path-echo <address> <cr>
```

Handler ` RVA 0x10328A80 `；selector ` 0 `；EOL ` RVA 0x34AC0F70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address or hostname, broadcast disallowed。

[条件 C-f3a822bfafba8f74](../../evidence/conditions-sets-094.md#c-f3a822bfafba8f74) · [参数 P-e66f9e849f86d530](../../evidence/parameters-sets-017.md#p-e66f9e849f86d530)

### observed_connections-008176

```text
(config-ip-sla)# path-jitter <?ipv4orv6_addr_action@55558a01a3d8> <cr>
```

Handler ` RVA 0x103309C0 `；selector ` 0 `；EOL ` RVA 0x34AC66E8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d986ab7cb07d9075](../../evidence/conditions-sets-084.md#c-d986ab7cb07d9075) · [缺口 G-c8812e6d755aa8bf](../../evidence/gaps-sets-007.md#g-c8812e6d755aa8bf)

### observed_connections-008132

```text
(config-ip-sla)# path-jitter <address> <cr>
```

Handler ` RVA 0x103309C0 `；selector ` 0 `；EOL ` RVA 0x34AC66E8 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address or Hostname, broadcast disallowed。

[条件 C-2d4e907038c36765](../../evidence/conditions-sets-018.md#c-2d4e907038c36765) · [参数 P-085dc3cbd199fb4f](../../evidence/parameters-sets-001.md#p-085dc3cbd199fb4f)

### observed_connections-008178

```text
(config-ip-sla)# tcp-connect <?ipv4orv6_addr_action@55558a00abd0> <number:0..65535> <cr>
```

Handler ` RVA 0x1031CBD0 `；selector ` 0 `；EOL ` RVA 0x34AB6848 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-1289142228dab056](../../evidence/conditions-sets-007.md#c-1289142228dab056) · [缺口 G-7e91010484520001](../../evidence/gaps-sets-005.md#g-7e91010484520001) · [参数 P-8af8184f7d6ff72d](../../evidence/parameters-sets-011.md#p-8af8184f7d6ff72d)

### observed_connections-008141

```text
(config-ip-sla)# tcp-connect <string> <number:0..65535> <cr>
```

Handler ` RVA 0x1031CBD0 `；selector ` 0 `；EOL ` RVA 0x34AB6848 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-e0d565ca29b0ad05](../../evidence/conditions-sets-087.md#c-e0d565ca29b0ad05) · [参数 P-dd92460a3990b114](../../evidence/parameters-sets-017.md#p-dd92460a3990b114)

### observed_connections-008177

```text
(config-ip-sla)# udp-echo <?ipv4orv6_addr_action@555589ffc720> <number:0..65535> <cr>
```

Handler ` RVA 0x10301F90 `；selector ` 0 `；EOL ` RVA 0x34AA8398 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-9294aa1c866fb2b0](../../evidence/conditions-sets-057.md#c-9294aa1c866fb2b0) · [缺口 G-35cd7eeb2f1a434d](../../evidence/gaps-sets-002.md#g-35cd7eeb2f1a434d) · [参数 P-57b7dd299ae5f000](../../evidence/parameters-sets-007.md#p-57b7dd299ae5f000)

### observed_connections-008136

```text
(config-ip-sla)# udp-echo <string> <number:0..65535> <cr>
```

Handler ` RVA 0x10301F90 `；selector ` 0 `；EOL ` RVA 0x34AA8398 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination IPv6/IP address or hostname；` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-52b9773d953e4722](../../evidence/conditions-sets-032.md#c-52b9773d953e4722) · [参数 P-f2b22b697bde1bff](../../evidence/parameters-sets-018.md#p-f2b22b697bde1bff)

### observed_connections-008181

```text
(config-ip-sla)# udp-jitter <?ipv4orv6_addr_action@55558a0029e8> <number:0..65535> endpoint-list <string> <cr>
```

Handler ` RVA 0x1036DDD0 `；selector ` 0 `；EOL ` RVA 0x34AE6E70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535；` string ` Endpoint list name。

[条件 C-61153c3f012e8eef](../../evidence/conditions-sets-038.md#c-61153c3f012e8eef) · [缺口 G-6553f5cef5e538d1](../../evidence/gaps-sets-004.md#g-6553f5cef5e538d1) · [参数 P-d0f013cb391b712a](../../evidence/parameters-sets-016.md#p-d0f013cb391b712a)

### observed_connections-008179

```text
(config-ip-sla)# udp-jitter <?ipv4orv6_addr_action@55558a0029e8> <number:1..65535> <cr>
```

Handler ` RVA 0x10307C70 `；selector ` 0 `；EOL ` RVA 0x34AAE428 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535。

[条件 C-1b8af8feeb9d9248](../../evidence/conditions-sets-011.md#c-1b8af8feeb9d9248) · [缺口 G-6553f5cef5e538d1](../../evidence/gaps-sets-004.md#g-6553f5cef5e538d1) · [参数 P-3f0f969df2548676](../../evidence/parameters-sets-005.md#p-3f0f969df2548676)

### observed_connections-008164

```text
(config-ip-sla)# udp-jitter <address> <number:0..65535> endpoint-list <string> <cr>
```

Handler ` RVA 0x1036DDD0 `；selector ` 0 `；EOL ` RVA 0x34AE6E70 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535；` string ` Endpoint list name。

[条件 C-ea48371454793884](../../evidence/conditions-sets-090.md#c-ea48371454793884) · [参数 P-c147bd872e9c33ba](../../evidence/parameters-sets-015.md#p-c147bd872e9c33ba)

### observed_connections-008144

```text
(config-ip-sla)# udp-jitter <string> <number:1..65535> <cr>
```

Handler ` RVA 0x10307C70 `；selector ` 0 `；EOL ` RVA 0x34AAE428 `。

模式根 ` RVA 0x34A94238 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination IP/IPv6 address or hostname；` unsigned_number ` Port Number. Recommended ports greater than 1023. For codec options recommended port range is an Even Port range between 16384-32767 or 49152-65535。

[条件 C-b7ea163e5ed8c4dc](../../evidence/conditions-sets-071.md#c-b7ea163e5ed8c4dc) · [参数 P-70adabcddc7d4553](../../evidence/parameters-sets-009.md#p-70adabcddc7d4553)

