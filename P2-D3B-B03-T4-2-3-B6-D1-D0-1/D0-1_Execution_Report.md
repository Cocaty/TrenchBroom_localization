# D0-1_Execution_Report — DumpShortcuts 递归 DLL 依赖闭包只读复核

## 最终状态：**ROOT_CAUSE_PARTIALLY_IDENTIFIED**

D1 的 17 项部署已验证完整且哈希正确，但不是完整递归闭包；仍有 8 个第二/三层 DLL 缺失于 DumpShortcuts/Release，足以解释 `0xc0000135`。具体第一个缺失项无法在不启动程序的情况下静态证明。

## 基线
Git `4c756be1…`、dirty=13，新增 dirty 文件仍为 D1 授权的 `app/DumpShortcuts/CMakeLists.txt`。正式 TS `f81162b3…`、B5 QM `4b213ce5…`、DumpShortcuts.exe `118b653…`、构建 EXE 仍为旧 `268df390…`。开始快照 51 项。

## 方法
使用 VS 18 MSVC 14.51 `dumpbin.exe /imports` 与 `/dependents` 对根 EXE 及所有非系统依赖做递归静态分析；vcpkg 路径从 CMakeCache 的 `VCPKG_INSTALLED_DIR` / `VCPKG_TARGET_TRIPLET` 实际读取（x64-windows），未猜测。脚本 `Evidence/analyze_pe_deps.py` 可复现。未启动任何 EXE、未构建、未复制/修改 DLL。

## 依赖图
生成 444 条依赖边/节点记录，分类：
- WINDOWS_APISET 197，WINDOWS_SYSTEM 146
- DEPLOYED_IN_APP_DIR 51，VCPKG_THIRDPARTY 22，QT_LIBRARY 28
- 普通/延迟导入字段保留在 `D0-1_PE_Dependency_Graph.csv`
- 所有可解析节点均记录路径、SHA256、架构、所属目录与是否需要应用目录部署

## D1 17 项复核
17/17 在 DumpShortcuts/Release 存在，源/目标 SHA256 一致、PE 架构一致；但它们的递归依赖并未全部部署。

## 第二/三层缺口
确认仍有 8 个必需 DLL 缺失于 DumpShortcuts/Release，但存在于 vcpkg bin：
`brotlicommon.dll`、`zlib1.dll`、`IlmThread-3_3.dll`、`OpenEXRCore-3_3.dll`、`deflate.dll`、`libsharpyuv.dll`、`lcms2-2.dll`、`liblzma.dll`

## Qt / Runtime
Qt DLL + 插件共 20 条审计无缺失导入；`platforms/qoffscreen.dll` 存在，符合 `QT_QPA_PLATFORM=offscreen` 的搜索位置。MSVCP140/VCRUNTIME140/VCRUNTIME140_1 在 System32 与 VC redist 均存在。当前 PATH 不含 vcpkg bin、Qt bin、VC redist、任一 Release 目录；因此 vcpkg 中的 DLL 不会被加载器自动找到。

## 根因与建议
根因分类 A+B（D1 闭包不完整、已部署 DLL 的依赖缺失）置信度 HIGH；G（搜索目录）可能伴随。具体首个失败项静态不可证明。最小修复建议：在同一 CMake POST_BUILD 中补 8 项，详见 `D0-1_Minimal_Fix_Proposal.md`。本轮未执行。

## 归档
`reports\P2-D3B-B03-T4-2-3-B6-D1-D0-1\` 含执行报告、根因、修复建议、基线、依赖图、D1 17 审计、二三层级审计、Qt/路径/保护审计、前后快照、分析脚本与 SHA256SUMS。保护对象无变化；Documents/用户配置为有限或 NOT_VERIFIED。未上传 GitHub，无可验证链接。等待授权，不进入任何后续阶段。
