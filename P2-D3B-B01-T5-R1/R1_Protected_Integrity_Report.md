# R1_Protected_Integrity_Report — 退出后完整性与边界（R1-6）

对比 `R1_Protected_Baseline.csv`（开始快照，12 对象）——**12/12 PASS**：

| 对象 | 结果 |
|---|---|
| T5 原测试副本 EXE / Preferences / 目录 | ✅ 未修改（EXE `9a1a8499…`，配置 `5e350e45…`） |
| T5 原测试副本 QM（独立文件不存在，与开始一致） | ✅ 无变化 |
| 构建树 EXE / QM | ✅ `9a1a8499…` / `a2f5cc1f…`，未变 |
| 正式 TS | ✅ `6582a382…`，未变 |
| 原版 Release EXE / Qt6Core.dll | ✅ `f5a02f40…` / `b712b475…`，未变 |
| 日常 INI / Preferences.json | ✅ `5062ef85…` / `50705006…`，大小与 mtime 未变 |
| Generic GameConfig.cfg / Generic.fgd | ✅ `a23c4851…` / `a7c37e3c…`，原始配置未修改 |

其他检查：
- Git HEAD `4c756be1…`、dirty=7，与开始一致；未 commit/reset/checkout
- TrenchBroom 进程数 **0**（CloseMainWindow 正常退出，无崩溃）；测试副本 stderr.log 0 B
- 未运行 lupdate/lrelease/lconvert、未 configure、未构建、未部署、未改源码/CMake/TS/QM
- 未打开真实地图、未访问真实游戏目录；未下载资源；未改注册表/Documents/系统环境变量
- 新增写入仅限 `test-runs\P2-D3B-B01-T5-R1\`（app/config、workspace、日志）与 `reports\P2-D3B-B01-T5-R1\`（本报告目录）

## 越界事件记录（如实）
1. 误点“文档另存为...”打开一次保存对话框，默认目录为测试副本 `app/config`，已取消，**未写出文件**
2. 尝试保存 `workspace\test.map` 时文件路径处理失败，控制台出现解析/文件名无效错误（测试副本日志内），**未产生文件，未写测试目录之外**
3. 期间菜单描述经状态栏验证，未执行任何破坏性命令

**结论：无受保护对象变化，无越界写入残留。**
