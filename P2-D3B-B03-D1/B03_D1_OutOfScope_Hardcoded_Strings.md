# D1_OutOfScope_Hardcoded_Strings — 范围外硬编码英文字符串

以下字符串在 v2026.2 源码中客观存在，但**不属于 RA-B03 的 20 条 TS 目标消息**，本轮不为其建立译文决策、不修改源码、不加入决策矩阵。

## CrashDialog.cpp
`lib/TbUiLib/src/CrashDialog.cpp:55, 72-80`：
- `Crash Report`（DialogHeader）
- `Info`
- `Reason`
- `Version`
- `Build`
- `Files`
- `Map File`
- `Log File`

## ObjExportDialog.cpp
`lib/TbUiLib/src/ObjExportDialog.cpp:64, 83, 88, 125`：
- `Export`（窗口标题与按钮）
- `Browse...`
- `Path`

## 处理建议
这些是硬编码字符串，不会出现在 TS 中，正常 lupdate 流程无法覆盖。建议未来单独立项做“硬编码 UI 字符串审计/源码改造”，而不是在本批次扩大 RA-B03 范围。本轮仅记录，不处理。
