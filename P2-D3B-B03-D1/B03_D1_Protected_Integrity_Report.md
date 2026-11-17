# B03_D1_Protected_Integrity_Report — 决策阶段只读核验

开始/结束快照共 13 项（Evidence/Start_Snapshot.csv、Final_Snapshot.csv），逐项大小与 SHA-256 一致：

| 对象 | 结果 |
|---|---|
| 正式 TS `901554891…`（131,100 B） | 未修改，20 条目标仍 unfinished |
| Revised_Batches.csv、B03-PRE 报告/矩阵/SHA 清单 | 未修改 |
| B02-D1 决策报告与决策记录 | 未修改；其中仅冻结 `Open Map → 打开地图` |
| v2026.2 关键源码（CMakeLists、app CMake、ObjExportDialog、ChoosePathTypeDialog、CrashDialog、SystemPaths） | 未修改 |
| Git 分支/HEAD/dirty | feature/zh-CN-v2026.2 / 4c756be1… / 7，与开始一致 |

未运行 lupdate/lrelease/lconvert，未构建，未启动 TrenchBroom 或测试副本，未部署，未修改日常配置/Documents/注册表/环境变量，未提交 Git。本轮新增文件仅限 `reports\P2-D3B-B03-D1\`。

**结论：无越界变化。**
