# 05_Placeholder_And_Shortcut_Audit — 格式化参数与快捷键风险

数据：`Evidence/P2D3A_Message_Index.csv` 的 placeholders / has_mnemonic / has_key_hint / has_technical 列。

## A. 格式化参数（58 条）

| 模式 | 出现条目 | 示例 |
|---|---|---|
| `%1` | 多数（示例：`Toggle %1 visible`、`Create %1`、` (%1)`） | 单参数模板 |
| `%2` | 与 %1 共现（示例：`%1 or %2`） | 多参数模板 |
| `%n` / `%%` | **0 条**（当前 TS 未使用 Qt 复数/百分号转义） | — |
| 其他 | 0 条（正则同时覆盖 %*、%L1、%s 等，未见命中） | — |

**翻译硬约束**：每条译文必须保留源文全部占位符，数量、编号与顺序一致；不得把 `%1` 译成中文数字或删去。58 条均应在 Translation_QA 中自动校验占位符集合相等。

## B. 快捷键与助记符

| 项 | 实测 | 判定 |
|---|---|---|
| `&File` 形式助记符 | **0 条** | — |
| `&&` 转义 | **0 条** | — |
| 明确键盘提示（Ctrl+/Shift+/Alt+ 或独立功能键） | **4 条** | 保留按键标识原样，不机械翻译（如 Ctrl、Shift） |
| `Move Left` / `Move Right` 等 | 初版正则误判为按键；已修正为普通方向词 | 属普通文字，可本地化（译为“向左移动”等，须与工具行为一致） |

## C. 文件路径、命令与专有标识（5 条）

| source（节选） | 类型 | 处理建议 |
|---|---|---|
| `Exports the current map to a .map file. Layers marked Omit From Export …` | 扩展名 `.map` | 保留 `.map` 原样 |
| `Set Grid Size 0.125` / `0.25` | 数值参数 | 保留数字与单位语义 |
| `github.com/TrenchBroom/TrenchBroom<br />…<b>Developers</b>…` | URL + HTML 标签 | 保留 URL/标签，只译文本节点 |
| `Wad files (*.wad);;All files (*.*)` | 文件过滤器模式 | 保留 `(*.wad)`、`(*.*)` 与 `;;` 分隔符，仅译 Wad files / All files |

## 结论

- 高风险翻译点：**58 条占位符 + 5 条技术标识 + 4 条按键提示**；需在每批 QA 中逐项校验
- 助记符风险当前为 0（若后续新增带 `&` 的文本需重新审计）
