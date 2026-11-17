# T4_2_2_Readiness_Assessment — 下一阶段准备度

## 结论：**可进入 T4-2-2，但需用户单独授权**

## 已具备条件
- 测试副本只启动过一次，`--portable` 隔离生效：`config/Preferences.json` 与 `config/games/` 在测试副本内生成
- 日常用户配置与 Documents 启动前后 7/7 UNCHANGED；构建目录、原版 Release、源码与 Git 未变
- 程序主窗口正常显示 30 秒并正常退出，无崩溃迹象
- 测试副本 EXE 仍为 `268df390…`，可继续使用

## 待 T4-2-2 解决
- 捕获运行期日志/stdout，确认 `QTranslator::load(":/translations/TrenchBroom_zh_CN.qm")` 是否成功
- 切换语言到简体中文（用户授权后）并观察界面
- 建立本阶段的启动前快照，避免把 T4-2-1 的 `config/Preferences.json` 当成新变化
- 如需截图，使用带 PIL 的 Python 解释器或另行授权的工具；不得为此重复无意义启动

## 无阻断风险
当前没有启动失败、配置污染或保护对象变化。翻译器初始化仍为 `NOT_VERIFIED`，这是 T4-2-2 的重点，不是 T4-2-1 的失败。

本文件不授权进入 T4-2-2，不启动任何进程。
