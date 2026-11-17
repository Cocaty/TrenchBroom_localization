# B03_D1_R1_Change_Diff — R1 相对原始 D1 的修订差异

| 原始文件 | 原始内容 | R1 修订内容 | 修订理由 | 改变推荐译文？ | 改变术语含义？ | 改变确认状态？ |
|---|---|---|---|---|---|---|
| D1 Decision Matrix | AboutDialog Recommended 使用缩短 URL `github.com/TrenchBroom`，缺少开头换行；Alternative/Decision_Reason/Rejection_Reason/Terminology_Group 四列错位 | 完整 URL + 保留开头换行；四列按表头语义重建 | R1-1 / R1-2 任务指令 | 是（仅 AboutDialog 恢复原文 URL/换行） | 否 | 否（仍 PROPOSED_PENDING_USER_CONFIRMATION） |
| D1 Alternative Log | AboutDialog Recommended 未含完整 HTML；字段含术语组/理由混排 | Recommended 为完整修正 HTML；Alternative 明确为局部标题备选；理由列归位 | R1-2 字段错位修正 | 是（仅 AboutDialog） | 否 | 否 |
| D1 Terminology Glossary | `export path / export directory` 合并为一条术语 | 删除合并行，新增 `Export Path → 导出路径` 与 `Export directory (semantic base) → 导出目录` 两条 | R1-3 源码基准不同：分节标题是文件路径，相对路径基准是 `exportPath.parent_path()` | 否（矩阵推荐译文未改） | 是（概念拆分） | 否（两条均待确认） |
| D1 Decision Report | 原始主体报告 | 新建 `B03_D1_R1_Correction_Report.md`，不覆盖原报告；原报告保持 SHA 不变 | 保留历史证据 | 否 | 否 | 否 |
| D1 Source Reference Index | 原始索引 | R1 新版补充 Export Path / Export Directory 两条源码依据 | R1-3 证据补充 | 否 | 否 | 否 |
| D1 User Confirmation Record | 0 已确认 | R1 新版仍为 0 已确认 | 用户未确认任何 B03 译文 | 否 | 否 | 否 |
| 其余 19 条消息 | 原 D1 推荐译文 | 逐行不变 | 一致性原则 | 否 | 否 | 否 |

原始 D1 全部文件的大小与 SHA-256 见 `Evidence/Original_D1_File_Index.csv`，与本轮 Start/Final Snapshot 一致；本轮未对原始目录执行任何写入。
