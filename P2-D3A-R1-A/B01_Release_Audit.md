# B01_Release_Audit — R1-B01 原 24 条逐项独立核验

逐项结果见 `B01_Release_Audit.csv`（24 行：order / id / source / am_function / action_path / new_category / confidence / verdict / note）。

## 汇总

| 判定 | 条数 |
|---|---|
| 允许翻译 | 9 |
| 需额外术语确认 | 9 |
| **不应进入本批次** | **6** |

## 原 R1-B01 的 24 条 → 修正后 B01（18 条）

**保留的 18 条**均满足：ID 可在最新索引找到、source 与 TS 一致、来自 `createFileMenu`、路径 `Menu/File/…`、属文件操作/项目管理。

- 允许翻译（9）：New Document、Open Document...、Save Document、Save Document as...、`Map...`、Reload Material Collections、Reload Entity Definitions、Revert Document、Close Document
- 需额外术语确认（9）：`Wavefront OBJ...`（格式名）；导出 `.map` 的提示（保留 `.map`、`Omit From Export`）；Load/Reload/Unload Point File（3，Point File 术语与 `...` 省略号）；Load/Reload/Unload Portal File（3，Portal File 术语）；Revert 说明句（保留 map file 语义）

注：`Reload Material Collections` / `Reload Entity Definitions` 带材质/实体辅助标签，但注册语句在 `Menu/File`，功能为资源重载，主分类仍为文件操作；如 ChatGPT 校阅认为术语冲突，可升级为“需确认”。

## 被移出的 6 条（全部为 R1 误混入）

| ID | source | 实际来源 | 去向 |
|---|---|---|---|
| 4e51812565de | Open Map | tb::ui::AppController.cpp:324 | RA-B24 隔离待确认 |
| 5b111135cfe7 | Set a GLOB pattern… | CompilationTaskListBox.cpp:158 | RA-B18 游戏配置 |
| 82fad02a71ea | Set the classname… | CompilationTaskListBox.cpp:165 | RA-B18 游戏配置 |
| 2a294870bcbd | Choose a name | GameEngineProfileEditor.cpp:64 | RA-B18 游戏配置 |
| f45f39eb562e | Click on the button to choose... | GameEngineProfileEditor.cpp:67 | RA-B18 游戏配置 |
| 5b8a5ea2d9b0 | Choose Engine | GameEngineProfileEditor.cpp:17 | RA-B18 游戏配置 |

## 新增进入 B01

**0 条**（所有 `createFileMenu` 消息已包含在原 24 条的前 18 条中）。

## 技术内容保留清单（翻译硬约束）

- `.map`（导出提示）与 `Wavefront OBJ` 格式名原样保留
- Point File / Portal File 为专有对象名：`...` 省略号保留；术语候选待校阅
- 文件过滤器/路径（本批无直接过滤器条目，仍按交接规范执行）
- 无 `%1` 等占位符（本批 18 条 `placeholders` 均为空）

## 放行结论

**原 24 条：不放行**（6 条跨功能域）。
**修正后 18 条：有条件放行**——9 条可直接翻译；9 条须先完成 Point/Portal File、Wavefront OBJ、`.map`、`Omit From Export` 等术语确认，并经用户明确授权。**本轮不自动放行、不开始翻译。**
