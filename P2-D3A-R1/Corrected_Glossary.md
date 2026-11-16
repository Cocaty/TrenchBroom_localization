# 修正后的术语表（R1）

数据：`Evidence/P2D3A_R1_Glossary.csv`（46 行；新增 `TS_exact_matches` 与 `In_current_batch` 列）。

## 口径修正

P2-D3A 报告称“仅 4 项无精确匹配”，实际重新逐项正则精确匹配（`\bEnglish\b`，忽略大小写）后为 **13 项**：

`Plane`、`Polygon`、`Geometry`、`Primitive`、`Model`、`Spawn`、`Mapping`、`Projection`、`Carve`、`Prefab`、`Package`、`Import`、`Game Configuration`。

报告、CSV、最终报告统一采用 **13 项无匹配** 口径；这些条目保留为**预备术语**，置信度统一标“低”，`In_current_batch` 列标“否（无精确匹配，预备）”，**不得混入当前翻译批次**。

## 有精确匹配的 33 项

每项 CSV 记录实际精确匹配次数（如 Brush 6、Face 4、Edge 6 等），置信度沿用候选表原值，候选译法未改动。

## 约束

1. 候选中文/备选译法仅建议，全部 `Review_status=待 ChatGPT 校阅`
2. 精确匹配为 0 的词不进入任何批次；后续 lupdate 若新增含这些词的 source，需重新统计
3. 术语表与批次计划交叉引用：核心术语批次（R1-B12/B13/B14/B15/B16）必须等校阅冻结后才启动
