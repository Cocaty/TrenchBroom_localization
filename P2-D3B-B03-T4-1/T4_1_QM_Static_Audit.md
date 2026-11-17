# T4_1_QM_Static_Audit — 构建生成 QM 静态验证

## 生成来源
- 构建日志：构建开始 2026-11-17 20:51:34 +0800，结束 20:52:06 +0800，退出码 0
- 构建目录实际生成路径：`build\v2026.2-msvc145-qt6103\app\TrenchBroom\TrenchBroom_zh_CN.qm`
- 文件时间 2026-11-17 20:51:48，落入本次构建窗口；大小 6,631 B；SHA `707011a3216511d051b07d0dba249af6d834e6795a447a4f09611c6a9bd2102c`
- 与 T3 QM SHA 相同，但这是同一正式 TS 经同一默认 lrelease 行为重建的预期结果，非旧文件复制；构建前该文件为旧版 1,871 B
- 构建目录中仅发现 1 个 `TrenchBroom_zh_CN.qm`，无同名歧义

## 格式检查
QM 魔数 `3cb86418caef9c95cd211cbf60a1bddd` 有效；第 17 字节 `0xA7`。已复制构建产物到 `Artifacts/TrenchBroom_zh_CN.build.qm` 归档。

## lconvert 回转
`lconvert.exe -i <build QM> -o Artifacts\TrenchBroom_zh_CN_roundtrip.ts`，退出码 0；审计 TS 9,177 B，XML 解析成功。正式 TS 的 42 条 finished 与回转结果在 Context+Source+Translation 上 42/42 完全一致。

## 目标译文
- B01 18 + B02 1 + B03 20 = 39 条，按 Context+Source 定位：39/39 在正式 TS finished 且与冻结译文一致；39/39 在构建 QM 回转中存在且译文一致
- 另 3 条原始 finished 消息（“语言”“更改后需要重启”“语言更改将在重启 TrenchBroom 后生效。”）单独核验，3/3 一致，未计入 39 条
- 逐条结果见 `T4_1_Translation_Target_Audit.csv` 与 `T4_1_QM_Translation_Audit.csv`

**结论：构建生成 QM 的静态内容与 T2/T3 权威基线一致。**
