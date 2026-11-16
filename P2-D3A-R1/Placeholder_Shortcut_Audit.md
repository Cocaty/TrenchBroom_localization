# 占位符与快捷键审查报告（R1）

## 占位符正则修正与实测

新正则（按优先级）：`%%` → `%L[1-9]\d*` → `%[1-9]\d*` → `%n`

纯字符串实测（脚本内验证）：
| 输入 | 识别结果 | 判定 |
|---|---|---|
| `%1` | `%1` | ✅ |
| `%10` | `%10`（**不是** `%1`） | ✅ 关键修正 |
| `%1 and %2` | `%1`, `%2` | ✅ |
| `%L1` / `%L12` | `%L1` / `%L12` | ✅ |
| `%n` / `%%` | `%n` / `%%` | ✅ |
| `100%` / `%0` | 无 | ✅ 不误报 |

当前 TS 562 条消息中含占位符 **58 条**；源码中未发现 `%10` 实例，但正则已支持 1–99 与 L1–L99；`%n` 与 `%%` 当前均为 0 条。

## 快捷键正则修正与实测

新规则：仅识别 `Ctrl/Shift/Alt + X`（X 可为 F1–F12）与独立 `F1`–`F12`；**不再**把独立 Enter/Delete/Esc 等英文词当按键标识。

实测当前 TS：
- 真实组合键 / F10–F12：**0 条**
- 旧规则误判 4 条实为普通英文：`Delete`、`Double-click an item to begin editing it. Click anywhere else to end editing.`、`Enter a path or click to browse`、`fix the JSON, or backup and delete the file`——已移出“按键提示”统计
- 助记符 `&X`：**0 条**；`&&` 转义：**0 条**

## 人工复核样本

`Evidence/P2D3A_R1_Uncertain_Samples.csv`：**33 条**（方向词 Move Left/Right/Up/Down、Move Textures Up…、可疑 % 序列等），均标记原因，供 ChatGPT 校阅时确认；不计入“真实按键提示”数量，也不作为翻译结论。

## 技术标识

5 条（.map/.wad 扩展名、URL+HTML 标签、文件过滤器、数值参数）——沿用 P2-D3A 结论，R1 重新校验一致。
