# 条件明细

[返回参考索引](README.md) · [阅读说明](../README.md)

### Ca-f470b02481ca2d2d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3572A3B8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f470f78e88d8ff0e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AA48240",
  "kind": "predicate",
  "node_rva": "0x36D51EE0"
}
```

### Ca-f47319ee1d5e41b8

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36067928",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f47558246c13c2ea

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36FF4D20",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f478e957744f88ea

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x34909838"
}
```

### Ca-f47a174bfb4eea0b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1615C1C0",
  "kind": "predicate",
  "node_rva": "0x35EE7B68"
}
```

### Ca-f47a8c86f6b33af1

```json
{
  "callback_rva": "0x1938FC70",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x369C9C80"
}
```

### Ca-f47df2e2f5824cd6

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D7CE60",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f47e3f286380353f

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825181549152,
      "reason": "Producer semantics unresolved; no function executed"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x337B5300",
  "source": {
    "dynamic_scratch_entry": false,
    "getter": 93825181549152,
    "kind": "producer_callback",
    "producer_executed": false,
    "release_callback": null
  }
}
```

### Ca-f482532b3af90c68

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825222112832,
      "reason": "Producer semantics unresolved; no function executed"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x33FCFAF0",
  "source": {
    "dynamic_scratch_entry": false,
    "getter": 93825222112832,
    "kind": "producer_callback",
    "producer_executed": false,
    "release_callback": null
  }
}
```

### Ca-f487312414c0c8b5

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34696F08",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f48e390e0c4c0c56

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xEE98890",
  "kind": "predicate",
  "node_rva": "0x344558A0"
}
```

### Ca-f48e98a7ef978ca5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3476A588",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f48f1990469d0b49

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3681BCE8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f49139a2d027b807

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34268478",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f491c2194919d459

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3784CDD8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f493f88b6354124b

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x357C0780",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f499f598bcbae8bb

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF02BF70",
  "kind": "predicate",
  "node_rva": "0x344D8BC0"
}
```

### Ca-f49a358b7cdbea30

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x344C9A88",
  "snapshot_only": true
}
```

### Ca-f4a20411eb633357

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDFFEAB0",
  "kind": "predicate",
  "node_rva": "0x341439C8"
}
```

### Ca-f4a4f6ca0381279c

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34A90440",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f4a546f7ea9e1c78

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x19414450",
  "kind": "predicate",
  "node_rva": "0x369DFF90"
}
```

### Ca-f4a9389a2fec9d35

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x34650F58",
  "snapshot_only": true
}
```

### Ca-f4ab1ac76e8e1de7

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x34A35FC0"
}
```

### Ca-f4b0c77b061719a6

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36ADBCF0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f4b46d2e5d9dd1fb

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3443F588",
  "parameter_omitted": false,
  "sense": 0
}
```

### Ca-f4b7af384f938e19

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x364679D8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f4bb83a865bd618d

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x172DB220",
  "kind": "predicate",
  "node_rva": "0x363604B0"
}
```

### Ca-f4bcb25ab2f693a8

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1AA050B0",
  "kind": "predicate",
  "node_rva": "0x36D29DB0"
}
```

### Ca-f4c3503fba881771

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDAD4680",
  "kind": "predicate",
  "node_rva": "0x33FCBF28"
}
```

### Ca-f4c419d3cffcb763

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825924716544,
      "reason": "Option keyword is not a single printable token",
      "text": "ipv6 pmtud"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x34826340",
  "source": {
    "dynamic_scratch_entry": false,
    "getter": null,
    "kind": "array",
    "producer_executed": false,
    "release_callback": null,
    "table_address": 93825924716352
  }
}
```

### Ca-f4c51a96cef3bd8c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x338AF198",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f4c8601a03a4a3ab

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xECEB5F0",
  "kind": "predicate",
  "node_rva": "0x343E3470"
}
```

### Ca-f4c9568bc28fd4a7

```json
{
  "context_fields": [
    14368,
    14896,
    15064,
    11960,
    12280,
    14372,
    14900,
    13620,
    12124
  ],
  "evaluated": false,
  "expected": false,
  "expression": "multiple_functions_check(csb) || remaining_input_check(csb)",
  "kind": "parser_ambiguity_or_remaining_input",
  "node_rva": "0x35752040",
  "normal_cli_only": true
}
```

### Ca-f4cf7186c947b1f7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF0145C0",
  "kind": "predicate",
  "node_rva": "0x3449D4F8"
}
```

### Ca-f4d209988e7e11c5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF125DF0",
  "kind": "predicate",
  "node_rva": "0x34577008"
}
```

### Ca-f4da1775fd97e85e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE093480",
  "kind": "predicate",
  "node_rva": "0x341E5670"
}
```

### Ca-f4dc738b797b9452

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36668F78",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f4e464942220dfa2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x363EAA28",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f4e7f58d4321768d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34954C60",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f4e9f27ac4c8a107

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378B2F30",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f4ea4fea324c88f0

```json
{
  "callback_rva": "0xEC57A10",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x343E48A0"
}
```

### Ca-f4eae3d62629f0d6

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xBF803A0",
  "kind": "predicate",
  "node_rva": "0x33958E80"
}
```

### Ca-f4eb4d8ffc86235c

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xCC7C980",
  "kind": "predicate",
  "node_rva": "0x33C32980"
}
```

### Ca-f4ed6c1801956627

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFCEBE80",
  "kind": "predicate",
  "node_rva": "0x3487FF90"
}
```

### Ca-f4ee847db879a13a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347319C0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f4f2c79ab42d1734

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE4F5D20",
  "kind": "predicate",
  "node_rva": "0x342E1928"
}
```

### Ca-f4f39511e952476e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE90F570",
  "kind": "predicate",
  "node_rva": "0x34342F70"
}
```

### Ca-f4f39e211b580c6a

