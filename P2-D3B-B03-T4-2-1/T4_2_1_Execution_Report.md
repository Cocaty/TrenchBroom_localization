# T4_2_1_Execution_Report — 独立测试副本首次隔离启动

## 总体结论：**PASS WITH LIMITATIONS**

启动与隔离目标通过；翻译资源初始化缺少运行期日志与截图，保持 `NOT_VERIFIED`，不得写成已加载。

## 启动结果
- 启动时间 2026-11-17 21:25:36 +0800；命令 `Start-Process -FilePath <test>\TrenchBroom.exe -ArgumentList "--portable" -WorkingDirectory <test> -PassThru`
- PID 23644，映像路径与测试副本 EXE 一致，EXE SHA `268df390…` 与预期一致
- 5 / 15 / 30 秒观察：`HasExited=False`、`MainWindow=True`、标题 `TrenchBroom`，无崩溃或错误对话框迹象
- 通过 `CloseMainWindow()` 正常请求关闭；15 秒内未退出，后续只读检查显示进程已不存在、剩余进程 0。未使用强制结束；退出码因进程对象跨检查消失而不可读取
- 窗口截图未生成：启动会话内置 Python 缺少 PIL；未重复启动。截图项 `NOT_VERIFIED`

## A–E 判定
| 项 | 判定 |
|---|---|
| A 启动结果 | **STARTED** |
| B portable 隔离 | **PASS** |
| C 日常用户配置 | **UNCHANGED** |
| D Documents | **UNCHANGED** |
| E 翻译资源初始化 | **NOT_VERIFIED** |

## portable 配置
测试副本 `config/` 内生成 `Preferences.json`（46 B，SHA `65f46db9…`，mtime 21:26:08）与 `games/` 目录；未生成测试副本内 `TrenchBroom.log`。用户配置与 Documents 启动后对照 7/7 UNCHANGED，无新增、删除或修改。构建目录、原版 Release、正式 TS、QRC、CMake、Main.cpp 与 Git 状态全部未变。

## 翻译初始化边界
T4-1 静态证据证明 QM 已嵌入 EXE；本阶段窗口正常显示且无可见错误，但未捕获 stdout/stderr，测试副本内无日志，且未切换语言。因此：
- 资源已嵌入：PASS（T4-1）
- 翻译器初始化成功：NOT_VERIFIED
- 中文界面实际显示：NOT TESTED

## 未执行
未启动原版/构建目录 EXE、未打开地图、未切换语言、未修改配置或注册表、未强制结束进程、未重启验证、未进入 T4-2-2。报告目录 `reports\P2-D3B-B03-T4-2-1\`，证据包含进程、配置、前后对照、保护状态、两个审计 CSV 与截图工具脚本。
