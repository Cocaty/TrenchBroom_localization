# B01_Term_Decision_Revision — 术语决策修订总说明

基线：HEAD 4c756be… / tag v2026.2 / TS SHA `83a9aa45…` ——重新实测通过；原始 P2-D3B-B01-T 8 份交付物完整。本轮只修订文档与决策口径，**未写入 TS，未冻结任何术语**。

## 修订前后决策状态对照

| 项 | 原提案 | 原术语表 | R1 统一后 |
|---|---|---|---|
| Map... | 地图文件... / Decision=推荐 | 地图文件... / Decision=待用户确认 | **两侧均为“推荐”**（本轮建议，未冻结，待用户最终确认） |
| Point File（3 动作） | 点位文件 / 待用户确认 | 点位文件 / 待用户确认 | **点轨迹文件**（备选 点位文件）/ 推荐，待用户确认 |
| Portal File（3 动作） | 门户文件 / 待用户确认 | 门户文件 / 待用户确认 | **BSP 门户文件**（备选 门户文件）/ 推荐，待用户确认 |
| Omit From Export | Omit From Export 引用 / 待用户确认 | Omit From Export / 待用户确认 | **不参与导出** / 推荐，存在跨批次依赖，待用户确认 |
| Wavefront OBJ | 保留原文 A / 待用户确认 | 保留原文 / 保留原文 | **A：Wavefront OBJ...**（备选 B：Wavefront OBJ 文件...）/ 推荐，待用户确认 |

## 逐项依据与风险

### 1. Map... → 地图文件...（Decision=推荐）
源码：`ActionManager.cpp` `Menu/File/Export/Map...`，handler `exportDocumentAsMap()`，同语句 tooltip 说明导出为 `.map`。属于 Export 子菜单格式项；与 `Save Document as...`（另存文档为...）语义分离，**不得混为导出/另存**。风险：用户可能偏好“Map 文件...”保留格式名，已列为备选。

### 2. Point File → 点轨迹文件
源码证据：
- `MapWindow.cpp:1196`：`Point files (*.pts *.lin);;Any files (*.*)`
- `PointTrace.h:16-40`：`std::vector<vec3f> m_points` + `m_current`，`currentPoint()` / `currentDirection()` / `advance()` / `retreat()`
- `MapView2D.cpp:284`：`moveCameraToPosition(pointTrace->currentPoint(), true)`；`MapView3D.cpp:460+` 类似定位
- `ActionManager.cpp:886-907`：Load/Reload/Unload 三个动作与 handler

**直接可证**：文件含点序列；视图可沿点序列定位。**推测/背景**：可能与地图泄漏调试相关——源码未见 leak 文案，故“泄漏点文件”只作背景术语记录，**不作为默认译名**。三动作统一名词“点轨迹文件”。“点轨迹”比“点位”更准确表达序列特征。

### 3. Portal File → BSP 门户文件
源码证据：
- `PortalFile.cpp:55` PRT1 文件头解析（另有 PRT1-AM，L82）
- `MapWindow.cpp:1237`：`Portal files (*.prt);;Any files (*.*)`
- `MapDocument.cpp:326`：`canLoadPortalFile()` 加载能力判断
- `ActionManager.cpp:918-938`：Load/Reload/Unload handler

**直接可证**：`.prt` PRT1 门户多边形数据，与 BSP 可见性相关；**非网页门户**。风险：菜单项“加载 BSP 门户文件...”比“加载门户文件...”长；本轮不因长度删减技术语义，长度风险留待 UI 实测。

### 4. Omit From Export → 不参与导出（跨批次依赖）
源码证据：`Layer.h:39 m_omitFromExport`；`LayerEditor.cpp:99 tr("Omit From Export")`（图层右键菜单标签）；`LayerListBox.cpp:54 tr("Toggle omit from export")`；本批 tooltip 位于 `ActionManager.cpp:878`。tooltip 候选：

> 将当前地图导出为 .map 文件。标记为“不参与导出”的图层将被忽略。

依赖：tooltip 是对 UI 属性名的引用；图层属性标签与切换提示尚未翻译，需同术语组处理（详见 `B01_Cross_Batch_Dependencies.md`）。**本轮不把这两个源码字符串加入 RA-B01 18 条**。

### 5. Wavefront OBJ → A 方案（保留原文）
源码证据：`ActionManager.cpp:863-864` 导出动作；`ObjExportDialog.cpp:66 tr("Export Wavefront OBJ")`、L137 `tr("Export Wavefront OBJ file")`；`Polyhedron::exportObj()`。默认 A：`Wavefront OBJ...`（格式名精确、菜单短）；备选 B：`Wavefront OBJ 文件...` 保留在术语表。不得译为“对象/实体”。

## 一致性复核

其余 9 条候选保持原状；Document 统一“文档”、Save as 为“另存为”、Map... 体现 Export 格式项、Revert Document 与 tooltip 语义一致、`...` 为 ASCII 三点、`.map`/Wavefront OBJ 未丢失。`B01_Translation_Proposal_R1.md` 由同名 CSV 直接生成，二者逐条一致。
