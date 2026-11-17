# B03_D1_R1_Protected_Integrity_Report — 保护对象核验

开始/结束快照共 16 项，逐项大小与 SHA-256 一致（`match_start=YES 16/16`）：

- 正式 TS：`901554891…`（131,100 B），未修改
- 权威批次清单 `Revised_Batches.csv`、PRE 目标清单与 SHA 清单：未修改
- v2026.2 源码：CMakeLists.txt、`ObjExportDialog.cpp`、`ObjSerializer.cpp`：未修改
- **原始 D1 全部报告/CSV/Evidence/SHA 清单**：逐项哈希与开始一致，**未被覆盖或修改**
- Git：feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7，与开始一致

未运行 lupdate/lrelease/lconvert，未构建，未启动 TrenchBroom 或测试副本，未部署，未修改日常配置/Documents/注册表/环境变量，未执行 Git 写操作。本轮新增文件仅限 `reports\P2-D3B-B03-D1-R1\`。

**结论：无越界变化。**
