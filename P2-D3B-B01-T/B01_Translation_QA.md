# B01_Translation_QA — 18 条译文预审独立核验

核验方法：直接读取原始 TS 与 R1-A 的 `B01_Release_Audit.csv` / `Revised_Message_Index.csv`，与 `B01_Translation_Proposal.csv` 独立比对。

| 检查项 | 实测 | 判定 |
|---|---|---|
| R1-A 保留的 B01 ID 数 | 18 | ✅ |
| 18 个 ID 全部可在最新索引找到 | 18/18 | ✅ |
| source 与原始 TS 逐字一致 | 18/18 | ✅ |
| 其他批次 ID 混入 | 0 | ✅ |
| 每条都有中文候选 | 18/18 | ✅ |
| Decision=推荐 | 9 | ✅（第一组） |
| Decision=待用户确认 | 9 | ✅（第二组） |
| 技术标识/扩展名有保留策略 | 6 项（见 Technical_Preservation_Audit） | ✅ |
| 占位符需保留 | 0 条（本批无 %1/%2/%n/%%） | ✅ |
| 术语表行数 | 17（推荐 6 / 待确认 9 / 保留原文 2） | ✅ |
| 源码上下文证据覆盖 | 18/18（函数/路径/上下文/handler） | ✅ |
| 本轮修改 TS / 源码 / CMake | 无 | ✅ |
| 运行 lupdate/lrelease/构建/启动 | 无 | ✅ |

## 术语一致性抽查

- Document：6 条菜单项统一“文档” ✅
- Load/Reload/Unload：Point/Portal 各 3 条动词组一致 ✅
- Revert Document ↔ 同语句 tooltip：译文“放弃所有未保存的更改，并重新加载地图文件。”与“还原文档”语义一致 ✅
- Save Document as...：译为“另存为”，未写成“导出” ✅
- Map...：按 Export 子菜单译“地图文件...”，非裸译“地图” ✅

## 未决事项（不构成 QA 失败，但需用户决定）

1. 9 条“待确认”译文的术语定稿
2. `Omit From Export` UI 标签是否同步翻译（跨批次依赖）
3. Point File / Portal File 候选名选择（中性 vs 调试/格式明确）

## 结论

译文预审数据完整、可逐条追溯；**QA 通过（预审级别）**，但本轮不修改 TS、不冻结术语，等待用户确认。
