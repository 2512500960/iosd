# 条件明细

[返回参考索引](README.md) · [阅读说明](../README.md)

### Ca-67f37c6a3b049bae

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346AF618",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-67fa0cfc441fe957

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33B92CE0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-67fb094e10eafbe9

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1181A500",
  "kind": "predicate",
  "node_rva": "0x35538F78"
}
```

### Ca-67fc387bdce8416e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x172DB340",
  "kind": "predicate",
  "node_rva": "0x36361870"
}
```

### Ca-67fd077da6d9f1f6

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDFF4F90",
  "kind": "predicate",
  "node_rva": "0x34125448"
}
```

### Ca-67fda727766873d4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348231E8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-67fefea7fa8bc3ec

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
  "node_rva": "0x356AA4E0",
  "normal_cli_only": true
}
```

### Ca-68010f4ad26234d9

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x36DDC0B8",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-68060f0b4328f851

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
  "node_rva": "0x344BDB60",
  "snapshot_only": true
}
```

### Ca-680b5758ddacbc2c

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x36DDED10",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-680b9ca5cabe8050

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xB27A740",
  "kind": "predicate",
  "node_rva": "0x336EA698"
}
```

### Ca-680f2844b6703bbb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34180DF8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-680fa474b3d3d9f7

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11C0B8C0",
  "kind": "predicate",
  "node_rva": "0x35639C60"
}
```

### Ca-681041a549ebc763

```json
{
  "callback_rva": "0xB27B990",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33705F78"
}
```

### Ca-68138d4eccd5bf2c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34B90498",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6814b9110e4ec2c4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D3B898",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6815c4b4e8952aba

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33C647E8",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-6816b4f31a701f3a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34649CA8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-681cc626daa9c259

```json
{
  "evaluated": false,
  "field_offset": 8908,
  "kind": "parser_state_mask_zero",
  "known_value": null,
  "mask_encoded_hex": "0000000000000001",
  "node_rva": "0x353AB008",
  "required": "value & mask == 0",
  "width_candidate": 4
}
```

### Ca-68226bcb211cb9c7

```json
{
  "callback_rva": "0xD5136A0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33E73CD0"
}
```

### Ca-68231d60329bafe8

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x19392A30",
  "kind": "predicate",
  "node_rva": "0x369CC968"
}
```

### Ca-6823e474c02507b8

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x368D59F8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6828e29d3ba9fc13

```json
{
  "evaluated": false,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x345E3560",
  "parameter_omitted": false,
  "sense": null
}
```

### Ca-682cf274e4d8de28

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB27E440",
  "kind": "predicate",
  "node_rva": "0x33703D70"
}
```

### Ca-682dbf4613c2268e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF36210",
  "kind": "predicate",
  "node_rva": "0x340C14B8"
}
```

### Ca-68306f072c9ce3b4

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xD512E20",
  "kind": "predicate",
  "node_rva": "0x33E73B60"
}
```

### Ca-6837fc3c6c368aca

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000002",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x34A40428"
}
```

### Ca-68383aa91dbb93c6

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x366641D8",
  "state": [
    1,
    1,
    0
  ]
}
```

### Ca-683b349b7f25ffac

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF034B90",
  "kind": "predicate",
  "node_rva": "0x344F9190"
}
```

### Ca-683ba159ab299e8c

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x3416A450",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6841f999f415e35b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35E290B8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68430caa0644bb1a

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAEAC8B8"
}
```

### Ca-68433ec120b27ad1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36621248",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68440782ebace6b4

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35453140",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6844babb47f1e9ec

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x19415370",
  "kind": "predicate",
  "node_rva": "0x369EC2F8"
}
```

### Ca-68460e2dcaa9815b

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3443FEC8",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-684ab4531e826b2c

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
  "node_rva": "0x35251B98",
  "snapshot_only": true
}
```

### Ca-684d87d4508c2409

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33AECA38",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-684e28303bdfaf80

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DAC708",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-684fff3083efdd06

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x349239A0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6851ab028f9af55a

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35888040",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6852dc7817398bcd

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3475E280",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-68549c2157de78a9

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
  "node_rva": "0x340CC0D8",
  "snapshot_only": true
}
```

### Ca-685711d2476fce05

```json
{
  "callback_rva": "0xF575070",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x346927E0"
}
```

### Ca-685da9e6d05b8373

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DBD788",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-685eeee2cd2c82b4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344EC088",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-686514f39f0ef4b3

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3489A1F8",
  "state": [
    1,
    null,
    0
  ]
}
```

### Ca-6865e1734abf53a2

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x18386F40",
  "kind": "predicate",
  "node_rva": "0x36748308"
}
```

### Ca-686b049a5797dd4b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1715D840",
  "kind": "predicate",
  "node_rva": "0x362A0EE0"
}
```

### Ca-686b284181c72eff

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3605D3F0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-686b3d1b2163ba8a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3392C1D0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-687043f3431e7616

```json
{
  "address_type_candidate": 1,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x34CAFB40",
  "registry_rva": "0x3CB56200"
}
```

### Ca-687105cf21adccac

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378AF0B0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-687220d154fb8b5c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354CF030",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6874b335c59365b7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16161520",
  "kind": "predicate",
  "node_rva": "0x35EFAB88"
}
```

### Ca-687871b8a2f30493

