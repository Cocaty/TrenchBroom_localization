# T5_Preflight_Baseline_Report — 运行前只读核验（T5-1）

- Git：feature/zh-CN-v2026.2，HEAD 4c756be1a54a…，tag v2026.2，dirty=7（与 T4 一致）
- T4 报告目录存在，13 个文件；T4 Release EXE 重算 SHA `9a1a84991c61d1d108477ab7f193c72d6336e1ed6c197d510339043d8b2c46d5`（29,761,536 B）；T4 QM 重算 SHA `a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66`（1,805 B）——均为本轮重新实测
- 正式 TS SHA `6582a38280e7ac1c…`（未变）
- 原版 Release：TrenchBroom.exe `f5a02f40…`、Qt6Core.dll `b712b475…`；日常配置 INI `5062ef85…`（1,399 B，mtime 12:42:23）；日常数据目录 Preferences.json / 两个日志哈希与历史一致
- TrenchBroom 进程数 0
- 目标测试目录 `test-runs\P2-D3B-B01-T5\` **不存在** → 允许新建，不覆盖既有目录

结论：全部通过，允许建立测试副本并启动。
