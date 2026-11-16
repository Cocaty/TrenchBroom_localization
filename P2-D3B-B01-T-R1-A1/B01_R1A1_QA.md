# B01_R1A1_QA — 三项修正与保护边界独立核验

## A. 基线与保护
| 检查 | 实测 | 判定 |
|---|---|---|
| 分支 / HEAD / tag | feature/zh-CN-v2026.2 / 4c756be1… / v2026.2 | PASS |
| TS SHA-256 | 83a9aa45…（前后相同） | PASS |
| R1 / R1-A 原始 SHA 清单 | 各 8 项全部 OK | PASS |
| 新目录独立创建 | reports/P2-D3B-B01-T-R1-A1 | PASS |
| 源码 / CMake 未修改 | git dirty=7 与基线一致 | PASS |

## B. 源码证据（按固定 HEAD 逐行读取）
- MapView2D.cpp **L284** `moveCameraToPosition(pointTrace->currentPoint(), true);` — PASS
- MapView3D.cpp **L462** `currentPoint()` 位置计算、**L463** `currentDirection()` — PASS
- PointTrace.h **L46** `currentPoint()`、**L47** `currentDirection()` — PASS
- Glossary Source Evidence 使用 284 / 462-463 / 46-47；R1-A1 文档无旧 `282`/`460` 行号残留 — PASS

## C. Point File
推荐“点轨迹文件”、正式备选“点位文件”、背景术语“泄漏点文件”（独立字段）；三条动作推荐/备选名词统一；提案 CSV/MD、术语表、决策记录中**无**“如用备选需确认‘泄漏’语义”残留；未新增 Point 决策项 — PASS

## D. Load / Reload / Unload
Glossary 末行 Formal Alternative 已清空，Notes 明确标记“历史备选方案：载入 / 重载 / 取消加载。本轮不作为 RA-B01 正式候选”；六条 Point/Portal 动作的正式备选精确为“加载/重新加载/卸载点位文件|BSP 门户文件（门户文件）”；无 D8 — PASS

## E. 18 条候选
ID / source / context 与 R1-A 完全一致；推荐译文与正式备选译文未发生变化（仅 Load Point File 的 Technical Preservation 字段按授权修正）；Markdown 由最终 CSV 直接生成且 18 行逐字段一致；无重复、缺失、新增 — PASS

## F. 决策记录与跨批次依赖
User_Decision_Record_R1A1.md 与 Cross_Batch_Dependencies_R1A1.md 与 R1-A **逐字相同**（D1–D7 原样继承、全部待用户确认、D4/D5 独立、两条 Layer UI 字符串仍不属于 RA-B01 18 条）— PASS

## G. 操作边界与哈希
未运行 lupdate/lrelease、未构建、未启动、未部署；SHA256SUMS 从实际目录枚举生成、不含自身，生成后全部校验通过（结果见下方复核记录）。

**SHA 复核记录（生成后实测）**：SHA256SUMS 覆盖 **9** 项、自哈希条目 **0**、`sha256sum -c` 校验 **9/9 OK**。

## 检查器误报说明
初次自动检查有两处 FAIL：① 旧短语仅出现在 `B01_R1A1_Correction_Report.md` 的“修订前”示例中（候选提案/术语表/决策记录中已无残留）；② 动词组检查错误地覆盖了 Document 系列备选（如“新建地图文档”）。收窄到授权字段后两项均为 PASS——属检查器范围过宽，非交付物缺陷。
