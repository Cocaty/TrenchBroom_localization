# B02_T3_Protected_Integrity_Report — 保护对象核验

开始/结束快照共 16 项（Evidence/Start_Snapshot.csv、Final_Snapshot.csv），逐项 SHA-256 与大小一致：

| 类别 | 对象 | 结果 |
|---|---|---|
| 正式 TS | TrenchBroom_zh_CN.ts（131,100 B / `901554891…`） | 未修改 |
| T2 证据 | TS_before_T2.ts（`6582a382…`）、TS_after_T2.ts（`901554891…`）及全部报告/SHA 清单 | 未修改 |
| T2-R1 证据 | 报告与 SHA 清单 | 未修改 |
| B02-D1 / B02-PRE 证据 | SHA 清单 | 未修改 |
| B01 历史证据 | T2/T3/T4/T5/T5-R1 SHA 清单 | 未修改 |
| 构建目录 | Release EXE `9a1a8499…`、QM `a2f5cc1f…` | 未修改（本轮 QM 写入独立 Work 目录） |
| 原版 Release | TrenchBroom.exe | 未修改 |
| 日常配置 | AppData INI | 未修改 |
| Git | HEAD `4c756be1…` / dirty=7 / 分支不变 | 无写操作 |

未运行 lupdate、未构建主程序、未启动 TrenchBroom、未部署；未修改 C++/CMake/QRC/资源；未改其他 TS 或测试配置。本轮新增文件仅限 `reports\P2-D3B-B02-T3\`（含 Work 与 Evidence）。

**结论：无越界变化。**
