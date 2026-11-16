# B01_R1A1_Correction_Report — 三项修正说明

基线：HEAD 4c756be1… / tag v2026.2 / TS SHA `83a9aa45…`；R1 与 R1-A 原始 SHA 清单均 8 项校验通过、未被修改。本轮仅在独立新目录生成 R1-A1 副本。

## 修正一：Point File 源码证据行号

固定 HEAD 下**逐行只读核对**（非字符串替换）：

| 文件 | 实际行 | 实际代码 | R1-A 旧引用 | R1-A1 新引用 |
|---|---|---|---|---|
| MapView2D.cpp | L284 | `moveCameraToPosition(pointTrace->currentPoint(), true);` | 282（旧报告） | **284** |
| MapView3D.cpp | L462 | `const auto position = pointTrace->currentPoint() + ...;` | 460（旧报告） | **462** |
| MapView3D.cpp | L463 | `const auto direction = pointTrace->currentDirection();` | 未单列 | **462-463** |
| PointTrace.h | L46 | `const vm::vec3f& currentPoint() const;` | L46 | **L46** |
| PointTrace.h | L47 | `const vm::vec3f currentDirection() const;` | 未单列 | **L47** |

已同步到 `B01_Glossary_Proposal_R1A1.csv`（Point File 的 Source Evidence）与修订说明文档；其他 R1-A1 文档无旧行号残留。

## 修正二：Point File 正式备选残留“泄漏语义”

| 位置 | 修订前 | 修订后 |
|---|---|---|
| `B01_Translation_Proposal_R1A1.csv`（ID c87e891f3904，Load Point File... 的 Technical Preservation） | `... 风格；如用备选需确认“泄漏”语义` | `保留原始动作省略号风格；正式备选“点位文件”为中性名称，不附加泄漏含义。` |
| 由该 CSV 生成的 R1A1 Markdown | 同步旧表述 | 同步新表述 |

未改变：推荐术语“点轨迹文件”、正式备选“点位文件”、背景术语“泄漏点文件”；未把泄漏语义提升到正式备选字段；未新增 Point 决策项。

## 修正三：Load / Reload / Unload 动词组备选口径

| 位置 | 修订前 | 修订后 |
|---|---|---|
| `B01_Glossary_Proposal_R1A.csv` 末行（Load / Reload / Unload） | Formal Alternative = `载入 / 重载 / 取消加载` | Formal Alternative = **空**；Notes 记录：“历史备选方案：载入 / 重载 / 取消加载。本轮不作为 RA-B01 正式候选，也不需要用户单独确认。18 条候选的正式备选采用加载 / 重新加载 / 卸载，与推荐动词组一致。” |

18 条译文候选中的正式备选字段原本就采用“加载 / 重新加载 / 卸载”，**未改动**；Markdown 中无其他位置把旧动词组列为当前正式备选；未新增 D8。

## 明确未变化的内容

- 18 条 ID / source / context、推荐译文、正式备选译文（除上述技术说明字段）
- D1–D7 决策记录（原样继承）、D4/D5 拆分与两条 Layer UI 字符串的批次范围
- 推荐术语方案、推荐与正式备选的区别、所有未冻结状态
- TS / 源码 / CMake；未运行 lupdate/lrelease、未构建、未启动、未部署
