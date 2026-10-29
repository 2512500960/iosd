# 证据与输出

先回答用户的问题，附上复核所需的证据。较大的图、表和采集存文件，对话中给关键路径、限制和链接。

## 建议字段

```json
{
  "identity":{"input_md5":"...","imagebase":0},
  "source":"saved_idb | debugger | elf_core | historical_capture",
  "observations":[],
  "candidates":[],
  "unknown":[],
  "coverage":{"scope":"...","limits":{},"truncated":false},
  "next_evidence":[]
}
```

这是可组合的输出约定，不强制改写旧脚本 schema。保存原始输出、raw_hex、引用类型、RVA、谓词和错误；报告链接回材料。历史材料缺少独立身份时明确标记。

## 未知项

保存位置、原因和来源，例如 `unread_page`、`unresolved_indirect_call`、`unbound_static_definition`、`unknown_opcode`、`state_condition_unverified`、`budget_limit`。区分未读、不能解码、未证明关系和当前未绑定。

完整路径、前缀、片段、边界和循环都保留。不完整 undocumented 候选仍可能有研究价值；静态定义也不证明特定状态下可输入或执行。

## 比较与解释

静态图和快照按身份、RVA、布局和来源关联。运行时堆节点、未绑定静态节点、条件拒绝和未读页分开统计。前后状态变化不自动证明唯一因果。

说明已取得节点、未知/缺页/限额项、mode 和 roots 范围。路径数需带去重、循环截断、参数投影和 variant 预算，不等于独立命令数。

解释可采用“入口 → 分发/条件 → handler/状态 → 结果”的简图，标明事实与候选。下一步明确到待核对的注册槽、待补读页或条件写入者，不笼统地说继续逆向。
