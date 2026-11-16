# 新版 Python 分析脚本说明（R1）

脚本：`Evidence/analyze_r1.py`（只读；不修改 TS/源码；输出到 R1 Evidence）。

## 功能与修正点

1. TS XML 解析：562 messages / 85 contexts / 3 finished / 559 unfinished；稳定 ID = SHA256(context+"\x1f"+source)[:12]
2. ActionManager 函数区间扫描：识别 `ActionManager::create*`（含跨行签名），提取每个 tr 调用所属 create* 函数、附近 `path{"Controls/..."}` 动作路径与 `ActionContext::` 标志
3. 分类：按函数名/路径/上下文→source 关键词→context/文件名的优先级规则；UNKNOWN 附理由
4. 全部 location 遍历：逐条检查文件存在、行号有效、源码片段、函数/路径/用途提示 → `P2D3A_R1_All_Locations.csv`（571 行）
5. 占位符正则 `%%|%L[1-9]\d*|%[1-9]\d*|%n`（%10 不再误判）
6. 快捷键正则仅认 Ctrl/Shift/Alt+ 与 F1–F12；普通 Enter/Delete 等转人工复核样本 CSV
7. 术语表逐项精确匹配计数（13 项无匹配）
8. 批次重排：按新分类，每批 ≤45，22 批覆盖 559 条未完成消息，ID 唯一
9. 生成不确定样本 CSV（33 条）

## 运行方式与产物

```
python reports/P2-D3A-R1/Evidence/analyze_r1.py
```
产物（均在 Evidence）：
- `P2D3A_R1_Message_Index.csv`（562 行分类索引）
- `P2D3A_R1_All_Locations.csv`（571 行逐 location 核验）
- `P2D3A_R1_Glossary.csv`（46 行术语 + 精确匹配计数）
- `P2D3A_R1_Batches.csv`（22 批 ID 清单）
- `P2D3A_R1_Uncertain_Samples.csv`（33 行人工复核样本）

## 复现性

脚本、输入 TS/源码路径均为绝对路径；重复运行结果确定（分类规则无随机性）；本轮已运行并核对统计输出。
