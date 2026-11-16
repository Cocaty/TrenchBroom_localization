# 全部 location 核验报告（R1）

数据：`Evidence/P2D3A_R1_All_Locations.csv`（**571 行**，逐 location 一行）。

## 口径修正

P2-D3A 只检查每条消息的**首个 location**（562 次）却描述为“源码 100% 覆盖”；R1 逐一解析全部 location 实例：

| 项 | P2-D3A 旧口径 | R1 正确口径 |
|---|---|---|
| 被检查的 location 实例 | 562（首 location） | **571（全部）** |
| 消息数 | 562 | 562（其中多 location 8 条，1 条有 3 个 location） |
| 文件存在 | 562/562（仅首 location） | **571/571** |
| 行号有效 | 562/562（仅首 location） | **571/571** |
| 源码片段采集 | 首行 ±2 | 每个 location 均采集 ±2 行 |

## 逐 location 检查字段

message_id / context / source / location_total / location_index / file / line / file_exists / line_valid / action_function / action_path / action_context / usage_hint / snippet / primary_category / category_reason。

## 多 location 消息（8 条，共 17 个 location）

| context | source | location 数 |
|---|---|---|
| QObject | Toggle %1 visible | 2 |
| tb::ui::ChoosePathTypeDialog | Could not build a path. | 3 |
| tb::ui::EntityDefinitionFileChooser | use builtin | 2 |
| tb::ui::GamePreferencePane | Game Path | 2 |
| tb::ui::QPreferenceStoreDelegate | Could not acquire lock file for reading the preference file | 2 |
| tb::ui::QPreferenceStoreDelegate | check for stale lock files | 2 |
| tb::ui::ViewPreferencePane | Requires restart after changing | 2 |
| tb::ui::ViewPreferencePane | Language | 2 |

合计 2+3+2+2+2+2+2+2 = **17**；单 location 消息 554 条 → 554+17 = **571** ✅ 与预期一致。

## 结论

全部 571 个 location 的文件与行号均有效、片段均可采集；**“全部 location 100% 覆盖”现由 571 行 CSV 直接支撑**，不再以首 location 推断。
