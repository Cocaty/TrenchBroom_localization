# T4_1_Execution_Report — 受控构建与 Qt 翻译资源静态验证

## 结论：**PASS WITH LIMITATIONS**

核心目标全部达成：构建成功、构建 QM 与正式 TS 42 条 finished/39 条目标译文一致、目标资源路径和 QM 字节进入最终 EXE。唯一限制：安全策略阻止直接读取 MSBuild.exe 哈希；由 CMake 生成器、Cache 与 `cmake --build` 间接调用确认，未影响构建与资源验证。

## A. 基线
正式 TS `f021e509…`/132,589 B（85/562/42/520），QRC `de72b206…`，根 CMake `fd3ef8de…`，app CMake `21cfabf0…`，Main.cpp `f4e756ab…`，T3 QM `707011a3…`，Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=7。构建目录 `build\v2026.2-msvc145-qt6103` 的 `CMAKE_HOME_DIRECTORY` 指向本工作区源码；Cache 为 Qt 6.10.3、Visual Studio 18 2026、x64。原版 Release 只读。报告目录创建前不存在；开始快照 12 项。

## B. 工具链
CMake 4.2.8（`C:\Users\yoshi\Tools\CMake\4.2.8\bin\cmake.exe`）、Qt 6.10.3 qmake/lrelease/lconvert/rcc、LinguistTools 均核验；MSBuild 路径由 VS18 安装确定，但哈希因安全策略标记为 NOT_VERIFIED。详见 `T4_1_Toolchain_Audit.csv`。

## C. 构建结果
命令：`cmake.exe --build <build> --config Release --target TrenchBroom -- -m:1 -v:m`；未重新 configure、未 lupdate、未安装/部署目标。开始 2026-11-17 20:51:34 +0800，结束 20:52:06 +0800，退出码 0，完整日志 `T4_1_Build_Log.txt`。目标 EXE：`build\...\app\TrenchBroom\Release\TrenchBroom.exe`，29,761,536 B，SHA `268df3904f16dc2e329542397531be4ef35f530cebde07cd720753707fca7212`。

## D. QM 结果
构建生成 `build\...\app\TrenchBroom\TrenchBroom_zh_CN.qm`，6,631 B，SHA `707011a3…`，QM 魔数有效，生成时间落入构建窗口，仅一个同名中文 QM。lconvert 回转通过；42/42 finished 与正式 TS 一致；39 条 B01/B02/B03 目标逐条一致；3 条原始 finished 单独记录。

## E. 资源嵌入结果
预期路径 `:/translations/TrenchBroom_zh_CN.qm`：**已进入 EXE**。静态证据：EXE 中路径字符串 ASCII 偏移 22,238,728；rcc 生成文件含该资源；EXE 中 QM 魔数偏移 23,382,020，提取 6,631 字节 SHA 与构建 QM 完全一致。运行时可加载性为 **NOT VERIFIED**，留待 T4-2。

## F. 保护状态
正式 TS、QRC、CMake、Main.cpp、ViewPreferencePane、T3 QM、原版 Release 与 Git 状态均未变化；构建目录中 EXE/QM 的变化是授权构建产物，标记 EXPECTED_CHANGE。详见 `T4_1_Protected_State_Audit.csv`。

## G. 未执行事项
未启动 TrenchBroom、未运行游戏、未部署/替换正式安装目录、未修改用户配置/地图/游戏文件、未 Git 写操作、未安装工具、未 lupdate、未进入 T4-2。本结论不代表运行期汉化成功。

## H. 归档
本阶段新增 15 个报告/证据/产物文件；SHA256SUMS 覆盖 14 项（清单自身不自列）并逐项校验。未上传 GitHub，无可验证链接。
