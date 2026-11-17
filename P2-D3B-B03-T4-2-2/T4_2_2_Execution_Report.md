# T4_2_2_Execution_Report — 简体中文运行期加载与界面验证

## 总体结论：**FAIL**（工具能力阻断，非 TrenchBroom 产品失败）

核心目标未完成：未能通过 UI 设置语言、未能重启验证中文界面、未能获得运行期翻译器加载证据。按本阶段结论标准，相关项均为 `NOT_VERIFIED`，不得写成 PASS。

## A–F 判定
| 项 | 判定 |
|---|---|
| A 语言选项 | **NOT_VERIFIED** |
| B 语言设置保存 | **NOT_VERIFIED** |
| C 中文界面显示 | **NOT_VERIFIED** |
| D 翻译资源加载 | **NOT_VERIFIED** |
| E portable 隔离 | **PASS**（继承 T4-2-1 证据，本轮无反证） |
| F 用户配置 / Documents | **UNCHANGED / UNCHANGED** |

## 已执行
- 启动前核验：报告目录不存在；测试 EXE `268df390…`、测试配置 `65f46db9…`（仍无 Interface language 字段）、Git `4c756be1…`/dirty=7，T4-2-1 证据可读，无其他进程。
- 第一次启动：21:34:20 +0800，PID 7560，`--portable`，工作目录为测试副本；5 秒时窗口标题 `Welcome to TrenchBroom`，进程存活，无崩溃迹象。
- 进程后续已不存在，剩余进程 0；未使用强制结束。
- 配置：`config/Preferences.json` 内容和哈希与 T4-2-1 基线一致；未发生语言设置变化。

## 阻断原因
1. 带 stdout/stderr 重定向的 `Start-Process` 失败：代理环境变量存在大小写重复键（`HTTPS_PROXY`/`https_proxy`），PowerShell 构造环境字典时抛异常；该次**未启动进程**。按授权要求未修改环境变量。
2. 不使用重定向后可以启动，但当前工具环境阻止所有可用于 GUI 自动化/截图的机制：.NET `Add-Type`/assembly load、COM `WScript.Shell`、反射加载、托管 .NET 动态代码均被安全策略拒绝；Bash 桌面会话枚举不到该窗口，无法点击 Preferences 或截取窗口。
3. 因此无法完成 UI 操作，也无法获取真实中文界面截图；未重复启动，未手工编辑 JSON，未复制 QM，未修改环境变量。

## 证据边界
- QM 编译并嵌入 EXE：**PASS**（T4-1 静态证据）
- QTranslator 实际加载：**NOT_VERIFIED**
- 中文界面实际显示：**NOT_VERIFIED**
- 静态嵌入证据不能替代运行期加载证据。

## 保护状态
测试副本配置、用户配置、Documents、正式 TS、QRC、CMake、源码、原版 Release 与 Git 状态均未变（保护对照全 UNCHANGED）；stdout/stderr 仅保存 NOT_VERIFIED 说明，非伪造日志。

## 停止
未进行第二次启动、未切换语言、未打开地图、未逐条验证译文、未进入 T4-2-3。等待 ChatGPT 审查，并需用户提供可执行 GUI 交互的授权环境后再重试本阶段。