```json
{
  "code": 45,
  "evaluated": false,
  "kind": "exact_input_character",
  "node_rva": "0x34B2EC70",
  "surrounding_whitespace_inferred": false
}
```

### Ca-f4f54eb3751f83aa

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF02B620",
  "kind": "predicate",
  "node_rva": "0x344D6800"
}
```

### Ca-f4f71e2e628c379d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF61C5A0",
  "kind": "predicate",
  "node_rva": "0x346FF7F8"
}
```

### Ca-f4fbb9b8832e720e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xEF165E0",
  "kind": "predicate",
  "node_rva": "0x3446DBC0"
}
```

### Ca-f4fde4b9719f72c2

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x37590490",
  "snapshot_only": true
}
```

### Ca-f4fe32dbebf2d593

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347CBC90",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f4ff255b28e959f0

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34138130",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f4ff8ec9e7e38d60

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x12528A00",
  "kind": "predicate",
  "node_rva": "0x35893148"
}
```

### Ca-f5010c5bcee015a2

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF61C2D0",
  "kind": "predicate",
  "node_rva": "0x346FF308"
}
```

### Ca-f503df6d135b8ab8

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF479800",
  "kind": "predicate",
  "node_rva": "0x346568C0"
}
```

### Ca-f50afd51fa3d227f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD8919E0",
  "kind": "predicate",
  "node_rva": "0x33F11410"
}
```

### Ca-f50d79f96a7079e3

```json
{
  "code": 46,
  "evaluated": false,
  "kind": "exact_input_character",
  "node_rva": "0x3539EB10",
  "surrounding_whitespace_inferred": false
}
```

### Ca-f50ef6a03962bd9e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF013E70",
  "kind": "predicate",
  "node_rva": "0x34493280"
}
```

### Ca-f5104384f06f4e90

```json
{
  "evaluated": false,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33F8F7D0",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f512b5aba194354e

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x36D2A950",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f514bf1dbfda3433

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF1474E0",
  "kind": "predicate",
  "node_rva": "0x345C64C0"
}
```

### Ca-f5168a915d2ff0c1

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x338F1DB8",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f517c6c97e8e2b57

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xEB6D950",
  "kind": "predicate",
  "node_rva": "0x343BD298"
}
```

### Ca-f51a2715c0a86bf1

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1D511860",
  "kind": "predicate",
  "node_rva": "0x3759B948"
}
```

### Ca-f51c7becac78e32a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x183877F0",
  "kind": "predicate",
  "node_rva": "0x36748F68"
}
```

### Ca-f51f7206a3d04b6c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34668FA0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f52008763fd0e2a4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D739E8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5211c78b5adb352

```json
{
  "context_fields": [
    14368,
    14896,
    15064,
    11960,
    12280,
    14372,
    14900,
    13620,
    12124
  ],
  "evaluated": false,
  "expected": false,
  "expression": "multiple_functions_check(csb) || remaining_input_check(csb)",
  "kind": "parser_ambiguity_or_remaining_input",
  "node_rva": "0x33D8F738",
  "normal_cli_only": true
}
```

### Ca-f521ecef01357480

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11AA1C30",
  "kind": "predicate",
  "node_rva": "0x355DE238"
}
```

### Ca-f52331e7a2060025

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36076150",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f5238c3e512653d5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34CD1048",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5264a59c5c5763d

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x357EEE08",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f5270f97ca9ff8cb

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x378BB148",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f52888e452b86866

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF028480",
  "kind": "predicate",
  "node_rva": "0x344B2440"
}
```

### Ca-f5289dea4008299e

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34569518",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-f529b688dbd862af

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F2808",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f52f20e20b9625ec

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x344989E8",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f531347bccbf0aa8

```json
{
  "callback_rva": "0xEC58240",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x343DE2F0"
}
```

### Ca-f53317fe941d4531

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x13A87680",
  "kind": "predicate",
  "node_rva": "0x35CAA998"
}
```

### Ca-f533896b6daa1054

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBD437C0",
  "kind": "predicate",
  "node_rva": "0x338F03C0"
}
```

### Ca-f535b23bead4505f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3491BC38",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f537bf5abd0e8db9

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BCF030",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5391cdaa602ba5d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x337D56D0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5399f2251a5de21

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF4DA1D0",
  "kind": "predicate",
  "node_rva": "0x3466BB98"
}
```

### Ca-f53a450675dacbe6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFA35780",
  "kind": "predicate",
  "node_rva": "0x347DA6C0"
}
```

### Ca-f53ae6afd93b1803

```json
{
  "address_type_candidate": 20,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x34212878",
  "registry_rva": "0x3CB56200"
}
```

### Ca-f53bb41f05789296

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33C450B0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f53be4fdb24642c8

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF123240",
  "kind": "predicate",
  "node_rva": "0x345614F8"
}
```

### Ca-f53cc48b59bf33bd

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34708190",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f53e23a2dd37712e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1ADF6DB0",
  "kind": "predicate",
  "node_rva": "0x36E0BF20"
}
```

### Ca-f53faa02e15725c3

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1615F590",
  "kind": "predicate",
  "node_rva": "0x35EF1120"
}
```

### Ca-f540b58996fde72e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x172952A0",
  "kind": "predicate",
  "node_rva": "0x3634C830"
}
```

### Ca-f5420cb48073a277

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x105B3290",
  "kind": "predicate",
  "node_rva": "0x34B61CC8"
}
```

### Ca-f5438e0c138f3fe6

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x3580BA10",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f543ac3be2e84a98

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3557B950",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f544d0ae79107ef4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34899438",
  "state": [
    1,
    1,
    0
  ]
}
```

### Ca-f5474028fc4f743b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xED68800",
  "kind": "predicate",
  "node_rva": "0x34416760"
}
```

### Ca-f549ea82b19b81ab

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346892C8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f54d2aa6b2158c29

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347304C0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f54d455a6636596f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xCAFBC90",
  "kind": "predicate",
  "node_rva": "0x33BAF020"
}
```

