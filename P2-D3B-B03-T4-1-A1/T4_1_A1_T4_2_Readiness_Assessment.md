# T4_1_A1_T4_2_Readiness_Assessment — T4-2 输入准备度评估

## 结论：**可进入 T4-2，但须由用户另行授权**

## 可用构建输入
- 主程序：`build\v2026.2-msvc145-qt6103\app\TrenchBroom\Release\TrenchBroom.exe`，当前 SHA `268df3904f16dc2e329542397531be4ef35f530cebde07cd720753707fca7212`
- 构建目录中文 QM：`build\...\app\TrenchBroom\TrenchBroom_zh_CN.qm`，SHA `707011a3…`，已嵌入 EXE（T4-1 静态证据）
- Qt DLL/插件：位于同一 `Release` 目录及其子目录；日志显示它们 `up to date`（无变化），但独立测试副本应保留构建目录相对布局
- 不要仅复制 EXE 或 T3 QM；应复制 Release 目录完整运行依赖（EXE + DLL + platforms/imageformats/tls 等插件 + translations/qt_*.qm），且不改变相对路径

## 必须建立独立测试副本
T4-2 应复制到 `test-runs\` 下新的独立目录，不写入原版 Release；配置使用 portable 模式，避免污染日常 Preferences。该复制动作本阶段未执行。

## 阻断风险
无。历史哈希冲突已解释：正确构建前基线为 `38d021…`，`9a1a8499…` 来自 B01-T5 测试副本，属 T4-1 Baseline_Audit.csv 的误录。

## 限制
用户配置目录与 Documents 未做前后快照（NOT_VERIFIED）；构建期间未启动程序且构建日志无相关写入路径，但没有全盘证明。T4-2 应在独立配置环境中执行。

本评估不授权 T4-2，不创建测试副本，不启动程序。
