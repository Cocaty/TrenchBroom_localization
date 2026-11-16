# T5_Implementation_Report — B01 受控运行期验证总结

日期：2026-11-16 22:37–23:00 ｜ 仅启动独立测试副本，未启动原版 Release

## 总体结论：**PASS WITH LIMITATIONS**

已满足：测试副本建立与哈希一致、正常启动/退出（3 次）、英文默认状态、QTranslator 中文资源实际加载、zh_CN 与 en 切换及重启持久化、全部保护边界、证据归档。
未满足（限制）：**B01 18 条正式译文的 UI 显示 18/18 为 NOT TESTED**——File 菜单需地图文档，而创建/打开地图需游戏配置或真实地图文件，均在本轮禁止范围内；未伪造结果。

## 实际启动的 EXE
`C:\Users\yoshi\Projects\TrenchBroom-zhCN\test-runs\P2-D3B-B01-T5\app\TrenchBroom.exe`（与 T4 产物 SHA 一致，29,761,536 B）

## 启动次数与退出
共 **3 次**（PID 2260 / 23996 / 29880），均 `--portable`；每次通过 CloseMainWindow （部分实例需二次/三次关闭残留 Welcome 窗口）正常退出，最终 TrenchBroom 进程数 **0**；stderr 日志 0 B，无崩溃与 Qt 警告。

## QTranslator 实际加载
功能级证据：重启后“语言”“简体中文”“更改后需要重启”及中文重启提示“语言更改将在重启 TrenchBroom 后生效。”实际显示；这些文本来自既有 3 条 finished 译文，可证明中文 QM 被 QTranslator 加载并生效。**B01 18 条本身未实测**（见 T5_Chinese_Runtime_Verification.csv 全部 NOT TESTED）。

## 语言切换与持久化
无语言键→选简体中文（英文提示）→配置 `zh_CN`→重启中文；中文状态选 English（中文提示）→配置 `en`→重启英文；第三次启动配置仍 `en`。三态（即时选择/写盘/重启加载）分别记录，未混同。

## 未测试项目
- B01 18 条 UI 显示（File 菜单与 tooltip）：无游戏配置、禁止打开真实地图，未触达
- 中文 tooltip 截图：目标控件无 tooltip 或位于不可触达菜单，未采集到
- 运行期 QTranslator load() 内部返回值：Release 无该日志，以译文显示作功能级证据

## 保护核验
原版 Release、构建树 EXE/QM、TS、Git、日常 INI 与日常数据目录、T2/T3/T4 证据哈希全部未变；Documents 未触碰；未部署、未构建、未提交 Git。

## 证据与交付
报告目录 `reports\P2-D3B-B01-T5\`：10 份报告 + Evidence（13 张真实运行截图、测试配置副本、stderr 日志）+ 测试副本清单 CSV；SHA256SUMS 从最终目录枚举生成、排除自身，逐项校验结果见下。

**T5 结束，立即停止：不进入 B02、不改 TS、不运行 lupdate/lrelease、不重建、不部署、不提交。等待用户下一步授权。**
