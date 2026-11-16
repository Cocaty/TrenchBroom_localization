# T4_QM_Artifact_Report — 构建树 QM 产物核验（T4-4 A）

构建树路径：`build\v2026.2-msvc145-qt6103\app\TrenchBroom\TrenchBroom_zh_CN.qm`

| 项 | 实测 |
|---|---|
| 大小 | **1,805 B**（构建前为 366 B） |
| SHA-256 | **a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66** |
| mtime | 2026-11-16 22:28:25 +0800（本轮构建时刻） |
| 与 T3 QM 比较 | SHA **完全一致**（T3 输出同哈希）✅ |
| 来源 | CMake 自动生成规则调用 lrelease，从正式 TS 生成（构建日志 L60-63："Generating TrenchBroom_zh_CN.qm"、"Generated 21 translation(s) (21 finished and 0 unfinished)"、"Ignored 541 untranslated source text(s)"）✅ |
| 资源路径 | 由 qrc alias `TrenchBroom_zh_CN.qm` + prefix `/translations` → `:/translations/TrenchBroom_zh_CN.qm` ✅ |

**注**：构建前正式构建目录中为旧 QM（366 B），本轮构建由 CMake 规则覆盖为当前 TS 编译结果——这是构建管线的正常行为，未手工写入、未部署到正式安装目录。副本存放于 `Evidence/TrenchBroom_zh_CN.qm`。
