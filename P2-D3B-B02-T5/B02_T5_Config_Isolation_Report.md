# B02_T5_Config_Isolation_Report — 测试配置隔离证明

## 隔离证据
- 启动命令：`TrenchBroom.exe --portable`，工作目录 `test-runs\P2-D3B-B02-T5\app`
- 首次启动后测试副本内生成 `app\config\Preferences.json`（初始仅 `"updater/Ask for auto updates": false`）
- 语言偏好与 game path 的全部变更只发生在该文件：
  - TC-03：`Editor/Interface language = zh_CN`
  - TC-07：`Editor/Interface language = en`
  - TC-08：`Editor/Interface language = invalid_locale`
- 配置文件副本已存入 Evidence（TC03_config_zhCN.json、TC07_config_en.json、TC08_config_before_invalid.json、TC08_config_after_invalid.json）

## 日常配置保护（开始 = 结束）
| 对象 | 路径 | SHA-256 |
|---|---|---|
| 日常 INI | `C:\Users\yoshi\AppData\Roaming\io.github.trenchbroom\TrenchBroom.ini` | 5062ef854b994caf… |
| 日常 Preferences.json | `C:\Users\yoshi\AppData\Roaming\TrenchBroom\Preferences.json` | 50705006dd1d58e1… |

两者大小与 mtime 也未变化。此前 P2-D2C-C 已确认语言偏好实际保存在 Preferences.json，故本轮将其明确列为保护对象并实测未变。

## 其他边界
原版 Release EXE (`f5a02f40…`)、T4 构建目录 EXE (`38d02195…`) 与 QM (`f480ae44…`) 均未变；未修改注册表、系统环境变量、Documents、测试副本之外的任何配置。

**结论：portable 配置隔离得到实际证明，未污染日常环境。**
