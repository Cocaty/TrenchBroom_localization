# B8_Execution_Report — 剩余场景只读可测性调查与最终覆盖矩阵

## 最终状态：**B8_PASS_WITH_LIMITATIONS**

本轮未启动 TrenchBroom、未执行 GUI、未修改历史归档、未修改正式项目文件，仅完成只读静态调查与归档整理。

## 基线与权威输入
Git `feature\zh-CN-v2026.2` / `4c756be1a54a28d921d18c77716a5f170bdc31d0` / dirty=13；正式 TS、五个源码文件、QRC、CMake、Main.cpp、构建 EXE/QM、TestCopy EXE/QM 与历史归档全部核验。任务书列出的 B2–B5 报告文件名与本地实际文件名不同，已按本地实际 `B*_Execution_Report.md` 读取并记录差异，无权威资料缺失。

## 14 条 NOT_TESTED 静态结论
- ChoosePathTypeDialog 7 条：`SAFE_WITH_ISOLATED_INPUT`，由加载 `.fgd/.def/.ent` 或添加 WAD 路径触发，Ok 会修改内存地图，Cancel 可避免写入；静态条件明确但未复现，列为 A 类可补测。
- Tooltip 2 条：实际是 QAction `statusTip`，不是 QToolTip；需 hover/focus 且状态栏可见。低价值，B 类不值得补测。
- OBJ placeholder 1 条：`QLineEdit::setPlaceholderText` 被 `MapWindow::exportDocumentAsObj()` 中 `updateExportPath()` 自动填值覆盖，分类 `PLACEHOLDER_OVERRIDDEN`，B 类。
- GameDialog / Autodetect 1 条：仅在 `DialogType::Open` 且地图游戏无法检测时加入 Map Format 组合框；不扫描游戏目录。状态难复现，B 类。
- CrashDialog 3 条：存在 Debug → Show Crash Report Dialog... 的理论安全入口，但 B8 禁止调用；真实路径会复制崩溃报告/日志/地图文件，保持 `NOT_TESTED_HIGH_RISK`，C 类不测试。

## Console 提示
`Failed to compile resource '.' (invalid path)` 在项目源码、TrenchBroom.exe 与主要 Qt DLL 中均未检索到对应字符串；无证据表明与 `qt_add_translations` 或中文化有关。保持 `CAUSE_NOT_IDENTIFIED`。

## 最终覆盖矩阵
48 条：`PASS=33`、`PASS_WITH_LIMITATION=1`、`NOT_TESTED=14`、`FAIL=0`。证据类型：B7 原始截图 22、R1 截图 11、历史截图 1、无运行期证据 14。`Reload Entity Definitions` 保留历史截图限制。

## 补测建议
A 类：ChoosePathTypeDialog 7 条值得一次隔离补测（dummy FGD，进入对话框后取消）。B 类：tooltip、placeholder、Autodetect 不值得常规补测。C 类：CrashDialog 不测试。若不追求 48/48，可冻结当前矩阵。

## B9 准备度
`READY_WITH_LIMITATIONS`。不因 CrashDialog 未测试阻断 B9；限制为 1 条历史证据、14 条未测试与 Console 提示未定位。

本轮只读归档，SHA256SUMS 与最终快照已生成。等待用户审阅；未进入 B9。
