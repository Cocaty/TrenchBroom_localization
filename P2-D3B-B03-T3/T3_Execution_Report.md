# T3_Execution_Report — B03 Qt 翻译编译与 QM 静态验证

## 结论：**PASS**

开始 2026-11-17 20:35:05 +0800；结束 2026-11-17 20:37 +0800（以最终快照/SHA 归档时点为准）。

## T3-0 基线
T3 报告目录原先不存在。正式 TS `f021e509cf9a8679eeda64624df0f5474335c0872f73940e1d48ef77447a261a`，132,589 B，85 Context / 562 Message / 42 finished / 520 unfinished，与 T2 基线一致；Git feature/zh-CN-v2026.2 / `4c756be1…` / dirty=7。开始快照 9 项覆盖正式 TS、源码/CMake、QRC、U3 矩阵、T2 报告、Qt 工具与原版 Release。

## T3-1 工具链
- `C:\Users\yoshi\tools\Qt\6.10.3\6.10.3\msvc2022_64\bin\lrelease.exe`，341,816 B，SHA `c59d5a5f…`，`-version` 输出 `6.10.3`
- 同目录 `lconvert.exe`，325,432 B，SHA `707af8e9…`；与 B02-T3 记录一致。`lconvert` 不支持 `-version` 输出，工具身份按真实路径 + SHA + B02-T3 记录确认
- 未下载、安装、升级或替换工具

## T3-2 编译
命令：`lrelease.exe <正式TS> -qm <T3/Artifacts/TrenchBroom_zh_CN.qm>`，与 B02-T3 默认策略一致，无过滤参数。退出码 0；QM 6,631 B，SHA `707011a3216511d051b07d0dba249af6d834e6795a447a4f09611c6a9bd2102c`。完整命令、开始/结束时间、stdout/stderr 见 `T3_Lrelease_Log.txt`。QM 仅写入本阶段 Artifacts 目录。

## T3-3 QM 静态验证
QM 魔数 `3cb86418caef9c95cd211cbf60a1bddd` 有效，文件非空。`lconvert.exe -i QM -o Artifacts\TrenchBroom_zh_CN_roundtrip.ts` 退出码 0；回转 TS 9,177 B，XML 解析成功，8 Context / 42 message。正式 TS 的 42 条 finished 与回转结果在 Context+Source+Translation 上 **42/42 完全一致**。ID/location/comment 等不作为 QM 存储字段比较，标记为不适用。

## T3-4 39 条目标译文
B01 18 条（来自 B01-T5-R1 UI 清单）、B02 1 条（`Open Map → 打开地图`）、B03 20 条（U3 冻结矩阵）共 **39 条**，均使用 Context+Source 联合定位，并记录导出 Message ID。正式 TS 中 39/39 finished 且译文一致；QM 回转中 39/39 存在且译文完全一致。另单独记录最初已有的 3 条 finished 消息（“语言”“更改后需要重启”“语言更改将在重启 TrenchBroom 后生效。”），未计入 39 条用户确认目标。详见 `T3_Completed_Translation_Audit.csv` 与 `T3_Original_Finished_Audit.csv`。

## T3-5 保护收尾
正式 TS、源码、CMake、实际 QRC、原版 Release、工具哈希与开始快照一致；Git HEAD/dirty 未变。正式 QM 资源目录、安装目录未被写入；未修改其他 TS。

## 未执行项目与原因
未运行 lupdate、未生成正式资源 QM、未构建、未启动 TrenchBroom/游戏、未部署、未修改 Git、未上传 GitHub、未进入 T4 —— 均不在本阶段授权范围。

## 归档
本阶段新增报告/证据/QM/回转 TS 共 14 个文件；SHA256SUMS 覆盖其中 13 项（清单自身不自列）并逐项校验通过。

**本阶段 concludes PASS；完成即停止，等待用户与 ChatGPT 独立审查。QM 编译成功不代表运行期汉化已验证。**
