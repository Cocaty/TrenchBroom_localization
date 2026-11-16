# B01_T2_Implementation_Report — B01 18 条正式译文写入报告

日期：2026-11-16 21:56–22:20 ｜ 授权范围：仅修改 `TrenchBroom_zh_CN.ts` 的 18 条指定消息

## 一、实施前基线（实测）

- Git：feature/zh-CN-v2026.2，HEAD 4c756be1a54a…，tag v2026.2，dirty=7（授权范围）
- TS SHA-256：`83a9aa45eaef5213ee58d44bb6096bf10288aa4668da6c63ca8e154742e0a198`
- XML 解析成功；85 context / 562 message / 3 finished / 559 unfinished
- 18 个稳定 ID 全部存在且唯一；context/source/location 与 R1-A1 候选记录一致；无目标已有译文冲突、无 numerus/plural/disambiguation 结构异常
- 原有 3 条 finished（`Requires restart after changing`、`Language`、`Language changes take effect after restarting TrenchBroom.`）与目标 ID 无重叠
- 原始 TS 备份：`Evidence/TS_before_T2.ts`（SHA `83a9aa45…`）

## 二、写入结果

- **实际修改 18 条消息、18 个 `<translation>` 节点**，全部按稳定 ID 定位，未做全局字符串替换
- 每条从 `<translation type="unfinished"></translation>` 改为 `<translation>中文</translation>`（移除 unfinished 状态）
- 最终 TS SHA-256：`6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8`
- 统计：85 context / 562 message / **21 finished** / **541 unfinished**（3+18 与 559-18 精确吻合）
- 逐条 ID / source / context / 前后状态 / 前后译文：`B01_T2_Message_Audit.csv`（18 行，全部 matches_decision=True）
- 精确差异：`B01_T2_Translation_Diff.patch`

## 三、D1–D7 冻结决策落实

D1 地图文件... ✅｜D2 点轨迹文件 ✅｜D3 BSP 门户文件 ✅｜D4 不参与导出 ✅｜D5 后续独立 Layer 批次（本轮未触碰两条 UI 字符串）✅｜D6 Wavefront OBJ... ✅｜D7 放弃所有未保存的更改，并重新加载地图文件。✅。未混入任何正式备选译法。

## 四、异常与恢复（如实记录）

首次写入尝试因把相对偏移错加到绝对位置，导致 18 个消息块错位（当时 XML 仍可解析但消息数变为 544）。**立即从备份恢复**（TS SHA 回到 `83a9aa45…`），随后改为仅对 `<translation>` 标签本身使用绝对偏移替换，并在写盘前完成 XML 解析校验；第二次写入后 QA 显示 562 条消息完整、变更恰好 18 条。该异常未留下任何残留影响，也未波及其他文件。

## 五、保护边界

未运行 lupdate/lrelease、未构建、未启动 TrenchBroom、未部署、未修改 C++/CMake/资源、未修改两条 Layer UI 字符串、未翻译其他批次、未 commit/push。Git tracked diff 仍为 6 文件/81 行（与本轮前一致）；TS 位于既有未跟踪 translations/ 目录内。

## 六、结论

**B01 的 18 条中文译文已写入 TS，并通过静态结构与保护边界检查。** 本阶段不代表全项目中文化完成，也不代表运行期效果已验证；lupdate/lrelease/构建需用户另行授权。
