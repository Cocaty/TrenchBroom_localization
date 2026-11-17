# B03_D1_R1_A1_F1_R2_Report — 最终快照与 SHA256SUMS 全量一致性修正

日期：2026-11-17 17:59 ｜ 审计元数据修正，不涉及译文或源码

## 结论：**PASS**

## R2-0 发现
1. **Correction Diff CSV 实际哈希**：`11cbb768c60d858c59fb5352f7fc8b96ff53e2c31e50476f434e6bfc9845a67d`
   - 与 `SHA256SUMS.txt` 记录一致
   - 与 `Evidence/F1_Final_Snapshot.csv` 记录一致
   - `Evidence/F1_Start_Snapshot.csv` 记录 `419e5de3…`，是 **F1 修正前**的历史值（F1 授权仅修正两处 Evidence 路径，必然改变哈希）；历史快照按任务要求不修改
   - 因此不存在当前 SHA 清单与实际文件不一致的问题；无需修改 CSV 内容
2. 目录递归枚举：R2 开始时 **25** 个文件；无符号链接/重解析点/不可读文件。
3. Git feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7；正式 TS `901554891…`，均符合基线。

## R2-1 独立最终快照
新建 `Evidence/F1_R2_Final_Snapshot.csv`，不改写 F1 历史快照。它覆盖 F1-R1 新增的 3 个文件以及本轮新增文件，按实际递归枚举记录大小与 SHA-256。

**排除项（明确说明）**：
- `SHA256SUMS.txt` 不纳入最终快照：其自身哈希与清单重建存在循环依赖；其实际内容由清单自身逐项校验记录。
- `Evidence/F1_R2_Final_Snapshot.csv` 不记录自身哈希，避免自引用。
- 最终目录文件总数 **30**；最终快照记录 **28** 项（24 项 UNCHANGED + 4 项 NEW），差额 2 即上述排除项。

## R2-2 SHA256SUMS
按最终 30 个文件重新生成，排除清单自身，覆盖 **29** 项；路径唯一、无重复、无缺失、无不存在路径。独立校验由本轮重新读取清单逐项执行：PASS=29，FAIL/MISSING/UNREADABLE=0。清单生成后未再修改被覆盖文件。

## R2-3 保护核验
正式 TS、源码、CMakeLists、Git 状态、PRE/D1/D1-R1/A1 全部历史报告、Correction Diff CSV、人数统计 JSON、AboutDialog HTML、R1_Corrected、Decision Matrix、Terminology Glossary、Alternative Log、F1/F1-R1 报告及历史快照均未修改。仅本轮明确授权的审计清单/报告发生新增或重建；详见保护完整性报告与差异表。

## 关于 GitHub 目录链接
本会话可读取的 Git remote 为 `https://github.com/TrenchBroom/TrenchBroom.git`（仅上游源码仓库）；本轮无授权将本地报告上传或提交，也无法验证这些报告在 GitHub 上的对应目录链接。因此交付以本地绝对路径为准，不虚构 GitHub 目录 URL。

## 最终结论
**PASS** — 所有本地实际哈希、独立快照与重建清单逐项一致；无越界修改。20 条候选译文仍全部为 `PROPOSED_PENDING_USER_CONFIRMATION`。

**停止：未进入 B03-T2，未修改 TS，未确认任何译文。**