### Ca-f551ea29e904634e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33C13760",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f55263560df7500b

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x36E8F598",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f553134cbf6ff7b9

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346AE1D8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f55776a1f427e2b4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345A2688",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f55896ec8e33ea02

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x10BDF330",
  "kind": "predicate",
  "node_rva": "0x34CCEBD8"
}
```

### Ca-f559da9526cae4b6

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378A6408",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f55a1cc2bf82b33c

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3557B278",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f55c5a45517a2bda

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1246F290",
  "kind": "predicate",
  "node_rva": "0x358762C0"
}
```

### Ca-f55ec5a9bb859509

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF5DAEF0",
  "kind": "predicate",
  "node_rva": "0x346C1890"
}
```

### Ca-f56208aadf1523b9

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347C5190",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f564c53cd00cf55e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFCF4D80",
  "kind": "predicate",
  "node_rva": "0x348B6CA8"
}
```

### Ca-f568476d82a3fd40

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33927C38",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f568994b5cc0695c

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35A1D758"
}
```

### Ca-f56a70fd5d9e4892

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346CB4F0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f56b8aa966235fc3

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x369B6B10",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f56d9e5691f2c472

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x370474E0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f578c09322ec7c52

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x36DA4C98",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-f57d7262e4d1bff8

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AE08040",
  "kind": "predicate",
  "node_rva": "0x36E2E750"
}
```

### Ca-f57e61766aff4f65

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3370E190",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f57fc4ad9eea67a3

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x118BC190",
  "kind": "predicate",
  "node_rva": "0x3559D5A8"
}
```

### Ca-f580e4538ea38f3c

```json
{
  "callback_rva": "0x1E730700",
  "evaluated": false,
  "expected": true,
  "kind": "no_argument_predicate",
  "node_rva": "0x3691F850",
  "normal_cli_only": true
}
```

### Ca-f5821055367f8b06

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x339B0738",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f58621e5ca961bbc

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D34A20",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f58f2bf8d0421363

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36BE5600",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f591777861cc0fb6

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346550A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f5919eb38813a48b

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x34B20680",
  "snapshot_only": true
}
```

### Ca-f591bec19eea8a65

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF61D480",
  "kind": "predicate",
  "node_rva": "0x34706220"
}
```

### Ca-f5926df0ed4e100a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345730A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f592c158d6566ed2

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x16014660",
  "kind": "predicate",
  "node_rva": "0x35E99860"
}
```

### Ca-f5940d505bbc0b82

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36BE73B0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f5943e0d1ce6f704

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346AB4C8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f595d7c2d529e810

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x35F6FC40",
  "snapshot_only": true
}
```

### Ca-f59a074bf6e386ee

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x337DD4A0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5a0867914deafa0

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825239137888,
      "reason": "Producer semantics unresolved; no function executed"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x343C3528",
  "source": {
    "dynamic_scratch_entry": true,
    "getter": 93825239137888,
    "kind": "producer_callback",
    "producer_executed": false,
    "release_callback": 93825239138416
  }
}
```

### Ca-f5a2663a542c5684

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF1488B0",
  "kind": "predicate",
  "node_rva": "0x345CCD60"
}
```

### Ca-f5a367021db78a72

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x34B68EA8",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f5a5e0360c18ca18

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x15FA1AD0",
  "kind": "predicate",
  "node_rva": "0x35E7F5F8"
}
```

### Ca-f5a9bdfc09d8f8a4

```json
{
  "evaluated": false,
  "flags_encoded_hex": "02400000",
  "kind": "general_keyword_flags_and_privilege",
  "minimum_match_candidate": 0,
  "node_captured_va": "0x7FFFBAEDD030",
  "privilege_descriptor_address": 140736329030368
}
```

### Ca-f5aad7157cc22480

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF61D350",
  "kind": "predicate",
  "node_rva": "0x34704368"
}
```

### Ca-f5ab75ea649adfbb

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x34B2A750",
  "snapshot_only": true
}
```

### Ca-f5aeecb8e5e51352

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE198DC0",
  "kind": "predicate",
  "node_rva": "0x3424D628"
}
```

### Ca-f5b2021afbfad4b1

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C0F2C0",
  "kind": "predicate",
  "node_rva": "0x35653B88"
}
```

### Ca-f5b31b7c91c47455

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x378C0F80",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f5b70a5cf60e03bf

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBC66F70",
  "kind": "predicate",
  "node_rva": "0x33885410"
}
```

### Ca-f5c4d5567d35b434

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347CE398",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5cb427220ee7851

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x35DA1340",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f5cb46907e922003

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336E1048",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f5ce58dacf93ddd5

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xD131720",
  "kind": "predicate",
  "node_rva": "0x33D8FF40"
}
```

### Ca-f5cfd55e5518901e

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x33B32028",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f5d340938870ad53

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DC4FB8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f5d87900f08b7819

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348B51C0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f5dc685ae37147c1

```json
{
  "constraints": [
    {
      "evaluated": true,
      "gates": [
        {
          "consumer_rva": "0xE38E8D0",
          "descriptor_native_u64_mask": "0x100",
          "direct_gate_passes": false,
          "evaluated": true,
          "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
          "name": "service internal direct keyword rejection gate",
          "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
          "value": 0,
          "variable_encoding": "big",
          "variable_runtime_va": 93825926624760,
          "variable_rva": "0x37B1B5F8",
          "variable_size": 4,
          "when_zero": "reject"
        }
      ],
      "kind": "keyword_access_gates",
      "snapshot_only": true
    },
    {
      "evaluated": false,
      "kind": "keyword_option_match",
      "minimum_match": 0,
      "note": "Privilege, parser mode, ambiguity and additional flags still constrain matching",
      "value": 0
    }
  ],
  "kind": "keyword_constraints",
  "node_rva": "0x33757C40"
}
```

