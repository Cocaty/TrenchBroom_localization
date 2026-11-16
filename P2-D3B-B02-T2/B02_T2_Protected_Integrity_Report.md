# B02_T2_Protected_Integrity_Report — 写入后保护核验

| 对象 | 结果 |
|---|---|
| Git HEAD / 分支 / dirty | 4c756be1… / feature/zh-CN-v2026.2 / 7 ——与开始一致 |
| tracked diff | 6 files / 81 insertions / 1 deletion ——与开始一致（既有授权修改） |
| C++ / CMake / QRC / QM | 未修改（WelcomeWindow.cpp `34a40df4…`、ActionManager.cpp `2a75f4ee…`、app/CMakeLists `21cfabf0…`） |
| 其他 TS 消息 | 561/561 逐字段未变 |
| 日常配置 / Documents / 注册表 / 环境变量 | 未触碰 |
| 原版 Release EXE | f5a02f40… 未变 |
| 构建目录 | 未运行 lrelease/build，未修改 |
| B02-PRE 证据 | SHA 清单 9/9 OK |
| B02-D1 决策证据 | SHA 清单 6/6 OK |
| B01-T2 / T3 / T4 / T5 / T5-R1 证据 | 8/8、12/12、12/12、26/26、58/58 OK |

本轮新增/修改的文件仅限：`TrenchBroom_zh_CN.ts`（授权目标）与 `reports\P2-D3B-B02-T2\`（报告目录，含两份 TS 证据副本）。未执行 Git 写操作，未启动程序。

**结论：无越界变化。**
