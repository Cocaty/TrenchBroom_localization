# T2_A1_Final_Report — T2 快照路径与证据一致性审计

## 结论：**PASS WITH LIMITATIONS**

路径、重复记录、SHA256SUMS 与保护对象审计均完成。发现一项**可解释的历史记录错误**：T2 Final Snapshot 把已存在的备份 TS 重复记录为 NEW；不影响 T2 正式 TS 写入结果，但 T2 原始统计需要勘误（本轮不改原始文件）。

## 范围与时间
- 开始：2026-11-17 20:24:05 +0800；结束：2026-11-17 20:25:04 +0800
- 只读审计输入：T2 Start/Final Snapshot、T2 SHA256SUMS、执行/差异/基线/写入审计、前后目标审计、备份 TS、U3 冻结矩阵、正式 TS
- 未修改正式 TS、源码、QRC、T2/U3 原始文件或任何历史报告

## 路径与分类
规范化算法见 `T2_A1_Path_Normalization_Audit.md`。Start 13 行=13 唯一逻辑文件；Final 23 行=**22 唯一逻辑文件**；Final 有 1 组重复路径。

| 分类 | 数量 |
|---|---:|
| YES | 11 |
| EXPECTED_CHANGE（正式 TS） | 1 |
| NEW | 8 |
| LATE_DISCOVERED | 1 |
| DUPLICATE_ALIAS（备份 TS） | 1 |
| MISSING / UNRESOLVED | 0 / 0 |

备份 TS 专项：两条记录规范化路径相同、大小 131,100 B、SHA256 均为 `901554891f322ed8…`，文件真实存在。明确结论：**备份 TS 是 Start Snapshot 中已存在的保护对象，Final Snapshot 的 NEW 分类属于重复路径记录错误，应重新归类为 YES。**

正式 TS：Start SHA `901554891f…` → Final SHA `f021e509c…`，属于授权写入导致的 EXPECTED_CHANGE；当前实测仍为 `f021e509cf9a8679eeda64624df0f5474335c0872f73940e1d48ef77447a261a`，132,589 B。

## T2 SHA256SUMS
10 条清单路径全部存在、格式有效、实际 SHA256 全部 PASS；T2 目录 10 个应归档文件（不含清单自身）全部覆盖；无重复、无缺失、清单未自列。

## 保护状态
正式 TS、CMakeLists、app CMake、实际 QRC、原版 Release 均与 T2 Final Snapshot 一致；Git feature/zh-CN-v2026.2、HEAD `4c756be1…`、dirty=7 未变。详见 `T2_A1_Protected_State_Audit.csv`。

## 发现的问题与建议
1. Final Snapshot 中备份 TS 被重复计入 NEW；建议在后续独立勘误轮次修正 T2 统计（本轮不改原始文件）。
2. 原始 Final Snapshot 的分类统计应改为：YES 12（含备份 TS 的正确逻辑分类）、EXPECTED_CHANGE 1、NEW 8、LATE_DISCOVERED 1，唯一逻辑文件 22。

## GitHub 链接
本轮未上传或发布 A1 材料；无可验证的 GitHub 目录链接，不虚构 URL。本地目录：`reports\P2-D3B-B03-T2-A1\`。

**本轮停止：未运行 lrelease、未构建、未启动、未部署、未提交 Git，未进入 T3。**