### Ca-f5ddf8cb68b7425e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFA34AA0",
  "kind": "predicate",
  "node_rva": "0x347CE768"
}
```

### Ca-f5df85880fc5ca36

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFCED970",
  "kind": "predicate",
  "node_rva": "0x34896250"
}
```

### Ca-f5dfeb81ebf225ed

```json
{
  "callback_rva": "0x13619AE0",
  "evaluated": false,
  "expected": true,
  "fallback_pointer_encoded_hex": "0000555568a10f70",
  "kind": "no_argument_predicate",
  "node_rva": "0x35BEDF58",
  "normal_cli_only": true,
  "observed_fallback_target": 93825315966832,
  "reviewed_model": {
    "evidence": {
      "file": "reports\\runtime-comparison-20261029\\options\\getter-evidence\\rva_13619ae0.json",
      "scope": "Reviewed normal CLI branch; producer not executed",
      "sha256": "79f739b3c91219036571b734cd3fd73c69fef88f40747f12d1d3046a23c37945"
    },
    "fallback_only_if_primary_query_fails": true,
    "fallback_pointer_rva": "0x3eba12b0",
    "fallback_when_pointer_null": true,
    "kind": "registry_or_callback",
    "registry_arguments": [
      27,
      1
    ]
  }
}
```

### Ca-f5e666530ab3a7b5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x105B4310",
  "kind": "predicate",
  "node_rva": "0x34B90C80"
}
```

### Ca-f5e78b67504064d6

```json
{
  "callback_rva": "0xC309320",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33A49078"
}
```

### Ca-f5e7efe65c69a157

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35803D38",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f5e7f946e79e3be4

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BB73F0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f5e80a9dc06d4462

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35A78B90"
}
```

### Ca-f5ebf5253dfda430

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34CD16D8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f5ee1d0cb5eb3c12

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDB544D0",
  "kind": "predicate",
  "node_rva": "0x33FDA1E8"
}
```

### Ca-f5efca3b6e52c6e5

```json
{
  "address_type_candidate": 1,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x344C7FB0",
  "registry_rva": "0x3CB56200"
}
```

### Ca-f5f1f67eca94b326

```json
{
  "evaluated": false,
  "expected": false,
  "kind": "interface_status_mask",
  "mask_candidate": 8,
  "node_rva": "0x35814A58",
  "note": "Normal CLI requires a current interface/IDB; help paths differ"
}
```

### Ca-f5f34b800da87e92

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34655420",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f5f5604fd24639c3

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35BDB3F0"
}
```

### Ca-f5fc238fa506d8b2

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x340C3A50",
  "snapshot_only": true
}
```

### Ca-f5fe3351f8784a19

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x341CFB80",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f60115c24e7cfbe6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF02B360",
  "kind": "predicate",
  "node_rva": "0x344CF9A0"
}
```

### Ca-f60138e51bc5109e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF028F20",
  "kind": "predicate",
  "node_rva": "0x344C25E0"
}
```

### Ca-f603651e4b9bf0b5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBD237B0",
  "kind": "predicate",
  "node_rva": "0x338C2290"
}
```

### Ca-f603d979901aa22e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAE7E708"
}
```

### Ca-f604c5fc41646230

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34703710",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6089184297c1da8

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA4EA8"
}
```

### Ca-f6091d36bed62d56

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34786478",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f60be58457a2cdfc

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE0013F0",
  "kind": "predicate",
  "node_rva": "0x3415C678"
}
```

### Ca-f60e022eabb71774

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xC209640",
  "kind": "predicate",
  "node_rva": "0x33A0AF68"
}
```

### Ca-f60e1c3ad3c2fefc

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x3375A768",
  "snapshot_only": true
}
```

### Ca-f611bd6ed0571c79

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2EEA0",
  "kind": "predicate",
  "node_rva": "0x33F9B7A0"
}
```

### Ca-f6143b0c3d82991d

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF5DAE10",
  "kind": "predicate",
  "node_rva": "0x346C1A10"
}
```

### Ca-f61756b264e6c070

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345CD4E8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f61c27972c824ee1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3386B100",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f61c4ad63b9182ed

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x13052EF0",
  "kind": "predicate",
  "node_rva": "0x35A12CC8"
}
```

### Ca-f61ed0634f0d75f0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xC95D750",
  "kind": "predicate",
  "node_rva": "0x33B33F90"
}
```

### Ca-f62461eb409c6eda

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34924FA8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f627b0336cca0357

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34720038",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f628aa4eec009346

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34127640",
  "state": [
    0,
    null,
    0
  ]
}
```

### Ca-f62ac90261b46021

```json
{
  "callback_rva": "0xE9ED690",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x34383CC8"
}
```

### Ca-f62b371f771e6c01

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xC6B20C0",
  "kind": "predicate",
  "node_rva": "0x33AD1CA0"
}
```

### Ca-f62d949ef04954a1

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF11CC80",
  "kind": "predicate",
  "node_rva": "0x3454CB18"
}
```

### Ca-f6320d332cec9e33

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x357C4F18",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f634cdc01d272891

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C0DF30",
  "kind": "predicate",
  "node_rva": "0x3564EFB0"
}
```

### Ca-f637f849117853a2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x367DFAF8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f63ff0c482074892

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000004",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x36893E90"
}
```

