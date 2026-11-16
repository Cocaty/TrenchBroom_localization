# R1_UI_Verification_Report — 18 条 B01 译文 UI 实测（R1-4 / R1-5）

环境：T5-R1 独立测试副本，`--portable`，语言 zh_CN；映射窗口标题 `unnamed.map - TrenchBroom`（Generic 配置、隔离 game path）。逐条结果见 `R1_UI_Verification.csv`（18 行）。

## 实测方法
- 打开 File 菜单直接读取菜单项文字（禁用项仅核对文字，不尝试启用）
- File > Export 子菜单读取 Wavefront OBJ... 与 地图文件...
- 悬停 Revert Document / Export>地图文件... 后，描述文字显示在**窗口底部状态栏**（Qt 菜单 tooltip 弹窗未出现），据此验证两条长说明译文
- 不点击 Revert / Load / Reload / Unload / Close 等命令；未打开任何真实地图或外部资源

## 汇总：**18/18 PASS**

| # | source | 实际 UI 文本 | 位置 |
|---|---|---|---|
| 01 | New Document | 新建文档 | File 菜单 |
| 02 | Open Document... | 打开文档... | File 菜单 |
| 03 | Save Document | 保存文档 | File 菜单 |
| 04 | Save Document as... | 文档另存为... | File 菜单 |
| 05 | Wavefront OBJ... | Wavefront OBJ...（保留英文，符合 D6） | Export 子菜单 |
| 06 | Map... | 地图文件... | Export 子菜单 |
| 07 | .map / Omit From Export 说明 | 将当前地图导出为 .map 文件。标记为“不参与导出”的图层将被忽略。 | 悬停 06 后状态栏 |
| 08 | Load Point File... | 加载点轨迹文件... | File 菜单 |
| 09 | Reload Point File | 重新加载点轨迹文件（禁用态） | File 菜单 |
| 10 | Unload Point File | 卸载点轨迹文件（禁用态） | File 菜单 |
| 11 | Load Portal File... | 加载 BSP 门户文件... | File 菜单 |
| 12 | Reload Portal File | 重新加载 BSP 门户文件（禁用态） | File 菜单 |
| 13 | Unload Portal File | 卸载 BSP 门户文件（禁用态） | File 菜单 |
| 14 | Reload Material Collections | 重新加载材质集合 | File 菜单 |
| 15 | Reload Entity Definitions | 重新加载实体定义 | File 菜单 |
| 16 | Revert Document | 还原文档 | File 菜单 |
| 17 | Discards any unsaved changes… | 放弃所有未保存的更改，并重新加载地图文件。 | 悬停 16 后状态栏 |
| 18 | Close Document | 关闭文档 | File 菜单 |

## 直接截图证据

- `Evidence/R1_19_file_menu.png`、`R1_28_save_dialog.png`：File 菜单中文条目（多项共用）
- `Evidence/R1_22_export_submenu2.png`：Export 子菜单（B01-05/06）
- `Evidence/R1_26_statusbar_export_map.png`：B01-07 状态栏描述
- `Evidence/R1_25_statusbar_revert.png`：B01-17 状态栏描述

## 限制与未执行
- Qt 菜单 tooltip 弹窗未出现，B01-07/17 通过状态栏描述验证（仍为实际 UI 显示文本）；其余项不需要 tooltip
- 未点击任何可能丢数据/引入外部资源的菜单命令；Save As 曾被误触发，保存对话框位于测试配置目录内，已取消，未写出文件
- 空白地图以内存文档创建（`unnamed.map`）；尝试保存到 `workspace\test.map` 时文件对话框拒绝绝对路径/路径拼接异常，**未产生磁盘地图文件**——R1-3 的地图文件 SHA 项不适用；不影响 18 条 UI 文字验证

**结论：RA-B01 18/18 运行期 UI 验证通过（PASS）。**
