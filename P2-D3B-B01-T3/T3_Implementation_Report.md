# T3_Implementation_Report — B01 翻译编译与 QM 静态验证总结

日期：2026-11-16 22:19–22:45 ｜ 本轮仅验证 `TrenchBroom_zh_CN.ts → TrenchBroom_zh_CN.qm`，未构建主程序、未启动 TrenchBroom

## 一、工具链核验（T3-2）

- 路径：`C:\Users\yoshi\Tools\Qt\6.10.3\6.10.3\msvc2022_64\bin\lrelease.exe`（实际存在）
- 版本命令输出：`lrelease version 6.10.3` ✅
- 大小 341,816 B；mtime 2026-03-30 19:54:41；SHA-256 `c59d5a5f9cf51cef2fbee80bcd22cf53b7453943bcf520b39d2e768fd639d8ee`
- 未使用 PATH 中来源不明的 lrelease；未安装/升级 Qt；未修改系统 PATH/注册表

## 二、编译（T3-3）

```
lrelease <T2 Evidence/TS_after_T2.ts> -qm <T3/Output/TrenchBroom_zh_CN.qm>
退出码: 0
输出: Generated 21 translation(s) (21 finished and 0 unfinished)
      Ignored 541 untranslated source text(s)
```
- 输入 TS SHA 编译前后均为 `6582a382…`，未被修改
- 输出 QM：1,805 B，SHA `a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66`
- 未使用 `-removeidentical` / `-nounfinished` / `-compress` 等额外选项
- **警告：无**（日志逐行已保存 `T3_lrelease_Log.txt`）
- 21 = 18 条 B01 新译文 + 3 条既有 finished；541 unfinished 被忽略属正常行为（非翻译丢失、也非已完成）

## 三、QM 验证（T3-4）

### 结构
16 字节魔数匹配、第 17 字节 0xa7 为独立 Language 标签；Language(5B)/Hashes(168B)/Messages(1601B) 三块齐全，逐块长度不越界，完整消耗至 EOF 1805/1805（详见 T3_QM_Structure_Report.md）。

### 18 条译文
- 先尝试编译独立 QTranslator 检查工具（`T3_QM_Verifier.cpp`），MSVC 因缺少 `/Zc:__cplusplus` 报 C1189 编译失败（已记录，未重试同类操作；不改项目源码/正式构建目录）
- 改用**同一 Qt 6.10.3 工具链的官方 `lconvert.exe`** 把 QM 离线回转 TS（`Output/QM_roundtrip.ts`，退出码 0、无输出），得到 21 条消息（全部完成、context 与 source 保留）
- 按稳定 ID 逐条比对 `TS_after_T2.ts` 的正式译文：**18/18 PASS**，含 3 条既有 finished 亦无异常（详见 `T3_QM_Translation_Verification.csv`）
- 该路径使用 Qt Linguist 的 QM 读取实现，属离线 QM 内容验证；未启动 TrenchBroom，未做运行期 GUI 验证

## 四、边界

正式 TS、其他 TS、C++/CMake/资源、T2 交付物、正式构建目录中的 QM、原版 Release、用户配置均未修改；未运行 lupdate；未构建主程序；未启动/部署；未提交 Git。所有编译与检查产物均在 `reports\P2-D3B-B01-T3\`。

## 五、结论

**PASS**：输入哈希正确、工具版本确认、编译成功、QM 结构通过、18/18 目标译文与 TS 一致、无未解释警告、报告与哈希清单齐全。

未解决事项：独立 QTranslator C++ 工具编译未成功（改用官方 lconvert 离线回转完成等价内容验证）；本轮不含运行期验证。
