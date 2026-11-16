# Batch_Integrity_Audit — 559 条 unfinished 批次唯一性独立校验

校验方法：**独立于批次生成代码**，重新读取 `Revised_Message_Index.csv` 与 `Revised_Batches.csv`，用集合/计数器重新计算。

| 校验项 | 实测 | 判定 |
|---|---|---|
| TS 消息总数 | 562 | ✅ |
| finished / unfinished | 3 / 559 | ✅ |
| 批次数 | 24（RA-B01…RA-B24） | ✅ |
| 已分配 ID 总数 | 559 | ✅ |
| 唯一 ID 数 | 559 | ✅ |
| 遗漏（unfinished 未分配） | 0 | ✅ |
| 重复分配 | 0 | ✅ |
| finished 误入批次 | 0 | ✅ |
| 超过 45 条的批次 | 0 | ✅ |
| 重复 (context,source) | 0 | ✅ |
| ID 碰撞 | 0 | ✅ |
| ID 与 SHA256(context+source)[:12] 不一致 | 0 | ✅ |

## 批次结果（24 批）

RA-B01 文件操作 18 ← **修正后第一批候选**；RA-B02 主菜单 1；RA-B03 对话框 20；RA-B04 提示 6；RA-B05 偏好 30；RA-B06–B09 2D（45/45/45/32）；RA-B10 3D 1；RA-B11 工具快捷 15；RA-B12–B13 几何（45/2）；RA-B14–B15 实体（45/4）；RA-B16–B17 材质（45/22）；RA-B18–B19 游戏配置（45/23）；RA-B20 错误 3；RA-B21 其他/待确认 8；RA-B22–B23 UNKNOWN（45/11）；**RA-B24 隔离待确认 3**（含 AppController 的 Open Map，禁止进入 B01）。

## 约束

- UNKNOWN（RA-B22/B23）、其他/待确认（RA-B21）、隔离（RA-B24）均标阻塞，不进入普通翻译批次
- 核心术语批次（RA-B12–B17）须待术语表校阅冻结
- 6 个被移出 B01 的 ID：3 个在 RA-B24 隔离、3 个在 RA-B18 游戏配置——均在普通 B01 之外，未遗漏
