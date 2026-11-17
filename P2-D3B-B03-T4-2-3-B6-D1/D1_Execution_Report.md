# D1_Execution_Report — GenerateManual 递归 DLL 部署最小修正与构建恢复

## 结论：**B6_FAILED**

唯一授权的 CMake 修正已正确实施并验证生效，但 Release 构建仍因 GenerateManual / shortcuts.js 自定义步骤失败而退出 1；未完成 B6 原定 QM 资源嵌入验证。未启动 GUI、未部署、未修改第二个文件。

## D1-0 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=12；正式 TS `f81162b3…`、B5 QM `4b213ce5…` 均符合基线。DumpShortcuts/CMakeLists.txt 原 SHA `90a45d05…` 已备份。D0 的 17 个候选 DLL 全部复核通过：vcpkg 来源存在、x64、SHA 记录完整，DumpShortcuts/Release 原先缺失，TrenchBroom/Release 可用；未发现需要纳入的额外文件。

## D1-1 唯一文件修正
仅修改 `app/DumpShortcuts/CMakeLists.txt`：在既有 Windows POST_BUILD 块内新增 17 条 `cmake -E copy_if_different`，来源 `${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin`，目标 `$<TARGET_FILE_DIR:DumpShortcuts>`。未改原有直接依赖复制、windeployqt、PATH、其他源码/CMake。修改后 Git dirty 13，新增项即该授权文件。完整 diff 见 `D1_CMake_Diff_Audit.md`。

## D1-2/3 构建与 GenerateManual
命令：`cmake --build <build> --config Release --target TrenchBroom -- -m:1 -v:m`；开始约 23:37，结束 23:38:28，**退出码 1**。

- 17/17 DLL 已在构建后复制到 DumpShortcuts/Release，SHA 与 vcpkg 来源一致
- 构建日志显示 DumpShortcuts.exe 重建与 windeployqt 完成
- `shortcuts.js` 存在 25,907 B，但日志仍出现 `Exit code 0xc0000135` 与 `MSB8066`
- GenerateManual.vcxproj 仍为失败目标；不能把 shortcuts.js 存在当作构建成功
- 构建目录 TrenchBroom.exe 仍为旧 `268df390…`，构建 QM 仍为旧 `707011a3…`

按授权未重试、未修改第二个文件、未清理构建目录。

## D1-4 QM 资源嵌入
**NOT_RUN**。没有新 EXE，未检查 `:/translations/TrenchBroom_zh_CN.qm`，未提取 embedded QM，未做 A/B/C 比较；九条菜单静态检查同样 NOT_RUN。

## 保护状态
正式 TS、B4/B5 文件、五个 B2 源码、QRC、主程序 CMake、Main.cpp、原构建 EXE/QM、原版 Release 与测试副本未变；Git HEAD 未变。用户配置未写入；Documents 全量 NOT_VERIFIED。唯一变化为授权的 DumpShortcuts/CMakeLists.txt。

## 归档
`reports\P2-D3B-B03-T4-2-3-B6-D1\` 含报告、基线/DLL/CMake diff/构建/GenerateManual/资源/保护审计、前后快照与 SHA256SUMS。NOT_RUN 项已如实标记，未伪造 PASS。未上传 GitHub，无可验证链接。等待审查，不进入 B7。
