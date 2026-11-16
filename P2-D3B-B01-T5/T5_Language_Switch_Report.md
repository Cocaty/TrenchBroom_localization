# T5_Language_Switch_Report — 语言切换与持久化（T5-4 / T5-5）

## 三次启动/退出序列（全部为测试副本，`--portable`）

| 次序 | PID | 配置初始语言 | 操作 | 配置结果 | 重启后界面 | 退出 |
|---|---|---|---|---|---|---|
| 1 | 2260 | 无语言键 | 选简体中文 → 英文提示 "Language changes take effect after restarting TrenchBroom." → OK → Preferences OK | `"Editor/Interface language": "zh_CN"` | （下一次启动）中文 | CloseMainWindow 成功 |
| 2 | 23996 | zh_CN | 检查中文界面 → 选 English → 中文提示 "语言更改将在重启 TrenchBroom 后生效。" → OK → Preferences OK | `"Editor/Interface language": "en"` | （下一次启动）英文 | CloseMainWindow 成功 |
| 3 | 29880 | en | 检查英文界面，不再切换 | 仍为 `"en"` | 英文 | CloseMainWindow 成功 |

## 三态区分

1. **下拉框即时状态**：选择后立即显示 简体中文 / English，但界面语言未即时变化（设计如此，出现重启提示）
2. **写盘持久化状态**：Preferences 对话框 OK 后配置出现 `zh_CN` / `en`（首启另有 `updater/Ask for auto updates: false`）
3. **重启后实际加载状态**：第二次启动显示中文，第三次启动恢复英文——与配置值一致

## 独立配置证据

`Evidence/test_config_final.json` 为测试结束后的测试配置副本（`"Editor/Interface language": "en"`）；zh_CN 状态的配置内容已在运行过程实测并记录于本报告与上表。日常 `AppData\Roaming\io.github.trenchbroom\TrenchBroom.ini` 与 `AppData\Roaming\TrenchBroom\Preferences.json` 哈希、大小、mtime 全程未变。

**结论：语言切换、提示文本、配置持久化与重启加载均通过。**
