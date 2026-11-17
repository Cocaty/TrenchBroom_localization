# B5_Execution_Report — QM 重新编译与静态验证

## 结论：**PASS**。B6 准备度：**READY_FOR_B6**。

## B5-0 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=12。正式 TS `f81162b383364c9a4a12db4490df910d4555d74ead0acc9f1b414dfc3f9fbfe0`，134,278 B，85 Context / 571 Message / 51 finished / 520 unfinished。B4 备份 `f021e509…`/132,589 B。lrelease/lconvert 均为 Qt 6.10.3 已核验工具。开始快照 17 项。

## B5-1 B4 写入独立复核（前置门槛 PASS）
使用 `Evidence/verify_b4_ts.py` 的可复现算法：对原始 XML `<message>` 块取 Counter 多重集，避免 Source 重复误配。
- 备份原有块 562，当前块 571
- 新增块 9，缺失块 0，原有块变化 0
- 九条新增菜单消息 9/9 正确且唯一、finished
- 39 条历史冻结译文 39/39 PASS
- `tb::ui::AppController/Open Map` 原始 XML 块与备份一致，仍 unfinished、译文为空，未接受 same-text heuristic
门槛全部通过后才执行 QM 编译。

## B5-2/3 lrelease 与 QM 静态
lrelease 命令与工作目录见 `B5_lrelease_Command.txt`；退出码 0，stdout：`Generated 51 translation(s) (51 finished and 0 unfinished)`，stderr 空。新 QM：`Artifacts/TrenchBroom_zh_CN.qm`，7,035 B，SHA `4b213ce5b33639069b87f435dddce6ba9fae54e552f19cb02a231c27ecd926ab`；QM 魔数 `3cb86418caef9c95cd211cbf60a1bddd` 有效。

## B5-4 lconvert 回转
lconvert 退出码 0，回转 TS 10,094 B，SHA `2683ccbd…`。正式 TS 51 条 finished 与回转 TS **51/51** 在 Context/Source/Translation/numerusform 上逐字一致；其中历史 39 条 + B4 新增 9 条专项 **48/48 PASS**；AboutDialog HTML 与其他 3 条历史 finished 也一致。unfinished 节点未要求保留，未误判为失败。

## B5-5 保护
正式 TS、B4 备份、五个源码、QRC、CMake、Main.cpp、原构建 EXE/QM、测试副本 EXE/Preferences、原版 Release 与 Git 状态均与开始快照一致；Git dirty 仍为 12。新 QM 仅存在于 B5 Artifacts。未运行 lupdate、未构建 EXE、未启动程序、未部署。

## 归档
`reports\P2-D3B-B03-T4-2-3-B5\` 含报告、可复现脚本、四份 B4 复核 CSV、工具/命令/输出、QM 与回转 TS、静态/51/48 审计、保护审计、前后快照与 SHA256SUMS。清单覆盖 22 项、清单不自列、独立复算全部通过。未上传 GitHub，无可验证链接。等待用户与 ChatGPT 审查，不进入 B6。
