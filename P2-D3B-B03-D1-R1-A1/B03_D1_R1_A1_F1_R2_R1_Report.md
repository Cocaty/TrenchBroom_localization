# B03_D1_R1_A1_F1_R2_R1_Report — R2 审计记录口径修正与最终复核

日期：2026-11-17 18:07 ｜ 仅审计元数据修正

## 结论：**PASS**

## 三项处理
1. **R2 差异表文件数量统计**：原 SHA256SUMS 行写为“最终 31 文件、覆盖 30 项”；实测 F1-R2 阶段结束后目录为 **30** 文件、清单覆盖 **29** 项，已改为“按 R2 最终 30 文件清单重建，覆盖 29 项；SHA256SUMS 自身不自列。”
2. **Correction Diff 哈希口径**：R2 差异表首行旧值由 `419e5de3…` 改为 `11cbb768…`，Old=New=`11cbb768…`，Change_Type 仍为 `UNCHANGED_IN_R2`；理由明确 `419e…` 是 F1 阶段开始时的历史哈希，已在 F1 授权修正，非 R2 变化。当前文件实测仍为 `11cbb768…`（633 B），与 F1 最终快照、R2 开始快照及 SHA256SUMS 一致。
3. **F1 基线报告历史口径**：原报告“旧哈希 11cbb768…”有误，但不修改原始报告；新建独立勘误说明，用 F1 开始/结束/R2 开始及本轮实测四份证据说明 `419e… → 11cbb…` 发生在 F1 阶段。

## 变化范围
本轮唯一修改的历史文件：`B03_D1_R1_A1_F1_R2_Diff.csv`（上述两处）。新增 6 项：历史哈希勘误说明、本报告、本差异表、保护报告、开始快照、最终快照。

## 计数口径
- R2-R1 开始文件数：30（含旧 SHA256SUMS）
- R2-R1 结束文件数：**36**
- SHA256SUMS 覆盖：**35** 项（清单自身不自列）
- F1_R2_R1_Final_Snapshot.csv 记录 **34** 项：28 项 UNCHANGED + 1 项 EXPECTED_CHANGE（R2 差异表）+ 5 项 NEW；排除 SHA256SUMS 自身与最终快照自身以规避循环依赖
- SHA256SUMS 独立校验：PASS=35，FAIL/MISSING/UNREADABLE=0

## 保护
正式 TS `901554891…`、源码、CMakeLists、Git `4c756be1…`/dirty=7；PRE/D1/D1-R1/A1 全部历史报告与快照、Correction Diff CSV、人数 JSON、AboutDialog HTML、R1_Corrected、Decision Matrix、Terminology Glossary、Alternative Log 均未变化。20 条候选译文仍为 `PROPOSED_PENDING_USER_CONFIRMATION`。

## 交付说明
本轮未上传 GitHub；无可验证的 GitHub 报告目录链接，不虚构 URL。交付以 A1 本地目录绝对路径为准。

**停止：未进入 B03-T2，未修改 TS，未确认任何译文。**
