# B02_T2_R1_Protected_Integrity_Report — 只读边界核验

## 保护对象（21 项，开始/结束哈希一致）

| 类别 | 对象 | 结果 |
|---|---|---|
| 正式 TS | app/TrenchBroom/translations/TrenchBroom_zh_CN.ts | 131,100 B / SHA `901554891…` / mtime 23:36:59 未变 |
| T2 证据 | Evidence/TS_before_T2.ts（131,106 B / `6582a382…`）、TS_after_T2.ts（131,100 B / `901554891…`） | 未修改 |
| T2 原始交付 | 实施报告、前后哈希记录、消息审计 CSV、逐消息差异 CSV、diff、保护报告、SHA256SUMS | 8 项全部哈希未变；原 SHA 清单 8/8 校验 OK |
| 构建目录 | Release EXE / TrenchBroom_zh_CN.qm | 未变（未运行 lrelease/build） |
| 原版 Release | TrenchBroom.exe | 未变 |
| 日常配置 | AppData/Roaming/.../TrenchBroom.ini | 未变 |
| 历史证据 | B02-PRE、B02-D1、B01-T2、T3、T4、T5、T5-R1 的 SHA256SUMS | 9/9、6/6、8/8、12/12、12/12、26/26、58/58 OK |

Git 分支 / HEAD / dirty：feature/zh-CN-v2026.2 / 4c756be1… / 7 ——开始与结束一致；无 commit/checkout/reset/clean。

未运行 lupdate/lrelease/lconvert；未构建、启动、部署；未修改 C++/CMake/QM/QRC、测试配置或 Documents。本轮新增文件仅限 `reports\P2-D3B-B02-T2-R1\`。

**结论：无保护对象发生变化。**
