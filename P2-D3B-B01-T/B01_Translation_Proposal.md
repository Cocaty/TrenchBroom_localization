# B01_Translation_Proposal — RA-B01 18 条译文预审（逐条）

唯一字符串基准：原始 TS（SHA-256 `83a9aa45eaef5213ee58d44bb6096bf10288aa4668da6c63ca8e154742e0a198`，与本轮基线一致）。18 条 source 与 TS 逐字核对通过；ID 取自 R1-A 稳定 ID。完整机器可读版：`B01_Translation_Proposal.csv`。

## 第一组：9 条允许翻译（Decision=推荐）

| ID | English | Chinese Candidate | Alternative | Rationale | 技术保留 |
|---|---|---|---|---|---|
| bcf80284ebf3 | New Document | 新建文档 | 新建地图文档 | `newDocument()`；Windows UI 通用 | 无 |
| 0843baa95d90 | Open Document... | 打开文档... | 打开地图文档... | `openDocument()`；保留 `...` | `...` |
| 08c86abe1b99 | Save Document | 保存文档 | 保存地图文档 | `saveDocument()`；Document 统一“文档” | 无 |
| c13f05ee9b4e | Save Document as... | 文档另存为... | 另存文档为... | `saveDocumentAs()`；**不是导出** | `...` |
| 88c5a8202a53 | Map... | 地图文件... | Map 文件... | `Menu/File/Export/Map...`，`exportDocumentAsMap()`；是导出格式项，不宜直译“地图” | `...` |
| 3dab7bfca406 | Reload Material Collections | 重新加载材质集合 | 重载材质集 | File 菜单资源重载；指材质资源集合 | 无 |
| 1e1111c64470 | Reload Entity Definitions | 重新加载实体定义 | 重载实体定义 | File 菜单资源重载；与术语表一致 | 无 |
| e6acb688ec6e | Revert Document | 还原文档 | 恢复文档 | `revertDocument()`；与同语句 tooltip 语义一致 | 无 |
| aa1646cea36e | Close Document | 关闭文档 | 关闭地图文档 | `closeDocument()`；Document 系列统一 | 无 |

**一致性约束**：Document 在以上 6 条中统一译“文档”；Save as 不写“导出”；Map... 以“文件”收尾体现 Export 子菜单格式项。

## 第二组：9 条需术语确认（Decision=待用户确认）

| ID | English | Chinese Candidate | Alternative | 关键理由 / 待确认点 |
|---|---|---|---|---|
| e7c5ab696447 | Wavefront OBJ... | Wavefront OBJ... | Wavefront OBJ 文件... | 技术格式名，ObjExportDialog 标题 `Export Wavefront OBJ`；默认保留原文，是否加“文件”由用户定 |
| 8626a59ed64f | Exports the current map to a .map file. Layers marked Omit From Export will be omitted. | 将当前地图导出为 .map 文件。标记为“Omit From Export”的图层将被忽略。 | …标记为“不导出”的图层将被省略。 | `.map` 原样；`Omit From Export` 是 LayerEditor.cpp:99 图层属性/勾选文本，当前 UI 未翻译——是否同步翻译该 UI 标签需决定 |
| c87e891f3904 | Load Point File... | 加载点位文件... | 加载泄漏点文件... | PointTrace 点序列 + 2D/3D 定位；过滤器 `*.pts *.lin`；“泄漏点”更贴近调试语义但源码无 leak 文案，须确认 |
| fe79d727b01f | Reload Point File | 重新加载点位文件 | 重载点位文件 | 与 Load/Unload 动词组一致 |
| d4365ad643a4 | Unload Point File | 卸载点位文件 | 取消加载点位文件 | 动词组一致性待确认 |
| c18158cfc475 | Load Portal File... | 加载门户文件... | 加载 BSP 门户文件... | `.prt` PRT1 门户多边形（BSP 可见性），非网页门户；备选更精确但菜单更长 |
| 8c049a323d0f | Reload Portal File | 重新加载门户文件 | 重载门户文件 | 与 Portal File 术语联动 |
| 92939021173f | Unload Portal File | 卸载门户文件 | 取消加载门户文件 | 与 Portal File 术语联动 |
| d82719c1af53 | Discards any unsaved changes and reloads the map file. | 放弃所有未保存的更改，并重新加载地图文件。 | 丢弃所有未保存更改并重新载入地图文件。 | 与 `Revert Document` 同一 addAction 语句；必须同时表达“全部未保存更改被丢弃”与“从磁盘重新载入地图”，不得弱化 |

## 说明

- 所有译文均为**候选**，本轮未写入 TS，未冻结任何术语
- 保留原文 `...`（ASCII 三点）风格
- 无 Qt 占位符（本批 18 条 `%1/%2` 均为空）
