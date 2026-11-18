# A0_Execution_Report — MSBuild 环境变量重复键冲突只读诊断

## 最终状态：**DIAGNOSIS_COMPLETE_WITH_LIMITATIONS**

已确认 MSB6001 的直接来源是当前 PowerShell/构建进程环境中的大小写重复代理变量，且同组值相同；用户级和系统级注册表无重复。临时子进程隔离方案可行。限制是无法只读取得 WorkBuddy 启动/父进程环境，无法证明这两个变量最初由哪一层注入。

## A0-0 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=13，dirty 清单与 B6-D2 一致；DumpShortcuts/CMakeLists.txt `b7a28067…`。正式 TS `f81162b3…`、B5 QM `4b213ce5…`、B4 备份、B5 回转、QRC、主程序 CMake、Main.cpp、B2 五源码、构建 EXE/QM 均与预期一致。开始快照 19 项，保护审计无变化；Documents/用户配置未写入。

## A0-1 环境冲突
- Bash 当前进程：223 个变量，0 个大小写重复组
- PowerShell 当前进程：214 个变量，`HTTP_PROXY/http_proxy` 与 `HTTPS_PROXY/https_proxy` 两组重复，组内值哈希相同（SAME_VALUE）
- 用户注册表：6 个变量，0 组重复
- 系统注册表：17 个变量，0 组重复
- 父进程/WorkBuddy 启动环境：NOT_VERIFIED

所有代理值仅以长度和 SHA256 记录，未写入明文；未尝试连接代理。

PATH：44 段，无空段。D0-1 的 `PATH_0=C` 异常属于以 POSIX 冒号解析 Windows PATH 的错误；A0 以分号解析，未发现该异常。完整 PATH 未进入报告。

## A0-2 MSBuild 错误链
B6-D2 日志显示 GenerateManual 已完成，shortcuts.js 已生成；QM 已生成且与 B5 QM 一致；rcc 已启动。随后 `Microsoft.CppCommon.targets(790,5)` 的编译器 ToolTask 抛出 MSB6001，堆栈为 `get_EnvironmentVariables()` → `GetProcessStartInfo()` → `ExecuteTool()`。异常发生在创建进程环境字典阶段，**不能表述为 CL.exe 编译失败**。

工具链仅做文件元数据与配置读取；版本查询命令被执行环境安全策略阻止，记录 LIMITATION。构建配置为 Release、目标 TrenchBroom，生成器 Visual Studio 18 2026 x64。

## A0-3 临时隔离
由于重复组内值相同，可以在单次构建子进程中按大小写不敏感规则保留一个规范名称，其他环境完整继承；不写注册表、不改 PATH、不用 setx。若未来组内值不同，必须用户选择，不得自行取舍。详见 `A0_Temporary_Environment_Isolation_Proposal.md`。

## 归档与停止
`reports\P2-D3B-B03-T4-2-3-B6-D2-A0\` 含执行报告、冲突评估、隔离方案、环境/来源/PATH/错误链/工具链/保护审计、前后快照、只读脚本与 SHA256SUMS。未修改环境、未构建、未启动任何编译/程序。未上传 GitHub，无可验证链接。等待独立审查与单独授权，不进入任何后续阶段。
