# B03_D1_R1_Correction_Report — D1 决策材料定点修正

日期：2026-11-17 13:06 ｜ 只修正报告材料，未改 TS、未确认任何译文

## 结论：**PASS**

三项问题均已修正，20 条决策矩阵与 19 条未触及推荐译文保持原 D1 内容；跨文件一致性检查 **10/10 PASS**；保护对象未变化。

## R1-0 基线
Git feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7；正式 TS `901554891…`（131,100 B，85/562/22/540/0）；RA-B03 20 ID；原始 D1 矩阵 20 行、状态 20/20 `PROPOSED_PENDING_USER_CONFIRMATION`、0 USER_CONFIRMED / 0 FINAL_FROZEN / 0 NEEDS_REVISION。

## 三项修正
### 1. AboutDialog HTML（R1-1）
从正式 TS 直接读取原始 Source（985 字符），修正推荐译文：
- URL 恢复为完整的 `github.com/TrenchBroom/TrenchBroom`
- 恢复字符串开头的换行符（无额外空格）
- 以原文为基准保留 `<br />`×24、`<b>`×3、`</b>`×3、标签序列、24 位贡献者姓名及顺序、13 个库/工具/字体产品名、结尾无换行的状态
- 程序化检查 **12/12 PASS**（见 Evidence/AboutDialog_HTML_Audit.json）

### 2. CSV 字段错位（R1-2）
原始 D1 矩阵 AboutDialog 行存在 `Alternative_Translation`/`Decision_Reason`/`Rejection_Reason`/`Terminology_Group` 四列内容轮转错位；R1 按任务书语义重建该行，Alternative 明确为“无完整替代译文；局部标题备选为‘第三方库、工具及素材’”。备选理由表 AboutDialog 行同步改为完整修正 HTML + 准确字段。两张 CSV 均为标准解析的 20 行、11 列 / 5 列，多行 HTML 引号转义正确。

### 3. Export Path / Export Directory 拆分（R1-3）
原术语表中合并的 `export path / export directory` 已删除，拆为：
- **Export Path** → 导出路径（ID `0011be948dd6`，UI 分节标题）
- **Export directory (semantic base)** → 导出目录（ID `26fd3ad9ed81`，源码 `exportPath.parent_path()` 语义概念；明确说明不是 TS 中的消息）
术语表由 11 行变为 12 行；决策矩阵中两条推荐译文分别维持“导出路径”和“相对于导出目录”。

## 其余 19 条
其余 19 条推荐译文、理由、术语组和待确认状态逐行与原 D1 一致（一致性检查 `other_19_unchanged=PASS`）；未重新翻译、未改变任何决策状态。

## 用户确认状态
20/20 仍为 `PROPOSED_PENDING_USER_CONFIRMATION`；0 已确认、0 冻结、0 需修订。修正材料不代表用户确认。

## 保护与交付
16 项保护对象（正式 TS、批次清单、PRE 材料、原始 D1 全部报告及 SHA 清单、关键源码）开始/结束哈希一致；Git 未变。未修改原始 D1/PRE/B01/B02 任何文件；未写 TS、未运行翻译工具、未构建/启动/部署。

R1 交付 16 项（报告/CSV/索引/证据）；SHA256SUMS 覆盖全部、主清单未自列，校验通过。

## 下一阶段建议
请你审查 R1 修正后的完整 HTML 与术语拆分；确认 20 条译文（可分组确认）后，另行授权 B03-T2 写入。
