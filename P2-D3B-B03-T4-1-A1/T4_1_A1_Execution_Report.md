# T4_1_A1_Execution_Report — 构建前哈希冲突与构建副产物补充审计

## 结论：**PASS WITH LIMITATIONS**

开始 2026-11-17 21:01:49 +0800；结束见最终快照归档时点。A1 目录创建前不存在；全程只读，未重建、未复制、未启动、未修改任何项目文件或 T4-1 原始报告。Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=7。

## 1. 哈希冲突（已解决）
- `38d021951ddd59cbef266b4c3c6dce925854c7cdcaceac3d3613d601be89ac0f`（297,615,36 B）：T4-1 Start Snapshot 记录为构建目录 EXE 的构建前哈希；当前仍存在于 `test-runs\P2-D3B-B02-T5\app\TrenchBroom.exe`，也是 B02-T4 构建 EXE。**这是正确的构建前基线。**
- `9a1a84991c61d1d108477ab7f193c72d6336e1ed6c197d510339043d8b2c46d5`（297,615,36 B）：当前仍存在于 `test-runs\P2-D3B-B01-T5\app\TrenchBroom.exe`；来源为 B01-T5 测试副本清单。被误抄入 `T4_1_Baseline_Audit.csv` 的构建前字段。
- 两者大小相同但**不是同一物理文件、不是同一时间点**；T4-1 Baseline_Audit.csv 的构建前值错误，Start Snapshot/Protected State 的值正确。
- 构建后 EXE 当前为 `268df3904f16dc2e329542397531be4ef35f530cebde07cd720753707fca7212`。当前时点哈希不反推历史状态。

## 2. 构建副产物
依据完整构建日志建立 93 条清单（`T4_1_A1_Build_Artifact_Inventory.csv`）：

| 动作 | 数量 |
|---|---:|
| LINK | 12 |
| UPDATE | 2 |
| CREATE | 32 |
| CHECK_ONLY | 47 |
| EXPECTED_BUILD_OUTPUT | 93 |
| UNEXPECTED / UNRESOLVED | 0 / 0 |

实际创建/更新：链接 12 个 lib/EXE 输出（含 TrenchBroom.exe）、更新 `TrenchBroom_zh_CN.qm` 与 rcc 生成 cpp、创建 32 个 windeployqt Qt 自带翻译 QM。Qt DLL/插件在日志中均为 `up to date`，不判定为变化。所有副产物均定位在指定 build 目录。

## 3. 写入范围与保护
构建目录发生预期变化；源码树、正式 TS、QRC、CMake、Main.cpp、ViewPreferencePane、T3 QM、原版 Release 与 Git 状态均无变化（保护审计 12/12）。用户配置目录与 Documents 未建立前后快照，标记 **NOT_VERIFIED**；无写入证据但不能证明未变。构建日志中所有解析到的 POST_BUILD 路径均位于 build 目录。

## 4. 对 T4-2 的影响
无阻断风险。T4-2 应使用 build 目录 `Release` 下的 EXE 及完整 DLL/插件布局，在独立 `test-runs\` 副本与 portable 配置下运行；不得仅使用 T3 QM 或复制单一 EXE。详见 `T4_1_A1_T4_2_Readiness_Assessment.md`。

## 5. 归档
本阶段新增 9 个报告/证据文件；SHA256SUMS 覆盖 8 项（清单自身不自列）并逐项通过。未上传 GitHub，无可验证链接。未重新构建、未复制文件、未启动程序、未进入 T4-2。
