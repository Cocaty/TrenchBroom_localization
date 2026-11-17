# B02_T5_Protected_Integrity_Report — 保护对象核验

12 项保护对象开始/结束哈希一致（Evidence/Start_Snapshot.csv、Final_Snapshot.csv，match_start=YES 12/12）：

| 对象 | SHA-256 | 结果 |
|---|---|---|
| 正式 TS | 901554891f322ed8… | 未修改 |
| T4 构建 EXE / QM | 38d02195… / f480ae44… | 未修改（本轮只读构建目录） |
| 测试副本 EXE | 38d02195…（与 T4 一致） | 未修改 |
| 原版 Release EXE | f5a02f40… | 未启动、未修改 |
| 日常 INI | 5062ef85… | 未修改 |
| 日常 Preferences.json | 50705006… | 未修改（语言实际保存位置） |
| T4 / T3 / T2 / T2-R1 / B01-T5-R1 SHA 清单 | 16/16、16/16、8/8、9/9、58/58 OK | 未修改 |

其他检查：Git 分支 feature/zh-CN-v2026.2、HEAD 4c756be1…、dirty=7 与开始一致；测试进程全部结束（进程数 0）；5 份 stderr 日志均 0 B，无崩溃；未向正式安装目录部署任何文件；未运行 lupdate/lrelease/lconvert、未构建、未提交 Git。

测试副本内部产生的 config 与日志变化属本轮预期，全部限定在 `test-runs\P2-D3B-B02-T5\`。

**结论：无越界变化。**
