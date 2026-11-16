# Evidence_Manifest — P2-D3A 证据包清单（实际目录枚举）

## 生成方式

`find reports\P2-D3A -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt`；数量与哈希均来自实际目录枚举，**不含 SHA256SUMS.txt 自身哈希**。

## 数量（实测）

| 类别 | 数量 |
|---|---|
| 报告 Markdown（含本文件） | **11** |
| Evidence 文件 | **9** |
| SHA256SUMS.txt | 1 |
| 正式文件总数 | **21**（SHA 覆盖 20 项） |

## Evidence 文件（9 项，全部已纳入 SHA256SUMS）

| 文件 | 用途 |
|---|---|
| `analyze_ts.py` | TS 解析/统计/分类/分批只读脚本 |
| `glossary_and_risk.py` | 术语候选与 UI 长度风险生成脚本 |
| `P2D3A_Message_Index.csv` | 562 条消息完整索引（稳定 ID、context、source、译文、类型、占位符、位置、分类等） |
| `P2D3A_Message_Index.json` | 同上机器可读版 + 统计对象 |
| `P2D3A_Context_Stats.csv` | 85 个 context 的消息数/finished/unfinished 分布 |
| `P2D3A_Usage_Hints.csv` | 562 条源码文件:行、类名/函数名提示、用途提示与用户场景 |
| `P2D3A_Glossary.csv` | 46 条术语候选（待 ChatGPT 校阅） |
| `P2D3A_Length_Risk.csv` | 559 条 unfinished 的 UI 长度风险预测 |
| `P2D3A_Batches.csv` | 19 个批次的完整 message ID 清单（覆盖 559 条，无重叠） |

## 说明

- 所有 CSV 均为 UTF-8（带 BOM 便于 Excel 打开）；JSON 为 UTF-8
- 脚本与数据均只读生成；未改动 TS、源码、CMake 或任何历史报告
- SHA256SUMS.txt 不含自身哈希（校验命令 `sha256sum -c SHA256SUMS.txt` 全部 OK）
