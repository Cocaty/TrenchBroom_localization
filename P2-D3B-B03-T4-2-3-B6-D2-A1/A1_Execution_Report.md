# A1_Execution_Report — 临时环境隔离、受控构建与 QM 嵌入验证

## 最终状态：**BUILD_AND_EMBEDDED_QM_VERIFIED**

一次性 Release 构建成功；新 EXE 生成；EXE 中 QM 嵌入资源路径、提取内容与 B5/构建 QM 字节一致；九条顶级菜单译文在 embedded QM 中 9/9 PASS。未启动程序、未部署、未进入 B7。

## 基线
Git `feature/zh-CN-v2026.2`/`4c756be1…`/dirty=13；正式 TS `f81162b3…`/134,278 B/85 Context/571 Message/51 finished/520 unfinished；B5 QM `4b213ce5…`/7,035 B；25 个 DLL 与 vcpkg 来源一致。B6-D2 原始命令已恢复并仅做 MSYS→Windows 路径归一化。开始快照 60 项。

## 环境隔离
原始 Windows 环境块通过 `GetEnvironmentStringsW` 读取：214 条目、两组预期重复代理变量、值相同。仅在内存副本中删除两个小写变体，清理后 212 条目。无害子进程用同一临时环境通过 `CreateProcessW` 启动，退出码 0，重复组 0，PATH 父/子 SHA 一致。未输出代理值，未改持久环境。

## 构建
一次构建退出码 0，17:16:32–17:17:07，无错误。新 EXE `d38feca451382d821697e2767898baea26dba0bb141659584b32d0a5141288e7`；shortcuts.js 与构建 QM 正常生成；25/25 DLL 保持不变。

## QM 嵌入
EXE 内资源路径偏移 22,238,728，QM 魔数偏移 23,382,020；提取 7,035 B，SHA `4b213ce5…`。A=B=C 字节一致。lconvert 回转 embedded QM 成功，51 finished；九条菜单 Source/Translation 9/9 PASS。

## 保护
源码、正式 TS、B4/B5 文件、QRC、主程序 CMake、Main.cpp、原版 Release、测试副本与用户配置范围未变；Git HEAD 未变、dirty 13。允许变化仅限构建目录产物、shortcuts.js 与报告目录。Documents 全量 NOT_VERIFIED。

## 归档
`reports\P2-D3B-B03-T4-2-3-B6-D2-A1\` 含报告、环境/构建/资源/菜单审计、命令与 stdout/stderr、embedded QM 与回转 TS、前后快照及 SHA256SUMS。SHA 清单覆盖全部归档文件、包含 Final Snapshot、不自列。未上传 GitHub，无可验证链接。阶段停止，等待独立审查与 B7 单独授权。
