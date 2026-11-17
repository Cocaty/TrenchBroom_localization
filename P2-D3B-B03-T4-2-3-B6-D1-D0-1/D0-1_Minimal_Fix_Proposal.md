# D0-1_Minimal_Fix_Proposal — 补齐递归依赖闭包

## 推荐方案（未执行）
继续沿用 D1 已授权并已修改的同一文件 `app/DumpShortcuts/CMakeLists.txt`，在既有 Windows POST_BUILD 块中再补 8 条 `cmake -E copy_if_different`：

`brotlicommon.dll`、`zlib1.dll`、`IlmThread-3_3.dll`、`OpenEXRCore-3_3.dll`、`deflate.dll`、`libsharpyuv.dll`、`lcms2-2.dll`、`liblzma.dll`

来源仍为 `${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin`，目标仍为 `$<TARGET_FILE_DIR:DumpShortcuts>`。

## 修改范围与风险
- 预计修改文件：仅 `app/DumpShortcuts/CMakeLists.txt`（已获 D1 修改授权；若再次实施仍需用户单独授权）
- 预计新增命令：8 条复制命令
- 不修改 PATH、不修改系统运行库、不修改源码逻辑、不修改正式 TS/QM
- 风险：若仍有未识别的递归缺口，构建会继续失败；但本轮已重建完整闭包，8 项是静态证据确认的剩余集合
- 不复制：系统 DLL、API Set、MSVC Runtime、Qt 插件（Qt DLL/插件检查无缺失导入）

## 验证建议（授权后）
1. 在同目录重新构建，确认 GenerateManual 退出 0、无 `0xc0000135`
2. 检查 25 项（17+8）DLL 均在 DumpShortcuts/Release，SHA 与 vcpkg 一致
3. 重新执行 B6 原定资源嵌入验证
4. 若仍失败，停止并做新的只读定位，不再扩大复制范围

本轮未执行任何修复。
