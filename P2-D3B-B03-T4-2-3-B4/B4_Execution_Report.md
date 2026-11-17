# B4_Execution_Report — 正式 TS 九条菜单译文写入与差异验证

## 结论：**PASS**

九条冻结译文已写入正式 TS；统计与保护状态全部符合预期。未运行 lrelease、未构建、未启动、未进入 B5。

## B4-0 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=12；五个 B2 源码文件哈希与 B2/B3 记录一致；正式 TS 基线 `f021e509…`，132,589 B，85 Context / 562 Message / 42 finished / 520 unfinished。备份 `Backup/TrenchBroom_zh_CN.ts.before` 与正式 TS 写入前完全一致。

## B4-1 写入
以正式 TS 为基础，在 `QObject` Context 末尾精确插入九条消息：

`File→文件`、`Edit→编辑`、`Selection→选择`、`Groups→分组`、`Tools→工具`、`View→视图`、`Run→运行`、`Debug→调试`、`Help→帮助`

均为 finished，无编造 Message ID；location 使用正式 TS 既有 `../../../lib/TbUiLib/src/ActionManager.cpp` 风格，行号取 B3 提取结果。未用 B3 临时 TS 覆盖正式 TS。

## B4-2 九条审计
9/9 在 QObject Context 精确命中，Source/Translation 与 B1 冻结矩阵逐字一致，均 finished，无重复、无意外内容。详见 `B4_New_Menu_Translation_Audit.csv`。

## B4-3 既有消息保护
- 39 条既有冻结译文：39/39 PASS（Context/Source/Translation/status 保持）
- 原有 562 条消息：原始 XML 消息块多重集比对，新增 9 块、缺失 0 块、原有块变化 0
- `tb::ui::AppController/Open Map` 仍为 unfinished 且无译文，未接受 B3 same-text heuristic
- AboutDialog 完整 HTML 未变
- 未引入 lupdate 的 561 条 Location 变化

## B4-4 最终统计
- 写入前：85 / 562 / 42 finished / 520 unfinished，SHA `f021e509…`
- 写入后：85 / 571 / **51 finished** / 520 unfinished，SHA `f81162b383364c9a4a12db4490df910d4555d74ead0acc9f1b414dfc3f9fbfe0`，134,278 B
- XML 解析通过；正式 TS 外所有保护对象未变；Git dirty 仍为 12

## 归档与停止
`reports\P2-D3B-B03-T4-2-3-B4\` 含执行报告、新九条/39条/全562条审计、源码复核、保护审计、B5 准备度、开始/结束快照、备份与 SHA256SUMS。SHA 覆盖全部应归档文件、清单不自列，独立复算全部通过。未上传 GitHub，无可验证链接。等待用户与 ChatGPT 审查，不进入 B5。
