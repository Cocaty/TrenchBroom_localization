# B02_D1_Decision_Report — RA-B02 正式翻译决策冻结

日期：2026-11-16 23:32 ｜ 本轮仅冻结决策，**未写入 TS**

## 结论：**PASS**

唯一目标消息身份准确且仍为 unfinished；正式译文、未采用备选、分类、理由与证据来源齐全；TS 与 Git 基线未变化。

## 冻结决策

| 字段 | 决策 |
|---|---|
| Batch | `RA-B02` |
| Message ID | `3e1b6ba4c40e` |
| Context | `tb::ui::WelcomeWindow` |
| Source | `Open Map` |
| 正式译文 | **打开地图** |
| 未采用备选 | **打开地图文件** |
| UI 分类 | **文件与文档操作 / 对话框** |
| 源码位置 | `WelcomeWindow.cpp:140`（沿用 P2-D3B-B02-PRE 证据，本轮未重新独立验证源码） |
| 源码语义 | Welcome 窗口中打开地图文件的文件选择对话框标题 |
| 原文状态 | `unfinished`（本轮核对仍未写入） |
| 决策状态 | `USER_CONFIRMED` |

## 翻译理由（用户已确认）
1. `Open Map` 此处是 `QFileDialog::getOpenFileName()` 的标题，不是普通菜单命令
2. 文件过滤器 `Map files (*.map)` 已明确限定文件类型
3. “打开地图”符合中文软件文件选择对话框常见表达，简洁自然
4. “打开地图文件”语义正确但略冗长，作为**未采用备选**记录
5. 不继承 B01“打开文档...”译法——界面场景不同，不为表面术语一致而强行统一
6. 原文无省略号，正式译文不得添加省略号

## 核对结果（D1-0 / D1-1 / D1-3）

- Git：feature/zh-CN-v2026.2，HEAD `4c756be1…`，dirty=7（与开始一致）
- TS：SHA `6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8`，131,106 B；85 context / 562 message / 21 finished / 541 unfinished / 0 obsolete
- 目标消息：全 TS 仅命中 **1** 条，context/source/location 与决策一致，`translation` 为 None 且 type=`unfinished`
- 批次归属：仅 `RA-B02`，559 个批次 ID 全部唯一；无重复、跨批冲突或其他消息混入
- 结束快照：TS SHA、大小、统计与目标状态与开始完全一致；保护对象（TS、权威批次文件、B02-PRE 8 份证据）哈希全部匹配

## 证据来源
`P2-D3B-B02-PRE` 的 `B02_PRE_Implementation_Report.md`、`B02_Source_Evidence_Index.md`、`B02_Terminology_Risk_Audit.csv`、`B02_Translation_Readiness.csv` 及权威批次文件 `P2-D3A-R1-A/Evidence/Revised_Batches.csv`。源码定位与调用链描述**沿用预审报告**，本轮未重新调查 C++ 源码。

## 停止声明
**本轮未修改 TS、未写入译文、未运行翻译工具、未构建、未启动程序、未提交 Git。下一阶段写入「打开地图」必须另行取得用户授权。**
