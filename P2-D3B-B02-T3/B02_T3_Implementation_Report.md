# B02_T3_Implementation_Report — 翻译编译与 QM 静态验证

日期：2026-11-16 23:47 ｜ 仅翻译编译与 QM 静态验证，未构建主程序、未启动程序

## 结论：**PASS**

## T3-0/T3-1 输入基线
- Git：feature/zh-CN-v2026.2，HEAD `4c756be1…`，dirty=7
- 正式 TS：131,100 B，SHA `901554891f322ed833385b84eca60fe87a5b92fb5c27849161393fe928abe773`，mtime 23:36:59；与指定基线完全一致
- XML 解析成功，language=`zh_CN`，UTF-8 无 BOM、声明与 DOCTYPE 正常；85 context / 562 message / 22 finished / 540 unfinished / 0 obsolete / 0 numerusform
- B02 目标唯一命中：`3e1b6ba4c40e` / `tb::ui::WelcomeWindow` / `Open Map` / WelcomeWindow.cpp:140 / `打开地图` / finished
- 工具：Qt 6.10.3 `lrelease.exe`（`c59d5a5f…`）与 `lconvert.exe`（`707af8e9…`）实际存在，`lrelease -version` 输出 6.10.3

## T3-3 编译
命令行（工作目录无关，显式输入输出）：
```
lrelease.exe <.../Work/TrenchBroom_zh_CN.ts> -qm <.../Work/TrenchBroom_zh_CN.qm>
```
exit code **0**；日志：`Generated 22 translation(s) (22 finished and 0 unfinished)`、`Ignored 540 untranslated source text(s)`；无警告/错误；未使用额外选项。
QM：1,871 B，SHA `f480ae44bb495cb84d516d4b1008abc07c71f15587d02e64870797c4bf1745b5`。

## T3-4 QM 顶层结构
16 字节魔数准确；第 17 字节 `0xA7` 为 Language 块标签（非魔数）；Language(5B) / Hashes(176B) / Messages(1659B) 块齐全，完整到达 EOF 1871/1871，无截断/越界/额外字节。**检查器仅验证顶层块结构，完整 QM 语义验证由 lconvert 回转承担。**

## T3-5/T3-6 回转与翻译集合
`lconvert.exe -i <QM> -o <Work/TrenchBroom_zh_CN_roundtrip.ts>`，exit code **0**，输出 3,338 B / SHA `5f0c2bb2…`，XML 解析成功。
- 回转共 **22** 条翻译，全部为完成状态
- B02 新增：`tb::ui::WelcomeWindow` / `Open Map` → **打开地图** ✅
- 对照 B01-T3 已验证回转结果，B01 历史 **21/21** 条全部保留且逐条一致 ✅
- 22/22 与正式 TS finished 集合按 context/source/translation 语义完全一致；无丢失、重复或意外新增；unfinished 未计入

## T3-7/T3-8 保护
正式 TS、T2 两份 TS 证据及报告、T2-R1 报告、构建目录 EXE/QM、原版 Release、日常配置、B01/B02 历史证据清单共 16 项开始/结束哈希一致；Git HEAD/分支/dirty 未变。未修改正式构建目录 QM，未运行 lupdate、未构建、未启动、未部署。

## 停止
**本轮完成即停止：未进入 B02-T4/T5，未构建主程序。等待另行授权。**
