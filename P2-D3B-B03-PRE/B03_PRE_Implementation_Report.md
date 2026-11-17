# B03_PRE_Implementation_Report — B03 批次只读预审

日期：2026-11-17 12:24 ｜ 全程只读，未翻译、未构建、未启动程序

## 结论：**PASS WITH LIMITATIONS**

B03 范围清晰（RA-B03 共 **20** 条）、全部 ID 在最新权威批次清单中唯一且无跨批重复、20/20 在正式 TS 中唯一命中；当前 v2026.2 源码语义与静态调用链已逐条核查。**13 条 READY_FOR_TRANSLATION、7 条 NEEDS_TERMINOLOGY_CONFIRMATION、0 条 NEEDS_FURTHER_INVESTIGATION、0 条 BLOCKED**。受限原因：7 条涉及相对路径措辞、纹理/材质术语、issue report 等需用户决定；所有调用链为静态证据，未做运行期验证。

## 数据来源与基线
- Git：feature/zh-CN-v2026.2，HEAD `4c756be1…`，dirty=7（6 个既知 tracked 修改 + translations/ 未跟踪），未清理
- 正式 TS：`901554891…`，131,100 B；85 context / 562 message / 22 finished / 540 unfinished / 0 obsolete，与预期一致
- 权威清单：`P2-D3A-R1-A/Evidence/Revised_Batches.csv`（`9e3a96d70e0f…`，24 批、559 条 ID）
- 源码：本工作区 v2026.2 实际文件（AboutDialog.cpp / ChoosePathTypeDialog.cpp / CrashDialog.cpp / GameDialog.cpp / ObjExportDialog.cpp / ActionManager.cpp / MapWindow.cpp / AppController.cpp / ViewUtils.cpp / WadUtils.cpp）

## 全局与 TS 核对
| 检查项 | 结果 |
|---|---|
| 总记录 / 批次 | 559 / 24 |
| RA-B03 记录 / 唯一 ID | 20 / 20 |
| B03 内部重复 / 跨批重复 / 空 ID | 0 / 0 / 0 |
| 跨 context 同 source 误合并 | 0（按 ID+context+source 分别审查） |
| B03 对应 TS 命中 | 20/20，全部 unfinished，无 finished 混入 |
| 多 location / comment / extracomment / numerusform | 均 0（每条仅 1 个 location） |

## 语义与 UI 分类摘要
- 关于对话框 1 条：HTML 贡献者名单（保留人名与 `<br />`/`<b>` 标签）
- Choose Path Type 对话框 7 条：窗口标题、说明文字、4 个相对路径单选项、DialogHeader
- Crash 对话框 3 条：标题、崩溃说明文本（含 `\n\n`）、Report 按钮（打开 GitHub issues）
- GameDialog 1 条：Open 模式地图格式组合框的 `Autodetect` 项
- ObjExportDialog 8 条：标题、Export Path 分节、占位符、Texture Paths 分节及 tooltip、2 个相对路径单选项、文件保存对话框标题
- 关键调用链：Help > About TrenchBroom（ActionManager.cpp:2054）→ showAboutDialog → AboutDialog；File > Export > Wavefront OBJ...（ActionManager.cpp:863）→ MapWindow::exportDocumentAsObj → ObjExportDialog；ChoosePathTypeDialog 由 ViewUtils.cpp:83（实体定义文件）与 WadUtils.cpp:55（WAD 材质路径）调用

## 术语继承与风险
- 可继承：B01 `Wavefront OBJ` 保留英文、`.map` 保留；B02 `game path`→“游戏路径”在 ObjExportDialog 中为 EXACT 概念；B01 `Material`→“材质”用于 material file
- 需确认：ChoosePathTypeDialog 的 `game directory` vs B02 `game path`（措辞差异）；`map file` vs `map document`；“相对路径”短语在 radio 标签与说明文字中的统一表达；`Texture Paths` 应为“纹理路径”还是“材质路径”；CrashDialog 的 `issue report` / `Report` 按钮译法；AboutDialog 分节标题“3rd Party Libraries, Tools and Assets”
- 无 `%1/%n`、快捷键、复数；保留 `Wavefront OBJ`、`*.obj`、HTML 标签和双换行
- 所有候选译文均标注 `PROPOSAL ONLY — NOT USER CONFIRMED`，未写入 TS

## 未解决问题
7 条 `NEEDS_TERMINOLOGY_CONFIRMATION` 需用户在 B03-D1 决定；本轮静态调用链未做运行期 UI 复核。

## 授权边界
未修改 TS/源码/CMake/QM/QRC，未运行 lupdate/lrelease/lconvert，未构建/启动/部署，未提交 Git，未修改任何历史报告；本轮仅新增本目录报告与证据。

## 建议下一步
用户审查本报告后，另行授权 B03-D1 冻结 20 条正式译文（其中 7 条先确认术语）。
