# B03_U2_Terminology_Consistency_Audit — 术语一致性审计

| 检查项 | 结果 | 证据 |
|---|---|---|
| game directory 与 game path 统一“相对于游戏目录” | PASS | `3a29ad146ceb`、`013b4028d792` 均为“相对于游戏目录”；源码同用 `gamePath` 基准 |
| `Relative to map file` = “相对于地图文件所在目录” | PASS | `docPath.parent_path()` 为地图文件所在目录 |
| `Relative to application executable` = “相对于应用程序目录” | PASS | `SystemPaths::appDirectory()` 返回包含 EXE 的目录 |
| `Export Path` = “导出路径” | PASS | UI 分节标题，ID `0011be948dd6` |
| `Relative to export path` = “相对于导出目录” | PASS | `exportPath.parent_path()`，ID `26fd3ad9ed81`；概念与上一项分离 |
| Texture Paths 与 tooltip 统一“纹理路径” | PASS | `0ee72f3c8645` / `10b21b3fc756`；tooltip 使用“生成的材质文件中纹理路径” |
| Crash report / 问题报告 / Report 按钮区分 | PASS | `f0f928f057b7` 保留“崩溃报告”“问题报告”“上传这三个文件”及双换行；`444a30e5e793` = “报告问题”，实际仅打开 GitHub Issue 页 |
| Autodetect = “自动检测” | PASS | `5a27052291cb`，仅 Open 模式地图格式项 |
| Wavefront OBJ 保留英文 | PASS | `ee439e50a835`、`eed1f27c4948` |
| AboutDialog 结构 | PASS | 完整复制 U1 矩阵字段：开头换行、完整 URL、2 开发者 + 22 贡献者顺序、13 个产品名、`<br />`×24、`<b>`×3/`</b>`×3 |
| 20 条状态 | PASS | 20/20 `USER_CONFIRMED`，0 `FINAL_FROZEN` |
| ID/Context/Source 与 U1 一致 | PASS | 按 Message ID 比对 20/20（U1 为分组排序） |

## 不合并的 UI 概念
`Export Path`（文件路径输入区）与 `Export directory (semantic base)`（相对路径计算基准）保持两条独立术语；`gamePath` 虽同源但两条 UI 消息分别核对；texture 与 material 不混用。

本轮只审计报告材料，未修改正式 TS、源码或任何历史决策。
