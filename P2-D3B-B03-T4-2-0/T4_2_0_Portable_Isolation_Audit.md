# T4_2_0_Portable_Isolation_Audit — portable 隔离机制准备

## 历史证据（P2-D2C-C，非本轮猜测）
- `02_Isolation_Preflight.md:10`：偏好文件 `Preferences.json`，位于 `userDataDirectory()`
- `02_Isolation_Preflight.md:11-13`：普通模式 Windows 使用 `QStandardPaths::AppDataLocation`；portable 模式使用 `appDirectory()/config`
- `02_Isolation_Preflight.md:14`：`Main.cpp L324-334` 检测 `--portable` 后设置 `QSettings::setPath(IniFormat, UserScope, "./config")`
- `02_Isolation_Preflight.md:17`：官方支持参数为 **`--portable`**，无需创建 marker 文件；工作目录应为测试副本 app 目录
- `04_Runtime_Test_Results.md:5`：历史启动命令使用 `Start-Process <测试副本 EXE> --portable -WorkingDirectory <app>`
- `07_Config_Persistence_Audit.md:3`、`P2-D2C-C_Final_Report.md:13`：历史验证中配置写入测试副本 `app\config\Preferences.json`，日常配置哈希不变

## 本阶段结论
| 项 | 结果 |
|---|---|
| portable 启动参数 | `--portable`（历史证据支持） |
| 是否需要 marker 文件 | 否；不得自行创建猜测文件 |
| 标记/配置文件位置 | 测试副本 EXE 同目录 `config/`（本轮未创建） |
| 配置文件实际保存位置 | portable：`app/config/Preferences.json`、`TrenchBroom.log`、`games/`、QSettings INI；普通模式：AppData 用户数据目录 |
| 日常配置差异 | 普通模式 AppData；portable 模式测试副本 `config/` |
| 退出后配置是否留测试副本 | 历史证据：是 |
| 是否访问 Documents | 历史证据仅证明日常配置未变；Documents 本轮标记 `NOT_VERIFIED`，已建立只读基线 |

## 启动前基线
`T4_2_0_Prelaunch_Baseline.csv` 已记录用户配置目录、Documents 项目相关目录（如存在）、测试副本 395 文件及环境存在性。本阶段未创建 `config/`，未启动程序。
