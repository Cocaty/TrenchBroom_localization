# Boundary_and_Integrity_Check — 完整性与边界核验

日期：2026-11-16 19:22（PowerShell 实测时间戳）

## 1. 原版 Release 哈希核验

| 文件 | 当前 SHA-256（前16） | P2-B 快照 | 一致 |
|---|---|---|---|
| TrenchBroom.exe | f5a02f40dde7108f | f5a02f40dde7108f | ✅ |
| Qt6Core.dll | b712b4754588e89f | b712b4754588e89f | ✅ |

## 2. 用户 INI 未修改的核验依据

- 路径：`C:\Users\yoshi\AppData\Roaming\io.github.trenchbroom\TrenchBroom.ini`（与 Main.cpp L314-318 setApplicationName/OrganizationDomain 对应）
- **最后修改时间：2026-11-16 12:42:23**（本轮实施开始于 ~19:05，此后无写入）
- **不含 `Interface language` 键**（Select-String 检索 False）——证明运行时集成代码从未被启动执行
- 大小 1,399 B

## 3. 进程未启动的核验依据

- `Get-Process -Name 'TrenchBroom'`：**运行中进程数 = 0**（PowerShell 实测，19:22:49）

## 4. 正式安装目录未修改的核验依据

- 原版 Release 目录（`Downloads\TrenchBroom-Win64-AMD64-v2026.2-Release`）关键文件哈希与 P2-B 快照一致（第 1 项）；本轮无任何复制/部署操作记录
- 新 EXE 仅存在于构建树 `TrenchBroom-zhCN\build\...\app\TrenchBroom\Release\`，未复制到任何安装位置

## 5. 其他边界

- 源码修改严格限于 5 个授权文件（见 Git_Status_and_Diff.md 归属表）
- TS/QM 更新均通过授权流程（lupdate + 授权译文填充），未重置/清空
- 无 git clean/reset；无 PATH/注册表/安全中心修改；构建树内 shortcuts.js 补救沿用既有预案