### Ca-f640dce73c4c9c8d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE074B90",
  "kind": "predicate",
  "node_rva": "0x34194C68"
}
```

### Ca-f641154c87a2fa4d

```json
{
  "evaluated": true,
  "expected_nvgen": 0,
  "kind": "iterator_nvgen_gate",
  "node_rva": "0x371DB800"
}
```

### Ca-f641b344462cfb8f

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 8920,
  "kind": "parser_state_comparison",
  "node_rva": "0x34891B60",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-f6422c538dd16cb3

```json
{
  "comparison_value_encoded_hex": "000000000000006f",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 4016,
  "kind": "parser_state_comparison",
  "node_rva": "0x343ED880",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f6427a0da82dbe56

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF5D9C00",
  "kind": "predicate",
  "node_rva": "0x346B61A8"
}
```

### Ca-f642a1d1e347b91b

```json
{
  "context_fields": [
    14368,
    14896,
    15064,
    11960,
    12280,
    14372,
    14900,
    13620,
    12124
  ],
  "evaluated": false,
  "expected": false,
  "expression": "multiple_functions_check(csb) || remaining_input_check(csb)",
  "kind": "parser_ambiguity_or_remaining_input",
  "node_rva": "0x35848330",
  "normal_cli_only": true
}
```

### Ca-f64310f7174ab66e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF850160",
  "kind": "predicate",
  "node_rva": "0x34765EF8"
}
```

### Ca-f645f96bd61372e2

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x17AFE130",
  "kind": "predicate",
  "node_rva": "0x3654A5A0"
}
```

### Ca-f646a6d395effa52

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16307640",
  "kind": "predicate",
  "node_rva": "0x35F70790"
}
```

### Ca-f64cf3173fe30680

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x113D7510",
  "kind": "predicate",
  "node_rva": "0x354B5C70"
}
```

### Ca-f64e29ab6a2986f8

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE15AB70",
  "kind": "predicate",
  "node_rva": "0x34221AA0"
}
```

### Ca-f650bcaaa616bba0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD30B060",
  "kind": "predicate",
  "node_rva": "0x33E12820"
}
```

### Ca-f650db4d9050aabb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356E5C28",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6539bcef2298c73

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AA491A0",
  "kind": "predicate",
  "node_rva": "0x36D513B8"
}
```

### Ca-f65b44f9eda4c9e1

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF02B720",
  "kind": "predicate",
  "node_rva": "0x344D6F30"
}
```

### Ca-f65c90ad2907b8da

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "interface_status_mask",
  "mask_candidate": 512,
  "node_rva": "0x34767A28",
  "note": "Normal CLI requires a current interface/IDB; help paths differ"
}
```

### Ca-f65c9bac4c94730b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35BECC90",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f65dd18e38aca67c

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336D5948",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f66069a7781eb59f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2E9A0",
  "kind": "predicate",
  "node_rva": "0x33FA0178"
}
```

### Ca-f66362994e931332

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF12AC40",
  "kind": "predicate",
  "node_rva": "0x34584E40"
}
```

### Ca-f666056271c4d70d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BE2E660",
  "kind": "predicate",
  "node_rva": "0x37184B28"
}
```

### Ca-f66ad0b160b07a15

```json
{
  "constraints": [
    {
      "evaluated": false,
      "field_offset": 8912,
      "kind": "parser_state_mask_zero",
      "known_value": null,
      "mask_encoded_hex": "0000000000000010",
      "width_candidate": 4
    },
    {
      "evaluated": false,
      "kind": "keyword_option_match",
      "minimum_match": 0,
      "note": "Privilege, parser mode, ambiguity and additional flags still constrain matching",
      "value": 16
    }
  ],
  "kind": "keyword_constraints",
  "node_rva": "0x3436D698"
}
```

### Ca-f66ba92dd540519e

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x3474D848",
  "snapshot_only": true
}
```

### Ca-f6712ab2d1188f29

```json
{
  "address_type_candidate": 1,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x35CEB090",
  "registry_rva": "0x3CB56200"
}
```

### Ca-f6718f175b49bc78

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD64D020",
  "kind": "predicate",
  "node_rva": "0x33EBAC58"
}
```

### Ca-f6744975e00352cc

```json
{
  "evaluated": false,
  "flags_encoded_hex": "02400000",
  "kind": "general_keyword_flags_and_privilege",
  "minimum_match_candidate": 0,
  "node_captured_va": "0x7FFF37E9F4D8",
  "privilege_descriptor_address": 140734131424544
}
```

### Ca-f6764c37442f30f4

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x368C6FD0"
}
```

### Ca-f6771716543110dd

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x112E3280",
  "kind": "predicate",
  "node_rva": "0x35460758"
}
```

### Ca-f678b81b00334f66

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35EE62F8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f67e75c3a16d137f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33AACD60",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f67e92bce274512e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xCA0AFA0",
  "kind": "predicate",
  "node_rva": "0x33B734C8"
}
```

### Ca-f67fd6153cac773a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34939960",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f681fdb71710c3fb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35FAD9B8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f683135af0bf99b5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33C37358",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6838e4acb290d31

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1E04A790",
  "kind": "predicate",
  "node_rva": "0x378ADFC8"
}
```

### Ca-f6874214b151cb39

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF84FC20",
  "kind": "predicate",
  "node_rva": "0x34763C08"
}
```

### Ca-f6874351d8e2f5cd

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF147CC0",
  "kind": "predicate",
  "node_rva": "0x345CA4A8"
}
```

### Ca-f68ac6f46831a612

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 4016,
  "kind": "parser_state_comparison",
  "node_rva": "0x33944A90",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-f68cff877114ed65

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF035A00",
  "kind": "predicate",
  "node_rva": "0x34502ED8"
}
```

### Ca-f68d860f873bd345

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34013B78",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6927120a832f872

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1407C200",
  "kind": "predicate",
  "node_rva": "0x35CF6620"
}
```

### Ca-f695fc6aac0c1123

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x344FB420",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-f696448b98408904

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34A51188",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f696a2c4b6cff77b

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11D09070",
  "kind": "predicate",
  "node_rva": "0x356CA1A0"
}
```

