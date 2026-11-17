# B6_Execution_Report — 受控 Release 构建与 QM 资源嵌入验证

## 结论：**FAIL**。B7 准备度：**NOT_READY**。

B6-0 全部门槛通过，但受控 Release 构建在 GenerateManual 自定义步骤失败；没有生成新 EXE，未能进行资源嵌入验证。本阶段未修改源码、未部署、未启动程序。

## B6-0 基线（全部 PASS）
- Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=12
- 正式 TS `f81162b3…`/134,278 B，85/571/51/520
- B4 备份 `f021e509…`；B4 原始消息块比对：562 原有、571 当前、新增 9、缺失 0、原有块变化 0；51 finished 与 B5 回转一致
- B5 QM `4b213ce5…`/7,035 B，魔数有效；B5 回转 TS 51 finished、可解析
- B2 五源码 16/16 设计检查 PASS：displayName、空值回退、九处 QObject::tr、Toolbar/ActionMenu/ActionManager 初始化点、内部英文 name 保护
- 构建目录指向本工作区，Qt 6.10.3 / CMake 4.2.8 / VS18 2026 x64；既有 EXE `268df390…`、既有 QM `707011a3…`
- 开始快照 25 项含用户配置只读范围

## B6-1 构建结果
命令：`cmake.exe --build <build> --config Release --target TrenchBroom -- -m:1 -v:m`，完整日志 `B6_Build_Log.txt`。开始约 23:20，结束 23:21:15，**退出码 1**。

失败点：
- `Generating gen-manual/shortcuts.js`
- `Exit code 0xc0000135`（STATUS_DLL_NOT_FOUND）
- `error MSB8066`：GenerateManual.vcxproj 自定义生成退出码 1

构建目录 EXE 与 QM 哈希保持不变，说明没有产生可验证的新产物。按授权未重试、未改 CMake/源码、未改工具链。

## B6-2 资源嵌入验证
**NOT VERIFIED / FAIL**：没有新 EXE，无法检查 `:/translations/TrenchBroom_zh_CN.qm`，无法提取 embedded QM，也无法进行 B5 QM / 构建目录 QM / 提取 QM 的 A/B/C 字节比较。B5 QM 与 B5 回转保持原样；B6 未生成 embedded QM。九条菜单翻译的 EXE 内静态检查亦 NOT_VERIFIED。

## B6-3 保护状态
正式 TS、B4 备份、B5 QM/回转、五个源码、QRC/CMake/Main.cpp、原构建 EXE/QM、测试副本、Preferences、用户配置范围与原版 Release 均无变化（保护审计中 Documents 全量标记 NOT_VERIFIED，仅作项目相关目录有限核查）；Git HEAD 未变，dirty 仍为 12。构建目录变化限于授权构建尝试，未删除或覆盖历史产物。

## 归档与停止
`reports\P2-D3B-B03-T4-2-3-B6\` 含执行报告、B7 评估、基线/源码/消息/QM/构建配置/执行/产物/资源/菜单/保护审计、前后快照、构建日志与 SHA256SUMS。未上传 GitHub，无可验证链接。未启动程序、未部署、未进入 B7。等待用户与 ChatGPT 审查并决定构建环境处理方式。