```json
{
  "evaluated": false,
  "kind": "descriptor_literal_matching",
  "literal": "*",
  "node_rva": "0x342C4888",
  "wrapper_whitespace_and_match_flags_symbolic": true
}
```

### Ca-68790bfb34badcb2

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11C08F70",
  "kind": "predicate",
  "node_rva": "0x35630DE8"
}
```

### Ca-687ac4803ba4ebb6

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xEB713A0",
  "kind": "predicate",
  "node_rva": "0x343C2480"
}
```

### Ca-68839bd25d3895e5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11C140C0",
  "kind": "predicate",
  "node_rva": "0x3567D0F8"
}
```

### Ca-6884199aab6eef24

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF1419D0",
  "kind": "predicate",
  "node_rva": "0x345A3BF8"
}
```

### Ca-68864931ad905c81

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x105B3CA0",
  "kind": "predicate",
  "node_rva": "0x34B7D780"
}
```

### Ca-688e812975a4e4f4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F1208",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-689043ac51797df1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34127640",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6891099d984dcc33

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1AB5C9A0",
  "kind": "predicate",
  "node_rva": "0x36D91950"
}
```

### Ca-6891da6d25b02db0

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37E59728"
}
```

### Ca-6898f8f62741c5cb

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xECEA710",
  "kind": "predicate",
  "node_rva": "0x343DD580"
}
```

### Ca-689e6574e8ae6e32

```json
{
  "evaluated": false,
  "kind": "url_registry_mode_and_input",
  "mode_gate_rva": "0xD651810",
  "node_rva": "0x35838428",
  "parser_rva": "0xD65D690",
  "registry_getter_rva": "0xD72C550"
}
```

### Ca-689fea08b22bd2bc

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3681B5D0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68acbad0a4f58f50

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x17D40CF0",
  "kind": "predicate",
  "node_rva": "0x366502D8"
}
```

### Ca-68adef957ff287f3

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33763840",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-68b3bd6d3b84f9df

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33710748",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-68b4df4b6cfc59a6

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x3412B6E0",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-68b518c836577edb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34BCAC70",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68bb09e83aca7597

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x343DF120",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-68bfe17c3f9e0c1e

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 8908,
  "kind": "parser_state_comparison",
  "node_rva": "0x34B95498",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-68bfe27e4be0eed6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37D654C0"
}
```

### Ca-68c24152dcdbb71c

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1ADF7940",
  "kind": "predicate",
  "node_rva": "0x36E1A3E0"
}
```

### Ca-68c2525d2378cec8

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3553A1A0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68c2becf5a38fd76

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AA49210",
  "kind": "predicate",
  "node_rva": "0x36D50FE8"
}
```

### Ca-68c4d3e550a4db34

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x338EE6E0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-68d19deadda5f50a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF128050",
  "kind": "predicate",
  "node_rva": "0x345815A8"
}
```

### Ca-68d1b7da908bdf29

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35EFB3A8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-68d2f8da6e887843

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34BC9050",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68d316156f7a45b7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1938DE40",
  "kind": "predicate",
  "node_rva": "0x369B6028"
}
```

### Ca-68d377d99ef2f5dd

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DB9450",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68d5ec43ad7d933d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35FD5C50",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-68d722f113d1d430

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA08000",
  "kind": "predicate",
  "node_rva": "0x33F865F8"
}
```

### Ca-68d8e8232973cb82

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354CD6B0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68df6cea19cdfceb

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x13690D40",
  "kind": "predicate",
  "node_rva": "0x35BEBE38"
}
```

### Ca-68e51f7fc72f4640

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3681CA48",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68e9dda9e49f43e0

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34740C80",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68ec8c57fda4b176

```json
{
  "callback_rva": "0xCC539D0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33C26CB8"
}
```

### Ca-68eca17fd6b9976a

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA4FC8"
}
```

### Ca-68ed458718dff028

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3567B978",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-68ee5c48beba1dbe

```json
{
  "callback_rva": "0x1938CFA0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x369B5598"
}
```

### Ca-68f5d329f8162ccc

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x357F91C0"
}
```

### Ca-68f78889ee66af2d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36899268",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-68f7eb4c0841fefd

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB25B970",
  "kind": "predicate",
  "node_rva": "0x336E15F8"
}
```

### Ca-68fad94fec57c215

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xC1E4BA0",
  "kind": "predicate",
  "node_rva": "0x339F9470"
}
```

### Ca-68fb43f640ad1b4f

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF121070",
  "kind": "predicate",
  "node_rva": "0x3455B6A8"
}
```

### Ca-69019b359edc4bd4

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x354ACF58",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-6901cf1e48cb31ad

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF142890",
  "kind": "predicate",
  "node_rva": "0x345ABA10"
}
```

### Ca-69028adbce7098f0

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35459BE0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6903499807591f5b

```json
{
  "evaluated": false,
  "kind": "url_registry_mode_and_input",
  "mode_gate_rva": "0xD651810",
  "node_rva": "0x33C24A78",
  "parser_rva": "0xD65D690",
  "registry_getter_rva": "0xD72C550"
}
```

### Ca-69035c27009d1e8e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D99318",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69053b6502be1f4a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x193552B0",
  "kind": "predicate",
  "node_rva": "0x369A4AF8"
}
```

### Ca-6906593e9eecb7d4

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x36D137C8"
}
```