### Ca-f698ec1054a12eb9

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x3611A218",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f6993ea20b15a6b4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346CDC28",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f69b3e31d2ce6f42

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF0141C0",
  "kind": "predicate",
  "node_rva": "0x34496DC0"
}
```

### Ca-f69b8ddaf5f84584

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x342BF478",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f69c74b555af6318

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D941A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6a0f34d6c1613bc

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34A56338",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6a2889917a07a1b

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35E5CE98",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6a6bcfa16da77e3

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF143470",
  "kind": "predicate",
  "node_rva": "0x345B1DE8"
}
```

### Ca-f6a7ac1a162d493a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFFE6180",
  "kind": "predicate",
  "node_rva": "0x34960658"
}
```

### Ca-f6a801330aa95e44

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD9F6AE0",
  "kind": "predicate",
  "node_rva": "0x33F5D730"
}
```

### Ca-f6a8ac2f76885a10

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x358926A8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6ab2c0206e81a96

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344E32A0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6ac5ae4821f9820

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDBDCFA0",
  "kind": "predicate",
  "node_rva": "0x34005188"
}
```

### Ca-f6afafb892fa84d8

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x36FD7590",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f6b03ffccb775c40

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344E1C10",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6b07c859e9bda33

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34888688",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6b4e2b7ec70d27f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F4348",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6b60e16854c1267

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x119ADDE0",
  "kind": "predicate",
  "node_rva": "0x355C5F18"
}
```

### Ca-f6bbe0d007c1ff6f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C0B9D0",
  "kind": "predicate",
  "node_rva": "0x356393F8"
}
```

### Ca-f6bcbee0c380f78d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16623EE0",
  "kind": "predicate",
  "node_rva": "0x35FB20A0"
}
```

### Ca-f6bd16e84ae6739c

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1DDE6510",
  "kind": "predicate",
  "node_rva": "0x37848100"
}
```

### Ca-f6c2808b327a9c4c

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35439E50",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6c30a9d68f07144

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1E04A920",
  "kind": "predicate",
  "node_rva": "0x378AD428"
}
```

### Ca-f6c50a836558155f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36E4E518",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6c5981d8c140933

```json
{
  "evaluated": true,
  "expected_nvgen": 0,
  "kind": "iterator_nvgen_gate",
  "node_rva": "0x37110EF0"
}
```

### Ca-f6c802f114a01ee2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35FD6D50",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6c9978045714aba

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x367858B0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6ca7ee14e3a0713

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x343E5B68",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6cb7d306aaef54f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35E76348",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6ded3f5c9f01dc9

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35437D08",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f6df499f9caa96c4

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1E04A9B0",
  "kind": "predicate",
  "node_rva": "0x378AD0E0"
}
```

### Ca-f6e5279696d00985

```json
{
  "descriptor": 93825860838080,
  "evaluated": false,
  "expected": true,
  "kind": "privilege_gate",
  "node_rva": "0x33C5E238"
}
```

### Ca-f6e584450ca0a80a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C156B0",
  "kind": "predicate",
  "node_rva": "0x35687D58"
}
```

### Ca-f6ec1d492251a61a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xC8D1140",
  "kind": "predicate",
  "node_rva": "0x33B11C98"
}
```

### Ca-f6eedcc6a7bed3c4

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BE1D510",
  "kind": "predicate",
  "node_rva": "0x37112548"
}
```

### Ca-f6efb2bce8e2c04e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36898D28",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f6f2b9efcac2a2d7

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x3375D7D8",
  "snapshot_only": true
}
```

### Ca-f6f2c2949a6f1187

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x161091A0",
  "kind": "predicate",
  "node_rva": "0x35ED6FF0"
}
```

### Ca-f6f4474207cf4f8d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF02D330",
  "kind": "predicate",
  "node_rva": "0x344DC3E8"
}
```

### Ca-f6f48d1968820e63

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336F4700",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f6f74a6bde96b324

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x33756BF0",
  "snapshot_only": true
}
```

### Ca-f6f8358d9ed6be50

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35546EB8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f6fa77f78fb8f3d8

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB2CFC00",
  "kind": "predicate",
  "node_rva": "0x33732E28"
}
```

### Ca-f6fc523c2d86dc75

```json
{
  "context_fields": [
    14368,
    14896,
    15064,
    11960,
    12280,
    14372,
    14900,
    13620,
    12124
  ],
  "evaluated": false,
  "expected": true,
  "expression": "multiple_functions_check(csb) || remaining_input_check(csb)",
  "kind": "parser_ambiguity_or_remaining_input",
  "node_rva": "0x340B9FE0",
  "normal_cli_only": true
}
```

### Ca-f6ffd9a91d7aefd1

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11D23980",
  "kind": "predicate",
  "node_rva": "0x356CD8F0"
}
```

### Ca-f7045a4c3b04f387

```json
{
  "evaluated": false,
  "field_offset": 10434,
  "kind": "parser_field_mask_zero",
  "mask": 1,
  "node_rva": "0x34388E18",
  "width": 1
}
```

### Ca-f706060d21eecf12

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1DDE7330",
  "kind": "predicate",
  "node_rva": "0x37842700"
}
```

### Ca-f709e991ce1d99d1

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x344DAC68",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-f70be7d29bd130a2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36FF5160",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f70ec6d6168e79bc

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000002",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35DE7D88"
}
```

### Ca-f712d5b4421bfd43

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3493D910",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-f714b8a30c05d117

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x33F931A8",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-f7152a4eb8d44f22

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11AA7E70",
  "kind": "predicate",
  "node_rva": "0x355E32D8"
}
```

### Ca-f715dd60f16fc810

```json
{
  "callback_rva": "0x15C91280",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x35E5D2C8"
}
```

### Ca-f7168bf6b789b2e0

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3467E760",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f71895eb5b9cb220

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1E3BBDA0",
  "kind": "predicate",
  "node_rva": "0x37904070"
}
```

