# 07_Terminology_Candidate_Glossary — 术语候选表（待 ChatGPT 校阅）

完整 CSV：`Evidence/P2D3A_Glossary.csv`（46 行，字段：English / Chinese_candidate / Alternative / Context / Evidence / Confidence / Review_status）。**以下均为候选，不写入 TS，不作为最终术语。**

## 几何与地图编辑（7）

| English | 候选 | 备选 | Confidence |
|---|---|---|---|
| Brush | 笔刷 | 刷子 | 中 |
| Face | 面 | 面片 | 中 |
| Vertex | 顶点 | — | 高 |
| Edge | 边 | 边缘 | 高 |
| Plane | 平面 | — | 低（当前 TS 无精确匹配，预备术语） |
| Polygon | 多边形 | — | 低（同上） |
| Geometry / Primitive | 几何体 / 图元 | 几何 / 基本体 | 低（当前 TS 无精确匹配） |

## 实体与游戏对象（8）

Entity→实体（高）；Point Entity→点实体（中）；Brush Entity→笔刷实体/固体实体（中）；World→世界（中）；Property→属性/特性（中）；Class→类/类别（中）；Model→模型（高）；Spawn→生成（中）。

## 材质与纹理（7）

Texture→纹理/贴图（中，旧术语）；Material→材质/贴图（高）；UV→UV/纹理坐标（高）；Surface→表面（中）；Mapping→贴图映射（中）；Alignment→对齐（中）；Projection→投影（中）。

## 编辑器操作（11）

Select→选择（高）；Move→移动（高）；Rotate→旋转（高）；Scale→缩放（高）；Snap→吸附（中）；Grid→网格（高）；Duplicate→复制（高）；Group→编组（中）；Ungroup→取消编组（中）；Clip→剪裁（中）；Carve→雕刻/切割（中）。

## 文件与资源（8）

Map→地图（高）；Prefab→预制件（中）；Package→包/资源包（中）；Export→导出（高）；Import→导入（高）；Save→保存（高）；Load→加载/载入（中）；Game Configuration→游戏配置（高）。

## 其他高频词（5）

Layer→图层（中，区别于 Group）；Apply→应用（高）；Fix→修复/修正（中）；Launch Engine→启动引擎/运行游戏（中）；Console→控制台（中）。

## 校阅要求

1. 每条候选必须结合 `Evidence/P2D3A_Usage_Hints.csv` 的源码用途再定
2. 同一术语在不同 context 可有不同译法，需显式记录（例如 Map 在 UV 映射语境）
3. 品牌名、类名、文件扩展名（.map/.wad）、配置键（Editor/…）、URL、HTML 标签不译
4. 低置信度项（当前 TS 无精确匹配者）仅供未来批次预备，不进入本批翻译
5. `Review_status` 全部为“待 ChatGPT 校阅”，校阅后方可冻结
