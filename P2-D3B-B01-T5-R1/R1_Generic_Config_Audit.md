# R1_Generic_Config_Audit — Generic 游戏配置只读审计（R1-0）

实际文件：`build\v2026.2-msvc145-qt6103\app\TrenchBroom\Release\games\Generic\GameConfig.cfg`（848 B），同目录 `Generic.fgd`（195 B）与 `Icon.png`（3,539 B）。T5 测试副本 config 目录仅有 `Preferences.json`（85 B），无用户自定义游戏配置；本轮**不修改**原始 Generic 配置。

## 配置内容逐项

| 字段 | 值 | 判定 |
|---|---|---|
| filesystem/searchpath | `.` | 相对玩家指定的游戏路径；可指向隔离目录，不要求真实游戏目录 ✅ |
| materials/root | `textures` | 相对游戏路径；空目录亦可（仅无材质显示）✅ |
| entities/definitions | `Generic.fgd` | 相对游戏配置目录，文件实际存在 ✅ |
| fileformats | Standard/Valve/Quake2，`initialmap: initial_*.map` | 初始地图文件在 Generic 目录中**不存在**；创建空白地图时可能回退空地图或失败，需实测判定 |
| packageformat | `.pak`/idpak | 无包文件亦可 ✅ |
| tags / faceattribs | 空数组 | 无外部依赖 ✅ |

## 外部路径与写入检查

- 配置中**没有**绝对路径、Steam/真实游戏目录、注册表路径或用户 Documents 路径 ✅
- 游戏路径由偏好键 `Games/Generic/Path` 决定（`GameInfo.cpp:31`）；偏好 JSON 为扁平键（`QPreferenceStoreUtils.cpp:writePreferencesToJson`），可在测试副本 `config/Preferences.json` 中设置到本轮隔离目录
- portable 模式下配置写入测试副本 `app/config`（`SystemPaths.cpp:76-85`），不会写日常配置 ✅
- 地图文件写入位置由用户/地图打开路径决定；本轮将地图限制在 `test-runs\P2-D3B-B01-T5-R1\workspace\` ✅

## 结论

**Generic 配置不要求真实游戏目录，也不要求修改原始配置文件**；可在隔离目录中指定 game path 并创建空白临时地图。R1-1 安全门禁除“实际能否创建/打开空白地图”需实测外，其余条件均满足，允许进入 R1-2/R1-3 验证该条件（若失败则 BLOCKED）。
