# Source_Implementation_Evidence — 源码实施证据（当前 v2026.2 行号，2026-11-16 19:20 实测）

完整源码副本（修改后）已在 `Evidence/Main.cpp`、`Evidence/Preferences.h`、`Evidence/ViewPreferencePane.h`、`Evidence/ViewPreferencePane.cpp`（SHA-256 见 SHA256SUMS.txt）。以下为关键代码的**当前实测行号**与上下文。

## 1. initTranslator() 完整实现（Main.cpp L173-193）

```cpp
// Main.cpp L173-175 注释（原文）
void initTranslator(QApplication& app)                                  // L176
{
  const auto& language = pref(Preferences::InterfaceLanguage);          // L178
  if (language != "zh_CN")                                              // L179
  {
    return; // "en" (default) and any unknown value stay English        // L181
  }
  auto* translator = new QTranslator(&app); // parented to app: lives   // L183
                                            // for the whole application
  if (translator->load(":/translations/TrenchBroom_zh_CN.qm"))          // L184
  {
    app.installTranslator(translator);                                  // L186
  }
  else
  {
    qWarning() << "Could not load Chinese translation from "            // L190
                  ":/translations/TrenchBroom_zh_CN.qm; falling back";  // L190-191
    translator->deleteLater();                                          // L192
  }
}
```

## 2. initTranslator(app) 调用位置（Main.cpp L353-359）

```
L355  loadStyleSheets();
L356  loadStyle(app);
L358  // Install the interface translator before any UI is created ...
L359  initTranslator(app);
L361  auto appController = createAppController();
```
时序：QApplication(L322) → PreferenceManager(L324-326) → 样式(L355-356) → **initTranslator(L359)** → AppController/首 UI(L361)。✅ 与 D2C-A 冻结设计一致。

## 3. Preferences::InterfaceLanguage 定义（Preferences.h L210）

```cpp
inline auto InterfaceLanguage = Preference<std::string>{"Editor/Interface language", "en"};
```
（位于 "Editor/Texture lock" L208、"Editor/UV lock" L209 之后，同域同风格；`Preference<std::string>` 有 Theme L53 等 3 处生产先例）

## 4. ViewPreferencePane 构造与控件初始化（ViewPreferencePane.cpp L129-141）

```cpp
L129  m_languageCombo = new QComboBox{};
L130  // Option labels are intentionally bilingual and not translated ...
L132  m_languageCombo->addItem("English");
L133  m_languageCombo->addItem("简体中文");
L135  languageInfo->setText(tr("Requires restart after changing"));   // 与主题行共享同一 tr 条目
L136  setInfoStyle(languageInfo);                                      // 复用既有 setInfoStyle
L138  languageLayout->addWidget(m_languageCombo);
L139  languageLayout->addSpacing(LayoutConstants::NarrowHMargin);
L140  languageLayout->addWidget(languageInfo);
```
表单行：`layout->addRow("Language", languageLayout);`（Theme 行后，"User Interface" 分节内）。

## 5. updateControls（ViewPreferencePane.cpp L364-367）

```cpp
  // Unknown / missing values fall back to English (index 0)
  const auto language =
    QString::fromStdString(prefs.getPendingValue(Preferences::InterfaceLanguage));
  m_languageCombo->setCurrentIndex(language == "zh_CN" ? 1 : 0);
```
**非法偏好值 → index 0 = English** ✅

## 6. bindEvents（ViewPreferencePane.cpp L277-283）

```cpp
  connect(m_languageCombo,
          QOverload<int>::of(&QComboBox::activated),
          this,
          &ViewPreferencePane::languageChanged);
```
（activated 信号，与 themeChanged 连接方式完全一致）

## 7. languageChanged（ViewPreferencePane.cpp L482-494）

```cpp
void ViewPreferencePane::languageChanged(int index)
{
  const auto language = index == 1 ? "zh_CN" : "en";                    // L484 索引↔值映射
  if (language != pref(Preferences::InterfaceLanguage))                 // L485 值变化才动作
  {
    auto& prefs = PreferenceManager::instance();
    prefs.set(Preferences::InterfaceLanguage, language);                // L488 写入
    QMessageBox::information(                                           // L489 模态提示
      this,
      tr("Language"),
      tr("Language changes take effect after restarting TrenchBroom."));
  }
}
```

## 8. resetToDefault（ViewPreferencePane.cpp L320）

```cpp
  prefs.resetToDefault(Preferences::InterfaceLanguage);   // → 恢复默认 "en" = 英文
```
（位于 MaterialBrowserIconSize/RendererFontSize 之后，doResetToDefaults 末尾）✅ 正确恢复英文默认值

## 9. 重点确认项汇总

| 确认点 | 结论 | 行号 |
|---|---|---|
| QTranslator 父对象/生命周期 | `new QTranslator(&app)`，app 为 main 栈对象（L322 创建、L371 exec 返回后析构）→ 覆盖全生命周期 | Main.cpp L183 |
| load 失败处理 | qWarning + deleteLater，不安装、不弹窗、不阻断 | L190-192 |
| installTranslator 条件 | 仅 load() 返回 true 时 | L184-186 |
| 非法偏好值处理 | 读取侧白名单（≠zh_CN→英文）+ UI 侧（≠zh_CN→index 0） | Main L179、VPP L367 |
| ComboBox 索引↔值映射 | index 1=zh_CN、其余=en（双向一致） | L484、L367 |
| 偏好写入时机 | activated（用户确认选择）后、值变化才 set | L484-488 |
| resetToDefault 恢复英文 | resetToDefault(InterfaceLanguage) → 默认 "en" | L320 |
| QMessageBox 调用时机 | 仅"偏好值实际变化"时弹一次；**模态**（PreferenceDialog/Pane 无状态栏，grep 实测） | L489-493 |