### Ca-69069f9f79dd1cd7

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378A7480",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-690c139aa5a09eb8

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346562C8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-690e73422c5eb395

```json
{
  "address_type_candidate": 20,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x35597FE8",
  "registry_rva": "0x3CB56200"
}
```

### Ca-6910e0752071c706

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFA34AA0",
  "kind": "predicate",
  "node_rva": "0x347CE768"
}
```

### Ca-69161cb03b108bff

```json
{
  "callback_rva": "0x13619AE0",
  "evaluated": false,
  "expected": true,
  "fallback_pointer_encoded_hex": "0000555568a10f70",
  "kind": "no_argument_predicate",
  "node_rva": "0x35BE32E8",
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

### Ca-69189d62ad6cbbbb

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA089A0",
  "kind": "predicate",
  "node_rva": "0x33F8C290"
}
```

### Ca-691ab192062ef425

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34938918",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-692084a29e2c9806

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3456E640",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6923f026c3ff7793

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3454D5E8",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-6927993a4dbd9bb2

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x344D9B70",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-692e01860ef1f111

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36787290",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-692f3ed3984c8e60

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF142AF0",
  "kind": "predicate",
  "node_rva": "0x345AD840"
}
```

### Ca-692f9d8df97cc3c9

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x33715268",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-69302d899e627822

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3495FE50",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-69353e0435c6f500

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
  "node_rva": "0x36D2BCB8",
  "snapshot_only": true
}
```

### Ca-6935ac78f19232ac

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34913AE8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69370b688c307244

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11827710",
  "kind": "predicate",
  "node_rva": "0x3553CE68"
}
```

### Ca-69371e15c41b38a6

```json
{
  "constraints": [
    {
      "evaluated": false,
      "field_offset": 8912,
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
  "node_rva": "0x337BF410"
}
```

### Ca-6937c3543a340eed

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF5E4310",
  "kind": "predicate",
  "node_rva": "0x346F76A0"
}
```

### Ca-693a3398d524a6cd

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
  "node_rva": "0x3375A228",
  "snapshot_only": true
}
```

### Ca-693a809cae6ae168

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x357ECC98",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-693dd7438bb2e73d

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
  "node_rva": "0x338F0488",
  "snapshot_only": true
}
```

### Ca-693f81acc1c790f7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB67EC40",
  "kind": "predicate",
  "node_rva": "0x337D6D18"
}
```

### Ca-693f9abe4da68f96

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34C36F38",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6940087a3fc1a692

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36760500",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69432fd73e1f742d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336DFF58",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-694a1b0d71b3b9e4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347C8948",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-694a7a6c08b67bb0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x10053EE0",
  "kind": "predicate",
  "node_rva": "0x34A56640"
}
```

### Ca-694af28d8457f2b3

```json
{
  "code": 46,
  "evaluated": false,
  "kind": "exact_input_character",
  "node_rva": "0x35478058",
  "surrounding_whitespace_inferred": false
}
```

### Ca-694b87590b53b94b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356C2388",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-694bfbca24db5cf7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF124F80",
  "kind": "predicate",
  "node_rva": "0x34572630"
}
```

### Ca-694fc8a65304b27a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3587D578",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6950cc4cf508beb6

```json
{
  "callback_rva": "0xB278760",
  "evaluated": false,
  "expected": false,
  "kind": "no_argument_predicate",
  "node_rva": "0x336F4970",
  "normal_cli_only": true
}
```

### Ca-6954dff722b94ad7

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x338F4BF0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6958d62631a459fe

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D4DC00",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-695d40375d3f2f9d

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDFF5890",
  "kind": "predicate",
  "node_rva": "0x3411EEF0"
}
```

### Ca-695d6b234e944953

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x10F29DC0",
  "kind": "predicate",
  "node_rva": "0x35245EC0"
}
```

### Ca-6960243f454ff41d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBBAA9C0",
  "kind": "predicate",
  "node_rva": "0x338712D0"
}
```

### Ca-69603fbd44c7ffc6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2E920",
  "kind": "predicate",
  "node_rva": "0x33FA1768"
}
```

### Ca-69641b9bf187d356

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3546C968",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6965d021cc4ea686

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAED4840"
}
```

### Ca-69675d2413d31d49

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36776020",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6968748b80da21c6

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE1A44F0",
  "kind": "predicate",
  "node_rva": "0x3426DFC8"
}
```

### Ca-696ea080acdf9229

```json
{
  "callback_rva": "0xC7A9400",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33AFDB50"
}
```

### Ca-696ea5cbb6222a91

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
  "node_rva": "0x3759AFD8",
  "snapshot_only": true
}
```

### Ca-696fffa874f46dc5

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF126010",
  "kind": "predicate",
  "node_rva": "0x34578630"
}
```

### Ca-6970181c57c6ec66

```json
{
  "evaluated": true,
  "expected_nvgen": 0,
  "kind": "iterator_nvgen_gate",
  "node_rva": "0x37181A48"
}
```

### Ca-6974aa3b4f29ead6

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35F83598",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-697555efba4d97bd

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3370DD60",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-697748b4cc162396

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F9318",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69799bf02b6817f0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x120E92D0",
  "kind": "predicate",
  "node_rva": "0x3579EB60"
}
```

### Ca-697e107f6f6d4800

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB277640",
  "kind": "predicate",
  "node_rva": "0x336ECD48"
}
```

