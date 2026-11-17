# B6_B7_Readiness_Assessment — 后续运行期验证准备度

## 结论：**NOT_READY**

B6 核心验收失败：Release 构建因 GenerateManual 自定义步骤失败而退出，未能生成新的 TrenchBroom.exe，未能提取 EXE 内嵌 QM，未能完成 B5 QM 与嵌入资源的字节一致性验证。不得进入 B7。

## 失败点
- `cmake --build ... --config Release --target TrenchBroom -- -m:1 -v:m` 退出码 1
- 日志：`Generating gen-manual/shortcuts.js` 后 `Exit code 0xc0000135`（STATUS_DLL_NOT_FOUND）
- MSBuild 错误：`MSB8066`，GenerateManual.vcxproj 的自定义生成退出码 1
- 构建目录 EXE/QM 哈希保持不变，确认未产生新产物

## 必须解决后重新授权
1. 查明 GenerateManual 自定义命令所需运行时 DLL / 工具链依赖为何缺失（本阶段不修改、不重试）
2. 在不修改源码的前提下恢复或正确配置构建环境
3. 重新执行 B6，获得退出码 0 的新 EXE
4. 完成 EXE 资源路径检查、QM 提取与 A/B/C 字节一致验证
5. 九条菜单译文静态检查 9/9

本文件不授权任何修复、重新构建、启动或 B7 操作。
