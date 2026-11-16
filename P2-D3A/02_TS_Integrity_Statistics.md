# 02_TS_Integrity_Statistics — 第二阶段 TS 完整统计（XML 实际解析）

解析脚本：`Evidence/analyze_ts.py`（只读）；完整索引：`Evidence/P2D3A_Message_Index.csv` / `.json`（562 行），context 统计：`Evidence/P2D3A_Context_Stats.csv`。

## 14 项必报统计

| # | 指标 | 实测 | 历史基线 | 差异 |
|---|---|---|---|---|
| 1 | context 总数 | **85** | 85 | 0 |
| 2 | message 总数 | **562** | 562 | 0 |
| 3 | finished | **3** | 3 | 0（Language/重启提示/Requires restart） |
| 4 | unfinished | **559** | 559 | 0 |
| 5 | obsolete | **0** | 0 | 0 |
| 6 | vanished | **0** | 0 | 0 |
| 7 | 多 location 消息 | **8** | — | 新增统计：Toggle %1 visible ×2、Could not build a path ×3、use builtin ×2、Game Path ×2、lock file ×2、stale lock ×2、Requires restart ×2、Language ×2 |
| 8 | 缺 location | **0** | — | 所有消息可追溯源码 |
| 9 | 重复 (context, source) | **0** | — | — |
| 10 | 空 source | **0** | — | — |
| 11 | 空 translation | **559**（=全部 unfinished） | — | 3 条 finished 均有译文 |
| 12 | numerus 消息 | **0** | — | — |
| 13 | 含格式化参数 | **58**（%1/%2 等，见 05 报告） | — | — |
| 14 | 含快捷键/助记符特征 | **4**（严格按键正则：Ctrl/Shift/Alt+ 或独立功能键；另有助记符 & 与 && 各 0） | — | — |

附加：`has_escaped_amp=0`；含技术标识（文件扩展名/URL/配置键/类名）5 条；含歧义候选词 195 条。

## 消息级稳定 ID

`id = SHA256(context + "\x1f" + source)[:12]`——不依赖 TS 行号；后续 lupdate 改变行号仍可稳定对账。索引字段：id/context/source/translation/type/numerus/locations/是否 finished/占位符集合/歧义词/源码位置/分类等（CSV 全字段见文件头）。

## 结论

**与历史 562/85/3/559/0 基线完全一致，无任何差异**；无需（也不允许）调整文件。
