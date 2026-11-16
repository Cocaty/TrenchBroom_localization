# 09_AI_Translation_Handoff_Guide — 后续 AI 翻译交接规范（WorkBuddy ↔ ChatGPT）

## 协作流程（冻结）

1. WorkBuddy 按批读取 TS 与源码上下文 → 初步翻译 → 生成完整 TS + 变更报告
2. ChatGPT 独立校阅：术语一致性、占位符完整性、语气与自然度、UI 场景适配
3. WorkBuddy 按校阅意见修订，输出修订版 TS + 修订说明
4. ChatGPT 复核修订结果；通过后该批译文**冻结**，后续批次不得随意改写
5. 冻结批次的 message ID 与译文进入基线记录，供后续批次对账

## 每批开始前（WorkBuddy 必做）

- 只处理 `08_Batch_Translation_Plan.md` 指定的批次（ID 清单见 `Evidence/P2D3A_Batches.csv`）
- 备份当前 TS（带批次编号，如 `TS_before_B10.ts`），记录 SHA-256
- 核对基线：562 条 / 85 context / 本批 ID 全部 unfinished

## 翻译硬约束（12 项）

1. 仅翻译本批消息；不修改其他已完成译文
2. 不修改源码、CMake、构建产物、用户配置
3. 不改变 context 与 source 的任何字符（含空格）
4. 不丢失 location（含多 location 条目；本批 8 条多 location 需原样保留）
5. 保留 `%1`/`%2` 等全部占位符（58 条相关消息），集合与编号一致
6. 保留按键标识（4 条 Ctrl/Shift/Alt/功能键），不机械翻译
7. 保留文件扩展名（.map/.wad）、URL、HTML 标签、配置键（Editor/…）、类名、品牌名（5 条技术标识）
8. 歧义词按 `07` 术语表候选并结合本批源码上下文确定；不确定则列入 Uncertain，不猜测
9. 不新增/删除 message，不把 obsolete 条目带入
10. 输出**完整 TS**（非片段），路径与编码/换行风格与基线一致
11. 输出 `Translation_Diff.md`：逐条 ID / source / 旧译文 / 新译文 / 变更原因
12. 输出 `Translation_Terminology.md`（本批术语决策）、`Translation_QA.md`（占位符/技术标识自动校验结果）、`Uncertain_Translations.md`、`SHA256SUMS.txt`

## ChatGPT 校阅清单

- 占位符集合一致性（逐条自动比对源文/译文）
- 术语一致性（跨 batch 的同一 English 是否译法一致；例外是否在 Terminology 文档说明）
- 自然度与语气（菜单短、提示友好、错误明确，不带翻译腔）
- UI 适配（短标签不宜过长；长错误句语序自然）
- 冻结条目是否被误改（对比基线 SHA 与 message ID）

## 对账与验收

- 修改前后消息数、context 数、finished 数逐项对账（基线 562/85/3）
- 已完成译文逐字比对（本轮 3 条）
- 新译文条数 = 本批 ID 数；无跨批修改
- Evidence 清单从实际目录枚举生成；SHA256SUMS 覆盖全部正式证据且不含自身

## 禁止

- 不运行 lupdate/lrelease（除非用户另行授权）
- 不启动程序做视觉验收（除非用户另行授权运行期测试）
- 不把 ChatGPT 校阅意见直接写入 TS 而不留变更记录
