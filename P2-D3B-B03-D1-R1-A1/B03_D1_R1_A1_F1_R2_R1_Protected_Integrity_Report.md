# B03_D1_R1_A1_F1_R2_R1_Protected_Integrity_Report — 保护核验

开始快照：`Evidence/F1_R2_R1_Start_Snapshot.csv`（30 项）。结束快照：`Evidence/F1_R2_R1_Final_Snapshot.csv`（34 项，排除 SHA256SUMS 自身与最终快照自身）。

| 对象 | 结果 |
|---|---|
| 正式 TS / 源码 / CMakeLists | 未修改（TS `901554891…`） |
| Git 分支 / HEAD / dirty | feature/zh-CN-v2026.2 / `4c756be1…` / 7 ——未变 |
| PRE / D1 / D1-R1 原始报告与修正副本 | 未修改 |
| A1 勘误报告、人数 JSON、Correction Diff CSV、AboutDialog HTML、R1_Corrected、Decision Matrix、Terminology Glossary、Alternative Log | 未修改 |
| F1 / F1-R1 / F1-R2 原始报告、差异表、保护报告与历史快照 | 未修改（除下项） |
| **B03_D1_R1_A1_F1_R2_Diff.csv** | 本轮唯一修改的既有文件：2 处口径修正 |
| SHA256SUMS.txt | 本轮授权重建 |
| 新增 R2-R1 文件 | 勘误说明、报告、差异表、保护报告、开始快照、最终快照 |

未运行 lupdate/lrelease/lconvert，未构建、启动、部署，未提交 Git。除上述授权项外，开始快照中的 29 个非清单文件：28 个 UNCHANGED、1 个 EXPECTED_CHANGE（R2 差异表），无其他变化。

**结论：无越界变化。**
