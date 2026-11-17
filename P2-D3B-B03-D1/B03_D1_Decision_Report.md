# B03_D1_Decision_Report — RA-B03 20 条正式译文决策（候选）

日期：2026-11-17 12:50 ｜ **只做决策材料，未写入 TS**

## 结论：**PASS WITH LIMITATIONS**

20/20 目标全部形成推荐译文与备选/拒绝理由；PRE 的两项遗漏已修正；源码争议点已复核。**但用户在本轮任务书中明确说明这些是推荐候选而非确认译文**，因此 20/20 状态均为 `PROPOSED_PENDING_USER_CONFIRMATION`，0 条 `FINAL_FROZEN`。PASS 仅表示决策材料完整，不表示译文已正式冻结。

## 基线与范围
- Git：feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7（既知状态，未清理）
- 正式 TS：`901554891…`，131,100 B，85/562/22/540/0，与 PRE/B02-T5 一致，未修改
- 权威批次：Revised_Batches.csv 中 RA-B03 的 20 个 ID，与 PRE 清单顺序与内容完全一致
- 全部 20 条 TS 定位仍唯一、unfinished

## PRE 修正落实
1. **修正 A**：`0ee72f3c8645`（Texture Paths）与 `10b21b3fc756`（tooltip）作为同一术语决策组，统一为“纹理路径 / 生成的材质文件中纹理路径”。PRE 将 tooltip 单列 READY 的口径已纠正。
2. **修正 B**：PRE 声称 B02-D1 冻结了 `game path → 游戏路径`，证据不成立。B02-D1 实际只冻结 `Open Map → 打开地图`。本轮以源码 `PathType::GameRelative` 与 `ObjMtlPathMode::RelativeToGamePath` 共用 `gamePath` 基准为依据，推荐两条统一为“相对于游戏目录”，并将“游戏路径”列为备选。
3. 决策前口径改为 11 READY / 9 需术语确认（原 PRE 13/7），但因本轮所有译文仍待用户确认，最终状态不按 READY 直接冻结。
4. 源码修正：`Relative to export path` 的实际基准为 `exportPath.parent_path()`（导出文件所在目录），因此本轮将“相对于导出目录”作为修正推荐，“相对于导出路径”列为备选待用户确认。

## 20 条推荐候选速览
| # | ID | Source | 推荐译文 |
|---|---|---|---|
| 1 | cfde892c46df | AboutDialog HTML 贡献者名单 | 完整中文版（见下），保留 HTML/人名/产品名 |
| 2 | f9081511b752 | Path Type | 路径类型 |
| 3 | df4ef91af93a | You can convert a path... | 可以将路径转换为相对于某个参考路径的形式，也可以保留为绝对路径。使用相对路径有助于与他人协作编辑地图。 |
| 4 | 8c9ed2e8de12 | Absolute | 绝对路径 |
| 5 | 6a5208c30cca | Relative to map file | 相对于地图文件所在目录 |
| 6 | dbbba8b54bd0 | Relative to application executable | 相对于应用程序目录 |
| 7 | 3a29ad146ceb | Relative to game directory | 相对于游戏目录 |
| 8 | 2c01921052f7 | Choose Path Type | 选择路径类型 |
| 9 | 8e40860a52a1 | Crash | 程序崩溃 |
| 10 | f0f928f057b7 | TrenchBroom has crashed... | TrenchBroom 已崩溃，但已成功保存崩溃报告、日志文件以及当前地图状态，文件位置如下。\n\n请创建一个问题报告，并上传这三个文件。 |
| 11 | 444a30e5e793 | Report | 报告问题 |
| 12 | 5a27052291cb | Autodetect | 自动检测 |
| 13 | ee439e50a835 | Export Wavefront OBJ | 导出 Wavefront OBJ |
| 14 | 0011be948dd6 | Export Path | 导出路径 |
| 15 | 2915922a2166 | Enter a path or click to browse | 输入路径，或点击“浏览...”进行选择 |
| 16 | 0ee72f3c8645 | Texture Paths | 纹理路径 |
| 17 | 10b21b3fc756 | Controls how the texture paths... | 控制生成的材质文件中纹理路径的计算方式。 |
| 18 | 013b4028d792 | Relative to game path | 相对于游戏目录 |
| 19 | 26fd3ad9ed81 | Relative to export path | 相对于导出目录（源码修正推荐） |
| 20 | eed1f27c4948 | Export Wavefront OBJ file | 导出 Wavefront OBJ 文件 |

完整 HTML 候选（ID `cfde892c46df`，严格保留 `<br />`/`<b>`、人名、URL、产品名、顺序与空行）：

```html
github.com/TrenchBroom<br />
<br />
<b>开发者</b><br />
<br />
Kristian Duske<br />
Eric Wasylishen<br />
<br />
<b>贡献者</b><br />
20kdc,
aapokaapo,
Amara M. Kilic,
Ari Vuollet,
bazhenovc,
chronicol,
Corey Jones,
iOrange,
Jonas Lund,
Jonathan Linat,
Josh Palmer,
mankeli,
Matthew Borkowski,
mittorn,
negke,
neogeographica,
Philipp Nahratow,
rebb,
Rohit Nirmal,
Scampie,
xaGe,
Yuki Raven
<br /><br />
<b>第三方库、工具与资源</b><br />
Qt（跨平台 GUI 库）<br />
FreeType（字体渲染库）<br />
FreeImage（图像加载与处理库）<br />
tinyxml2（XML 解析库）<br />
miniz（归档库）<br />
Assimp（资源导入库）<br />
Catch 2（C++ 测试框架）<br />
StackWalker（C++ 调用栈分析工具）<br />
CMake（跨平台构建工具）<br />
Vcpkg（C/C++ 依赖管理工具）<br />
Pandoc（通用文档转换工具）<br />
Source Sans Pro（字体）<br />
Font Awesome 5 Free（图标集）<br />
```

## 术语组决策
见 `B03_D1_Terminology_Glossary.csv`（11 组）。要点：相对路径/绝对路径 structurally 统一；“相对于……”用于单选项；地图文件目录、应用程序目录、游戏目录、导出目录分别保留不同基准；Texture Paths=纹理路径且 tooltip 同步；Wavefront OBJ 保留英文；crash report / issue report / Report 按钮三者区分。

## 用户确认与冻结状态
完整候选 20；等待用户确认 20；需修订 0；真正冻结 0。历史可继承术语（Wavefront OBJ、Material→材质、B02 的 Open Map→打开地图）仅作为证据来源，不构成 B03 译文确认。

## 范围外发现
CrashDialog 的 `Crash Report/Info/Reason/Version/Build/Files/Map File/Log File` 与 ObjExportDialog 的 `Export/Browse.../Path` 为硬编码英文，不在 20 条目标内；仅记录于 `B03_D1_OutOfScope_Hardcoded_Strings.md`。

## 停止与建议
**未写入 TS，未运行翻译工具，未构建/启动/部署。** 下一步：请用户逐条或按术语组确认；获得明确授权后再进入 B03-T2 写入。
