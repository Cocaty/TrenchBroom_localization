# B01_User_Decision_Record — 用户决策记录（尚未确认）

本文件列出所有需要你确认的选项。**本轮未勾选、未冻结任何术语**；“推荐”仅表示 WorkBuddy 依据源码证据提出的建议。

| # | 决策项 | 推荐方案 | 备选方案 | 状态 |
|---|---|---|---|---|
| D1 | Map...（Export 子菜单） | 地图文件... | Map 文件... | 待用户确认（两侧 Decision 已统一为“推荐”） |
| D2 | Point File（Load/Reload/Unload） | 点轨迹文件（加载/重新加载/卸载点轨迹文件） | 点位文件（加载/重新加载/卸载点位文件） | 待用户确认；背景术语“泄漏点文件”不作为默认 |
| D3 | Portal File（Load/Reload/Unload） | BSP 门户文件（加载/重新加载/卸载 BSP 门户文件） | 门户文件 | 待用户确认；菜单长度风险未实测 |
| D4 | Omit From Export | 不参与导出；tooltip 同步使用该名称 | 保留英文属性名 `Omit From Export` | 待用户确认；存在跨批次依赖（Layer UI） |
| D5 | Wavefront OBJ... | A：Wavefront OBJ...（保持原文） | B：Wavefront OBJ 文件... | 待用户确认 |
| D6 | Revert tooltip | 放弃所有未保存的更改，并重新加载地图文件。 | 丢弃所有未保存更改并重新载入地图文件。 | 待用户确认（沿用上轮状态） |
| D7 | 图层属性 UI（LayerEditor/LayerListBox 两字符串） | 后续批次与 D4 同术语组翻译 | 暂不翻译 | 待用户决定批次归属；不属于当前 18 条 |

## 已经统一且无需再选的一致性口径

- Document（6 条）统一“文档”
- Save Document as... → 文档另存为...（不是导出）
- Revert Document → 还原文档，与 D6 tooltip 语义一致
- `...` 保持 ASCII 三点；`.map` 与 Wavefront OBJ 技术名不得丢失

## 授权状态

**本轮不授权正式翻译、不授权写入 TS。** 需要你在审阅本记录后明确：①各项决策采用推荐/备选；②是否授权进入正式翻译实施。
