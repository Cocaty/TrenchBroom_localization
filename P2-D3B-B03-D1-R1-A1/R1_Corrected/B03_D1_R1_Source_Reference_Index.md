# B03_D1_R1_Source_Reference_Index — R1 修订相关源码依据

| 条目 | 源码 | 证据 |
|---|---|---|
| AboutDialog 原始 Source | 正式 TS `cfde892c46df` | 985 字符；开头 `\n`；URL `github.com/TrenchBroom/TrenchBroom`；`<br />`×24；`<b>`×3 / `</b>`×3；2 位开发者、22 位贡献者，共 24 位具名人员；13 个产品名；结尾无换行 |
| AboutDialog 实现 | `lib/TbUiLib/src/AboutDialog.cpp:39-90` | `tr(R"( ... )")` 原始字符串直接送入 `QLabel`；HTML 与名单顺序不可改动 |
| Export Path（UI） | `lib/TbUiLib/src/ObjExportDialog.cpp:74` | `formLayout->addSection(tr("Export Path"))`，分节标题，用户输入/选择 OBJ 输出文件路径 |
| Export Directory（语义基准） | `lib/TbMdlLib/src/ObjSerializer.cpp:130, 142-144` | `basePath = options.exportPath.parent_path()`；相对路径以导出 OBJ 文件所在目录为基准 |
| 术语区分 | R1 术语表 | `Export Path` 与 `Export directory (semantic base)` 两条独立术语；后者仅为源码语义概念，TS 中无 `Export Directory` 消息 |
| 其他 19 条 | 沿用 D1 `B03_D1_Source_Reference_Index.md` | R1 未重新调查，未改变原结论 |

静态源码证据；本轮未启动程序。完整 HTML 审计结果见 `Evidence/AboutDialog_HTML_Audit.json`。