### Ca-f7197f6e50d11889

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3488D180",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f719adf5c560426b

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFCF5440",
  "kind": "predicate",
  "node_rva": "0x348B4820"
}
```

### Ca-f719d1e51d817fbb

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000004",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x3581C680"
}
```

### Ca-f71e656055d07e68

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x100540A0",
  "kind": "predicate",
  "node_rva": "0x34A4EDE0"
}
```

### Ca-f7266baa5c64941f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3523A128",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f727d781285157c4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33E79C00",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f727f40cc4c2a72b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34602AC8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f7291653ee3ec7a0

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346F7598",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f729e48d7d847358

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x33742C30"
}
```

### Ca-f72bbd3a93151443

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35D12340",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f72c7befa2e8ac57

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDC48670",
  "kind": "predicate",
  "node_rva": "0x340133C0"
}
```

### Ca-f72f31202ea8f943

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36098318",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f72f85e5f532e33b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C0C2C0",
  "kind": "predicate",
  "node_rva": "0x356478C8"
}
```

### Ca-f732c1c61643a81b

```json
{
  "descriptor": 93825887276744,
  "evaluated": false,
  "expected": false,
  "kind": "privilege_gate",
  "node_rva": "0x35594E68"
}
```

### Ca-f7337c60f2e776cf

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xCAEF2A0",
  "kind": "predicate",
  "node_rva": "0x33BA6520"
}
```

### Ca-f7346fda3735c3e9

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3564B358",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f738b9a2c0eff5f5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1606C110",
  "kind": "predicate",
  "node_rva": "0x35EAB880"
}
```

### Ca-f73a6b86e69d50c2

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33B1F7B0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f73fe25ad0369ec6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD65F9C0",
  "kind": "predicate",
  "node_rva": "0x33EC1298"
}
```

### Ca-f7403f2091026f9f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33A67EF8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f740ba3bbdc66472

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35513830",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f743b079f2ac3e81

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DBD380",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f74a0b703774e714

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA0AC8"
}
```

### Ca-f74cebb623e61d92

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3666ABD0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f74e041190abdc67

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36061428",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f75074e906b5b7e6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16220AA0",
  "kind": "predicate",
  "node_rva": "0x35F22320"
}
```

### Ca-f7509d99a55707e1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x338AF198",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f752a9d860e18f35

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344F8350",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7537d0f31a2f5c1

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33FCDEC0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f75564a34f437b2a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D17AD8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7584ae54b311012

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35BE4C68",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f75cfd9f6f7dca69

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33A6AB88",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f75d455abd1930fe

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3468D2D0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f76078a5b9404767

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35FB6D90",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f765698a5967c035

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE9472A0",
  "kind": "predicate",
  "node_rva": "0x34348A78"
}
```

### Ca-f76587d5da040a85

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x378BEF50",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f765b2403fd66d68

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE4D4680",
  "kind": "predicate",
  "node_rva": "0x342D4D10"
}
```

### Ca-f765cda5492ab2f6

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x33DE24C0"
}
```

### Ca-f76df4cd9dd7b359

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000002",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35DE75D0"
}
```

### Ca-f76dfbda5981e328

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xCEFE640",
  "kind": "predicate",
  "node_rva": "0x33D4EFB0"
}
```

### Ca-f77745146d95546a

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1E143A10",
  "kind": "predicate",
  "node_rva": "0x378E42F0"
}
```

### Ca-f7781f5920e25379

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x3455E6F8",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-f77c8f8a8c787ba6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF126190",
  "kind": "predicate",
  "node_rva": "0x34577030"
}
```

### Ca-f780b0e48931f9d6

```json
{
  "context_fields": [
    14368,
    14896,
    15064,
    11960,
    12280,
    14372,
    14900,
    13620,
    12124
  ],
  "evaluated": false,
  "expected": false,
  "expression": "multiple_functions_check(csb) || remaining_input_check(csb)",
  "kind": "parser_ambiguity_or_remaining_input",
  "node_rva": "0x342201C8",
  "normal_cli_only": true
}
```

### Ca-f7845c1d6a7a85b1

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x368E9DA8",
  "snapshot_only": true
}
```

### Ca-f78a5401659965be

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3475F9B0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f78d2f56d4cf2e56

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x341A8478",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f78e1e3554ae74d8

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3546A050",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f791daec2ba922a9

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE0079B0",
  "kind": "predicate",
  "node_rva": "0x34164A80"
}
```

### Ca-f793be2c7e54fcf7

```json
{
  "constraints": [
    {
      "evaluated": false,
      "field_offset": 8912,
      "kind": "parser_state_mask_zero",
      "known_value": null,
      "mask_encoded_hex": "00000000ffffffff",
      "width_candidate": 4
    },
    {
      "evaluated": false,
      "kind": "keyword_option_match",
      "minimum_match": 0,
      "note": "Privilege, parser mode, ambiguity and additional flags still constrain matching",
      "value": 55
    }
  ],
  "kind": "keyword_constraints",
  "node_rva": "0x360A85E8"
}
```

### Ca-f7984e65b7e96b9b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1230E580",
  "kind": "predicate",
  "node_rva": "0x357F2240"
}
```

### Ca-f798cd27eeba94b9

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF84E880",
  "kind": "predicate",
  "node_rva": "0x3474FE30"
}
```

### Ca-f799c6c0c6659249

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1AAEA140",
  "kind": "predicate",
  "node_rva": "0x36D756C0"
}
```

### Ca-f79a654df14611ca

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB278CF0",
  "kind": "predicate",
  "node_rva": "0x336F3D70"
}
```

### Ca-f79dded0224c5771

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C14DC0",
  "kind": "predicate",
  "node_rva": "0x35684208"
}
```

### Ca-f79dedacc43779e6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16B7F270",
  "kind": "predicate",
  "node_rva": "0x361161E8"
}
```