### Ca-697fccb807dd5c73

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378426D8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6982ab09eee9074c

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x35BD8DF0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-69837de63b4843b9

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x17B644B0",
  "kind": "predicate",
  "node_rva": "0x365C5BE0"
}
```

### Ca-6984ad7abec5b53b

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1BE1D4B0",
  "kind": "predicate",
  "node_rva": "0x37111A48"
}
```

### Ca-69862fbf7c5228c8

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xFE24FD0",
  "kind": "predicate",
  "node_rva": "0x348F3DC8"
}
```

### Ca-6987b3aa2c377c62

```json
{
  "descriptor": 93825886646200,
  "evaluated": false,
  "expected": true,
  "kind": "privilege_gate",
  "node_rva": "0x354FAEE0"
}
```

### Ca-6988233ed09171e2

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xECEC750",
  "kind": "predicate",
  "node_rva": "0x343EA3A0"
}
```

### Ca-69897caca280b85e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348BF5A8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-698d3c860b5d5824

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x356DE860",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-698e7bffe7fbe10d

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x345A57C8",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6990273e12a27653

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x378A5688",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69929a4d251dbca9

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35EBC2F0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-699487d6fa99742b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34692E50",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6995c609150b4c5f

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346E9588",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6999442f6104968e

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3581D0F8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-699df4ef656e5477

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1AB5C530",
  "kind": "predicate",
  "node_rva": "0x36D90D88"
}
```

### Ca-699f59cdd13ce83c

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x337DF498",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-699f5ea263efa0ae

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34B7AAB0",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-69a43186fb0edc6a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x17295550",
  "kind": "predicate",
  "node_rva": "0x3634E098"
}
```

### Ca-69a5ab027e27a963

```json
{
  "address_type_candidate": 20,
  "evaluated": false,
  "kind": "registered_address_parser_and_prefix_length",
  "node_rva": "0x357DFE30",
  "registry_rva": "0x3CB56200"
}
```

### Ca-69a63de3fddb34f4

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34BB6FA8",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-69a68f759dfb7d0b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDB54420",
  "kind": "predicate",
  "node_rva": "0x33FDA288"
}
```

### Ca-69a697e19d4a7492

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34918558",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-69ac0775eb360eda

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33A453D8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69b007a7258f71c3

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BBC8C0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69b7e84f4c659e5c

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34569518",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-69bb97105e696cef

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x36DDAC90",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-69bbeef0ec650f81

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x17E96850",
  "kind": "predicate",
  "node_rva": "0x36661960"
}
```

### Ca-69bc7648268d9ff3

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34B37F60",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69bd0e656c68b309

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34516700",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-69be9372570e909c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33A9E7F0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69c1abd472580372

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xCED3320",
  "kind": "predicate",
  "node_rva": "0x33D1FFC8"
}
```

### Ca-69c1e6214d0b88ba

```json
{
  "comparison_value_encoded_hex": "0000000000000000",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x3559BD40",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-69c7943b94836467

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
  "node_rva": "0x36B402B8",
  "snapshot_only": true
}
```

### Ca-69c88d1619a53895

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37E69EA8"
}
```

### Ca-69cb1f55a08f72dc

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34960118",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-69cee4dc9c3f91b1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33710748",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69cf000f5bc6600c

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x368CF700",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-69d278074114c321

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3418D948",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69d69e9f036ea8ea

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000004",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x342110A8"
}
```

### Ca-69d799686b193b13

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35FB1778",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69d95ba5d150bcbb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3475C1E0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-69dc6ca3d88af2ab

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3587FF10",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-69dc8c2717223cb5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35563578",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-69e1962903ca3b5d

```json
{
  "callback_rva": "0xECEAF70",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x343E3CF8"
}
```

### Ca-69e217797ffd09ef

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16B7ECC0",
  "kind": "predicate",
  "node_rva": "0x3610B7B8"
}
```

### Ca-69e3e6df4be43edb

```json
{
  "callback_rva": "0xBF374F0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x3395CDB0"
}
```

### Ca-69e481fbf9716f3b

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
  "node_rva": "0x376C7790",
  "snapshot_only": true
}
```

### Ca-69e8a147dbf06e07

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x15DD2C30",
  "kind": "predicate",
  "node_rva": "0x35E286A8"
}
```

### Ca-69edffb93f1fd18a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x342FD3A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69efbf605bbd0d4d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34827F78",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-69efe7a7eef2277b

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345C38D8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-69f27f4776b7cb07

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB27BBD0",
  "kind": "predicate",
  "node_rva": "0x33704900"
}
```

### Ca-69f6ab1c2a62cf6d

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "runtime_boolean",
  "node_rva": "0x349021F8",
  "variable_address_rva": "0x3CB54590"
}
```

### Ca-69fa5ea07504d2f3

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3457FB88",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-69fb8c9af9fcf411

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x346EF2E0"
}
```

### Ca-6a0012a03daca271

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34899B18",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a04b7149aa932e0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xB279230",
  "kind": "predicate",
  "node_rva": "0x336EFE50"
}
```

