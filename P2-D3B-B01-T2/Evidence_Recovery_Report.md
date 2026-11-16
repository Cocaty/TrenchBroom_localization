# Evidence_Recovery_Report — P2-D3B-B01-T2-E1 最终 TS 证据恢复与核验

日期：2026-11-16 22:09 ｜ 任务：确认当前 TS 为 T2 最终版本并补充 `Evidence/TS_after_T2.ts`

## 一、第一阶段只读核验结果（全部通过）

- Git：feature/zh-CN-v2026.2，HEAD 4c756be1a54a28d921d18c77716a5f170bdc31d0，tag v2026.2，dirty=7（与 T2 基线一致）
- 当前 TS：`src\TrenchBroom\app\TrenchBroom\translations\TrenchBroom_zh_CN.ts` 存在
- 大小 **131,106 B**；mtime **2026-11-16 21:58:12 +0800**（与 T2 写入时刻一致，之后无修改）
- SHA-256 **6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8** ——与 T2 历史预期值**完全一致**
- XML 解析成功；根节点 language=`zh_CN`；`<?xml version="1.0" encoding="utf-8"?>` 与 `<!DOCTYPE TS>` 保持
- 编码 UTF-8 无 BOM；CRLF=0、LF=3,151（原格式未变）
- 统计：85 context / 562 message / **21 finished** / **541 unfinished**
- 18 个 T2 目标 ID 全部存在且唯一；译文与 D1–D7 冻结决策逐条一致，均已完成
- 544 条非目标消息与 `TS_before_T2.ts` 逐字段一致（source/translation/type/location/context）
- 结论：**不存在 T2 完成之后的其他修改；路径 A 成立**

## 二、补证操作（仅路径 A 允许的操作）

- 以 `cp` **原样字节复制**当前 TS 至 `reports\P2-D3B-B01-T2\Evidence\TS_after_T2.ts`
- 未重新序列化 XML，未改变编码、换行、空格或任何字节
- 源文件 SHA-256 = `6582a38280e7ac1c…`
- 副本 SHA-256 = `6582a38280e7ac1c…`（**完全一致**）
- `cmp -s` 结果：**identical**；大小 131,106 B = 131,106 B
- 副本 SHA 亦等于历史预期值 `6582a38280e7ac1c45bc5dcf12575bd4235e0502f5543e27b3daed2c5d2c72d8`

## 三、SHA256SUMS 更新

清单从 T2 报告目录**实际枚举**生成，排除清单自身；覆盖原有全部文件（报告、CSV、patch、哈希记录、原始备份 `TS_before_T2.ts`）并**新增** `Evidence/TS_after_T2.ts` 条目；生成后逐项校验全部 OK。旧证据未删除、未覆盖。

## 四、边界与未执行事项

本轮未修改 TS 源文件、C++/CMake/资源、其他翻译文件；未运行 lupdate/lrelease；未构建、未启动、未部署；未提交 Git；未回滚或重建 TS；未修改 T2 原始报告/CSV/diff/备份；未开始 T3。写入操作仅限：新增 `Evidence/TS_after_T2.ts`、新增本报告、更新 SHA256SUMS.txt。

## 五、文件前后哈希与大小记录

| 文件 | SHA-256 | 大小 |
|---|---|---|
| 当前 TS（源） | 6582a38280e7ac1c… | 131,106 B |
| Evidence/TS_after_T2.ts（副本） | 6582a38280e7ac1c… | 131,106 B |
| Evidence/TS_before_T2.ts（原有备份） | 83a9aa45eaef5213… | 130,964 B |

## 六、结论

**PASS：最终 TS 已确认并补齐证据。** 本轮完成后立即停止。
