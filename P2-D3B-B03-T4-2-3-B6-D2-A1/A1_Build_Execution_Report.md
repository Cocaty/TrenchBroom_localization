# A1_Build_Execution_Report — 一次性受控 Release 构建

## 结果：**PASS**

构建命令复用 B6-D2 原始记录：

`/c/Users/yoshi/Tools/CMake/4.2.8/bin/cmake.exe --build /c/Users/yoshi/Projects/TrenchBroom-zhCN/build/v2026.2-msvc145-qt6103 --config Release --target TrenchBroom -- -m:1 -v:m`

为 `CreateProcessW` 仅将 MSYS 路径写法归一化为 Windows 路径，目标、配置、参数与工作目录均未改变。

## 执行
- 开始：2026-11-18 17:16:32 +0800
- 结束：2026-11-18 17:17:07 +0800
- 用时：35.57 s
- 退出码：**0**
- stdout/stderr 已归档；无 `error` / `MSB6001` / `MSB8066` / `0xc0000135`

## 产物
- TrenchBroom.exe：`d38feca451382d821697e2767898baea26dba0bb141659584b32d0a5141288e7`，29,761,536 B，mtime 2026-11-18 17:16:51；旧 EXE 为 `268df390…`，确认本次更新
- DumpShortcuts.exe 与 25 个 DLL 已核验；25/25 SHA 与 vcpkg 来源一致
- shortcuts.js：25,907 B，SHA `95411fbe…`，本次生成
- 构建 QM：7,035 B，SHA `4b213ce5…`，与 B5 QM 一致

只执行一次构建，失败重试未发生；未启动 TrenchBroom、未部署、未修改源码/TS/CMake。
