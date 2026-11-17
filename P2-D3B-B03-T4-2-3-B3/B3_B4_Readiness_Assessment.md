# B3_B4_Readiness_Assessment — B4 正式 TS 写入准备度

## 结论：**READY_WITH_LIMITATIONS**

九条新消息已由 lupdate 正确提取，39 条冻结译文全部保留，正式 TS 与保护对象未变。限制是 lupdate 的 same-text heuristic 在非冻结重复消息中复制了一条译文，以及 561 条 location 元数据路径变化；两者都不应被 B4 自动写入正式 TS。

## 满足的 READY 条件
1. B2 五文件差异复核通过
2. lupdate 正常执行，退出码 0
3. 九条消息全部提取（9/9）
4. 九条 Context 全部为 `QObject`
5. 九条 Source 与 B1 冻结矩阵完全一致
6. 原有 39 条冻结译文全部保留（39/39）
7. 正式 TS 仍为 `f021e509…`，未被修改
8. 保护对象无意外变化

## 限制 / B4 必须处理
- `tb::ui::AppController/Open Map` 是既有 unfinished 重复消息；lupdate 通过 same-text heuristic 从 `tb::ui::WelcomeWindow/Open Map` 复制了“打开地图”。它不属于 39 条冻结目标。B4 只能写入九条顶级菜单译文，不得顺带接受该启发式结果。
- 561 条 location 变化源于 lupdate 将源码相对路径从 `../../../lib/...` 规范化到 `../../../src/TrenchBroom/lib/...`；B4 如果只写译文，应避免在正式 TS 中引入这些无关元数据变化。
- stderr 中的 generated manual HTML / vcpkg header 警告来自项目既有 lupdate project 扫描范围，退出码仍为 0；非本阶段引入。

## B4 允许输入
使用 `Artifacts/TrenchBroom_zh_CN.lupdate.tmp.ts` 中的九条新消息作为结构依据，写入目标仅为九条 `QObject` Context 的 finished 译文；正式 TS 的其余内容必须保持不变。

本文件不授权进入 B4。