### Ca-6a06f793d602f7ed

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3605F4C0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a08de57629a113e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3488D578",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a091d4f45eafe26

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF96F10",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAE9D2A0"
}
```

### Ca-6a0abd97f2916bb7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF1431B0",
  "kind": "predicate",
  "node_rva": "0x345B11D0"
}
```

### Ca-6a0addce3db99a24

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA06200",
  "kind": "predicate",
  "node_rva": "0x33F7CCA0"
}
```

### Ca-6a0be25c37bb2f49

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDA2C0B0",
  "kind": "predicate",
  "node_rva": "0x33FA03C0"
}
```

### Ca-6a10e6d0e5b967bf

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3424D098",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a12401da5244362

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D4F0A0",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-6a15efb59b6a8dc8

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x354AA308",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-6a15fc06b7c02c7b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BC0C48",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a1ff360d1cb9530

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF1226C0",
  "kind": "predicate",
  "node_rva": "0x34562870"
}
```

### Ca-6a202260852f8136

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xC09EA20",
  "kind": "predicate",
  "node_rva": "0x33998A30"
}
```

### Ca-6a20260fafdf3bb7

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36FF33A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a21d0e5615967b6

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x358922A0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a220c60e5a2fab0

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x368965A0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a2274fdd3715a01

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34B3B5C8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a24371d599679b0

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35547F18",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a2636136edd7e09

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35435B00",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a266ab3ae07dac1

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
  "node_rva": "0x34008AB8",
  "normal_cli_only": true
}
```

### Ca-6a284d5525deb13a

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x15E78C30",
  "kind": "predicate",
  "node_rva": "0x35E551F0"
}
```

### Ca-6a285bcf7fff88ef

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDFF5120",
  "kind": "predicate",
  "node_rva": "0x34124350"
}
```

### Ca-6a2b62eb98f0580b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1426D5E0",
  "kind": "predicate",
  "node_rva": "0x35D14BC0"
}
```

### Ca-6a2bbfc507545968

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33E50C00",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a314273687f7c84

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000004",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x34BD6FA8"
}
```

### Ca-6a32253efa7e0e1b

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34914DB8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a35fcac25d828d8

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F8988",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6a3827208ada1fc5

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xF031E50",
  "kind": "predicate",
  "node_rva": "0x344F4C10"
}
```

### Ca-6a3a897099e66320

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34829C60",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a40496752f5963b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF148520",
  "kind": "predicate",
  "node_rva": "0x345C8BC0"
}
```

### Ca-6a4244a81ba2ccb2

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE1A33B0",
  "kind": "predicate",
  "node_rva": "0x3426A448"
}
```

### Ca-6a479053de6030fd

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF11B470",
  "kind": "predicate",
  "node_rva": "0x345403F0"
}
```

### Ca-6a49afd4b07f9ffc

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33984940",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6a4b67487254d81c

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35536650",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a4ee23818271569

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF61DF10",
  "kind": "predicate",
  "node_rva": "0x34707BD0"
}
```

### Ca-6a567f59c3e7027a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16984130",
  "kind": "predicate",
  "node_rva": "0x3605B770"
}
```

### Ca-6a57652988d4296a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x339BB360",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a57c3d9f64abf50

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336E1988",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a58b43eb865fa33

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x13026CB0",
  "kind": "predicate",
  "node_rva": "0x35A12178"
}
```

### Ca-6a5d7125cd7be035

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x136909E0",
  "kind": "predicate",
  "node_rva": "0x35BEA908"
}
```

### Ca-6a614b072778054d

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x356F1550",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a615f4c0d259ed9

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
  "node_rva": "0x37756010",
  "normal_cli_only": true
}
```

### Ca-6a69ae9cc9d0fab4

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34BDED10",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a711dacc65b0268

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3443FE88",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-6a77d7de7ed7c6ea

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF125A60",
  "kind": "predicate",
  "node_rva": "0x34571020"
}
```

### Ca-6a780b82087bfbdb

```json
{
  "evaluated": false,
  "kind": "descriptor_literal_matching",
  "literal": "*",
  "node_rva": "0x35674180",
  "wrapper_whitespace_and_match_flags_symbolic": true
}
```

### Ca-6a7ad905f88497b0

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
  "node_rva": "0x33E7ED98",
  "snapshot_only": true
}
```

### Ca-6a7d8eedb5317f5a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344178B8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6a7f475b2e9b6f59

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33DE2428",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6a7ffe3fcb0f05c6

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF11B920",
  "kind": "predicate",
  "node_rva": "0x34544A00"
}
```

### Ca-6a8123d34ec02767

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33D16BF8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a8215995c4e6033

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1715D3D0",
  "kind": "predicate",
  "node_rva": "0x362A0638"
}
```

### Ca-6a831ec666e0cacc

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346A6128",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6a979f7346fbec8e

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825332275040,
      "reason": "Producer semantics unresolved; no function executed"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x35D6D020",
  "source": {
    "dynamic_scratch_entry": false,
    "getter": 93825332275040,
    "kind": "producer_callback",
    "producer_executed": false,
    "release_callback": null
  }
}
```

### Ca-6a997112e70b1339

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
  "node_rva": "0x37576728",
  "snapshot_only": true
}
```

### Ca-6a9d5ef8a5da2e9a

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE196BE0",
  "kind": "predicate",
  "node_rva": "0x34230BF8"
}
```

### Ca-6a9f97388144d5e7

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF039FF0",
  "kind": "predicate",
  "node_rva": "0x345095E0"
}
```

