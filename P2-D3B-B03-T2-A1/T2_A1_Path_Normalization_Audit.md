# T2_A1_Path_Normalization_Audit — 路径规范化与重复记录审计

## 算法
1. 将 `\` 统一为 `/`。
2. 合并连续 `/`。
3. 使用 `ntpath.normpath` 解析 `.` 与 `..`，再用 `ntpath.abspath` 得到绝对规范化路径。
4. 保留两份路径：`Canonical_Path`（可读绝对路径）与小写形式 `Normalized_Path`（大小写不敏感比较键）。
5. 路径别名判断只基于完整规范化路径，不使用 basename。

## 结果
- Start Snapshot：13 行原始记录，13 个唯一逻辑文件
- Final Snapshot：23 行原始记录，**22 个唯一逻辑文件**
- 重复记录：Start 0 组；Final **1 组**

### 重复记录（Final）
同一规范化路径：
`C:/Users/yoshi/Projects/TrenchBroom-zhCN/reports/P2-D3B-B03-T2/Backup/TrenchBroom_zh_CN.ts.before`

两条原始路径：
- `C:/Users/yoshi/Projects/TrenchBroom-zhCN\reports\P2-D3B-B03-T2\Backup\TrenchBroom_zh_CN.ts.before`（对象 `备份TS`，verdict `YES`）
- `C:/Users/yoshi/Projects/TrenchBroom-zhCN/reports/P2-D3B-B03-T2\Backup\TrenchBroom_zh_CN.ts.before`（对象 `T2/Backup/...`，verdict `NEW`）

两者仅 `reports` 后的分隔符不同（`/` vs `\`），规范化后完全相同，文件真实存在、大小 131,100 B、SHA256 均为 `901554891f322ed8…`。

**结论：备份 TS 是 Start Snapshot 中已存在的保护对象，Final Snapshot 的 `NEW` 分类属于重复路径记录错误，应重新归类为 `YES`。** 本轮未修改原始快照，仅在 `T2_A1_Duplicate_Path_Audit.csv` 与 `T2_A1_Snapshot_Reconciliation.csv` 中记录正确分类 `DUPLICATE_ALIAS`/逻辑 `YES`。

## 规范化后的逻辑分类
| 分类 | 数量 |
|---|---:|
| YES | 11 |
| EXPECTED_CHANGE（正式 TS） | 1 |
| NEW | 8 |
| LATE_DISCOVERED（实际 QRC） | 1 |
| DUPLICATE_ALIAS（备份 TS） | 1 |
| MISSING / UNRESOLVED | 0 / 0 |
| 合计唯一逻辑文件 | 22 |

原始 T2 Final Snapshot 的 `NEW=9` 是把备份 TS 重复计入所致；规范化后有效新增为 8。
