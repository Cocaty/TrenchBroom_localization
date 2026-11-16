# Final_Review_Report — P2-D3B-B01-T 译文预审最终结论

日期：2026-11-16 21:23–21:45 ｜ 只读预审；TS/源码/CMake 未修改；未运行翻译工具、未构建、未启动、未部署

## 一、交付物

| 文件 | 内容 |
|---|---|
| B01_Translation_Proposal.md / .csv | 18 条逐条译文候选（ID/context/source/中文/备选/理由/技术保留/Decision） |
| B01_Source_Context_Audit.csv | 18 条源码证据（函数/动作路径/ActionContext/handler/位置/分类/裁决） |
| B01_Glossary_Proposal.csv | 17 行 B01 专用术语表（推荐 6 / 待用户确认 9 / 保留原文 2） |
| B01_Technical_Preservation_Audit.md | `.map`、Wavefront OBJ、Omit From Export、`...`、过滤器等保留策略 |
| B01_Translation_QA.md | 18 条独立核验（全部通过预审级别） |
| SHA256SUMS.txt | 实际枚举生成、不含自身 |

## 二、结论摘要

- **9 条普通文件操作**：已给出正式候选（新建/打开/保存/文档另存为/地图文件.../重新加载材质集合/重新加载实体定义/还原文档/关闭文档），Document 译法统一，Save as 未误译为导出
- **9 条待确认**：Wavefront OBJ 建议保留原文（是否加“文件”待定）；`.map` 必须原样保留且明确“标记为 Omit From Export 的图层不导出”；Point File 候选“点位文件/泄漏点文件”、Portal File 候选“门户文件/BSP 门户文件”（均非网页门户）；Revert tooltip 明确“放弃全部未保存更改 + 重新加载磁盘地图文件”
- **技术保留**：18 条无 Qt 占位符；6 项技术内容有明确保留策略
- **QA**：18/18 ID 存在、source 与 TS 逐字一致、无跨批次混入、每条均有候选——预审级通过

## 三、尚需用户决定的事项

1. 9 条待确认术语/译文是否按推荐候选定稿（尤其 Point File、Portal File 的命名）
2. `Omit From Export` 图层属性 UI 文本是否纳入后续批次并与本 tooltip 同步
3. “Wavefront OBJ...”是否补“文件”二字
4. 是否授权进入正式翻译实施阶段（本轮**不自动授权**）

## 四、停止声明

本轮完成后立即停止：未修改 TS、未翻译入库、未运行 lupdate/lrelease、未构建、未启动程序、未部署。等待用户审阅并明确授权。
