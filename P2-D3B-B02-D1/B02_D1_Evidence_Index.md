# B02_D1_Evidence_Index — 决策证据索引（本轮只读核对）

| 证据 | 路径 | 本轮用途 | 说明 |
|---|---|---|---|
| 权威批次文件 | `reports\P2-D3A-R1-A\Evidence\Revised_Batches.csv` | 确认 RA-B02 归属唯一 | 本轮只读哈希记录 |
| 当前 TS | `src\TrenchBroom\app\TrenchBroom\translations\TrenchBroom_zh_CN.ts` | 核对目标 ID/context/source/location/translation 状态、统计与 SHA | **未修改** |
| PRE 实施报告 | `reports\P2-D3B-B02-PRE\B02_PRE_Implementation_Report.md` | 决策结论与证据来源 | 沿用，不重新验证其源码调查 |
| PRE 源码证据索引 | `reports\P2-D3B-B02-PRE\B02_Source_Evidence_Index.md` | 源码位置 `WelcomeWindow.cpp:140` 与调用链 | 沿用预审记录，非本轮独立验证 |
| PRE 语义审计 CSV | `reports\P2-D3B-B02-PRE\B02_Source_Semantic_Audit.csv` | UI 归属：文件对话框标题 | 沿用 |
| PRE 术语风险 CSV | `reports\P2-D3B-B02-PRE\B02_Terminology_Risk_Audit.csv` | “打开地图文件/打开地图”候选来源 | 沿用 |
| PRE 就绪 CSV | `reports\P2-D3B-B02-PRE\B02_Translation_Readiness.csv` | 预审状态 `NEEDS_TERMINOLOGY_CONFIRMATION` → 本轮由用户确认冻结 | 沿用 |
| PRE 范围审计 CSV | `reports\P2-D3B-B02-PRE\B02_Batch_Scope_Audit.csv` | 历史 R1-B02 两条的移出记录 | 沿用 |
| 本轮决策 CSV | `B02_D1_Decision_Record.csv` | 正式决策结构化记录 | 本轮新建 |
| 本轮开始/结束哈希 | `Evidence_Start_Hashes.csv`、`B02_D1_Baseline_And_Final_Hashes.txt` | 基线一致性证明 | 本轮新建 |

## 边界说明
本轮仅**只读检查 TS 中的消息身份与状态**，没有重新打开或核对 `WelcomeWindow.cpp` 源码；报告中的源码位置与调用链均明确标注为来自 `P2-D3B-B02-PRE`。
