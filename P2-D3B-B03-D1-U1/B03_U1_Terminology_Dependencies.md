# B03_U1_Terminology_Dependencies — 术语依赖说明

本文件只解释**依赖关系与源码事实**，不替用户确认译文。所有候选状态仍为 `PROPOSED_PENDING_USER_CONFIRMATION`。

## 1. game directory / game path
| 项目 | A 组 | B 组 |
|---|---|---|
| Message ID | `3a29ad146ceb` | `013b4028d792` |
| UI Source | Relative to game directory | Relative to game path |
| 源码 | `PathType::GameRelative` → `absPath.lexically_relative(gamePath)`（ChoosePathTypeDialog.cpp:48, 77, 115） | `ObjMtlPathMode::RelativeToGamePath`（ObjExportDialog.cpp:95, 147-150；ObjSerializer.cpp:137-143） |
| 实际基准 | 同一个 `gamePath` 参数 | 同一个游戏路径基准 |
| 推荐统一译法 | 相对于游戏目录 | 相对于游戏目录 |
| 备选 | 相对于游戏路径 | 相对于游戏路径 |
| 用户需决定 | 两条必须一起决定：用“游戏目录”还是“游戏路径” | 同左 |

**重要纠正**：B02-D1 只冻结了 `Open Map → 打开地图`，没有冻结 `game path → 游戏路径`。不得把 B02 的那条具体译文扩大为 B03 术语依据。

## 2. Export Path / Export directory
| 概念 | ID | 类型 | 推荐 | 源码 |
|---|---|---|---|---|
| Export Path | `0011be948dd6` | UI 分节标题，用户输入/选择 OBJ 输出文件路径 | 导出路径 | ObjExportDialog.cpp:74 |
| Export directory（语义概念） | `26fd3ad9ed81` | 相对路径计算基准 | 相对于导出目录 | ObjSerializer.cpp:130 `basePath = options.exportPath.parent_path()` |

`Export directory (semantic base)` 是对源码计算基准的命名，TS 中**不存在** `Export Directory` 消息。不要把分节标题改成“导出目录”，也不要把相对基准按字面译成“相对于导出路径”而丢失目录语义。两条需分别审阅。

## 3. Texture / Material
| 项 | ID | 推荐 | 关系 |
|---|---|---|---|
| Texture Paths（标题） | `0ee72f3c8645` | 纹理路径 | texture 指材质文件引用的纹理资源 |
| tooltip | `10b21b3fc756` | 控制生成的材质文件中纹理路径的计算方式。 | material file 是材质文件；必须与标题同术语 |

B01 已确认 `Material Collections → 材质集合`，说明 material 译为“材质”；但这不意味着 texture 也译为“材质”。标题与 tooltip 为同一决策组，不能一个用“纹理路径”、另一个用“材质路径”。

## 4. 其他路径基准（A 组）
- `Relative to map file`：源码 `absPath.lexically_relative(docPath.parent_path())`，基准是**地图文件所在目录**，不是地图文件本身。
- `Relative to application executable`：源码 `SystemPaths::appDirectory()` 返回包含 TrenchBroom 可执行文件的**目录**，不是 EXE 文件本身。
- `Absolute`：路径类型单选项，须保留“路径”概念。

## 5. Crash 术语链
- crash report → 崩溃报告（崩溃时保存的文件）
- issue report → 问题报告 / GitHub 问题单（用户需创建）
- Report 按钮 → 报告问题（实际行为只是打开 `github.com/TrenchBroom/TrenchBroom/issues/new`，不上传文件、不自动提交）

## 6. AboutDialog
URL、人名、24 位具名人员顺序、13 个库/工具/字体产品名、HTML 标签与换行均属于受保护结构；只翻译 3 个分节标题及功能说明。人数口径：2 位开发者 + 22 位贡献者 = 24 位具名人员。
