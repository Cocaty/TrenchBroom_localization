# B01_Cross_Batch_Dependencies — Omit From Export 跨批次依赖

## 依赖链

| 环节 | 源码/字符串 | 当前状态 |
|---|---|---|
| 数据模型 | `Layer.h:39 m_omitFromExport`；`Layer.cpp:82-89 omitFromExport()/setOmitFromExport()` | C++ 标识，不译 |
| 图层右键菜单标签 | `LayerEditor.cpp:99` `tr("Omit From Export")` | TS 中未翻译（属其他批次），本轮不加入 B01 |
| 图层列表切换提示 | `LayerListBox.cpp:54` `tr("Toggle omit from export")` | TS 中未翻译（属其他批次），本轮不加入 B01 |
| 本批 tooltip | `ActionManager.cpp:878` `Exports the current map to a .map file. Layers marked Omit From Export will be omitted.` | ID `8626a59ed64f`，RA-B01 18 条之一；候选译文引用“不参与导出” |

## 术语建议与约束

- 推荐统一术语：**Omit From Export → 不参与导出**
- tooltip 推荐：`将当前地图导出为 .map 文件。标记为“不参与导出”的图层将被忽略。`
- `.map` 为扩展名，逐字保留
- 图层 UI 标签与 tooltip 必须**同一术语组**处理：若后续批次把界面标签译为其他说法，本 tooltip 必须同步修订
- 本轮不把两个 UI 字符串加入 RA-B01，不修改 TS，不把待确认项标为冻结

## 后续批次要求（供用户决策/授权）

1. 将 `Omit From Export` 与 `Toggle omit from export` 纳入同一批 Layer/图层相关翻译
2. 正式实施时，检查 tooltip 中的引号内属性名与 UI 标签逐字一致
3. 如果用户决定 tooltip 暂保留英文属性名 `Omit From Export`，则 UI 翻译批次仍需记录该决定，避免后续不一致

## 风险

- 只翻译 tooltip 而不译 UI 标签 → 用户看到的界面属性名与提示引用不一致
- 两处 UI 文案译为不同中文 → 术语分裂

## 状态

**待用户确认**：是否采用“不参与导出”、是否同步翻译图层属性 UI 文案、何时安排后续批次。本轮不做决定。
