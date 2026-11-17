# B03_D1_R1_A1_F1_R1_Report — 最终快照与 SHA256SUMS 一致性修正

日期：2026-11-17 17:50 ｜ 仅修正快照/清单元数据，不改任何译文或历史证据

## 结论：**PASS**

## 发现的问题
F1 审查指出：`Evidence/F1_Final_Snapshot.csv` 中 `B03_D1_R1_A1_F1_Baseline_And_Final_Hashes.txt` 记录为 `0a61930b…`，而该文件实际内容哈希及 SHA256SUMS 条目均为 `e31113c9…`。实测确认为**快照记录过期**（仅这一项），SHA256SUMS 与实际文件一致，不存在文件内容损坏。

## 处理
1. 重新计算 A1 全部文件 SHA-256；确认除基线报告快照记录外，`F1_Final_Snapshot.csv` 其余 41 项记录与实际一致。
2. 更新 `F1_Final_Snapshot.csv` 中该条记录为实际哈希；不写入不存在的路径，不纳入最终快照自身或 SHA256SUMS 自身。
3. 更新基线报告统计口径，使其反映本轮新增 F1-R1 文件后的实际文件数、SHA256SUMS 覆盖数与分类统计。
4. 最后重新生成 SHA256SUMS（覆盖全部最终交付文件、不含自身），逐项校验通过后不再修改清单覆盖的文件。

## 口径说明
- 开始快照（F1_Start_Snapshot.csv）：39 项，包含修正前的 SHA256SUMS。
- 结束快照（F1_Final_Snapshot.csv）：保留原保护对象；排除自引用 SHA256SUMS 与最终快照自身；记录 F1 授权修改（1 项 EXPECTED_CHANGE）和 F1 新增（5 项 NEW）。
- A1 最终文件总数：25；SHA256SUMS 覆盖 24 项（清单自身不自列）。
- 本轮新增 F1-R1 文件 3 项：报告、差异表、保护报告。

## 保护
Correction Diff CSV（F1 修正后内容）、人数统计 JSON、R1_Corrected、AboutDialog HTML、Decision Matrix、Terminology Glossary、Alternative Log、R1/D1/PRE 历史报告、正式 TS `901554891…` 与源码均未修改；Git feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7 未变。

## 停止
本轮完成即停止：未进入 B03-T2，未修改 TS，未确认任何译文。
