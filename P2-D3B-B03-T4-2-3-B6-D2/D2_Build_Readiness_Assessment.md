# D2_Build_Readiness_Assessment — 构建恢复状态

## 结论：**BUILD_FAILED**

D2 的 8 项递归依赖补齐成功，GenerateManual 已不再出现 `0xc0000135` / `MSB8066`，`shortcuts.js` 由本次构建生成。但 Release 构建在 `TrenchBroom.vcxproj` 的 CL.exe 编译步骤以 `MSB6001` 失败，退出码 1；未产生新 EXE。按授权未重试、未修改第二个文件或环境变量。

## 已完成
- 8 个 DLL 来源、SHA、架构、直接父依赖与非系统导入均复核通过
- CMake 仅修改授权文件，新增命令恰好 8 条
- 25/25 DLL（D1 17 + D2 8）在 DumpShortcuts/Release 存在、SHA 与 vcpkg 一致、x64
- GenerateManual 通过：无 `0xc0000135`，无 `MSB8066`，shortcuts.js 生成
- 构建目录 QM 更新为 B5 QM 哈希 `4b213ce5…`（51 finished）

## 失败点
`MSB6001`：`CL.exe` 启动时 `System.ArgumentException`：环境变量字典中 `HTTPS_PROXY` 与 `https_proxy` 被判定为重复键（大小写不敏感）。这是构建进程环境冲突，不是 DLL 依赖问题。

## 未完成
- 新 TrenchBroom.exe 未生成（仍为旧 `268df390…`）
- 未进行新 EXE 资源嵌入验证、extracted QM 比较或菜单静态检查（属后续阶段）
- 未启动 GUI、未部署、未修改测试副本

## 下一步（需单独授权）
在不修改项目文件、不进入 GUI、不部署的前提下，另行决定如何处理构建进程中的大小写重复代理变量冲突。本轮不得重试构建。
