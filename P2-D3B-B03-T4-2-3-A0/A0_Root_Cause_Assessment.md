# A0_Root_Cause_Assessment — 九个顶级菜单未汉化根因

## 统一根因
九个顶级菜单标题均未进入 Qt 翻译管线：

`ActionManager.cpp:824/985/1251/1337/1424/1588/1935/1970/2040` 使用 `createMainMenu("File"/"Edit"/...)` 以普通 `std::string` 字面量建立 `Menu::name`；`ActionManager.cpp:2059-2062` 的 `createMainMenu` 只构造 `Menu{std::move(name), ...}`；`ActionBuilder.cpp:136` 在顶级菜单处直接 `qtMenuBar.addMenu(QString::fromStdString(menu.name))`，没有 `tr()`、`QCoreApplication::translate()` 或显式 Context。

因此正式 TS 中对九个标题的精确 Source 检索为 **0/9**，QM（T4-1 回转 TS）中也为 **0/9**。QTranslator 没有可查找的 TS/QM 消息，顶级标题保持源码英文字面量。

## 为什么 File 下拉菜单能显示中文
菜单内部 QAction 的 label 使用 `QObject::tr(...)`（例如 `ActionManager.cpp:825` 附近的 `QObject::tr("New Document")`），`ActionBuilder.cpp:68-69` 用 `tbAction.label()` 创建 QAction。正式 TS 中 `New Document`、`Open Document...`、`Save Document`、`Revert Document`、`Close Document` 等均存在于 Context `QObject`，状态 finished，译文分别为“新建文档”“打开文档...”“保存文档”“还原文档”“关闭文档”。这与截图中 File 下拉菜单部分汉化一致。

因此，截图现象**不是 QTranslator 加载失败证据**；恰恰相反，菜单项翻译生效说明翻译器很可能在工作，但顶级菜单名从未经过同一翻译链。

## 九条菜单分类
M01 File、M02 Edit、M03 Selection、M04 Groups、M05 Tools、M06 View、M07 Run、M08 Debug、M09 Help 均为：

**`MISSING_FROM_TS`**（置信度 HIGH）

含义：源码创建位置可唯一确认；标题赋值未调用 Qt 翻译；正式 TS 不存在可靠对应消息；QM 不存在对应翻译。不是 unfinished 未编译，也不是 Context 候选不匹配；是消息从一开始就未被纳入 TS 管线。

## 对照链断点
`截图菜单标题 → ActionManager createXxxMenu → createMainMenu(字面量) → [断点：无翻译调用] → 无 Runtime Context → 无 TS 消息 → 无 QM 条目`

`QMenuBar::addMenu(QString)` 接收的是已确定的字符串，QTranslator 不会自动翻译普通 QString。

## 最小修正建议（不实施）
不建议无差别新增九条 TS 消息。最安全方向是：在获得独立授权后，考虑把九个顶级菜单名改为显式 `QObject::tr("File")` 等（或项目约定的显式 Context），再按正规流程 lupdate → 审阅/冻结 → lrelease → 构建验证。风险：需确定 Context 与已有翻译体系一致，避免影响子菜单同名字符串；必须重新验证 QM 与运行期界面。当前阶段仅记录建议，不改源码/TS。

## 未验证事项
本阶段未启动程序，未直接读取 QTranslator 运行日志；QTranslator 是否“成功加载”仍 NOT_VERIFIED。上述根因解释的是“即使翻译器工作，顶级菜单也不会被翻译”的静态代码原因。
