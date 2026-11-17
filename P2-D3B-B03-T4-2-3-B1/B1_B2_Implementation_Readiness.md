# B1_B2_Implementation_Readiness — B2 实施准备清单

## 状态：**TECHNICAL_DESIGN_READY_PENDING_USER_TRANSLATION_CONFIRMATION**

技术方案 D 经复核无未解决结构风险；九条中文译文仍为候选，状态 `PENDING_USER_CONFIRMATION`，未冻结、未写入。

## 1–2. 预计修改文件与内容
| 文件 | 预计修改 |
|---|---|
| `lib/TbUiLib/include/ui/ActionMenu.h` | 新增 `std::string displayName`；保留 `name` 类型与语义 |
| `lib/TbUiLib/src/ActionMenu.cpp` | `Menu::addMenu` 的 `Menu{...}` 初始化补 displayName（设为空，UI 回退 name） |
| `lib/TbUiLib/include/ui/ActionManager.h` | `createMainMenu` 签名扩展；**L60 `m_toolBar = Menu{"Toolbar", ...}` 初始化补 displayName** |
| `lib/TbUiLib/src/ActionManager.cpp` | L2059-2062 聚合初始化补 displayName；九处 `createMainMenu("X", QObject::tr("X").toStdString())` |
| `lib/TbUiLib/src/ActionBuilder.cpp` | L136 顶级菜单优先使用 displayName，空则回退 name；L140 子菜单维持 name 回退逻辑 |

## 3. 全部 Menu 初始化位置
1. `ActionManager.h:60` —— `Menu{"Toolbar", MenuEntryType::None, {}}`（A1 未单列，B2 必须处理）
2. `ActionManager.cpp:2061` —— `Menu{std::move(name), MenuEntryType::None, {}}`
3. `ActionMenu.cpp:47` —— `Menu{std::move(name_), entryType_, {}}`
另有 `ActionManager.h:54 std::vector<Menu> m_mainMenu` 与 `ActionManager.h:155 createMainMenu` 签名需适配；均在已列五文件内，**没有发现五个文件以外的 tb::ui::Menu 初始化点**。其他 `QMenu{...}` 是 Qt 类，不属于本结构。

## 4. 九个菜单调用位置
`ActionManager.cpp:824/985/1251/1337/1424/1588/1935/1970/2040`，分别 File/Edit/Selection/Groups/Tools/View/Run/Debug/Help。

## 5–7. displayName 与英文 name 保护
- `name` 继续保存英文 `"File"` 等，作为内部稳定标识
- `displayName` 保存 `QObject::tr("File")` 等结果；空值时 UI 回退 `name`
- `KeyboardShortcutModel.cpp:260` 与 `DumpShortcuts/src/Main.cpp:141` 继续读取 `name`，不受中文显示影响
- Context 统一 `QObject`，与 ActionManager 现有 `QObject::tr(...)` 约定一致

## 8. 编译前静态检查
- 三个聚合初始化点全部补齐新字段
- 九处 Source 字面量与 TS 候选逐字一致
- 未改动 39 条冻结译文
- 未改动 KeyboardShortcutModel / DumpShortcuts 的 name 读取
- 不新增独立 Context；不运行 lupdate/lrelease

## 9. 回滚
撤销五个文件的受控修改；如有已备份 TS/QM 则恢复；重新静态验证 39 条译文、name 路径与九条 Source 未残留。

## 10. 不得在 B2 顺带处理
用户译文确认、lupdate 生成消息、TS 译文写入、QM 重编译、构建、运行期验证、Open Recent/Export/BSP 菜单、全项目翻译机制重构、其他 unfinished 消息。
