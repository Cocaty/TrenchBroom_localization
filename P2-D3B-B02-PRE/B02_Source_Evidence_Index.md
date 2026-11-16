# B02_Source_Evidence_Index — 源码证据索引

## 权威批次材料
- `reports\P2-D3A-R1-A\Evidence\Revised_Batches.csv`（2026-11-16 21:15，最新生效）：24 批，559 条 unfinished 唯一归属；RA-B02 = 1 条 `3e1b6ba4c40e`
- 历史版本：`P2-D3A\Evidence\P2D3A_Batches.csv`（19 批，旧 B02=45 条）、`P2-D3A-R1\Evidence\P2D3A_R1_Batches.csv`（22 批，旧 R1-B02=3 条）

## B02 唯一消息源码证据

| 项 | 内容 |
|---|---|
| Message ID | `3e1b6ba4c40e` |
| context / source | `tb::ui::WelcomeWindow` / `Open Map` |
| TS location | `lib/TbUiLib/src/WelcomeWindow.cpp:140`（唯一 location） |
| 函数 | `WelcomeWindow::openOtherDocument()`（L134–150） |
| 同语句代码 | `QFileDialog::getOpenFileName(nullptr, tr("Open Map"), fileDialogDefaultDirectory(FileDialogDir::Map), "Map files (*.map);;Any files (*.*)")` |
| 调用链 | Welcome 面板 `m_openOtherDocumentButton`（文本 `"Browse..."`，L88–97）→ `openOtherDocument()` → 文件对话框 → `openDocument(path)`（L152–157）→ `m_appController.openDocument(path)` |
| UI 显示位置 | **文件选择对话框标题**（不是菜单项、不是 ActionManager 动作、不是工具栏） |
| 语义分类 | 文件与文档操作 / 对话框 |
| 证据强度 | 高（单 location、tr 调用与调用链完整；其余 create* 按钮文本为硬编码英文，不在本批） |

## 历史 R1-B02 两条的现归属（范围变更证据）
- `fa31bab9325d` "TrenchBroom Manual" → 最新 `RA-B08`（2D 视图与地图编辑操作）
- `b52021e3d78f` "About TrenchBroom" → 最新 `RA-B24`（隔离待确认）
- 两条历史分配保留在 B02_Batch_Scope_Audit.csv，不视为当前 B02
