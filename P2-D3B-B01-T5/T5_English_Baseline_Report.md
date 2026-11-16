# T5_English_Baseline_Report — 首次启动与英文基线（T5-3）

## 运行事实
- 实际启动 EXE：`C:\Users\yoshi\Projects\TrenchBroom-zhCN\test-runs\P2-D3B-B01-T5\app\TrenchBroom.exe`，命令行 `TrenchBroom.exe --portable`，工作目录为测试 app 目录
- PID 2260；启动后按首次运行流程弹出自动更新询问，选择 **No**（仅写入测试配置 `"updater/Ask for auto updates": false`）；无崩溃、无 DLL/插件错误、无 QTranslator 失败信息（stderr.log 为 0 B）
- 测试副本 `app\config\` 在启动后生成（独立配置），正式 TS/构建目录未写

## 界面实测
- Welcome 窗口正常显示，英文界面
- 通过 New map → Select Game → Open preferences → View 打开偏好设置（未打开任何地图文件）
- Language 行显示 **Language**，下拉框当前 **English**，右侧提示 **"Requires restart after changing"**；控件无错位/遮挡
- 英文状态菜单项与提示均为英文

截图：`Evidence/T5_01_english_start.png`（首启含更新询问）、`Evidence/T5_02_update_dialog_crop.png`、`Evidence/T5_03_preferences_english.png`、`Evidence/T5_04_language_english.png`

## 隔离
测试配置与日志全部位于 `test-runs\P2-D3B-B01-T5\`；日常配置哈希未变（见 Post_Test_Integrity_Report）。
