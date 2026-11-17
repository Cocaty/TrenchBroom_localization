# D1_B6_Readiness_Assessment — B6 恢复状态

## 结论：**B6_FAILED**

D1 的 DLL 部署修正本身已生效，但 Release 构建仍在 GenerateManual / shortcuts.js 自定义步骤返回 `0xc0000135` 与 `MSB8066`。没有新 EXE，没有完成 QM 资源嵌入验证。按授权未修复第二个问题、未重试、未修改第二个文件。

## 已完成
- D0 17 个候选 DLL 全部复核：来源存在、x64、SHA 记录完整
- 仅修改 `app/DumpShortcuts/CMakeLists.txt`，新增 17 条 `copy_if_different`，现有直接依赖与 windeployqt 未改
- 构建后 17/17 DLL 已复制到 DumpShortcuts/Release，且 SHA 与 vcpkg 来源一致
- 构建日志显示 DumpShortcuts.exe 已重建并完成 windeployqt

## 未完成 / 失败
- 构建退出码 1
- 仍出现 `Exit code 0xc0000135` 与 `MSB8066`
- `shortcuts.js` 存在（25,907 B），但不能据此判定 GenerateManual 成功；MSBuild 仍判定自定义生成失败
- 没有新 TrenchBroom.exe / 新构建 QM
- EXE 资源路径检查、embedded QM 提取、A/B/C 字节比较、九条菜单静态检查全部 NOT_RUN

## 下一步（需单独授权）
对剩余 `0xc0000135` 做新的只读定位（可能是另一依赖、插件或命令链环境差异），不得在本轮继续修改。B6 保持 FAIL，B7 不得进入。

本文件不授权进一步修复、构建或启动。
