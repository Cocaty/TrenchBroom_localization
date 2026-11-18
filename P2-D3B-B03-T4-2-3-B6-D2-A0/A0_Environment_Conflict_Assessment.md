# A0_Environment_Conflict_Assessment — HTTPS_PROXY / https_proxy 冲突评估

## 结论
冲突发生在 **当前 PowerShell/构建进程环境**，不是用户级或系统级注册表中的持久变量，也不是 B6-D2 构建脚本写入的。Bash 工具当前环境未观察到重复组；PowerShell 工具当前环境同时存在 `HTTPS_PROXY`/`https_proxy` 与 `HTTP_PROXY`/`http_proxy`，每组大小写变体的值哈希一致（`SAME_VALUE`）。用户级和系统级注册表均无大小写重复组。

## 证据
| 来源 | 重复情况 | 值关系 | 结论 |
|---|---|---|---|
| Bash 当前进程 | 0 组 | - | 与 PowerShell 进程环境不一致 |
| PowerShell 当前进程 | 2 组（HTTP_PROXY、HTTPS_PROXY） | 同组值完全相同 | 直接冲突来源 |
| 用户注册表 HKCU\Environment | 0 组 | - | 非持久化用户变量来源 |
| 系统注册表 HKLM\...\Environment | 0 组 | - | 非持久化系统变量来源 |
| WorkBuddy 启动/父进程环境 | NOT_VERIFIED | - | 无法只读取得父进程完整环境 |

B6-D2 构建命令未修改 PATH 或任何环境变量；MSBuild 从调用进程继承了 PowerShell 环境中的两组大小写重复变量，构造 `ProcessStartInfo.EnvironmentVariables` 时因 Windows 名称不区分大小写抛出 `ArgumentException`。

## 错误阶段
B6-D2 日志显示：
- GenerateManual 已完成，shortcuts.js 生成，无 `0xc0000135` / `MSB8066`
- TrenchBroom_zh_CN.qm 已生成且 SHA 与 B5 QM 一致
- rcc 已启动
- 随后在 `Microsoft.CppCommon.targets(790,5)` 的编译器 ToolTask 中失败
- 堆栈为 `ProcessStartInfo.get_EnvironmentVariables()` → `ToolTask.GetProcessStartInfo()` → `ToolTask.ExecuteTool()`
- 异常发生在创建进程环境字典阶段，不能表述为“CL.exe 已编译失败”

## 限制
无法只读确认这两个变量最初由哪个父进程或 WorkBuddy 启动层注入；无法读取已经退出的 B6-D2 MSBuild 进程完整环境。该部分标记 NOT_VERIFIED，但不影响“当前 PowerShell 构建进程存在冲突、注册表无冲突、同组值相同”的结论。

## PATH
A0 使用 Windows 分号解析 PATH：44 段，无空段；D0-1 的 `PATH_0=C`、`PATH_9=C` 是将 Windows PATH 当作 POSIX 冒号分隔导致的解析异常。本阶段不输出完整 PATH、路径值或凭据。
