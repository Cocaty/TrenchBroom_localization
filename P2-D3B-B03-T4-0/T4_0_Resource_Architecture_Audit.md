# T4_0_Resource_Architecture_Audit — Qt 翻译资源架构只读审计

## A. QRC 资源结构
实际文件 `app\TrenchBroom\resources\qrc\resources.qrc`（106 B，SHA `de72b206…`）仅 5 行：
- L1 RCC 1.0；L2 `<qresource>` 无显式 prefix，即资源根 `/`
- L3 唯一资源 `<file>opengl_buglist.json</file>`
- 无 alias、无 translations 路径、无任何 `.qm` 资源
- 资源相对 QRC 所在目录解析（与 `TB_RESOURCE_DIR` 一致）
- 现有资源命名不使用别名，按文件基名暴露

**结论：QRC 当前没有翻译资源，但翻译资源不应手工塞入这个 QRC —— 逃避重复注册。**

## B. CMake 资源处理
- `app/TrenchBroom/CMakeLists.txt:8` 将 `resources.qrc` 放入 APP_SOURCE
- `app/TrenchBroom/CMakeLists.txt:151` `AUTORCC TRUE`，构建时自动 rcc
- 根 `CMakeLists.txt:119` `find_package(Qt6 COMPONENTS ... LinguistTools REQUIRED)`
- `app/TrenchBroom/CMakeLists.txt:493-496` 已存在完整翻译管线：
  `qt_add_translations(TrenchBroom SOURCE_TARGETS TrenchBroom TbUiLib UpdateLib TS_FILES ".../translations/TrenchBroom_zh_CN.ts" RESOURCE_PREFIX "/translations")`
- `windeployqt` 段（L222-234）Debug `--no-translations`；Release 会尝试部署外部翻译，但本项目 QM 已通过 RESOURCE_PREFIX 嵌入，外部部署不存在路径依赖

**结论：CMake 已实现“TS → 构建期 lrelease → QM 嵌入 :/translations/”的最小集成；无需新增 QRC 条目或自定义命令。**

## C. 运行时翻译加载
- `app/TrenchBroom/src/Main.cpp:176-194` `initTranslator(QApplication&)`；L184 `translator->load(":/translations/TrenchBroom_zh_CN.qm")`；L186 `app.installTranslator`
- L183 QTranslator 父对象为 `app`，生命周期覆盖整个应用；L188-193 加载失败仅 warning 并回退英文，不阻塞启动
- L358-359 `initTranslator(app)` 在 `createAppController()` 之前，早于任何 UI 创建
- `lib/TbUiLib/src/ViewPreferencePane.cpp:129-139` 语言下拉 English/简体中文；L482-493 写入 `Preferences::InterfaceLanguage` 并提示重启；L365-367 从偏好恢复选项
- `lib/TbPreferencesLib/include/Preferences.h:210` 键 `Editor/Interface language`，默认 `en`

**结论：运行时资源路径 `:/translations/TrenchBroom_zh_CN.qm` 与 CMake `RESOURCE_PREFIX "/translations"` + TS 基名 `TrenchBroom_zh_CN.ts` 推导出的资源名完全一致，不需要修改运行时代码。**

## 集成链总结
正式 TS（`f021e509…`）→ 构建期 `qt_add_translations`/lrelease → QM 嵌入资源 `:/translations/TrenchBroom_zh_CN.qm` → `initTranslator` 在 UI 创建前加载。T3 独立 QM（`707011a3…`）只是对该编译链的静态验证产物，不应复制进源码 QRC。
