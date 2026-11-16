# B01_R1_QA — 修订交付物独立核验

核验时间：2026-11-16 21:33 ｜ 方法：直接读取原始 TS、原/新 CSV、新 Markdown，与原始报告哈希清单独立比对。

| QA 项 | 实测 | 判定 |
|---|---|---|
| Git 分支/HEAD/tag | feature/zh-CN-v2026.2 / 4c756be1… / v2026.2 | ✅ |
| TS SHA-256 | 83a9aa45eaef5213ee58d44bb6096bf10288aa4668da6c63ca8e154742e0a198 | ✅ 与固定基线一致 |
| 原始 P2-D3B-B01-T 交付物完整性 | 8 文件；原 SHA 清单 7 项校验全部 OK（清单本体除外） | ✅ 未修改 |
| 18 条稳定 ID 存在 | 18/18；原/新 ID 集合一致 | ✅ |
| source 与原始 TS 逐字一致 | 18/18 | ✅ |
| context 未变化 | 18/18 | ✅ |
| Map... Decision（提案 vs 术语表） | 推荐 / 推荐 | ✅ 完全一致（仍待用户最终确认、未冻结） |
| Point File 三动作术语 | 加载/重新加载/卸载**点轨迹文件** | ✅ 名词统一 |
| Portal File 三动作术语 | 加载/重新加载/卸载 **BSP 门户文件** | ✅ 名词统一 |
| Omit From Export 跨批次依赖 | 独立报告记录，tooltip 候选改为“不参与导出”，未把 Layer UI 字符串加入 18 条 | ✅ |
| Wavefront OBJ 默认/备选 | A `Wavefront OBJ...` 推荐；B `Wavefront OBJ 文件...` 保留 | ✅ |
| Document / Save as / Export / Revert 一致性 | 文档统一；另存非导出；Map 为 Export 格式项；Revert 与 tooltip 语义一致 | ✅ |
| Markdown / CSV 18 条一致 | 18 行逐字段比对完全一致 | ✅ |
| 未把待确认项标为已确认 | Decision 仅为“推荐/推荐，待用户确认/…跨批次依赖…/保留原文”；User_Decision_Record 明列待确认 | ✅ |
| 未修改 TS / 源码 / CMake | TS 哈希不变；git dirty=7 与基线一致 | ✅ |
| 未运行 lupdate/lrelease/构建/启动/部署 | 本轮无相关操作 | ✅ |

## 术语表 Decision 分布（R1）

推荐 7 / 推荐，待用户确认 8 / 保留原文 1 / 推荐，存在跨批次依赖，待用户确认 1（合计 17）。

## 唯一未决项

D1–D7 全部在 `B01_User_Decision_Record.md` 列为“待用户确认/决定”，本轮不代替用户勾选。

**QA 结论：全部验收项通过。**
