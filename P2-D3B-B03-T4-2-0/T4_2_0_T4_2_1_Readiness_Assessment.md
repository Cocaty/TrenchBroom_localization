# T4_2_1_Readiness_Assessment — 启动前准备度评估

## 结论：**PASS WITH LIMITATIONS**（无启动阻断；仍需用户单独授权 T4-2-1）

## 已满足的启动前置条件
- 独立测试副本已创建：`test-runs\P2-D3B-B03-T4-2\`
- 源 Release 目录 395 文件 / 38 目录，测试副本 395 文件 / 38 目录；相对路径集合一致，395/395 文件大小与 SHA256 一致，缺失 0、多余 0、哈希不一致 0
- 测试副本 EXE 仍为 `268df390…`；构建中文 QM 仍为 `707011a3…`
- Qt DLL、插件、Qt 自带翻译、第三方 DLL 均从 Release 完整复制，未只复制 EXE，也未单独注入 T3 QM
- portable 机制由 P2-D2C-C 历史证据支持：使用 `--portable`，工作目录设为测试副本目录；无 marker 文件
- 正式 TS、QRC、CMake、Main.cpp、构建目录、原版 Release 与 Git 状态均未变
- 用户配置、Documents 项目相关目录、测试副本与环境存在性已建立启动前基线

## 限制
- T4-1-A1 中用户配置/Documents 为 NOT_VERIFIED；本轮虽已建立只读基线，但未验证历史期间是否发生过变化。T4-2-1 应直接使用本轮基线做启动前后对比。
- 本阶段没有启动程序；QTranslator 实际加载、语言切换、中文 UI 显示全部 **NOT TESTED**。

## 建议启动参数（仅建议，本轮不执行）
`Start-Process <测试副本>\TrenchBroom.exe --portable -WorkingDirectory <测试副本>`

本轮未执行启动，未创建配置，未修改任何项目或用户文件。
