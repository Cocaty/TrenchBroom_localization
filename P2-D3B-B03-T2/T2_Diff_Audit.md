# T2_Diff_Audit — 正式 TS 写入差异审计

## 对比对象
- 写入前：`Backup/TrenchBroom_zh_CN.ts.before`（SHA `901554891…`）
- 写入后：`src\TrenchBroom\app\TrenchBroom\translations\TrenchBroom_zh_CN.ts`（SHA `f021e509…`）

## 实际修改的 20 个目标消息
以下每条仅 translation 文本与状态由 unfinished 变为 finished；Message_ID、Context、Source、Location、Comment、节点顺序均未变：

`f9081511b752`（路径类型）、`2c01921052f7`（选择路径类型）、`8c9ed2e8de12`（绝对路径）、`df4ef91af93a`（路径说明）、`6a5208c30cca`（地图文件所在目录）、`dbbba8b54bd0`（应用程序目录）、`3a29ad146ceb`（游戏目录）、`013b4028d792`（游戏目录）、`ee439e50a835`（导出 Wavefront OBJ）、`0011be948dd6`（导出路径）、`2915922a2166`（路径占位提示）、`0ee72f3c8645`（纹理路径）、`10b21b3fc756`（纹理路径 tooltip）、`26fd3ad9ed81`（相对于导出目录）、`eed1f27c4948`（导出 Wavefront OBJ 文件）、`8e40860a52a1`（程序崩溃）、`f0f928f057b7`（崩溃正文，双换行保留）、`444a30e5e793`（报告问题）、`cfde892c46df`（AboutDialog 完整 HTML）、`5a27052291cb`（自动检测）

## 非目标消息差异
- 非目标消息数：542
- 逐节点 XML 比较差异：**0**
- 消息序列（Context+Source）一致：是
- 非授权字段变化：0

## 文本差异说明
unified diff 删除 20 行 `<translation type="unfinished"></translation>`，新增 67 行翻译内容；新增行数多于 20 是因为 AboutDialog HTML 与崩溃报告正文包含多行文本。所有新增/删除行均位于 20 个目标 translation 节点内，不存在额外差异。

**结论：差异严格归因于授权范围。**
