# A1_Execution_Report — 顶级菜单标题翻译接入方案只读设计

## 最终状态：**PASS_WITH_LIMITATIONS**

只读调查完成并给出唯一推荐方案。限制：未运行 lupdate、未构建、未启动程序，lupdate 对新字面量的实际行为与运行期效果需未来验证，标记 `LUPDATE_BEHAVIOR_NOT_VERIFIED` / `RUNTIME_NOT_VERIFIED`。

## 路径与基线
任务书给出的 `app\TrenchBroom\src\mdl\ActionManager.cpp` / `ActionBuilder.cpp` 在本工作区不存在；真实路径为 `lib\TbUiLib\src\ActionManager.cpp` 与 `lib\TbUiLib\src\ActionBuilder.cpp`，相关头文件在 `lib\TbUiLib\include\ui\`。Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=7；正式 TS `f021e509…`、QM `707011a3…`、QRC `de72b206…`、CMake/Main.cpp、构建/测试 EXE 与测试配置均与基线一致，保护对象 15/15 未变。

## 14 个问题逐条回答
1. **Menu::name 类型**：`std::string`，定义于 `ActionMenu.h:64`
2. **全部读写位置**：见 `A1_Menu_Name_Usage_Audit.csv` 9 条；写入在 `ActionMenu.cpp:47`、`ActionManager.cpp:2061`；UI 读取在 `ActionBuilder.cpp:136/140`；内部路径读取在 `DumpShortcuts/src/Main.cpp:141`、`KeyboardShortcutModel.cpp:260`
3. **是否承担内部逻辑标识功能**：是。参与快捷键模型路径与 DumpShortcuts 路径构造；不应替换为中文
4. **createMainMenu 调用链**：见 `A1_Menu_Creation_Callgraph.csv`；`createXxxMenu()` → `createMainMenu("...")` → `Menu::name` → `ActionBuilder.cpp:136` → `QMenuBar::addMenu()`；九个均唯一，无其他入口
5. **ActionManager 是否适合 QObject::tr()**：它不是 QObject 派生类，不能写成员 `tr()`；但本项目在该文件大量使用静态 `QObject::tr("...")`，可直接沿用，生成 Context `QObject`
6. **现有 Context 约定**：`QObject`（ActionManager/ActionBuilder 静态调用）与类 Context（如 `tb::ui::ViewPreferencePane` 成员 `tr`）并存；近邻 ActionManager 采用 `QObject`
7. **翻译调用最合理位置**：在 ActionManager 九个 `createMainMenu` 调用处用静态字面量生成显示标题，并保留英文 name；UI 层只读取显示标题
8. **是否新增独立 Context**：不需要；推荐复用 `QObject`，与 ActionManager 现有约定一致
9. **是否修改 Menu 数据结构**：推荐方案 D 需新增一个 `displayName` 字段，但不改变 `name` 语义；这是为避免中文进入内部路径所需的最小结构扩展
10. **lupdate 是否识别**：静态 `QObject::tr("File")` 是标准可提取形式；历史 QObject 条目证明机制曾工作。但本轮未运行 lupdate，实际行为 `LUPDATE_BEHAVIOR_NOT_VERIFIED`
11. **最小修改文件/函数**：5 个文件，见 `A1_Minimal_Fix_Proposal.md`
12. **是否新增九条 TS 消息**：是，预计 9 条 Context `QObject` 新消息；中文仅为候选，当前不确认、不冻结、不写入
13. **保护 39 条冻结译文**：未来 lupdate 后逐条审计差异；推荐方案只新增消息，不设计任何改写既有译文的步骤
14. **风险与回滚**：见方案文档；主要是聚合初始化遗漏与同名 Source 多 Context 条目；回滚为撤销五个文件修改并从备份恢复 TS/QM

## 候选方案比较
A（直接把 name 改中文）会污染内部路径，排除；B（新独立 Context）可稳定但偏离现有约定且需新 Context，非首选；C（ActionBuilder 动态 translate）因 lupdate 无法静态提取动态字符串，排除；**D（保留 name + 新增 displayName + QObject::tr 字面量）为唯一推荐方案**。

## 归档
报告目录 `reports\P2-D3B-B03-T4-2-3-A1\`，新增 11 个文件；SHA256SUMS 覆盖 10 项、独立复算全部通过、清单不自列。未上传 GitHub，无可验证链接。未修改源码/TS/QM、未 lupdate/lrelease、未构建、未启动、未进入后续阶段。
