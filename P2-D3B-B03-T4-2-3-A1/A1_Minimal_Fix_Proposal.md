# A1_Minimal_Fix_Proposal — 顶级菜单标题翻译接入最小方案（设计，不实施）

## 推荐方案：方案 D —— 保留稳定 name，新增 displayName，使用 QObject::tr 静态字面量

### 设计原则
- 不改变 `Menu::name` 的英文稳定标识用途：它已被 `KeyboardShortcutModel.cpp:260` 和 `DumpShortcuts/src/Main.cpp:141` 用于构建内部路径；把它改成中文会改变快捷键模型路径、排序/冲突关联与导出路径
- 翻译只发生在显示层：`ActionBuilder.cpp:136` 应使用 display title 而非稳定 name
- 使用项目已有约定：`ActionManager.cpp` 已大量使用 `QObject::tr("...")`，Context 为 `QObject`，lupdate 可静态识别
- 九条中文仅为候选，未确认、未冻结、未写入

### 示意代码（仅报告展示，不保存为补丁）
```cpp
// ActionMenu.h
struct Menu {
  std::string name;        // 稳定英文标识，保持不变
  std::string displayName; // 新增：UI 显示标题；为空时回退 name
  MenuEntryType entryType;
  std::vector<MenuEntry> entries;
};

// 两个 Menu 聚合初始化点补齐 displayName：
// ActionMenu.cpp:47；ActionManager.cpp:2061

// ActionManager.h
Menu& createMainMenu(std::string name, std::string displayName);

// ActionManager.cpp（九处）
auto& fileMenu = createMainMenu("File", QObject::tr("File").toStdString());
// Edit / Selection / Groups / Tools / View / Run / Debug / Help 同理

// ActionBuilder.cpp:136
currentMenu = qtMenuBar.addMenu(
  QString::fromStdString(menu.displayName.empty() ? menu.name : menu.displayName));
```

### 预计修改范围
| 文件 | 位置 | 修改 |
|---|---|---|
| `lib/TbUiLib/include/ui/ActionMenu.h` | L64 附近 | 增加 `displayName` 字段；保持 `name` 不变 |
| `lib/TbUiLib/src/ActionMenu.cpp` | L45-47 | 初始化 `displayName`（子菜单可为空回退） |
| `lib/TbUiLib/include/ui/ActionManager.h` | L155 | `createMainMenu` 增加 displayName 参数 |
| `lib/TbUiLib/src/ActionManager.cpp` | L2059-2062、L824/985/1251/1337/1424/1588/1935/1970/2040 | 构造带 displayName 的 Menu；九处 QObject::tr 静态字面量 |
| `lib/TbUiLib/src/ActionBuilder.cpp` | L136 | 使用 displayName 回退 name |

### 预计 TS 影响
- 新增 9 条 `QObject` Context 消息：File/Edit/Selection/Groups/Tools/View/Run/Debug/Help
- 当前九条中文仅为候选，状态应为 unfinished，需用户确认后才能写入正式译文
- 预计不影响已冻结的 B01/B02/B03 39 条译文；未来 lupdate 后必须做差异审计确认

### 验证步骤（需独立授权）
1. 修改后运行 lupdate，确认 9 条新消息出现在 QObject Context
2. 确认 39 条已冻结译文未被改写
3. 用户逐条确认九条候选译文
4. 写入 TS、lrelease、构建、静态验证 QM/EXE
5. portable 测试副本运行期验证九个顶级标题为中文
6. 验证 KeyboardShortcutModel 与 DumpShortcuts 路径仍为英文稳定标识

### 风险与回滚
- 风险：聚合初始化点遗漏；子菜单 displayName 回退处理错误；lupdate 生成同名 Source 多 Context 条目；用户尚未确认译文
- 回滚：撤销上述五个文件的受控修改；从备份恢复 TS/QM；重新构建并验证 39 条译文与快捷键路径不变
- 本阶段不实施任何修改。
