# Revised_Statistics — 562 条重新分类统计（R1-A）

数据：`Revised_Message_Index.csv`（562 行，全部消息）；`Action_Registration_Audit.csv`（181 条动作级证据）。

| 分类 | 条数 |
|---|---|
| 2D 视图与地图编辑操作 | 167 |
| 游戏配置与资源管理 | 68 |
| Texture 与材质管理 | 67 |
| Entity 与属性编辑 | 49 |
| Brush、Face 和几何编辑 | 47 |
| UNKNOWN | 56 |
| Preferences 和设置页面 | 33 |
| 对话框和确认提示 | 20 |
| 文件操作与项目管理 | 21 |
| 工具快捷操作 | 15 |
| 其他或待确认 | 8 |
| 工具提示与状态信息 | 6 |
| 错误信息和警告 | 3 |
| 3D 视图与摄像机操作 | 1 |
| 主菜单和主窗口 | 1 |
| **合计** | **562** |

- finished=3 / unfinished=559 / context=85（与 TS 解析一致）
- 动作级证据覆盖：**181 条**（全部含 addAction(Action{...}) 语句的 ActionManager 消息）
- 证据置信度：高=动作语句级；中=context/文件名关键词；低=UNKNOWN

## 与 R1 的主要变化（原因见 Correction_Findings.md）

- 几何 24→47、实体 49（含 5 个 View Filter 实体动作）、工具快捷 28→15——动作 handler 优先，避免 `Controls/Map view`/`*Tool` 上下文误判
- 游戏配置 47→68——Compilation/GameEngine 等非文件域消息不再因 `file/map/load` 关键词混入 B01
- UNKNOWN 61→56——仍保留保守标记

## 稳定 ID 与重复核验

- 重复 `(context, source)`：**0**
- ID 碰撞：**0**
- ID 与 `SHA256(context+"\x1f"+source)[:12]` 不一致：**0**（独立校验，见 Batch_Integrity_Audit.md）
