# B03_D1_R1_A1_Protected_Integrity_Report — 保护对象核验

开始/结束快照（`Evidence/Start_Snapshot.csv`、`Evidence/Final_Snapshot.csv`）逐项大小与 SHA-256 一致：

- 正式 TS：`901554891…`（131,100 B），未修改
- 权威批次清单 `Revised_Batches.csv`、D1 决策矩阵、PRE 主报告：未修改
- **R1 原始目录全部文件**：逐项哈希与开始一致（见 `Evidence/R1_Original_File_Index.csv`），未被覆盖或修改
- Git：feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7，与开始一致

未修改 AboutDialog HTML、20 条候选译文、术语表、Alternative Log 或任何用户确认状态；未运行 lupdate/lrelease/lconvert，未构建、启动、部署，未执行 Git 写操作。本轮新增文件仅位于 `reports\P2-D3B-B03-D1-R1-A1\`，其中 `R1_Corrected/` 明确标注为修正副本。

**结论：无越界变化。**
