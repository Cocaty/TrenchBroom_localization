# B01_T2_QA_Report — 写入后静态 QA（A–F）

所有结果由独立 Python 对比原始 TS 备份与最终 TS 得出。

## A. 稳定 ID
- 18 目标 ID 全部存在且唯一；重复 (context,source)=0 ✅
- 全部 ID 的 context/source/location 与基线及候选记录一致 ✅
- message 总数 562→562，无新增/删除 ✅

## B. 译文
- 18 条译文逐条与任务冻结清单一致（18/18）✅
- 18 条全部处于已完成状态（无 `type="unfinished"`）✅
- 无备选译文残留、无遗漏、无重复写入 ✅
- finished 3→21、unfinished 559→541（恰好 +18/-18）✅

## C. 非目标消息保护
- 非目标 544 条消息逐字段完全相同（source/translation/type/location/context）✅
- 原有 3 条 finished 未被覆盖 ✅
- 其他 context/location 未变化 ✅

## D. XML 结构
- XML 解析成功；根节点 language 仍 `zh_CN`；XML 声明与 DOCTYPE 保持原样 ✅
- 编码仍 UTF-8（无 BOM），换行风格未变 ✅
- 中文字符正确保存；无意外 XML 转义 ✅

## E. 术语一致性
`.map` 保留 ✅｜`Wavefront OBJ` 保留 ✅｜`BSP` 大写保留 ✅｜“点轨迹文件”三条统一 ✅｜“BSP 门户文件”三条统一 ✅｜“不参与导出”与 tooltip 一致 ✅｜“材质集合”“实体定义”一致 ✅｜“文档”与“地图文件”语义区分 ✅｜英文三点 `...` 保留（5 条）✅｜Revert tooltip 同时保留“放弃所有未保存更改”和“重新加载地图文件” ✅

## F. 文件与边界
- 修改前后 SHA-256 已记录（见 `B01_T2_Baseline_And_Final_Hashes.txt`）✅
- 精确 diff 111 行、仅 18 个 translation 节点变化（见 patch）✅
- 实际修改 message 数 18、translation 节点数 18 ✅
- Git tracked diff 与本轮前一致（6 文件/81 行）；源码/CMake/资源未改 ✅
- 两条 Layer UI 字符串未触碰；未运行 lupdate/lrelease、未构建、未启动、未部署 ✅
- 原始 TS 可恢复副本：`Evidence/TS_before_T2.ts` ✅

## 结论
A–F 全部通过；本轮为**静态验收**，不含运行期验证。
