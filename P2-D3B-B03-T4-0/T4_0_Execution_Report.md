# T4_0_Execution_Report — B03 Qt 翻译资源集成前置调查

## 结论：**PASS**（仅代表 T4-1 实施方案调查通过；不代表 QM 已集成或构建成功）

开始 2026-11-17 20:43:13 +0800；结束见最终快照归档时点。T4-0 报告目录创建前确认不存在；全程只读，未修改任何项目文件。

## T4-0-0 基线
Git feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7；正式 TS `f021e509…` 132,589 B（42 finished/520 unfinished），T3 QM `707011a3…` 6,631 B，实际 QRC `de72b206…` 106 B，均与任务书一致。构建目录 `build/v2026.2-msvc145-qt6103` 存在；原版 Release 保护对象已记录。开始快照 9 项。

## T4-0-1 架构调查
- QRC：仅 `<file>opengl_buglist.json</file>`，无 prefix/alias、无 translations、无 QM；AUTORCC TRUE
- CMake：根 L119 已找 LinguistTools；app L8 QRC 入目标、L151 AUTORCC、L493-496 `qt_add_translations(... RESOURCE_PREFIX "/translations")`
- 运行时：Main.cpp L176-194 `initTranslator` 加载 `:/translations/TrenchBroom_zh_CN.qm`，L358-359 在 UI 创建前调用；失败仅 warning 并回退英文；ViewPreferencePane 与偏好键 `Editor/Interface language` 已实现选择与重启生效
- **架构结论：构建期 TS→QM→资源嵌入链路已完整，加载路径与资源名一致。**

## T4-0-2 T3 QM 可行性
T3 QM 真实存在、哈希与 T3 报告一致、文件头与 lconvert 回转在 T3 已验证。它是 T3 静态验证产物；不应复制到源码资源目录或通过 QRC alias 重复注册。无文件名/资源路径冲突。

## T4-0-3 唯一推荐方案
**零项目文件修改**：依赖既有 `qt_add_translations` 管线；不新增 QRC 条目、不改 CMake、不改运行时代码、不落盘 QM 到源码树。T4-1 若获授权，只做构建后资源嵌入验证。详细对照、当前哈希与待用户决策项见 `T4_0_QM_Integration_Plan.md`。

## T4-0-4 风险与回滚
路径不匹配、重复注册、未进入目标、旧产物、TS/QM 不一致、资源覆盖等风险及检查/回滚方式已列于 `T4_0_Risk_and_Rollback.md`；本阶段未执行任何回滚。

## 保护与归档
正式 TS、QM、QRC、CMake、Main.cpp、ViewPreferencePane、原版 Release 与 Git 状态均与开始快照一致（10/10 UNCHANGED）。本阶段新增 11 个报告/证据文件；SHA256SUMS 覆盖其中 10 项，清单自身不自列并已逐项通过。

## 未执行 / 限制
未修改或复制 QM、未改 QRC/TS/CMake/源码、未运行 lupdate/lrelease/lconvert、未构建、未启动、未部署、未 Git 写操作；未上传 GitHub，无可验证链接。本结论不代表运行期汉化已验证，不进入 T4-1。
