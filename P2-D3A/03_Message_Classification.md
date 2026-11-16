# 03_Message_Classification — 功能区域分类（全 562 条）

分类方法：按 `(context, source, location 文件路径/类名)` 的关键词规则自动归类（脚本 `Evidence/analyze_ts.py`），每条记录 `category` 与 `category_reason`；规则无法可靠判定者标记 UNKNOWN 并给出原因。**未依据英文单词表面含义强行猜测功能**。完整清单：`Evidence/P2D3A_Message_Index.csv`（按 id 可查），context 视图：`Evidence/P2D3A_Context_Stats.csv`。

## 分类统计（主要分类）

| 分类 | 条数 |
|---|---|
| 主菜单和主窗口 | 185 |
| 2D 视图与地图编辑操作 | 62 |
| 游戏配置与资源管理 | 58 |
| Brush、Face 和几何编辑 | 50 |
| Texture 与材质管理 | 42 |
| Entity 与属性编辑 | 34 |
| Preferences 和设置页面 | 33 |
| 对话框和确认提示 | 26 |
| 文件操作与项目管理 | 23 |
| 工具提示与状态信息 | 15 |
| 错误信息和警告 | 4 |
| **UNKNOWN** | **30** |
| 3D 视图与摄像机操作 / 工具栏和快捷操作 / 地图加载保存导出 / 其他 | 0（当前 562 条中无可靠归入的独立条目；对应功能文本已并入相邻分类）|

合计 **562**，每条恰好一个主分类；无重复归属。

## UNKNOWN 30 条（均为规则无可靠线索）

代表样例（context | source | 位置）：
- QObject | `%1 Name` / `Group` / `Layer` | ViewUtils.cpp（通用视图工具函数，具体 UI 用途需结合调用方人工确认）
- tb::ui::CollapsibleTitledPanel | `hide` / `show` | CollapsibleTitledPanel.cpp（折叠面板动作）
- tb::ui::Console | `Clear` | Console.cpp（控制台右键菜单）
- tb::ui::IssueBrowserView | `Show` / `Hide` / `Fix` | IssueBrowserView.cpp（问题列表右键菜单）
- tb::ui::LayerEditor | `Make active layer` | LayerEditor.cpp（图层右键菜单）

原因统一说明：这些文本在通用工具函数或右键菜单中出现，context 名称本身不指向唯一功能域；自动规则保守标记 UNKNOWN，**待人工/校阅阶段按源码调用链确认**，不猜测分类。

## 用途限制说明

本分类是**翻译批次组织依据**，不是产品功能规格；少数条目可能跨功能域，统一取主分类以避免批次重叠。
