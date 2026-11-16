# R1_Preflight_Report — T5-R1 只读预检与安全门禁（R1-0 / R1-1）

## 预检实测
- T5 原测试目录存在；EXE SHA `9a1a84991c61d1d1…`；config/Preferences.json 85 B；应用内 `translations/TrenchBroom_zh_CN.qm` 1,805 B（SHA `a2f5cc1f…`）；T5 目录文件完整，可在不修改的情况下复制
- Generic 配置（构建 Release `games/Generic/`）：仅相对路径，无真实游戏目录依赖；详见 R1_Generic_Config_Audit.md
- 游戏路径可由 `Games/Generic/Path` 偏好键指定（GameInfo.cpp:31），偏好 JSON 扁平键；可写入隔离测试配置
- 不存在需要写入用户目录/Documents/注册表/系统环境的配置行为；portable 模式保证配置隔离
- 保护基线 12 对象已记录（R1_Protected_Baseline.csv），含 T5 EXE/配置、构建 EXE/QM、正式 TS、原版 Release、日常配置、Generic 配置

## 安全门禁 R1-1

| 条件 | 判定 |
|---|---|
| Generic 不要求真实游戏目录 | ✅ 通过 |
| 可在隔离目录建立/打开空白临时地图 | ⏳ 需实测（R1-3），失败则 BLOCKED |
| 不需修改原始 Generic 配置 | ✅ 通过 |
| 不需修改 T5 原测试副本 | ✅ 通过 |
| 不需修改日常配置 | ✅ 通过 |
| 不需修改注册表/Documents/环境变量 | ✅ 通过 |
| 不需要下载/安装外部资源 | ✅ 通过 |

**门禁结论：允许进入 R1-2（独立副本）与 R1-3（临时地图实测）；若空白地图无法在隔离条件创建，立即 BLOCKED，不切换到真实游戏配置。**
