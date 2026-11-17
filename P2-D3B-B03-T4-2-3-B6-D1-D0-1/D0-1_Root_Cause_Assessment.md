# D0-1_Root_Cause_Assessment — D1 后仍 0xc0000135 的静态根因评估

## 最终状态：**ROOT_CAUSE_PARTIALLY_IDENTIFIED**

静态证据明确表明 D1 的 17 项部署不构成完整递归依赖闭包：还有 **8 个**第二/三层第三方 DLL 存在于 vcpkg bin、但不存在于 DumpShortcuts/Release，且不在当前 DLL 搜索路径中。它们由其父 DLL 实际导入，任何一个缺失都可产生 `0xc0000135`。但不能在不启动 DumpShortcuts.exe 的前提下证明加载器首先尝试的是哪一个，因此不使用 ROOT_CAUSE_IDENTIFIED。

## 仍需补齐的 8 项
`brotlicommon.dll`、`zlib1.dll`、`IlmThread-3_3.dll`、`OpenEXRCore-3_3.dll`、`deflate.dll`、`libsharpyuv.dll`、`lcms2-2.dll`、`liblzma.dll`

主要导入链：
- `brotlidec.dll` → `brotlicommon.dll`
- `libpng16.dll` / `freetype.dll` / `FreeImage.dll` / `assimp-vc143-mt.dll` / `minizip.dll` → `zlib1.dll`
- `OpenEXR-3_3.dll` → `IlmThread-3_3.dll`、`OpenEXRCore-3_3.dll`
- `OpenEXRCore-3_3.dll` → `deflate.dll`
- `libwebp.dll` → `libsharpyuv.dll`
- `raw.dll` → `lcms2-2.dll`
- `tiff.dll` → `liblzma.dll`

## A–H 分类
| 类别 | 结论 | 支持证据 | 反对证据 | 置信度 |
|---|---|---|---|---|
| A D1 闭包不完整 | **成立** | 8 项必需 DLL 未部署；均在 vcpkg bin | D1 17/17 哈希正确，但只覆盖第一层缺失 | HIGH，静态确认 |
| B 已部署 DLL 的依赖缺失 | **成立** | D1 部署的 OpenEXR/libwebp/raw/tiff/brotlidec 等导入上述 8 项 | 部分父 DLL 可正常工作若其依赖已在 PATH（实际不在） | HIGH，静态确认 |
| C 架构/版本不匹配 | 未成立 | 17 项 x64 且源/目标 SHA 一致；8 项 vcpkg 来源也是 x64 | 未发现版本冲突证据 | LOW |
| D Qt 插件/依赖缺失 | 未成立 | 20 条 Qt DLL/插件审计无缺失导入；offscreen 插件存在 | 未启动验证运行期加载 | LOW |
| E MSVC Runtime 缺失 | 未成立 | msvcp140/vcruntime140/vcruntime140_1 在 System32 与 VC redist 均存在 | 构建进程 PATH 未直接含 redist，但系统目录可解析 | LOW |
| F 项目自有 DLL 缺失 | 未成立 | 未发现项目自有 DLL 依赖缺口 | - | LOW |
| G DLL 搜索目录/相对路径问题 | **可能伴随** | vcpkg bin、Qt bin、VC redist、TrenchBroom/Release 均不在当前 PATH；只有 EXE 目录可兜底 | MSBuild 实际 PATH 未完整快照 | MEDIUM |
| H 其他静态不可解释原因 | 未排除 | 无法静态捕获启动瞬间加载顺序 | 已发现明确依赖缺口 | LOW |

## 具体第一个缺失项
无法静态确定。Windows 加载器按导入表与加载顺序尝试解析，且本轮禁止启动 DumpShortcuts.exe。当前结论是“缺失集合已确定，首个触发项 NOT_VERIFIED”。

## 结论
D1 修正方向正确但不完整。最小后续动作应是在同一 POST_BUILD 中补齐 8 项，随后在单独授权下重新构建；不得修改第二个文件、不得修改 PATH、不得复制系统 DLL。
