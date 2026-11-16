# 06_UI_Length_And_Ambiguity_Risks — UI 长度与上下文歧义风险（预测）

数据：`Evidence/P2D3A_Length_Risk.csv`（559 条 unfinished 逐条预测），歧义词标记来自消息索引 `ambiguous_terms` 列。

## UI 长度风险（预测，非布局实测）

| 等级 | 条数 | 判定规则（脚本） |
|---|---|---|
| 高 | **72** | 含格式化参数或 source > 90 字符——译文可能更长、参数展开后布局不确定 |
| 中 | **207** | 含按键/技术标识，或属于短按钮/菜单词（≤12 字符，中文可能变宽） |
| 低 | **280** | 中等长度（13–55 字符）普通 UI 文本 |
| 无法判断 | 0（全部给出启发式等级，但均为**预测风险**） | — |

**限制声明**：未做实际 UI 布局截图/像素测量，中文长度是否截断**无法确认**；上表是保守预测，不得当作实测结果。后续批次完成后应在真实 UI 中抽查短按钮、菜单、固定宽度标签。

## 上下文歧义（195 条含候选歧义词）

| 词 | 风险点 | 建议（待校阅） |
|---|---|---|
| Face | 几何面 vs 界面 | 几何上下文译“面”；与 UI 无关词形单独判断 |
| Brush | 几何笔刷 vs 画笔工具 | TrenchBroom 中主要是几何体，候选“笔刷/刷子” |
| Entity / Point Entity / Brush Entity | 游戏对象术语 | 候选“实体/点实体/笔刷实体”，与 Class/Property 组合需一致 |
| Group | 编组 vs 分组/图层 | 与 Layer（图层）区分；结合 LayerEditor/Group action 源码确认 |
| World | 世界实体 vs 世界坐标 | 需看上下文，勿统一强译 |
| Layer | 图层（地图组织） | 与 Group 区分 |
| Texture / Material | 旧新术语并存 | 建议统一译法映射，保留 UI 当前用词习惯 |
| Apply | 应用按钮 vs 应用更改 | 按钮场景下译“应用”即可 |
| Select / Scale / Snap | 工具动作 | 需与工具名一致性（选择/缩放/吸附） |
| Map | 地图 vs 映射（UV Mapping） | 按 context 区分，不可一刀切 |

完整 46 项术语候选见 `07_Terminology_Candidate_Glossary.md` 与 `Evidence/P2D3A_Glossary.csv`。歧义标记仅作**校阅提示**，不构成强制译法。
