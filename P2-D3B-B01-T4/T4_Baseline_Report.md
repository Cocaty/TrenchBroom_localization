# T4_Baseline_Report — 构建前快照（T4-1）

- Git：feature/zh-CN-v2026.2，HEAD 4c756be1a54a28d921d18c77716a5f170bdc31d0，tag v2026.2，dirty=7
- 工作区：6 tracked 修改（P2-D2B 2 CMake + P2-D2C-B 4 代码）+ 未跟踪 translations/；与本轮前一致
- 正式 TS：存在，131,106 B，SHA `6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8`（与 T2 最终值一致）✅
- T3 QM：存在，1,805 B，SHA `a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66`（与 T3 报告一致）✅
- 构建目录存在；CMakeCache：Generator=Visual Studio 18 2026，配置类型含 Release（多配置生成器无单值 CMAKE_BUILD_TYPE，Release 由 `--config Release` 选择）
- 工具链：CMake 4.2.8；Qt qmake -v → Qt 6.10.3（msvc2022_64）；MSVC v145 沿用既有构建目录（未更换）
- 原版 Release：TrenchBroom.exe `f5a02f40…` / Qt6Core.dll `b712b475…`（历史基线）

**结论：构建前基线全部通过，允许进入 CMake 管线检查与 Release 构建。**
