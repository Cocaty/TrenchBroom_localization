# B03_D1_R1_A1_F1_R2_R1_R1_Report — 差异表哈希同步修正

日期：2026-11-17 18:15 ｜ 极小审计元数据修正

## 结论：**PASS**

## 修正的三处问题
1. `B03_D1_R1_A1_F1_R2_R1_Report.md` 的 New_Hash 由过期的 `92618c11…` 改为实际 `d46ef65d34c1c299c13c30ce6bea97617406f310f2ab77f67549047c282736f3`。
2. `B03_D1_R1_A1_F1_R2_R1_Protected_Integrity_Report.md` 的 New_Hash 由过期的 `dd42da51…` 改为实际 `dcb2ffe57d1ac0966521e22bc39777146ebc901c20aa79595615505c72ec3262`。
3. R2 差异表首行 Old/New 从 16 位截断值补齐为完整 SHA-256：
   - Old：`bca1d14edac0514d27bd71f5fdca99b8e1821f1ab91612f269649988a45a8989`
   - New：`fa9d031989d7f1663ceb7f36641b9ca50c7efc14293c2b2ea3f9b805d08e46c4`
   两者均由 F1-R2-R1 开始/最终快照实证，非推测。

## 历史证据保留
修正前的差异表已复制为 `Evidence/F1_R2_R1_R1_Diff_Before.csv`，其哈希记录于开始快照；原始 R2-R1 报告、F1-R2-R1 报告、最终快照与 SHA256SUMS 的历史含义均保留在本轮开始快照中。

## 同步更新
差异表本身变化后，已同步更新 `Evidence/F1_R2_R1_Final_Snapshot.csv` 中所有受影响条目，并按最终目录重建 `SHA256SUMS.txt`。最终文件数 **40**；SHA256SUMS 覆盖 **39** 项（清单自身不自列）；最终快照记录 **38** 项（排除清单自身与快照自身后与实际文件一一对应）。

## 保护
正式 TS `901554891…`、源码、Git `4c756be1…`/dirty=7、全部历史报告与快照、Correction Diff CSV、人数 JSON、AboutDialog HTML、R1_Corrected、决策矩阵/术语表/备选表均未修改；20 条候选译文仍全部待用户确认。

**停止：未进入 B03-T2，未修改 TS，未确认任何译文。**
