# B03_PRE_Protected_Integrity_Report — 只读边界核验

开始/结束快照共 14 项（Evidence/Start_Snapshot.csv、Final_Snapshot.csv），逐项 `match_start=YES 14/14`：

| 对象 | 结果 |
|---|---|
| 正式 TS（901554891… / 131,100 B） | 未修改 |
| Revised_Batches.csv（9e3a96d70e0f…）、Revised_Message_Index.csv | 未修改 |
| v2026.2 关键源码（CMakeLists.txt、app/TrenchBroom/CMakeLists.txt、Main.cpp） | 未修改 |
| B01-T5-R1、B02-PRE/D1/T2/T2-R1/T3/T4/T5 的 SHA256SUMS | 全部未修改 |
| Git 分支 / HEAD / dirty | feature/zh-CN-v2026.2 / 4c756be1… / 7，与开始一致；dirty 中的 6 个 tracked 修改与 translations/ 未跟踪目录为既知本地翻译管线集成状态，未清理 |

未运行 lupdate/lrelease/lconvert，未构建，未启动 TrenchBroom 或测试副本，未部署，未修改日常 Preferences/Documents/注册表/环境变量，未执行 Git 写操作，未覆盖历史报告。本轮新增文件仅限 `reports\P2-D3B-B03-PRE\`（含 Evidence 与 Source_Excerpts）。

**结论：无越界变化。**
