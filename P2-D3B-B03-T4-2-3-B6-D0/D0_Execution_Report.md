# D0_Execution_Report — GenerateManual DLL 依赖故障只读定位

## 结论
失败进程是 **`DumpShortcuts.exe`**，不是 CMake、MSBuild、pandoc 或其他辅助程序。故障类型为 Windows 加载器 `STATUS_DLL_NOT_FOUND`（`0xc0000135`），由 GenerateManual 的 `shortcuts.js` 自定义命令触发。全仓源码未修改、未重新构建、未复制 DLL、未修改 PATH。

## 1. 自定义命令实际路径与参数
CMake 源码 `app/TrenchBroom/cmake/GenerateManual.cmake:42-47` 定义 `shortcuts.js` 输出规则：
1. `cmake.exe -E make_directory <gen-manual>`
2. `cmake.exe -E env QT_QPA_PLATFORM=offscreen "$<TARGET_FILE:DumpShortcuts>" "<gen-manual>/shortcuts.js"`

生成到 `GenerateManual.vcxproj` 的 Release 命令为：
`C:\Users\yoshi\Tools\CMake\4.2.8\bin\cmake.exe -E env QT_QPA_PLATFORM=offscreen C:/Users/yoshi/Projects/TrenchBroom-zhCN/build/v2026.2-msvc145-qt6103/app/DumpShortcuts/Release/DumpShortcuts.exe C:/Users/yoshi/Projects/TrenchBroom-zhCN/build/v2026.2-msvc145-qt6103/app/TrenchBroom/gen-manual/shortcuts.js`

`QT_QPA_PLATFORM=offscreen` 只影响 Qt 平台插件选择；命令没有显式 `WORKING_DIRECTORY`，但全部使用绝对路径。

## 2. 失败进程
B6 日志在 `Generating gen-manual/shortcuts.js` 后输出 `Exit code 0xc0000135`，随后 `MSB8066` 指向 `GenerateManual.vcxproj`。命令链中 cmake 只是 env 启动器；`DumpShortcuts/src/Main.cpp` 静态搜索未发现 `QProcess` / `CreateProcess` / `system()` / `ShellExecute` 等子进程调用，因此返回 `0xc0000135` 的进程为 **`DumpShortcuts.exe` 本身**。

## 3. 静态 DLL 依赖
使用 VS 18 MSVC 14.51 `dumpbin.exe /dependents` 对 `DumpShortcuts.exe` 及其可解析依赖做递归静态检查（仅读 PE 导入表，未启动程序）：
- 直接依赖 24 项全部可解析：Qt6Core/Gui/Widgets/Network/OpenGL/OpenGLWidgets/Svg、freetype、assimp-vc143-mt、FreeImage、tinyxml2、miniz、MSVCP140、VCRUNTIME140/140_1、KERNEL32 与 API Set
- 递归依赖中发现 **17 个具体 DLL 缺失于 DumpShortcuts/Release 且不在当前 PATH / Qt bin / MSVC redist 搜索范围**
- API Set 与 `ext-ms-*` 为系统解析别名，不按磁盘文件存在性判定；`wpaxholder.dll` / `HvsiFileTrust.dll` 为系统可选组件线索，不纳入本故障的根因集合

## 4. 缺失 DLL、预期位置与原因
缺失集合（父依赖 → 缺失项）：
- `freetype.dll` → `brotlidec.dll`、`bz2.dll`、`libpng16.dll`
- `FreeImage.dll` → `libpng16.dll`、`jpeg8.dll`、`tiff.dll`、`openjp2.dll`、`raw.dll`、`libwebp.dll`、`libwebpdecoder.dll`、`libwebpmux.dll`、`Iex-3_3.dll`、`Imath-3_2.dll`、`OpenEXR-3_3.dll`
- `assimp-vc143-mt.dll` → `kubazip.dll`、`minizip.dll`、`poly2tri.dll`、`pugixml.dll`

这 17 个 DLL 均：
- **不存在**于 `DumpShortcuts\Release`
- **存在**于 `TrenchBroom\Release`
- **存在**于 `vcpkg_installed\x64-windows\bin`

Windows 加载器首先按 EXE 所在目录搜索 DLL；DumpShortcuts/Release 只有 17 个 DLL，TrenchBroom/Release 有 52 个。B6 构建日志显示 windeployqt 为 DumpShortcuts 部署了 Qt DLL 与若干直接依赖，但没有把 FreeImage/assimp/freetype 的递归第三方依赖部署到 DumpShortcuts/Release。当前 PATH 不含任一 Release 目录、Qt bin 或 MSVC redist，无法兜底解析。

具体第一个缺失项无法在不启动程序的情况下静态证明；上述 17 项任一缺失均可产生 `0xc0000135`。此点标记 `FIRST_MISSING_DLL_NOT_VERIFIED`，但根因集合已确定。

## 5. 最小修复建议
见 `D0_Minimal_Fix_Proposal.md`。核心：仅为 `DumpShortcuts` 目标增加构建目录内的第三方递归依赖部署，来源用 vcpkg bin；不改源码逻辑、不改正式 TS、不改 PATH、不部署到正式安装目录。

本阶段未执行任何修复。
