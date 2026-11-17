# D2_Execution_Report — 补齐递归 DLL 依赖与受控 Release 构建

## 结论：**BUILD_FAILED**。构建准备度：**NOT_READY**（见 D2_Build_Readiness_Assessment）。

D2 成功补齐 D0-1 确认的 8 个递归 DLL，GenerateManual 已通过；但 Release 构建随后因 MSBuild 启动 CL.exe 时的代理环境变量重复键冲突失败。未重试、未修改第二个文件、未修改 PATH。

## D2-0 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=13，dirty 清单与 D1-D0-1 一致；正式 TS `f81162b3…`、B5 QM `4b213ce5…`/7,035 B、B4 备份与 B5 回转均符合基线。vcpkg 来源由 CMakeCache 实际读取：`VCPKG_INSTALLED_DIR=x64-windows` 对应 `build/.../vcpkg_installed/x64-windows/bin`，未猜测。

8 个 DLL 全部来源存在、x64、SHA 与 D0-1 一致；DumpShortcuts/Release 修复前均不存在。50 条非系统导入检查 0 缺失。开始快照 51 项。

## D2-1 单文件修正
仅修改 `app/DumpShortcuts/CMakeLists.txt`：在 D1 的 Windows POST_BUILD 块中新增 8 条 `cmake -E copy_if_different`（来源 vcpkg bin，目标 `$<TARGET_FILE_DIR:DumpShortcuts>`）。diff 为 +10/-0（含注释与空行），17 条 D1 命令全部保留，无重复 DLL。Git dirty 仍为 13。

## D2-2 DLL 部署
25/25 DLL（D1 17 + D2 8）在 DumpShortcuts/Release 存在，SHA256 与 vcpkg 来源一致，PE 架构均为 x64。

## D2-3 构建
命令：`cmake.exe --build <build> --config Release --target TrenchBroom -- -m:1 -v:m`，工作目录为既有 build 目录；完整 stdout/stderr 已归档。

- **退出码 1**
- GenerateManual 通过：构建日志显示 `Generating gen-manual/shortcuts.js`，无 `0xc0000135`、无 `MSB8066`
- shortcuts.js 由本次构建生成（mtime 23:56:52），大小 25,907 B
- 构建目录 QM 更新为 `4b213ce5…`（51 finished，与 B5 QM 一致）
- 失败：`MSB6001`，`CL.exe` 启动时 `System.ArgumentException`：环境变量字典重复键 `HTTPS_PROXY` / `https_proxy`（大小写不敏感）
- 失败目标：`TrenchBroom.vcxproj` 的 CL.exe 编译步骤
- 新 EXE 未生成，仍为旧 `268df390…`

未自动重试、未临时修改环境变量、未复制 DLL、未启动 GUI。

## D2-4 产物审计
DumpShortcuts.exe 与 25 项 DLL 已就位；shortcuts.js 与构建 QM 已生成本次更新；TrenchBroom.exe 未更新。资源嵌入验证、extracted QM、菜单静态检查均 NOT_RUN（属后续阶段）。

## D2-5 保护状态
正式 TS、B4 备份、B5 QM/回转、QRC、主程序 CMake、Main.cpp、B2 五源码、原版 Release、测试副本与用户配置范围未变；Git HEAD 未变、dirty 13。预期变化仅限 DumpShortcuts/CMakeLists.txt、8 个新部署 DLL、构建 QM 与 shortcuts.js。Documents 全量 NOT_VERIFIED。

## 归档
`reports\P2-D3B-B03-T4-2-3-B6-D2\` 含报告、CMake diff、DLL/闭包/构建/GenerateManual/产物/保护审计、前后快照、构建 stdout/stderr 与 SHA256SUMS。未上传 GitHub，无可验证链接。等待审查与单独授权，不进入任何后续阶段。
