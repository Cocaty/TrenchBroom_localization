# B03_D1_R1_A1_Erratum_Report — AboutDialog 人数统计勘误

日期：2026-11-17 17:36 ｜ 只修正报告描述，不修改译文、TS 或确认状态

## 结论：**PASS**

## 勘误内容
R1 把 AboutDialog 的 **24 位具名人员**整体误称为“24 位贡献者”。程序化重新计数结果：

| 类别 | 人数 |
|---|---:|
| Developers（开发者） | 2 |
| Contributors（贡献者） | 22 |
| Total named people（具名人员合计） | 24 |

名单：Kristian Duske、Eric Wasylishen 为开发者；20kdc 至 Yuki Raven 共 22 位为贡献者。两组名单无重复、无交叉、无空项，顺序与正式 TS 原始 Source 及 R1 推荐 HTML 完全一致；第三方库/工具/字体名称未被计入人员（完整名单与验证结果见 `B03_D1_R1_A1_AboutDialog_People_Audit.json` 与 `Evidence/People_Count_Extraction.csv`）。

## R1 全文定位
对 R1 目录全部 `.md/.csv/.json/.txt` 文件按关键词检索（结果见 `Evidence/R1_File_Search_Results.csv`），发现 **2 处**错误描述：
1. `B03_D1_R1_Correction_Report.md:17` — “24 位贡献者姓名及顺序”
2. `B03_D1_R1_Source_Reference_Index.md:5` — “24 位贡献者”

均修正为“2 位开发者、22 位贡献者，共 24 位具名人员”口径，并在副本中加入统一表述：
> AboutDialog 包含 2 位开发者和 22 位贡献者，共 24 位具名人员；两组名单及顺序均与原始 Source 一致。

`R1_Corrected/` 中仅保存这 2 份修正副本及 `Evidence/AboutDialog_HTML_Audit.json` 的人数说明副本；R1 原始文件全部未改。

## 未变项
- AboutDialog HTML 推荐译文：未修改（SHA 见审计 JSON）
- 20 条决策矩阵推荐译文：未修改
- 术语表、Alternative Log：未修改
- 用户确认状态：20/20 `PROPOSED_PENDING_USER_CONFIRMATION`，0 已确认、0 冻结
- 正式 TS、源码、Git 基线、D1/PRE/R1 历史报告：未修改

## 差异与保护
逐条差异见 `B03_D1_R1_A1_Correction_Diff.csv`（2 行，`Translation_Changed=NO`、`Decision_Status_Changed=NO`）。保护对象开始/结束哈希一致，详见 Protected Integrity Report。

## 停止
本轮完成即停止；未进入 B03-T2，未确认任何译文，未修改 TS。
