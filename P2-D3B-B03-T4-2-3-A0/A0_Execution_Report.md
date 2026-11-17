# A0_Execution_Report — 顶级菜单未汉化原因调查

## 最终状态：**PASS_WITH_LIMITATIONS**

静态根因已以源码、正式 TS 与 QM 回转三方证据确认；限制是未启动程序、未直接读取 QTranslator 运行日志，QTranslator 运行期加载状态仍 NOT_VERIFIED。

## A0-0 基线
仓库 `C:\Users\yoshi\Projects\TrenchBroom-zhCN`，分支 `feature/zh-CN-v2026.2`，HEAD `4c756be1…`，dirty=7。正式 TS `f021e509…`、QRC `de72b206…`、根/app CMake、Main.cpp、构建 QM `707011a3…`、测试 EXE `268df390…`、测试 Preferences `c048b77a…`（`zh_CN`）、原版 Release 均与历史基线一致；无 BASELINE_MISMATCH。M1 截图与报告可读取。开始快照 11 项。

## A0-1~A0-4 证据链
1. **源码创建位置**：九个标题均由 `ActionManager.cpp` 的 `createXxxMenu()` 在行 824/985/1251/1337/1424/1588/1935/1970/2040 调用 `createMainMenu("...")` 建立；`createMainMenu` 位于 2059-2062，仅把字面量存入 `Menu::name`
2. **标题赋值**：`ActionBuilder.cpp:136` 顶级菜单直接 `qtMenuBar.addMenu(QString::fromStdString(menu.name))`
3. **翻译调用**：九条均为 `NONE`；无 `tr()` / `translate()` / 显式 Context
4. **正式 TS**：九个 Source 精确匹配均为 0；`Message_ID` 均为 `NO_ID`，状态 `NOT_FOUND`
5. **QM**：使用 T4-1 回转 TS 检查，九个 Source 均 0 命中；结合源码无翻译调用与 TS 无消息，确认 QM 不可能含对应翻译
6. **菜单项对照**：`New Document` 等 QAction label 使用 `QObject::tr()`，TS 中 Context `QObject`、finished、译文中文，解释 File 下拉菜单汉化

本阶段未运行 lconvert；使用 T4-1 已生成并归档的回转 TS 作为 QM 只读审计材料。

## 12 个问题逐条回答
1. **源码创建位置**：见上，九个均在 ActionManager.cpp 对应 `createXxxMenu()`，行号见矩阵
2. **是否都经过 Qt 翻译机制**：否，9/9 均为普通字符串，无 tr/translate
3. **实际 Context**：无运行时翻译 Context
4. **TS 是否存在对应消息**：否，9/9 NOT_FOUND
5. **消息 Translation 状态**：无消息；不是 unfinished，而是 MISSING_FROM_TS
6. **QM 是否包含对应翻译**：否；回转中 0 命中，且与源码/TS 证据一致
7. **Source 相同但 Context 不同**：本阶段未发现与这九个标题可靠对应的 TS 消息；文件内其他相同字符串构不成菜单标题对应消息
8. **动态赋值/特殊机制**：标题通过 `Menu::name` → `QString::fromStdString` 直接建菜单；这是非 TS 翻译路径，但不是未知动态机制
9. **已有 finished 翻译却显示英文的菜单**：无。九个均根本没有对应消息
10. **确实缺少翻译的菜单**：M01–M09 全部
11. **原因仍无法确定的菜单**：无；九条均为 HIGH 置信度 MISSING_FROM_TS
12. **最小安全建议**：不直接新增九条 TS 消息；在独立授权后考虑源码改为 `QObject::tr("...")`（或项目约定 Context）并走完整 lupdate/审阅/lrelease/构建验证流程；详见根因评估

## 保护与归档
正式项目文件、测试副本、用户配置、原版 Release 与 Git 状态均未变；报告目录内新增文件属预期。新增报告/CSV/快照共 11 个文件；SHA256SUMS 覆盖 10 项并独立复算通过、清单不自列。

**本轮停止：未修改翻译、未构建、未启动、未进入任何后续阶段。等待用户与 ChatGPT 审查。**