### Ca-f79f56bfe2d4ea68

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xB6C50A0",
  "kind": "predicate",
  "node_rva": "0x337E3740"
}
```

### Ca-f7a1d269d0627867

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378BC398",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7a43160edca01a8

```json
{
  "evaluated": false,
  "flags_encoded_hex": "02400000",
  "kind": "general_keyword_flags_and_privilege",
  "minimum_match_candidate": 0,
  "node_captured_va": "0x7FFFBAED9A30",
  "privilege_descriptor_address": 140736329187296
}
```

### Ca-f7a4ae127d30261e

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x338DBF38",
  "snapshot_only": true
}
```

### Ca-f7a51a7c9ba8b0ba

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x337626D8",
  "snapshot_only": true
}
```

### Ca-f7acdd3bd2270b6f

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336DF828",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7ae2af0edad0651

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D17AD8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7b10648ff8fefca

```json
{
  "callback_rva": "0xEA63E60",
  "evaluated": false,
  "expected": false,
  "kind": "no_argument_predicate",
  "node_rva": "0x34395408",
  "normal_cli_only": true
}
```

### Ca-f7b15713fe6db713

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x376C70F0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7b36c6a7c5fd01c

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1BE1D810",
  "kind": "predicate",
  "node_rva": "0x371149C8"
}
```

### Ca-f7b40e5cd677bd1d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3370D600",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7b613cca7b9657f

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x345E8C90",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f7bc2cef51296618

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF12BF00",
  "kind": "predicate",
  "node_rva": "0x3457B1B8"
}
```

### Ca-f7c0361e80681247

```json
{
  "callback_rva": "0x1BF88950",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x371FF0D8"
}
```

### Ca-f7c0573abb2d5964

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "interface_status_mask",
  "mask_candidate": 8,
  "node_rva": "0x354AA228",
  "note": "Normal CLI requires a current interface/IDB; help paths differ"
}
```

### Ca-f7c8f7abaf96c037

```json
{
  "callback_rva": "0xD7D55B0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33F93D40"
}
```

### Ca-f7d354b139eaa563

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34A558A8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7d40a7cc242faba

```json
{
  "callback_rva": "0xB2CFB70",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33732EF8"
}
```

### Ca-f7d4d16c4e102998

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD015E60",
  "kind": "predicate",
  "node_rva": "0x33D815C8"
}
```

### Ca-f7d8ad5e32c521e2

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34883D48",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7d8e96bdd214432

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF127EA0",
  "kind": "predicate",
  "node_rva": "0x3457F5D8"
}
```

### Ca-f7d9deffa6ac4539

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x355D8398",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7daa6de0566b95d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD84D3F0",
  "kind": "predicate",
  "node_rva": "0x33F08CB8"
}
```

### Ca-f7dbdaca7565f86c

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDC495D0",
  "kind": "predicate",
  "node_rva": "0x34017270"
}
```

### Ca-f7dc237d448c64e4

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF143C20",
  "kind": "predicate",
  "node_rva": "0x345AF0D0"
}
```

### Ca-f7dc4643789d1c85

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346A78E8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-f7dc5bd7e7dbf966

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDA05740",
  "kind": "predicate",
  "node_rva": "0x33F7AE58"
}
```

### Ca-f7e1aedb9b51c7d3

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356FC2F8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f7e1d81c7db2d316

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34704D78",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-f7e7d990213770a7

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000004",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x3496C418"
}
```

### Ca-f7e86b55bdc65939

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "interface_status_mask",
  "mask_candidate": 512,
  "node_rva": "0x35814A90",
  "note": "Normal CLI requires a current interface/IDB; help paths differ"
}
```

### Ca-f7e8cc287ebe4d59

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x378BE6B8"
}
```

### Ca-f7eb8d9302f96585

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2D0F0",
  "kind": "predicate",
  "node_rva": "0x33FA2A58"
}
```

### Ca-f7ebc9b2d273b538

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C10920",
  "kind": "predicate",
  "node_rva": "0x3565A540"
}
```

### Ca-f7ee4214e22ada9b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF123610",
  "kind": "predicate",
  "node_rva": "0x3455F5A0"
}
```

### Ca-f7ef5bbba4964215

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348BF1B0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f7f20680e3592886

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x35BF38B0"
}
```

### Ca-f7f48d590657438d

```json
{
  "evaluated": true,
  "gates": [
    {
      "consumer_rva": "0xE38E8D0",
      "descriptor_native_u64_mask": "0x100",
      "direct_gate_passes": false,
      "evaluated": true,
      "evidence": "runtime-comparison-20261029/function-e38e8d0.json",
      "name": "service internal direct keyword rejection gate",
      "scope": "Only this direct mask check is evaluated; other privilege/context checks remain unresolved",
      "value": 0,
      "variable_encoding": "big",
      "variable_runtime_va": 93825926624760,
      "variable_rva": "0x37B1B5F8",
      "variable_size": 4,
      "when_zero": "reject"
    }
  ],
  "kind": "keyword_access_gates",
  "node_rva": "0x35252748",
  "snapshot_only": true
}
```

### Ca-f7f63b804b6bdf93

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BCD588",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-f7f7c62bc4efd0be

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348A3BE8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f7fd50e09db081c9

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xECEB890",
  "kind": "predicate",
  "node_rva": "0x343E0C68"
}
```

### Ca-f800b17cd9e38bb8

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFA354E0",
  "kind": "predicate",
  "node_rva": "0x347DBE88"
}
```

### Ca-f803665836cf60a5

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33706F00",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f805070df1e832de

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x370B2A08",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-f8103c5231ae6fa9

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35BE1F78",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-f813eaae259e1631

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AA48080",
  "kind": "predicate",
  "node_rva": "0x36D52120"
}
```

### Ca-f815d1cebeff8504

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xCB25ED0",
  "kind": "predicate",
  "node_rva": "0x33BB9110"
}
```

