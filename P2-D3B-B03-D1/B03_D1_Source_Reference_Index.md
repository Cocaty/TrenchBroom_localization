# B03_D1_Source_Reference_Index — 争议决策源码依据（v2026.2）

| 决策 | 源码路径与行 | 关键事实 |
|---|---|---|
| 地图文件相对路径 | `lib/TbUiLib/src/ChoosePathTypeDialog.cpp:39-52` | `PathType::DocumentRelative` → `absPath.lexically_relative(docPath.parent_path())`；基准是地图文件**所在目录** |
| 游戏目录相对路径（选择路径类型） | `ChoosePathTypeDialog.cpp:48, 77, 115` | `PathType::GameRelative` → 相对构造参数 `gamePath` |
| 应用程序目录 | `lib/TbUiLib/include/ui/SystemPaths.h:34-37`；`src/SystemPaths.cpp:56-58` | `appDirectory()` 返回 `QCoreApplication::applicationDirPath()`，注释明确为“包含 TrenchBroom 可执行文件的目录” |
| 游戏路径相对模式（OBJ 导出） | `lib/TbUiLib/src/ObjExportDialog.cpp:95, 147-150`；`lib/TbMdlLib/src/ObjSerializer.cpp:137-143` | `RelativeToGamePath` 使用材质相对游戏路径；与 ChoosePathTypeDialog 共用 gamePath 基准概念 |
| 导出路径相对模式 | `ObjExportDialog.cpp:99, 147-150`；`ObjSerializer.cpp:130, 142-144` | `basePath = options.exportPath.parent_path()`，即导出 OBJ 文件**所在目录**；故本轮把“相对于导出目录”作为修正推荐，“相对于导出路径”保留为备选待确认 |
| Texture / Material | `ObjExportDialog.cpp:91-92` | `Texture Paths` 标题与“生成的材质文件中的纹理路径计算方式”tooltip 同属一组；纹理是材质文件引用的资源 |
| Report 按钮 | `lib/TbUiLib/src/CrashDialog.cpp:58-60, 89-93` | 按钮 `Report` 的 handler 仅 `QDesktopServices::openUrl(github.com/.../issues/new)`；不上传文件、不自动提交 |
| Autodetect | `lib/TbUiLib/src/GameDialog.cpp:262-274` | 仅 `DialogType::Open` 时加入 `Autodetect`；是地图格式自动检测，非游戏或目录扫描 |
| AboutDialog | `lib/TbUiLib/src/AboutDialog.cpp:39-88` | 完整 HTML 名单为单个 `tr(R"(...)"` 原始字符串；`<br />`、`<b>`、人名与产品名必须保留 |
| OBJ 导出入口 | `ActionManager.cpp:863`；`MapWindow.cpp:1069-1080` | `Menu/File/Export/Wavefront OBJ...` → `exportDocumentAsObj()` → `ObjExportDialog` |
| About 入口 | `ActionManager.cpp:2054`；`AppController.cpp:403` | `Menu/File/About TrenchBroom` → `showAboutDialog()` → `AboutDialog` |
| 路径对话框入口 | `ViewUtils.cpp:83`；`WadUtils.cpp:55` | 分别由加载外部实体定义文件、添加 WAD 材质路径触发 |

本轮未启动程序；以上均为静态源码证据。PRE 中“B02-D1 冻结 game path→游戏路径”的说法已在本轮纠正：B02-D1 只冻结 `Open Map → 打开地图`。
