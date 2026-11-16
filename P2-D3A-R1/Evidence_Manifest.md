# Evidence Manifest — P2-D3A-R1（实际目录枚举）

## 数量（实测）

| 类别 | 数量 |
|---|---|
| 报告 Markdown（含本文件） | **10** |
| Evidence 文件 | **6** |
| SHA256SUMS.txt | 1 |
| 正式文件总数 | **17**（SHA 覆盖 16 项） |

## Evidence 文件（6 项）

| 文件 | 用途 |
|---|---|
| `analyze_r1.py` | 新版只读分析脚本（分类/location/占位符/术语/批次） |
| `P2D3A_R1_Message_Index.csv` | 562 条消息重新分类索引（稳定 ID、分类理由、函数/路径证据） |
| `P2D3A_R1_All_Locations.csv` | **571 行逐 location 核验**（文件/行号/片段/函数/用途） |
| `P2D3A_R1_Glossary.csv` | 修正术语表（46 行，含 TS_exact_matches 与 In_current_batch） |
| `P2D3A_R1_Batches.csv` | 修正批次计划（22 批，559 条 ID 唯一） |
| `P2D3A_R1_Uncertain_Samples.csv` | 33 条按键/占位符人工复核样本 |

## 生成方式

`find reports\P2-D3A-R1 -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt`——实际枚举，**不含自身哈希**；校验 `sha256sum -c SHA256SUMS.txt` 全部 OK。

## 不变性

P2-D3A 原始报告与 Evidence 未改动（本轮仅新建 P2-D3A-R1 目录）；TS/源码/CMake/构建产物零修改。
