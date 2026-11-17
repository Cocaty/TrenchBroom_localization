# B02_T5_Implementation_Report — B02 独立测试副本运行期验证

日期：2026-11-17 00:02–00:35 ｜ 仅启动独立测试副本，未启动原版 Release，未部署

## 总体结论：**PASS WITH LIMITATIONS**

核心中文运行期功能通过：启动、语言控件、切换与持久化、B02 新增译文显示、切回英文、非法语言值回退均正常；B01 历史 21 条中 **20 条 PASS、1 条 NOT TESTED**（Revert 状态栏描述因宿主面板抢焦点未能稳定采集）。NOT TESTED 未计入 PASS。

## 测试副本与隔离

- 实际启动 EXE：`C:\Users\yoshi\Projects\TrenchBroom-zhCN\test-runs\P2-D3B-B02-T5\app\TrenchBroom.exe`，SHA `38d021951ddd59cbef266b4c3c6dce925854c7cdcaceac3d3613d601be89ac0f`，与 T4 最终 EXE 一致
- 参数 `--portable`；配置位于测试副本 `app\config\Preferences.json`；日常 INI `5062ef85…` 与日常 `AppData\Roaming\TrenchBroom\Preferences.json`（`50705006…`）哈希未变
- 启动 5 次（PID 2328 之前的 22276、23092、23532、24932 及首启），均正常退出，最终进程 0；5 个 stderr 日志全 0 B

## 用例结果（详见 Test_Case_Matrix.csv）

| TC | 结果 | 要点 |
|---|---|---|
| TC-01 English 默认启动 | PASS | Welcome 正常，English，无 QM 错误 |
| TC-02 语言控件 | PASS | Language / English / 简体中文 / "Requires restart after changing"，布局正常 |
| TC-03 切换简体中文 | PASS | 英文重启提示；测试配置写入 `zh_CN` |
| TC-04 重启中文生效 | PASS | “语言”“简体中文”“更改后需要重启”实际显示 |
| **TC-05 B02 新增译文** | **PASS** | Welcome → Browse... 打开的文件对话框标题实际显示 **「打开地图」**，无乱码/截断 |
| TC-06 B01 21 条回归 | PASS WITH LIMITATIONS | 20/21 PASS；Revert 状态栏描述 NOT TESTED |
| TC-07 切回 English | PASS | 中文提示；配置 `en`；重启英文；标题恢复 `Open Map` |
| TC-08 非法语言值 | PASS | `invalid_locale` 下正常启动英文、无崩溃；值被保留未自动纠正 |
| TC-09 退出与隔离 | PASS | 进程 0；原版/构建目录/历史证据/日常配置未变 |

## B01 回归说明
File 菜单 16 条中文、Export 子菜单 2 条（Wavefront OBJ... 保留英文、地图文件...）、地图导出状态栏描述，以及 3 条既有 finished 译文均用本轮测试副本**重新实测**（未沿用旧 PASS）；B01-17 Revert 状态栏描述因宿主面板反复抢占前台，真实悬停无法稳定触发，标记 NOT TESTED，未伪造。

## 保护与边界
12 项保护对象开始/结束哈希一致（正式 TS、T4 EXE/QM、测试副本 EXE、原版 Release、日常 INI/Preferences、T4/T3/T2/B01-T5-R1 证据清单）；Git HEAD/dirty 未变。未修改 TS/源码/CMake/QM，未构建、未部署、未提交 Git。

## 停止
**本轮停止：未进入正式部署、未进入 B03。等待用户审查。**
