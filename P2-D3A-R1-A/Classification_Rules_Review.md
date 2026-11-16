# Classification_Rules_Review — R1-A 分类原则（功能优先）

## 优先级（自上而下，命中即停止）

1. **同一动作注册语句的实际处理逻辑**（handler/callback：如 `toggleShowPointEntityBounds()`、`performSweep()`、`duplicateAndMoveObjects()`）
2. **完整动作路径语义**（`Menu/File/…` 文件；`Controls/Map view/View Filter > …` 视图过滤；不以 `Map view` 前缀直接判 2D）
3. **完整 ActionContext 枚举列表**（多行表达式全量提取；`SelectionOwnedByTool` / `SweepTool` / `ClipTool` 只作辅助标签，不直接决定功能域）
4. 所属函数与调用关系（`createFileMenu`、`createViewActions` 等）
5. source 关键词（辅助证据）
6. 无法可靠判断 → **UNKNOWN**（附证据原因，不强行归类）

## 关键边界

| 概念 | 处理 |
|---|---|
| 菜单显示位置 | 仅当路径确为 `Menu/...` 时才作为菜单类证据；不把“显示在 View 菜单”等同于普通 2D 编辑 |
| 动作路径组织层级 | `Controls/Map view/...` 是控制路径，不代表 2D 功能；Entity View Filter、Sweep 等按 handler 归类 |
| 工具上下文 | `SweepTool`/`ClipTool`/`SelectionOwnedByTool` 为辅助标签；工具命令（sweep/clip 本身）归几何，移动对象命令归 2D |
| 实际功能 | 由 handler 中的 `context.xxx().yyy()` 调用链判定，证据写入 CSV |
| 翻译领域 | 每条消息唯一主分类；辅助标签不分裂批次 |

## 证据字段

`Action_Registration_Audit.csv`（181 条 ActionManager 消息）逐条记录 message_id / source / source_line / am_function / action_path / **action_context_full**（全部枚举值）/ handler_callback / statement_start / statement_end / category / reason / evidence_confidence。

非 ActionManager 消息按 context/文件名/source 关键词规则处理，证据强度标“中”；证据不足者标“低”并保留 UNKNOWN。

## 限制

- handler 提取依赖 lambda 结构（当前源码 181 条均来自 addAction 语句），个别复杂 lambda 可能只截到首行（CSV 中如实记录截断片段）
- 分类仍为自动规则结果，最终术语与领域归属需 ChatGPT 校阅确认；UNKNOWN 56 条未强行归类
