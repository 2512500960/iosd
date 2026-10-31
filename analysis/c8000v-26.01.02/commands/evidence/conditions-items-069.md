# 条件明细

[返回参考索引](README.md) · [阅读说明](../README.md)

### Ca-ff77a8ed1e5591f1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356879F0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ff7ad72764b8e3f6

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3475E9F0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-ff7e47edec4aca39

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BF89660",
  "kind": "predicate",
  "node_rva": "0x371FF870"
}
```

### Ca-ff803eb2132bf851

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BB9C68",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ff82e93bf9969465

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF1217F0",
  "kind": "predicate",
  "node_rva": "0x34560C48"
}
```

### Ca-ff8928ae6766b6c7

```json
{
  "callback_rva": "0xB2CFA80",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33732130"
}
```

### Ca-ff913d53d656b2ee

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAE7E708"
}
```

### Ca-ff914a20dd28986c

```json
{
  "constraints": [
    {
      "evaluated": false,
      "field_offset": 8936,
      "kind": "parser_state_mask_zero",
      "known_value": null,
      "mask_encoded_hex": "0000000000000000",
      "width_candidate": 4
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
  "node_rva": "0x337D5358"
}
```

### Ca-ff97fb9af7cb6d5a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345664B8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-ff9cff6519e5d147

```json
{
  "descriptor": 93825912463876,
  "evaluated": false,
  "expected": true,
  "kind": "privilege_gate",
  "node_rva": "0x36D99B30"
}
```

### Ca-ff9fb92b0aeb4409

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x376CD2B0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-ffa04030a6f0dab5

```json
{
  "callback_rva": "0xEC57C80",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x343E4090"
}
```

### Ca-ffa040e083df7589

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 8944,
  "kind": "parser_state_comparison",
  "node_rva": "0x347D23D0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-ffa06b958442a9fc

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16015AC0",
  "kind": "predicate",
  "node_rva": "0x35E9F518"
}
```

### Ca-ffa44691f51175ce

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF850820",
  "kind": "predicate",
  "node_rva": "0x34769368"
}
```

### Ca-ffa4539ed16117d0

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3488D020",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-ffa497bccad508e5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3546DD30",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-ffa709c42eea9ed1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3456E640",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-ffa8cc11a39e21ce

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1E142D50",
  "kind": "predicate",
  "node_rva": "0x378E17C8"
}
```

### Ca-ffa9e7d6bd7dc3c3

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
  "node_rva": "0x35A9BC20",
  "snapshot_only": true
}
```

### Ca-ffac38ae11e2e9bd

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35437440",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ffacb6e41add6d13

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
  "node_rva": "0x357A6680",
  "snapshot_only": true
}
```

### Ca-ffad5e24c82466d7

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
  "node_rva": "0x34BE62D8",
  "snapshot_only": true
}
```

### Ca-ffad9f02e05d388f

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37E9E320"
}
```

### Ca-ffafd33222e96956

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xBFFA720",
  "kind": "predicate",
  "node_rva": "0x3396A488"
}
```

### Ca-ffb102502e77f61c

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF84FCC0",
  "kind": "predicate",
  "node_rva": "0x34763068"
}
```

### Ca-ffb141a378bfc9fc

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF43D440",
  "kind": "predicate",
  "node_rva": "0x346482F0"
}
```

### Ca-ffb5f7bdc4560d92

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFBA53A0",
  "kind": "predicate",
  "node_rva": "0x3482CD80"
}
```

### Ca-ffb7a4c491a40f3b

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xCED4E30",
  "kind": "predicate",
  "node_rva": "0x33D3C5C0"
}
```

### Ca-ffb81d426b60e12d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345ED918",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ffbddce216f0c2e4

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x13F582C0",
  "kind": "predicate",
  "node_rva": "0x35CDE200"
}
```

### Ca-ffbdddce18cd838d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x357BC7E8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ffc18b25b45d54cc

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
  "node_rva": "0x34474780",
  "snapshot_only": true
}
```

### Ca-ffc4ce17b0390ba0

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFA350A0",
  "kind": "predicate",
  "node_rva": "0x347D8290"
}
```

### Ca-ffc4e06703ac64a3

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB558F40",
  "kind": "predicate",
  "node_rva": "0x3379B6D8"
}
```

### Ca-ffc680b561a6b676

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xD581BD0",
  "kind": "predicate",
  "node_rva": "0x33E8B4E0"
}
```

### Ca-ffc69e0344df6f69

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35470400",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-ffc6d48bc4d0edce

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
  "node_rva": "0x3757EB98",
  "snapshot_only": true
}
```

### Ca-ffca14861547d112

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA1DE8"
}
```

### Ca-ffca8d01a11e631e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xFA35400",
  "kind": "predicate",
  "node_rva": "0x347D98C0"
}
```

### Ca-ffd099e087f2b756

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11DBEF90",
  "kind": "predicate",
  "node_rva": "0x356FBFB0"
}
```

### Ca-ffd0a9c3441e3d38

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x3391FE88"
}
```

### Ca-ffd0df8d86c28bd1

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x16626180",
  "kind": "predicate",
  "node_rva": "0x35FB61D8"
}
```

### Ca-ffd20b8c38646718

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x36D6E878"
}
```

### Ca-ffd216635fc497ca

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBD43270",
  "kind": "predicate",
  "node_rva": "0x338EA198"
}
```

### Ca-ffd2a51febb4c587

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB280090",
  "kind": "predicate",
  "node_rva": "0x3370B148"
}
```

### Ca-ffd32d0f6188b932

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2E7A0",
  "kind": "predicate",
  "node_rva": "0x33FA4650"
}
```

### Ca-ffd363625dc41d03

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xECEC7B0",
  "kind": "predicate",
  "node_rva": "0x343E9998"
}
```

### Ca-ffd898e6a2a6538b

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x16984640",
  "kind": "predicate",
  "node_rva": "0x3605CC38"
}
```

### Ca-ffd8ff2ab2743d36

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x118A3250",
  "kind": "predicate",
  "node_rva": "0x3557C6F0"
}
```

### Ca-ffd9fde55c754c08

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354396A0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-ffdd104fb6664be0

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354D5BB8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-ffde31d511f6d723

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x360A0DA0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-ffe1596c27b8645c

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x15F41430",
  "kind": "predicate",
  "node_rva": "0x35E72230"
}
```

### Ca-ffe3ed1828cdff65

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BD987E0",
  "kind": "predicate",
  "node_rva": "0x3700B9D8"
}
```

### Ca-ffe47c7c8f375347

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBF87110",
  "kind": "predicate",
  "node_rva": "0x3395A230"
}
```

### Ca-ffe4f1d0b3bcb79f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF128BB0",
  "kind": "predicate",
  "node_rva": "0x34586730"
}
```

### Ca-ffe8a7cdcd4acfc2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354A4118",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-fff169f4944f0c92

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xBF80490",
  "kind": "predicate",
  "node_rva": "0x33959288"
}
```

### Ca-fff1e2974645720b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3418C870",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-fff368741bccbc27

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
  "node_rva": "0x33757448"
}
```

### Ca-fff7895f977c5518

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
  "node_rva": "0x35EA3F30",
  "snapshot_only": true
}
```

### Ca-fffb88ee3b29f50a

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xECEBC90",
  "kind": "predicate",
  "node_rva": "0x343E79B0"
}
```

### Ca-fffe84aff4e3694f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA4EA8"
}
```

### Ca-ffffaa78b501fe75

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF634CE0",
  "kind": "predicate",
  "node_rva": "0x347107B8"
}
```
