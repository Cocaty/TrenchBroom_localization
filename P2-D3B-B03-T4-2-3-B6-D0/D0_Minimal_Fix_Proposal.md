# D0_Minimal_Fix_Proposal — GenerateManual DLL 缺失的最小修复建议

## 推荐方案：仅为 DumpShortcuts 目标补齐递归第三方 DLL

### 修改范围
- 预计仅修改 `app/DumpShortcuts/CMakeLists.txt`（本阶段未修改）
- 预计在 DumpShortcuts 的 POST_BUILD 阶段，将已确认的 17 个 DLL 从 `vcpkg_installed/x64-windows/bin` 复制到 `$<TARGET_FILE_DIR:DumpShortcuts>`
- 不修改 TrenchBroom 主程序 CMake、源码、QRC、TS、QM、PATH 或系统运行库

### 需要复制的 17 项
`brotlidec.dll`、`bz2.dll`、`libpng16.dll`、`Iex-3_3.dll`、`Imath-3_2.dll`、`OpenEXR-3_3.dll`、`jpeg8.dll`、`openjp2.dll`、`raw.dll`、`tiff.dll`、`libwebp.dll`、`libwebpdecoder.dll`、`libwebpmux.dll`、`kubazip.dll`、`minizip.dll`、`poly2tri.dll`、`pugixml.dll`

来源均已在 `build/v2026.2-msvc145-qt6103/vcpkg_installed/x64-windows/bin` 确认存在；预期位置均为 `build/.../app/DumpShortcuts/Release/`。

### 为什么不采用其他方案
- **修改 PATH**：会改变构建环境并影响其他工具；不符合最小、可审计原则
- **从 TrenchBroom/Release 复制**：虽然文件存在，但会引入目标间顺序耦合；vcpkg bin 是更稳定来源
- **跳过 GenerateManual / 预生成 shortcuts.js**：会改变构建语义与产物链，范围更大
- **复制整个 TrenchBroom/Release**：粗放、不可审计，超出最小范围

### 风险与回滚
- 风险：POST_BUILD 复制列表若遗漏，故障仍会出现；新增 17 个构建目录文件，但仅限 DumpShortcuts/Release
- 验证：再次构建应使 `shortcuts.js` 自定义步骤退出 0，并生成新 EXE；随后重新执行 B6 的资源嵌入验证
- 回滚：撤销 `app/DumpShortcuts/CMakeLists.txt` 的局部修改并重新构建；无需触碰源码/TS/QM

本文件仅为建议，未执行修复、未复制 DLL、未修改 CMake。
