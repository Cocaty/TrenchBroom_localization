# B03_U1_User_Review_Guide — RA-B03 20 条候选译文用户审阅指南

## 本阶段性质
**用户决策准备，不是翻译写入。** 20 条候选全部保持 `PROPOSED_PENDING_USER_CONFIRMATION`；你可以逐条或按术语组确认，未表态的条目不会被默认接受。

## 权威输入真实路径（已只读核验）
任务书列举的文件中，`B03_D1_Decision_Matrix.csv` 等 D1 原始文件实际位于：
`reports\P2-D3B-B03-D1\`
修正后的 R1 矩阵/术语表/备选表位于：
`reports\P2-D3B-B03-D1-R1\`
最新 A1 修正报告位于：
`reports\P2-D3B-B03-D1-R1-A1\B03_D1_R1_A1_F1_R2_R1_R1_R1_Report.md`

本指南以 **R1 修正后的矩阵**（AboutDialog URL/换行已修正）为准，并与 PRE 目标清单核对：20 条 ID、Context、Source 完全一致，无新增、遗漏或合并；小组按术语依赖排序。完备字段见 `B03_U1_User_Review_Matrix.csv`。

## A 组：路径类型与相对路径（7 条）
| 顺序 | ID | Source | 推荐译文 | 需你决定 |
|---|---|---|---|---|
| 1 | f9081511b752 | Path Type | 路径类型 | 标题措辞是否接受 |
| 2 | 2c01921052f7 | Choose Path Type | 选择路径类型 | DialogHeader 与窗口标题关系是否自然 |
| 3 | 8c9ed2e8de12 | Absolute | 绝对路径 | 是否需保留“路径”二字 |
| 4 | df4ef91af93a | You can convert a path... | 可以将路径转换为相对于某个参考路径的形式，也可以保留为绝对路径。使用相对路径有助于与他人协作编辑地图。 | “相对路径”说明是否自然 |
| 5 | 6a5208c30cca | Relative to map file | 相对于地图文件所在目录 | 源码基准是 `docPath.parent_path()`，是否采用更精确的“所在目录” |
| 6 | dbbba8b54bd0 | Relative to application executable | 相对于应用程序目录 | 源码基准是 `appDirectory()`，是否接受“目录”而非“可执行文件” |
| 7 | 3a29ad146ceb | Relative to game directory | 相对于游戏目录 | 是否与 B 组的 game path 统一为“游戏目录” |

## B 组：OBJ 导出与纹理路径（8 条）
| 顺序 | ID | Source | 推荐译文 | 备注 |
|---|---|---|---|---|
| 1 | ee439e50a835 | Export Wavefront OBJ | 导出 Wavefront OBJ | 格式名保留英文 |
| 2 | 0011be948dd6 | Export Path | 导出路径 | UI 分节标题，不因相对基准改为“导出目录” |
| 3 | 2915922a2166 | Enter a path or click to browse | 输入路径，或点击“浏览...”进行选择 | QLineEdit 占位提示 |
| 4 | 0ee72f3c8645 | Texture Paths | 纹理路径 | 与第 5 条同组，必须同步术语 |
| 5 | 10b21b3fc756 | Controls how the texture paths... | 控制生成的材质文件中纹理路径的计算方式。 | tooltip 不得改用“材质路径” |
| 6 | 013b4028d792 | Relative to game path | 相对于游戏目录 | 与 A 组第 7 条同一 `gamePath` 基准 |
| 7 | 26fd3ad9ed81 | Relative to export path | 相对于导出目录 | 源码基准 `exportPath.parent_path()` |
| 8 | eed1f27c4948 | Export Wavefront OBJ file | 导出 Wavefront OBJ 文件 | 保存对话框标题，不加省略号 |

## C 组：崩溃报告（3 条）
| 顺序 | ID | Source | 推荐译文 | 备注 |
|---|---|---|---|---|
| 1 | 8e40860a52a1 | Crash | 程序崩溃 | 对话框标题 |
| 2 | f0f928f057b7 | TrenchBroom has crashed... | TrenchBroom 已崩溃，但已成功保存崩溃报告、日志文件以及当前地图状态，文件位置如下。\n\n请创建一个问题报告，并上传这三个文件。 | 双换行与“上传三个文件”必须保留 |
| 3 | 444a30e5e793 | Report | 报告问题 | 按钮实际只打开 GitHub 新建 Issue 页面 |

## D 组：AboutDialog（1 条）
`cfde892c46df` 为完整 HTML 名单（2 位开发者、22 位贡献者，共 24 位具名人员）。推荐译文见审阅矩阵完整字段；仅“开发者/贡献者/第三方库、工具与资源”及功能说明中文化，URL `github.com/TrenchBroom/TrenchBroom`、人名、产品名、`<br />`/`<b>` 标签、顺序与换行必须原样保留。

## E 组：GameDialog（1 条）
`5a27052291cb`：`Autodetect` → 自动检测；仅用于 Open 模式地图格式组合框，不是检测游戏或扫描目录。

## 审阅方式
建议按 A→B→C→D→E 顺序确认：先定路径术语，再定 texture/material，再定崩溃措辞，最后确认 AboutDialog 与 Autodetect。任何条目都可以要求修订；未表态即保持待确认。
