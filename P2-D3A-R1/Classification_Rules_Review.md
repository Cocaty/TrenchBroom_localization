# 分类规则审查报告 — ActionManager / ActionBuilder 专项

## 实测源码结构（当前 v2026.2，非历史行号）

`lib\TbUiLib\src\ActionManager.cpp` 函数（grep 实测）：
- 动态动作：`createTagActions`(L58)、`createEntityDefinitionActions`(L94)
- 视图动作：`createViewActions`(L149)——内含 `std::filesystem::path{"Controls/Map view/Create brush"}` 等**动作路径**与 `ActionContext::View3D | ... | AssembleBrushTool` 等**上下文标志**
- 菜单：`createFileMenu`(L822)、`createEditMenu`(L983)、`createSelectionMenu`(L1249)、`createGroupsMenu`(L1335)、`createToolsMenu`(L1422)、`createViewMenu`(L1586)、`createRunMenu`(L1933)、`createDebugMenu`(L1967)、`createHelpMenu`(L2038)
- 主菜单与工具栏：`createMainMenu`(L2059)、`createToolbar`(L2064)

`ActionBuilder.cpp` L47：`QObject::tr(" (%1)").arg(keySequence.toString(...))`——快捷键显示后缀，属工具快捷操作，不是主菜单。

## R1 分类规则（优先级从上到下）

1. `createTagActions` / `createEntityDefinitionActions` → **Entity 与属性编辑**（动态 tag/实体动作）
2. `createFileMenu` → 文件操作；`createRunMenu` → 游戏配置与资源管理；`createToolbar` → 工具栏和快捷操作
3. `createEditMenu` → 2D 视图与地图编辑操作（撤销/剪切/复制等）；`createSelectionMenu`/`createGroupsMenu` → 2D 视图与地图编辑操作
4. `createDebugMenu` → **其他或待确认**（开发者调试动作，不进入普通用户批次）；`createHelpMenu`/`createMainMenu` → 主菜单和主窗口
5. `createViewMenu` → 2D/3D（路径含 3D/摄像机 → 3D）
6. `createViewActions` → 按**动作路径**优先：`texture|material|uv` → 材质；`entity|tag` → 实体；`brush|clip|face|vertex|geometry` → 几何；`3d`/`ActionContext::View3D` → 3D；`tool` → 工具快捷；`anyview`/`Map view` → 2D；路径不足时按 source 关键词兜底
7. `ActionBuilder.cpp` → 工具快捷操作
8. 非 Action 文件 → context/文件名/source 关键词规则
9. 以上均不可靠 → **UNKNOWN**（附具体原因）

## 关键修正效果

| source | P2-D3A 分类 | R1 分类 | 证据 |
|---|---|---|---|
| Create Brush | 主菜单和主窗口 | Brush、Face 和几何编辑 | `Controls/Map view/Create brush` + View3D/AssembleBrushTool |
| Toggle Show Point Entity Bounds | 主菜单和主窗口 | Entity 与属性编辑 | source 实体线索 + createViewActions |
| Move Textures Up | 主菜单和主窗口 | Texture 与材质管理 | 动作路径/ source 材质线索 |
| Undo / Cut / Copy | 主菜单和主窗口 | 2D 视图与地图编辑操作 | `createEditMenu` |
| Print Vertices to Console（Debug 菜单） | 主菜单和主窗口 | 其他或待确认 | `createDebugMenu` |
| " (%1)"（快捷键后缀） | 主菜单和主窗口 | 工具快捷操作 | ActionBuilder.cpp L47 |

## 边界

- 分类基于函数名/路径/上下文的**自动规则**，每条均记录 category_reason；仍可能需要 ChatGPT 校阅时按调用链微调
- 61 条 UNKNOWN 保持标记，未强行归类
