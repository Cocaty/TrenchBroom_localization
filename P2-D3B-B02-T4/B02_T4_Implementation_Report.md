# B02_T4_Implementation_Report — Release 增量构建与资源嵌入验证

日期：2026-11-16 23:55 ｜ 仅构建与静态验证；未启动程序、未部署

## 结论：**PASS**

## T4-0/T4-1 基线与配置
Git feature/zh-CN-v2026.2 / HEAD `4c756be1…` / dirty=7；正式 TS `901554891…`（131,100 B）与 T3 QM `f480ae44…`（1,871 B）均与指定基线一致；构建树旧 EXE `9a1a8499…`、旧 QM `a2f5cc1f…`。CMake 配置符合冻结设计（LinguistTools、`qt_add_translations` 绑定 TrenchBroom/TbUiLib/UpdateLib、正式 TS、prefix `/translations`、资源名 `TrenchBroom_zh_CN.qm`），生成器 Visual Studio 18 2026 / x64，Qt 6.10.3 / CMake 4.2.8。

## T4-2 构建命令与结果
```
cmake --build "C:\Users\yoshi\Projects\TrenchBroom-zhCN\build\v2026.2-msvc145-qt6103" --config Release --target TrenchBroom -- -m:1 -v:m
```
exit code **0**；日志 `Evidence/build_log.txt`。CMake 自动调用 lrelease：`Generated 22 translation(s) (22 finished and 0 unfinished)`、`Ignored 540 untranslated source text(s)`；随后重新生成 `qrc_TrenchBroom_translations.cpp`、重编译资源 OBJ、重新链接 EXE；无 shortcuts.js 问题、无人工补救、无警告/错误。

## T4-3/T4-4 产物与嵌入证据链
- 构建 QM：1,871 B，SHA `f480ae44bb495cb84d516d4b1008abc07c71f15587d02e64870797c4bf1745b5` ——**与 T3 独立 QM 完全一致**
- EXE：29,761,536 B，SHA `38d021951ddd59cbef266b4c3c6dce925854c7cdcaceac3d3613d601be89ac0f`，PE Machine 0x8664，mtime 23:55:49（构建前 `9a1a8499…`）
- 证据链：QRC（prefix `/translations` + alias）→ RCC cpp 十六进制数组还原载荷与 QM **逐字节一致** → 资源 OBJ 含完整 QM 字节 → EXE 含 `:/translations/TrenchBroom_zh_CN.qm` 资源路径、QM 魔数及“打开地图”等 UTF-16BE 译文
- **边界**：未从 PE 节直接提取资源二进制做 EXE↔QM 字节级比较；嵌入结论基于上述可追溯构建链，不声称直接的 EXE 内提取字节一致

## T4-5 译文集合
用 Qt 6.10.3 lconvert 回转最终 QM（exit 0）：22 条完成译文；B02 新增 `3e1b6ba4c40e`/`tb::ui::WelcomeWindow`/`Open Map` → **打开地图**；对照 B01-T3 回转，B01 历史 **21/21** 全保留；22/22 按 context/source/translation 核对，无丢失/重复。

## T4-6/T4-7 保护
正式 TS、T3 QM 与报告、T2/T2-R1/B02-D1/PRE、B01 历史证据、原版 Release、日常 INI 与 `AppData\Roaming\TrenchBroom\Preferences.json`、Git 状态全部未变；构建目录 EXE/QM/RCC/OBJ 为本轮**预期更新**，单独标注。未运行 lupdate、未启动程序、未部署、未提交 Git。

## 停止
**本轮完成即停止：未进入 B02-T5，未部署，未做运行期验证。**
