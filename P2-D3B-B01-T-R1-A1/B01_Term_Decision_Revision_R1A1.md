# R1-A1 文档修订说明（继承 R1-A，仅同步源码行号与备选口径）

# B01_Term_Decision_Revision_R1A — 术语备选口径统一修订说明

基线：HEAD 4c756be… / TS SHA `83a9aa45…`；R1 原始 9 份交付物存在且其 SHA256SUMS 8 项校验通过。本轮只生成独立 R1-A 副本文档，未改动 R1 原始文件。

## R1 → R1-A 差异总览

| 项 | R1 | R1-A |
|---|---|---|
| Point File | 推荐“点轨迹文件”；备选“点位文件”；“泄漏点文件”散见于理由字段 | **分字段**：推荐=点轨迹文件；正式备选=点位文件；背景术语=泄漏点文件（不作候选） |
| Portal File | 推荐“BSP 门户文件”；备选“门户文件”；解释性说法混在理由中 | **分字段**：推荐=BSP 门户文件；正式备选=门户文件；解释性术语=BSP 可见性门户文件（不作候选） |
| Omit From Export | 术语选择与图层 UI 范围部分混合 | 拆为 **D4（术语：不参与导出 / 不导出）** 与 **D5（图层 UI 翻译范围）** 两个独立决策 |
| 用户决策记录 | D1–D7，部分备选含解释性/背景词 | D1–D7 每项的“推荐/正式备选”严格分开，背景/解释性术语不进备选字段 |
| 18 条译文 | ID/source/context 不变 | 完全继承；仅推荐/备选文案按上述口径统一 |

## Point File 统一口径

| 类型 | 术语 |
|---|---|
| 英文原文 | Point File |
| 推荐中文 | **点轨迹文件** |
| 正式备选 | **点位文件** |
| 背景术语 | 泄漏点文件（仅历史/调试背景解释，不作正式候选） |

三条动作：加载点轨迹文件... / 重新加载点轨迹文件 / 卸载点轨迹文件；正式备选分别为加载/重新加载/卸载点位文件（...）。源码证据（本次重新只读确认行号）：`MapWindow.cpp:1196`（`*.pts *.lin`）、`PointTrace.h:16-40`（点序列结构；L46 currentPoint()、L47 currentDirection()）、`MapView2D.cpp:284` 与 `MapView3D.cpp:462-463`（按 currentPoint/currentDirection 定位）、`ActionManager.cpp:886-907`（Load/Reload/Unload handler）。**不暗示源码已证明所有 Point File 都是泄漏点文件。**

## Portal File 统一口径

| 类型 | 术语 |
|---|---|
| 英文原文 | Portal File |
| 推荐中文 | **BSP 门户文件** |
| 正式备选 | **门户文件** |
| 解释性术语 | BSP 可见性门户文件（仅解释技术含义） |

三条动作：加载 BSP 门户文件.../重新加载 BSP 门户文件/卸载 BSP 门户文件；正式备选为加载/重新加载/卸载门户文件（...）。源码证据：`PortalFile.cpp:43-55`（PRT1 解析，L55 格式码）、`MapWindow.cpp:1237`（`*.prt`）、`MapDocument.cpp:326`（`canLoadPortalFile`）、`ActionManager.cpp:918-938`（三动作）。非网页门户；**无运行期 UI 实测**，“BSP 门户文件”菜单长度风险仍为预测，未验证。

## Omit From Export 拆分

D4 仅决定术语：推荐“不参与导出”，正式备选“不导出”。D5 仅决定图层 UI 翻译范围：推荐后续独立 Layer 批次同步翻译两条 UI 字符串；备选暂时保留英文（此时 tooltip 也必须保留英文属性名 `Omit From Export`，不得宣称已全局统一）。两条 UI 字符串均**不属于** RA-B01 18 条，本轮不修改 TS。

## 其他

Document 统一“文档”、Save as 为“另存为”、Map... 为 Export 格式项、Wavefront OBJ 默认保留原文、Revert tooltip 语义不变；以上不作为新增决策项。