### Ca-6aa02ae907977633

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1215D1B0",
  "kind": "predicate",
  "node_rva": "0x357AF798"
}
```

### Ca-6aa623cad4ca8d57

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x3426BEB0"
}
```

### Ca-6aa6c8e7d647239d

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x368CFAD0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6aa7a7f22050dd15

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x12529AA0",
  "kind": "predicate",
  "node_rva": "0x35894660"
}
```

### Ca-6aaa0cc7fa8f96c3

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x347C7530",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6aaa2c022c412802

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x354D4170",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6aaa42073b6f171e

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x357F9C18",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6aac359ea1919443

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xE19AA70",
  "kind": "predicate",
  "node_rva": "0x34251418"
}
```

### Ca-6aae0685ff6411b0

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF123040",
  "kind": "predicate",
  "node_rva": "0x34562770"
}
```

### Ca-6aae3035b0ffb878

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
  "node_rva": "0x3379E240",
  "snapshot_only": true
}
```

### Ca-6aaeeb1572b20418

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BBC008",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ab10bfb37e18760

```json
{
  "evaluated": false,
  "expected": false,
  "kind": "runtime_boolean",
  "node_rva": "0x342001B8",
  "variable_address_rva": "0x3CB6A36C"
}
```

### Ca-6ab2d3222e243295

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344E13F8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6ab38cd55fb50b38

```json
{
  "callback_rva": "0x178191A0",
  "evaluated": false,
  "expected": false,
  "kind": "no_argument_predicate",
  "node_rva": "0x36571900",
  "normal_cli_only": true
}
```

### Ca-6ab55373baa94b85

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34A433A8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6ab562953f36522b

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x36DA5728",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-6ab68b41d751e557

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "interface_status_mask",
  "mask_candidate": 4194432,
  "node_rva": "0x354B5C20",
  "note": "Normal CLI requires a current interface/IDB; help paths differ"
}
```

### Ca-6ab903dade6818e2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x348B9428",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6abc82c6e01eb865

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x355A4470",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6abdba35c7d16409

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x346E0DC8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6ac0c02009bac2a1

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BBC8C0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ac2a0e7fe7ee885

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33711198",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6ac4292495123cf8

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33B33F68",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6ac4c6fcef5c4269

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x16A41140",
  "kind": "predicate",
  "node_rva": "0x36075D78"
}
```

### Ca-6ac51edf55686e65

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x161611A0",
  "kind": "predicate",
  "node_rva": "0x35EF8D38"
}
```

### Ca-6ac786377aceb7a5

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000002",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x33D015B8"
}
```

### Ca-6aca2ef20077f82e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE9C7B40",
  "kind": "predicate",
  "node_rva": "0x3437C6F0"
}
```

### Ca-6acb1ab657912c44

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
  "node_rva": "0x33D1F238",
  "normal_cli_only": true
}
```

### Ca-6acb971b0aa7d918

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
  "node_rva": "0x347FD5A0",
  "snapshot_only": true
}
```

### Ca-6acf6eeab3ca3243

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11860480",
  "kind": "predicate",
  "node_rva": "0x3555BF28"
}
```

### Ca-6acfb4163f457b38

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36777118",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ad15027b3737ac7

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35469040",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ad25c14981e3538

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3605C220",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ae265f55bf8b4b6

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D5A128",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6ae67c8cb15eb210

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3417ED40",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6ae84ff13d54a11a

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x33CF79B8",
  "parameter_omitted": false,
  "sense": 0
}
```

### Ca-6aeafb63d9b60378

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x12364610",
  "kind": "predicate",
  "node_rva": "0x35822810"
}
```

### Ca-6aefe79ef1c66e4f

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x13053580",
  "kind": "predicate",
  "node_rva": "0x35A14C18"
}
```

### Ca-6af10277a9848b80

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF121570",
  "kind": "predicate",
  "node_rva": "0x3455FC30"
}
```

### Ca-6af1b247c0a1e14c

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11C15710",
  "kind": "predicate",
  "node_rva": "0x356879B0"
}
```

### Ca-6af8e425ecf26a0d

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BB77B0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6af8f4a170194670

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xDFF55F0",
  "kind": "predicate",
  "node_rva": "0x3411F2F0"
}
```

### Ca-6afba3c92989b300

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33DBB848",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6afdc35b4dc79fb8

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x369B4590",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b006c66b09d74e7

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34441668",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-6b036bf32c372128

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x346665E0",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6b0aa4687893b8a5

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xBD41DD0",
  "kind": "predicate",
  "node_rva": "0x338D1268"
}
```

### Ca-6b0ab9098d1c442b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xBD42F60",
  "kind": "predicate",
  "node_rva": "0x338E6D70"
}
```

### Ca-6b0cc349d7aca153

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x344F2068",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b0f4e3adb5a5e29

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9328,
  "kind": "parser_state_comparison",
  "node_rva": "0x347CFF18",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-6b1182d864559cfb

```json
{
  "evaluated": false,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x36D782E8",
  "parameter_omitted": false,
  "sense": null
}
```

### Ca-6b136f4ac76a1f33

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
  "node_rva": "0x33758508"
}
```

### Ca-6b15520e21ef6634

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xB36BE20",
  "kind": "predicate",
  "node_rva": "0x33753370"
}
```

