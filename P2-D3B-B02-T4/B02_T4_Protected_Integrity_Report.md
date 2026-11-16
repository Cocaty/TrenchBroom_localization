# B02_T4_Protected_Integrity_Report — 保护对象核验（T4-6/T4-7）

开始/结束快照共 19 项，逐项结果见 `Evidence/Start_Snapshot.csv` 与 `Evidence/Final_Snapshot.csv`。

| 类别 | 对象 | 结果 |
|---|---|---|
| 正式 TS | 131,100 B / `901554891…` | 未变 |
| T3 证据 | 原始 QM `f480ae44…`（1,871 B）与报告/SHA 清单 | 未变 |
| T2 / T2-R1 / B02-D1 / B02-PRE | 原始 TS 证据、报告、SHA 清单 | 未变 |
| B01 历史 | T2/T3/T4/T5/T5-R1 SHA 清单 | 未变 |
| 原版 Release | TrenchBroom.exe `f5a02f40…` | 未变 |
| 日常配置 | `AppData\Roaming\io.github.trenchbroom\TrenchBroom.ini`（语言实际保存位置对应 `AppData\Roaming\TrenchBroom\Preferences.json`，已列入快照） | 未变 |
| Git | 分支/HEAD `4c756be1…`/dirty=7 | 未变 |
| **预期更新（构建目录）** | EXE `9a1a8499…`→`38d02195…`；QM `a2f5cc1f…`→`f480ae44…`；RCC cpp/OBJ 重新生成 | `EXPECTED_CHANGE`，与本轮构建授权一致 |

Documents 未触碰；未修改注册表、系统环境变量、测试配置；未运行 lupdate、未部署、未启动 TrenchBroom、未提交 Git。本轮新增/更新文件仅限构建目录内构建产物及 `reports\P2-D3B-B02-T4\`。

**结论：无越界变化。**
