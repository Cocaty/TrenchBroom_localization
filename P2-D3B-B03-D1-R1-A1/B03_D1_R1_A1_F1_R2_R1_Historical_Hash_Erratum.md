# B03_D1_R1_A1_F1_R2_R1_Historical_Hash_Erratum.md — F1 基线报告历史哈希口径勘误

## 勘误对象
`reports\P2-D3B-B03-D1-R1-A1\B03_D1_R1_A1_F1_Baseline_And_Final_Hashes.txt`

原始描述：
> `Correction_Diff.csv 旧哈希 11cbb768…`

## 快照证据（逐项实测）
| 阶段 | 来源 | Correction Diff CSV 哈希 | 大小 |
|---|---|---|---|
| F1 开始 | `Evidence/F1_Start_Snapshot.csv` | `419e5de308428c7a0921601145b64894480bf3bfed5020f037d75143f105f51c` | 651 B |
| F1 结束 | `Evidence/F1_Final_Snapshot.csv` | `11cbb768c60d858c59fb5352f7fc8b96ff53e2c31e50476f434e6bfc9845a67d` | 633 B |
| F1-R2 开始 | `Evidence/F1_R2_Start_Snapshot.csv` | `11cbb768c60d858c59fb5352f7fc8b96ff53e2c31e50476f434e6bfc9845a67d` | 633 B |
| R2-R1 开始（本轮实测） | 本地文件重新计算 | `11cbb768c60d858c59fb5352f7fc8b96ff53e2c31e50476f434e6bfc9845a67d` | 633 B |

## 结论
F1 基线报告中的“旧哈希 11cbb768…”存在**历史口径错误**。依据 F1 开始快照，F1 阶段的真实旧哈希为 `419e5de3…`；F1 阶段经授权修正两处 Evidence 路径后，F1 结束快照记录为 `11cbb768…`。因此 `11cbb768…` 是 **F1 修正后的哈希**，不是 F1 开始时的旧哈希。变化发生在 F1 阶段，不属于 R2 或 R2-R1 本轮变化。

本说明只修正审计解释，不修改原始 F1 基线报告、Correction Diff CSV、任何翻译决策、正式 TS 或源码；不推断或虚构修改时间、操作者或具体写入过程。