### Ca-6b15af440e4d9b99

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35459760",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b15c33640d6503a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3417DCE0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b1764f967709687

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x378F5458",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6b19633fca017b67

```json
{
  "callback_rva": "0x11DBDE20",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x356F21D8"
}
```

### Ca-6b1b319596a5ddda

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1937C790",
  "kind": "predicate",
  "node_rva": "0x369AF3A8"
}
```

### Ca-6b1bb22a3ff9e470

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1771FE50",
  "kind": "predicate",
  "node_rva": "0x36472950"
}
```

### Ca-6b29ef08091ab16a

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x358130D0"
}
```

### Ca-6b2a4f92ead9d0f9

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35484160",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b2e9fa49c2ea27b

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BD96070",
  "kind": "predicate",
  "node_rva": "0x36FF20C0"
}
```

### Ca-6b32e47be11ec5c0

```json
{
  "callback_rva": "0x166253C0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x35FB7658"
}
```

### Ca-6b33a9bfe8bbfce4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3605F4C0",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6b39b6cc7d84c560

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3495FE28",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-6b3b70ebeb6aa8fc

```json
{
  "evaluated": false,
  "field_offset": 8908,
  "kind": "parser_state_mask_zero",
  "known_value": null,
  "mask_encoded_hex": "0000000000000004",
  "node_rva": "0x35396298",
  "required": "value & mask == 0",
  "width_candidate": 4
}
```

### Ca-6b41a49982d3522e

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x11DBEED0",
  "kind": "predicate",
  "node_rva": "0x356FC968"
}
```

### Ca-6b422a39b6a68350

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
  "node_rva": "0x3526EAB0",
  "snapshot_only": true
}
```

### Ca-6b42c67ec0e18e9e

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
  "node_rva": "0x37586758",
  "normal_cli_only": true
}
```

### Ca-6b45cd7e9225b132

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3523A128",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b47fe2a5af409d8

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36777118",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b4925efc238ae9d

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16624430",
  "kind": "predicate",
  "node_rva": "0x35FAE800"
}
```

### Ca-6b4b7fcef4166ead

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34C46600",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6b4f6b4e40ab6062

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFFBAEDD1E0"
}
```

### Ca-6b4ff60b6d8b4a4e

```json
{
  "evaluated": false,
  "field_offset": 10434,
  "kind": "parser_field_mask_zero",
  "mask": 1,
  "node_rva": "0x33FDE178",
  "width": 1
}
```

### Ca-6b503d27637c8afb

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36FF3040",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b504c00db5f25b8

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x33E13900",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6b55d00ed5e96acd

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36FF3AA0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b589c5afc1312dc

```json
{
  "comparison_value_encoded_hex": "0000000000000008",
  "evaluated": false,
  "evaluation_source": "unresolved",
  "field_offset": 8952,
  "kind": "parser_state_comparison",
  "node_rva": "0x33AEB040",
  "relation": "eq",
  "width_candidate": 4
}
```

### Ca-6b5901f743bf0095

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x1251FDF0",
  "kind": "predicate",
  "node_rva": "0x3587F690"
}
```

### Ca-6b5ab2abd65e8f82

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x336F3DF0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b5abc4feafd7882

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34648330",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6b5eb753557abc2a

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33EC2F88",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b5f380eba772115

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33BBD790",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b631ed2405e8b30

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x105B4430",
  "kind": "predicate",
  "node_rva": "0x34B85EC8"
}
```

### Ca-6b66f15453f98242

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xE4D4860",
  "kind": "predicate",
  "node_rva": "0x342D3620"
}
```

### Ca-6b67935bb4433b16

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xDF97130",
  "kind": "predicate",
  "node_captured_va": "0x7FFF37EA3A68"
}
```

### Ca-6b6a293d901cc68b

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x357FB680"
}
```

### Ca-6b743d4c1edeb455

```json
{
  "evaluated": false,
  "kind": "descriptor_literal_matching",
  "literal": "wlan ap",
  "node_rva": "0x35E9A8F0",
  "wrapper_whitespace_and_match_flags_symbolic": true
}
```

### Ca-6b74d6f0b84dcc54

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x33FEDDA8",
  "parameter_omitted": false,
  "sense": 1
}
```

### Ca-6b750499673e26e1

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x105B43C0",
  "kind": "predicate",
  "node_rva": "0x34B91190"
}
```

### Ca-6b75b7332c4aff28

```json
{
  "comparison_value_encoded_hex": "0000000000000001",
  "evaluated": true,
  "evaluation_source": "symbolic local state",
  "field_offset": 9636,
  "kind": "parser_state_comparison",
  "node_rva": "0x344D0190",
  "relation": "ne",
  "width_candidate": 4
}
```

### Ca-6b75cf726f65d3b5

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x360602E0",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b7a74e9d0939a69

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34880010",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b7b261d628d3842

```json
{
  "evaluated": false,
  "frontiers": [
    {
      "address": 93825419565408,
      "reason": "Producer semantics unresolved; no function executed"
    }
  ],
  "kind": "unresolved_option_source",
  "node_rva": "0x36A53408",
  "source": {
    "dynamic_scratch_entry": true,
    "getter": 93825419565408,
    "kind": "producer_callback",
    "producer_executed": false,
    "release_callback": null
  }
}
```

