# 562 条消息重新分类统计（R1）

数据：`Evidence/P2D3A_R1_Message_Index.csv`（562 行，稳定 ID = SHA256(context+source)[:12]，分类理由逐条记录）。

| 主分类 | 条数 |
|---|---|
| 2D 视图与地图编辑操作 | **169** |
| Texture 与材质管理 | 67 |
| Entity 与属性编辑 | 47 |
| 游戏配置与资源管理 | 47 |
| 对话框和确认提示 | 32 |
| Preferences 和设置页面 | 33 |
| 工具快捷操作 | 28 |
| 文件操作与项目管理 | 24 |
| Brush、Face 和几何编辑 | 24 |
| UNKNOWN | **61** |
| 主菜单和主窗口 | 3 |
| 工具提示与状态信息 | 6 |
| 3D 视图与摄像机操作 | 5 |
| 错误信息和警告 | 8 |
| 其他或待确认 | 8 |
| **合计** | **562** |

## 与 P2-D3A 的变化

| 分类 | 旧 | 新 | 原因 |
|---|---|---|---|
| 主菜单和主窗口 | 185 | **3** | ActionManager 按函数/路径/上下文拆分 |
| 2D 视图与地图编辑操作 | 62 | **169** | createEditMenu/createSelectionMenu/createViewActions 归入 |
| Texture 与材质管理 | 42 | **67** | 动作路径含 texture/material/uv |
| Entity 与属性编辑 | 34 | 47 | 动态 tag/entity 动作与实体线索 |
| UNKNOWN | 30 | **61** | 规则更保守：ActionManager 路径不足者不再强行归主菜单；详见索引 category_reason |

## 稳定 ID 与证据

每条消息保留 `id`、context、source、location、category、category_reason、am_function、action_path；可按 ID 与旧 P2-D3A 索引（`P2D3A_Message_Index.csv`）逐条对比，**同一 (context,source) 的 ID 不变**。
