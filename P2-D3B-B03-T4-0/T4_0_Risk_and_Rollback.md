# T4_0_Risk_and_Rollback — T4-1 风险与回滚预案

本阶段只列预案，不执行任何修改或回滚。

| 风险 | 具体检查方法 | 回滚方式 |
|---|---|---|
| QM 资源路径不匹配 | 构建后检查可执行文件 Qt 资源列表是否含 `:/translations/TrenchBroom_zh_CN.qm`；运行时 warning 是否出现 | 不改 QRC；先核对 `qt_add_translations` 的 RESOURCE_PREFIX 与 TS 基名，修正构建输入后重建 |
| QRC prefix/alias 不一致 | 本方案不新增 QRC 条目；若未来手工集成，核对 prefix `/translations` 与 alias 基名 | 撤销手工 QRC 条目，恢复 `de72b206…` 原文件 |
| 资源重复注册 | 检查 QRC 中不得新增 translation 条目，构建日志不得出现重复资源警告 | 删除重复 QRC 条目；本推荐方案天然避免 |
| 资源未进入构建目标 | 核对 `app/CMakeLists.txt:8` QRC 在 APP_SOURCE、L151 AUTORCC TRUE、L493-496 qt_add_translations | 恢复 CMake 原哈希；不新增自定义命令 |
| 构建产物仍使用旧资源 | 清理/重建构建树由用户另行授权；本阶段不执行；比对构建时间与 TS/QM 时间戳 | 按 T2/T3 报告恢复正式 TS 备份 `901554891…`，重新执行 T2/T3 流程 |
| 正式 TS 与 QM 不一致 | 比对 TS SHA `f021e509…` 与 T3 QM 的 lrelease 输入记录 | 回退正式 TS 到 T2 备份；重新编译 QM |
| 资源文件意外覆盖 | 每步前后比对 QRC/TS/CMake/Main SHA 与本报告保护表 | 用 T2 Backup 或本阶段快照恢复；不部署 |

## 当前推荐方案的特殊性
T4-1 推荐“零项目文件修改”，因此上述多数代码级回滚不适用；若后续构建验证失败，应先调查构建配置/资源生成，而不是把 T3 QM 手工复制进 QRC。任何扩展修改必须获得用户新授权。

本阶段未执行回滚，未修改任何文件。