### Ca-6b7d0153df9bac9b

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x340B8920",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6b7fe77378b1c25a

```json
{
  "evaluated": false,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x34018448",
  "state": [
    null,
    null,
    0
  ]
}
```

### Ca-6b829b8980cdd83f

```json
{
  "evaluated": false,
  "expected": true,
  "kind": "runtime_boolean",
  "node_rva": "0x354C9398",
  "variable_address_rva": "0x33613278"
}
```

### Ca-6b84b9ee1845b0b4

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3546A050",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b851414951b0d28

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x3436AF28",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b87a1f387af29ed

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0x14043FE0",
  "kind": "predicate",
  "node_rva": "0x35CE7168"
}
```

### Ca-6b954d5c2ad16729

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1938F2D0",
  "kind": "predicate",
  "node_rva": "0x369C3198"
}
```

### Ca-6b95c214e4e59331

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33AA2BF8",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b9682d2a5742200

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35418650",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6b97afb14c8d2d92

```json
{
  "boundary_codes": [
    0,
    33,
    59
  ],
  "boundary_requires_field_zero": 11960,
  "character_table_rva": "0x7A139E0",
  "class_mask": 8,
  "consumption": "DEF4DC0 temporarily advances input offset while scheduling accept",
  "evaluated": false,
  "expected_nvgen": 0,
  "input_offset_field": 12124,
  "kind": "whitespace_or_input_boundary",
  "node_rva": "0x346242A0",
  "nvgen_field": 9636
}
```

### Ca-6ba30d8fb08c419f

```json
{
  "constraints": [
    {
      "evaluated": false,
      "kind": "keyword_option_match",
      "minimum_match": 0,
      "note": "Privilege, parser mode, ambiguity and additional flags still constrain matching",
      "value": 0
    }
  ],
  "kind": "keyword_constraints",
  "node_rva": "0x33734278"
}
```

### Ca-6bae791271413870

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x358806F8",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6bb1e19da5cf4b21

```json
{
  "evaluated": false,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x34BEAEE0",
  "parameter_omitted": false,
  "sense": null
}
```

### Ca-6bb221b7a20690de

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35437838",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6bb5247702a9014c

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x345A41A8",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6bb656b373d829bc

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x342BEBE0",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6bbb38220e9adcf5

```json
{
  "evaluated": false,
  "kind": "descriptor_literal_matching",
  "literal": "low percent",
  "node_rva": "0x3608F2E8",
  "wrapper_whitespace_and_match_flags_symbolic": true
}
```

### Ca-6bbe0f2c4be4ada3

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000001",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x33B34980"
}
```

### Ca-6bbfaf65a85b88f6

```json
{
  "evaluated": true,
  "kind": "combined_keyword_parameter_terminal",
  "node_rva": "0x3487D170",
  "parameter_omitted": true,
  "sense": 0
}
```

### Ca-6bcb7c3e9202ec9e

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF1469B0",
  "kind": "predicate",
  "node_rva": "0x345BB1C8"
}
```

### Ca-6bcecc462f6081ca

```json
{
  "callback_rva": "0xD1D8DC0",
  "evaluated": false,
  "kind": "dynamic_number_bounds",
  "node_rva": "0x33DB9C30"
}
```

### Ca-6bd22e47e3380f65

```json
{
  "callback": 0,
  "evaluated": false,
  "flags_encoded_hex": "00000000",
  "kind": "interface_registry_and_validation",
  "node_rva": "0x3483BA78"
}
```

### Ca-6bd2472158cd5ae2

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x371FD720",
  "state": [
    0,
    0,
    0
  ]
}
```

### Ca-6bd3e44bb43c8399

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x11258830",
  "kind": "predicate",
  "node_rva": "0x3543B480"
}
```

### Ca-6be2cc0ac0d77a93

```json
{
  "evaluated": true,
  "expected_positive": true,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x36D90C58",
  "state": [
    1,
    0,
    0
  ]
}
```

### Ca-6be4236ba953bd92

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x16A9BEF0",
  "kind": "predicate",
  "node_rva": "0x36084E00"
}
```

### Ca-6be67b19e55136d9

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x35657268",
  "state": [
    0,
    1,
    0
  ]
}
```

### Ca-6bef893e39cbba35

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xED66A40",
  "kind": "predicate",
  "node_rva": "0x3440FEE8"
}
```

### Ca-6bf32ac09d6724fc

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0xF574530",
  "kind": "predicate",
  "node_rva": "0x3468C358"
}
```

### Ca-6bf67e71512a93ce

```json
{
  "evaluated": false,
  "expected": true,
  "function_name": "",
  "function_rva": "0x1BD96450",
  "kind": "predicate",
  "node_rva": "0x36FF4CD8"
}
```

### Ca-6bf76ff7e16f7115

```json
{
  "evaluated": false,
  "expected": false,
  "function_name": "",
  "function_rva": "0xB617100",
  "kind": "predicate",
  "node_rva": "0x337BE550"
}
```

### Ca-6bf821dc93b34e6e

```json
{
  "evaluated": true,
  "expected_positive": false,
  "kind": "normal_cli_noprefix",
  "node_rva": "0x33FD7610",
  "state": [
    0,
    1,
    0
  ]
}
```
