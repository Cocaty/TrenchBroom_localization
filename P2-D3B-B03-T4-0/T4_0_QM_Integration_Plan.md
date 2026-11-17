# T4_0_QM_Integration_Plan — T4-1 唯一推荐实施方案

## 结论：**零项目文件修改**（推荐方案）

现有架构已经支持 T3 已验证 QM 的等价集成：正式 TS 由 `qt_add_translations` 在构建期编译并嵌入 `:/translations/TrenchBroom_zh_CN.qm`，运行时代码已加载该路径。**T4-1 不应手工复制 QM 或修改 QRC/CMake/运行时代码。**

| 要求项 | 实施方案 |
|---|---|
| QM 最终放置路径 | 不落盘到源码资源目录；构建期由正式 TS 生成于构建树并嵌入可执行文件。T3 QM 仅保留在 `reports/P2-D3B-B03-T3/Artifacts/` 作为审计产物 |
| QRC 增加/调整 | 不增加、不调整。QRC 保持仅有 `opengl_buglist.json` |
| prefix / alias | 无需新增；由 `qt_add_translations(RESOURCE_PREFIX "/translations")` 自动生成。若未来放弃自动管线而手工集成，才需要 `prefix="/translations"` 与 alias `TrenchBroom_zh_CN.qm`，但本方案不采用 |
| 运行时加载路径 | 不修改；`Main.cpp:184` 已是 `:/translations/TrenchBroom_zh_CN.qm` |
| CMake | 不修改；`CMakeLists.txt:119` LinguistTools、`app/CMakeLists.txt:493-496` qt_add_translations 已就绪 |
| 其他源码 | 不修改 |
| 修改后预期资源路径 | `:/translations/TrenchBroom_zh_CN.qm`，与运行时加载路径一致 |

## 候选文件当前 SHA256（仅确认，不修改）
| 文件 | SHA256 |
|---|---|
| 正式 TS | `f021e509cf9a8679eeda64624df0f5474335c0872f73940e1d48ef77447a261a` |
| T3 QM | `707011a3216511d051b07d0dba249af6d834e6795a447a4f09611c6a9bd2102c` |
| QRC | `de72b206c01058daea020a24dac86846167bd161348f297b0aa6dae4a60c2cca` |
| app/CMakeLists.txt | 见 `T4_0_Protected_State_Audit.csv` |
| 根 CMakeLists.txt | 见 `T4_0_Protected_State_Audit.csv` |
| Main.cpp | 见 `T4_0_Protected_State_Audit.csv` |

## 拟修改位置
无。现有关键位置作为证据：`app/CMakeLists.txt:8,151,493-496`、`CMakeLists.txt:119`、`Main.cpp:176-194,358-359`、`ViewPreferencePane.cpp:129-139,365-367,482-493`。

## T4-1 实施动作（本阶段不执行）
1. 不做文件修改；直接以当前工作区作为 T5 构建输入。
2. 构建后验证资源嵌入：检查构建日志中 `qt_add_translations`/lrelease 无错误；检查可执行文件 Qt 资源中是否存在 `:/translations/TrenchBroom_zh_CN.qm`；运行期验证需下一阶段授权。
3. 若发现构建产物仍缺资源，才回到本报告风险表逐项排查，不得提前修改 QRC/CMake。

## 必须修改 / 可不修改 / 待用户决策
- **必须修改**：无
- **可不修改**：TS、T3 QM、QRC、CMakeLists、Main.cpp、ViewPreferencePane、原版 Release
- **待用户决策**：是否接受“零修改、依赖既有 qt_add_translations 管线”的 T4-1 方案；是否授权后续 T5 构建与运行期验证

本阶段不执行上述动作，不进入 T4-1。
