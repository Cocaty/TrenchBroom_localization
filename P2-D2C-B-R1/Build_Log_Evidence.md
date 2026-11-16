# Build_Log_Evidence — 构建日志证据

日期：2026-11-16 ｜ 原始日志全部存档于 `Evidence\`（SHA-256 见 SHA256SUMS.txt）

| 日志 | 存档文件 | 关键内容 |
|---|---|---|
| CMake configure | **本轮未执行**（无 CMake 变更；管线沿用 P2-D2B 已配置状态）——如实注明 | — |
| lupdate 增量 | `p2d2cb_lupdate.log`（6f78d303…） | exit=0；"Found 562 source text(s) (2 new and 560 already existing)" |
| lrelease | 无独立日志文件 | 内嵌于 MSBuild 构建日志（p2d2cb_build2.log）：`Generating TrenchBroom_zh_CN.qm` / `Updating '…TrenchBroom_zh_CN.qm'…`；命令行可于 TrenchBroom.vcxproj L4989 复核 |
| MSBuild 第一次 | `p2d2cb_build.log`（2c379b26…） | **失败**：MSB8066 @ GenerateManual（shortcuts.js 0xc0000135——已知宿主缺陷） |
| MSBuild 第二次（成功） | `p2d2cb_build2.log`（64eb15e7…） | **exit=0**；含 lrelease 步骤与 windeployqt（"Creating qt_zh_CN.qm…"） |
| DumpShortcuts 补救 | 无独立日志文件 | PowerShell 直接调用 DumpShortcuts.exe（退出码 0，PowerShell 会话记录）；shortcuts.js 25,907 B 重生成——**人工补救，如实记录为非全自动构建** |

## 构建前后 SHA-256

| 产物 | 构建前 | 构建后 |
|---|---|---|
| TrenchBroom_zh_CN.qm | da258499047608f5…（26 B） | 8992562d9ad15460…（366 B） |
| TrenchBroom.exe | 3778891cde865612…（29,728,256 B） | e138ba45483efd91…（29,761,536 B） |

## 构建环境守则执行记录

- MSBuild 串行（-m:1）✅
- 依赖缓存复用（无 vcpkg 重装）✅
- 代理变量进程级清空（MSBuild 期）/ NO_PROXY 单份（如涉 vcpkg 步骤）✅
- 无持久 PATH/注册表/安全中心修改 ✅
