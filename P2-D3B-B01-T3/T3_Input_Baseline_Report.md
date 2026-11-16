# T3_Input_Baseline_Report — 输入只读核验（T3-1）

- Git：feature/zh-CN-v2026.2，HEAD 4c756be1a54a28d921d18c77716a5f170bdc31d0，tag v2026.2，dirty=7（授权既有范围）
- 工作区状态：6 个 tracked 修改（P2-D2B/D2C-B 既有）+ 未跟踪 translations/；本轮未新增其他变化
- 正式 TS：`app\TrenchBroom\translations\TrenchBroom_zh_CN.ts`，131,106 B
- T2 证据 TS：`reports\P2-D3B-B01-T2\Evidence\TS_after_T2.ts`，131,106 B
- 两份 TS SHA-256 **均为** `6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8` ——与历史预期值完全一致
- XML 解析成功；language=`zh_CN`；声明 `<?xml version="1.0" encoding="utf-8"?>` + `<!DOCTYPE TS>`；UTF-8 无 BOM；CRLF=0 / LF=3,151
- 统计：85 contexts / 562 messages / **21 finished** / **541 unfinished**（与预期完全一致）
- 18 个 B01 目标 ID：全部存在且唯一；译文与 T2 冻结 D1–D7 逐条一致、均为完成状态

**结论：路径 A（输入有效）成立，允许进入 lrelease 编译。**
