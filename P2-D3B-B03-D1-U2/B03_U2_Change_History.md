# B03_U2_Change_History — U1 → U2 变更历史

| 阶段 | 决策状态 | 译文内容 | 术语口径 |
|---|---|---|---|
| B03-D1 / R1 / R1-A1 系列 | `PROPOSED_PENDING_USER_CONFIRMATION` | 候选译文，AboutDialog 经 R1 修正 URL 与开头换行 | 待用户确认 |
| B03-D1-U1 | `PROPOSED_PENDING_USER_CONFIRMATION` | 20 条候选按 A/B/C/D/E 分组供审阅 | 待决问题已列出 |
| **B03-D1-U2（本轮）** | **20/20 `USER_CONFIRMED`** | **逐字继承 U1 推荐译文，无改动** | **用户逐组确认，术语审计 PASS** |

## 本轮实际变化
1. 新建最终决策矩阵：20 行，`Decision_Status=USER_CONFIRMED`
2. 新建最终术语表：R1 术语表 12 条，确认状态更新为 `USER_CONFIRMED`
3. 新建确认记录、术语一致性审计、变更历史、保护报告、快照与 SHA
4. 未修改：正式 TS、源码、CMake、QRC、QM、D1/R1/A1/U1 历史报告、U1 快照

## 后续状态规则
本轮不将任何条目设为 `FINAL_FROZEN`。需用户与 ChatGPT 复核最终决策矩阵，并获得明确的冻结/写入授权后，才能进入后续状态或 B03-T2。
