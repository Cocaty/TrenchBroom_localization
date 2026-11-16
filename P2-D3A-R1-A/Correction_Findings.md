# Correction_Findings — R1 分类问题与 R1-A 修正证据

## 1. R1 的两处技术缺陷（实证）

### 1.1 ActionContext 正则截断
R1 正则 `ActionContext::([A-Za-z0-9_| ]+)` 对
`ActionContext::AnyView | ActionContext::AnyOrNoSelection | ActionContext::ClipTool`
实测提取为 `['AnyView | ActionContext', 'ClipTool']`——把第二个 `ActionContext` 名吞入第一个枚举值。
R1-A 改为在同一 addAction 语句内提取全部 `ActionContext::(\w+)`，实测得到 `['AnyView','AnyOrNoSelection','ClipTool']`。

### 1.2 动作路径失联
R1 用 ±25 行窗口取附近 `path{...}`，会把相邻动作的路径误配给无路径动作；R1-A 改为**花括号配对的完整 `addAction(Action{ ... });` 语句**，只从同一语句取路径/上下文/处理函数；缺失则留空并标记，不用邻项补齐。

## 2. 重点误判修正（含 handler 证据）

| source | 旧分类 | R1-A 分类 | 同语句证据 |
|---|---|---|---|
| Toggle Show Entity Classnames | 2D/主菜单 | Entity 与属性 | path `Controls/Map view/View Filter > Toggle show entity classnames`；ctx `Any`；handler `context.mapView().toggleShowEntityClassnames();` |
| Toggle Show Brush Entity Bounds | 2D | Entity 与属性 | handler `toggleShowBrushEntityBounds()` |
| Toggle Show Point Entity Bounds | 2D | Entity 与属性 | handler `toggleShowPointEntityBounds()` |
| Toggle Show Point Entities | R1 曾为 UNKNOWN | Entity 与属性 | handler `toggleShowPointEntities()` |
| Toggle Show Point Entity Models | 2D | Entity 与属性 | handler `toggleShowPointEntityModels()` |
| Perform Sweep | 工具快捷/2D | Brush、Face 和几何 | ctx `AnyView,AnyOrNoSelection,SweepTool`；handler `performSweep()`——SweepTool 仅辅助标签，按实际功能归几何 |
| Decrease/Increase Sweep Scale | 工具快捷 | Brush、Face 和几何 | ctx 含 `SelectionOwnedByTool,SweepTool`；handler `decreaseSweepScale()` / `increaseSweepScale()` |
| Move Forward/Backward/Left/Right/Up/Down | 工具快捷 | 2D 视图与地图编辑 | handler `mapView().move(vm::direction::…)`——对象移动，不是工具自身快捷键 |
| Duplicate and Move Forward/Backward | 工具快捷 | 2D 视图与地图编辑 | handler `duplicateAndMoveObjects(...)` |

**结论**：路径含 `Controls/Map view` 不再直接判为 2D；含 `Tool` 的 ActionContext 不再直接判为工具快捷操作。

## 3. R1-B01 混入非文件操作消息（最严重问题）

原 24 条中 **6 条不属于 `createFileMenu` / `Menu/File` 注册语句**：
`4e51812565de`(AppController Open Map)、`5b111135cfe7`/`82fad02a71ea`(CompilationTaskListBox)、`2a294870bcbd`/`f45f39eb562e`/`5b8a5ea2d9b0`(GameEngineProfileEditor)。详见 `B01_Release_Audit.md`。

## 4. 统计与产物

全部 562 条重新分类（`Revised_Message_Index.csv`）、181 条具备动作级证据（`Action_Registration_Audit.csv`）、559 条 unfinished 重排 24 批（`Revised_Batches.csv`），独立校验结果见 `Batch_Integrity_Audit.md`。
