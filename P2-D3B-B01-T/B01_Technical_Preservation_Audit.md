# B01_Technical_Preservation_Audit — 技术标识与格式保留策略

基准：18 条 source（TS 逐字核对）；源码证据见 `B01_Source_Context_Audit.csv`。

## 必须原样保留的内容

| ID | 技术内容 | 类型 | 保留要求 |
|---|---|---|---|
| e7c5ab696447 | `Wavefront OBJ` | 导出格式/品牌名 | 不译作“对象”“实体”；候选保留原文，是否补“文件”待定；`...` 保留 |
| 8626a59ed64f | `.map` | 文件扩展名 | 逐字保留，不得译为“地图格式”而删扩展名 |
| 8626a59ed64f | `Omit From Export` | UI 属性名引用（LayerEditor.cpp:99 / LayerListBox.cpp:54） | 当前 UI 为英文；译文引用时保持引号内原文，若将来翻译该 UI 标签须同步 |
| c87e891f3904 | `...` | 菜单省略号 | 保留 |
| c18158cfc475 | `...` | 菜单省略号 | 保留 |
| 0843baa95d90 / c13f05ee9b4e | `...` | 菜单省略号 | 保留 |

## 源码确认的格式与扩展名（未在译文里翻译，只作术语依据）

| 对象 | 证据 | 说明 |
|---|---|---|
| Point File | `MapWindow.cpp:1196`：`Point files (*.pts *.lin);;Any files (*.*)` | 支持 .pts/.lin；PointTrace 点序列，MapView2D.cpp:282 / MapView3D.cpp:460 据 currentPoint/currentDirection 定位视图 |
| Portal File | `MapWindow.cpp:1237`：`Portal files (*.prt);;Any files (*.*)`；`PortalFile.cpp:43-55` PRT1 | .prt 门户多边形数据（BSP 可见性），非网页门户 |
| Omit From Export | `Layer.h:39 m_omitFromExport`、`LayerEditor.cpp:99 tr("Omit From Export")`、`LayerListBox.cpp:54 tr("Toggle omit from export")` | 图层级布尔属性；tooltip 中的 Layers 即这些图层 |
| Wavefront OBJ | `ObjExportDialog.cpp:66 tr("Export Wavefront OBJ")`、`Polyhedron::exportObj()` | 导出几何为 OBJ 格式 |

## 占位符

18 条 source 中 `%1`、`%2`、`%L1`、`%n`、`%%` 均为 **0 条**——无占位符保留负担；本轮候选译文也未引入占位符。

## 风险清单

1. `Omit From Export` 当前 UI 英文与 tooltip 译文潜在不同步——需用户决定：是否把该属性 UI 文本纳入后续批次
2. Point/Portal File 中文名尚未冻结——菜单候选使用中性译法，术语确认前不得正式写入
3. `.map`、`Wavefront OBJ`、`...` 在正式翻译实施时必须逐字复核

## 结论

技术内容均有明确保留策略；无占位符风险。两条“待用户确认”的格式名/属性名需在正式翻译前定稿。
