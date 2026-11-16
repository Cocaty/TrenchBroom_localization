# T4_CMake_Translation_Audit — CMake 翻译管线只读检查（T4-2）

实际配置（当前源码，未修改）：

| 项 | 证据 | 判定 |
|---|---|---|
| Qt6 LinguistTools | `CMakeLists.txt:119` `find_package(Qt6 COMPONENTS Core Widgets OpenGL OpenGLWidgets Network Svg Test LinguistTools REQUIRED)` | ✅ |
| qt_add_translations | `app/TrenchBroom/CMakeLists.txt:493` | ✅ |
| SOURCE_TARGETS | 同文件 L494：`TrenchBroom TbUiLib UpdateLib` | ✅ 与冻结设计一致 |
| TS 路径 | L495：`${CMAKE_CURRENT_SOURCE_DIR}/translations/TrenchBroom_zh_CN.ts` | ✅ 指向正式 TS |
| RESOURCE_PREFIX | L496：`/translations` | ✅ |
| QM 嵌入 | 由 `qt_add_translations` 生成 qrc 并参与主程序资源编译（本轮构建日志与 RCC 产物证实） | ✅ |
| 额外翻译文件/重复规则 | TS 目录仅 `TrenchBroom_zh_CN.ts`；CMake 中仅一处 `qt_add_translations` | ✅ 无重复 |
| 其他相关逻辑 | `CMakeLists.txt:222-234`：仅 Release 复制翻译、Debug 用 `--no-translations` | 与既有设计一致 |

**结论：配置与冻结设计完全一致，无异常，未修改任何 CMake 文件。**
