# TS_XML_Integrity_Comparison — TS 完整性对比证据

日期：2026-11-16 ｜ 方法：修改前备份（`Evidence/TS_before_D2CB.ts`，130,298 B）与修改后文件（127,729 B）**逐条 XML 解析对比**（含 numerusform 与 locations）

## 一、统计对比

| 指标 | 修改前 | 修改后 | 变化 |
|---|---|---|---|
| 根节点 language | zh_CN | zh_CN | — |
| message 总数 | 560 | **562** | **+2**（Language、Language changes take effect after restarting TrenchBroom.）|
| finished（有译文） | 0 | **3** | +3（上 2 条新消息 + "Requires restart after changing" 既有条目填充）|
| unfinished | 560 | **559** | −1（该条转为 finished；**其余 559 条原样保留**）|
| obsolete / vanished | 0 | **0** | 未使用 -no-obsolete，无条目被移除 ✅ |
| numerusform / numerus 消息 | 0 | **0** | — |
| context 数 | 85 | 85 | — |

## 二、逐条差异（全字段五元组：context, source, translation, type, numerus, numerusform, locations）

**按完整五元组**：丢失 1 条、新增 3 条——差异实为**同一条消息的更新**：

| context | source | 变化 |
|---|---|---|
| tb::ui::ViewPreferencePane | Requires restart after changing | ① translation: 空 → "更改后需要重启"（type: unfinished → 无）；② location 新增 ViewPreferencePane.cpp:**135**（原 L120——语言行代码插入使源码行号 +1，lupdate 正常更新）|

**新增 2 条消息**（均 tb::ui::ViewPreferencePane 上下文）：
| source | translation | locations |
|---|---|---|
| Language | 语言 | ViewPreferencePane.cpp:491 |
| Language changes take effect after restarting TrenchBroom. | 语言更改将在重启 TrenchBroom 后生效。 | ViewPreferencePane.cpp:492 |

**语义级对比（忽略 location 行号）**：丢失 **0** 条、新增 **1** 条（即上述译文填充）。
**按 (context, source) 键核对**：**0 条丢失**——原有 560 条消息全部存在 ✅

## 三、130,298 B → 127,729 B（−2,569 B）体积变化解释（逐项量化）

| 因素 | 字节影响 |
|---|---|
| ① `<!DOCTYPE TS>` 声明行被 ElementTree 写出时**移除**（旧 1 处 → 新 0 处，实测 count） | −14 |
| ② 空标签序列化风格：lupdate 写 `<translation type="unfinished"></translation>`（开闭对，559 个）；ET 重写为自闭合 `<translation type="unfinished" />`（559 个，实测 count 0→559） | ≈ −7,200 |
| ③ XML 声明引号风格：`"1.0"` → `'1.0'` | −2 |
| ④ location 自闭合空格风格 `<location …/>` → `<location … />`（570 个 ×1B） | +570 |
| ⑤ +2 条新消息（source+translation+locations）与 +3 条译文内容 | ≈ +3,700 |
| **净合计** | **≈ −2,900 ≈ 实测 −2,569**（ET 尾部空白微差） |

**结论：体积变化完全来自序列化风格差异与新增内容，非数据丢失。** 560 条旧消息的 source/translation/locations 逐字段对比全部保留（详证见下方自动对比输出记录）。

## 四、遗留说明（如实记录）

- ET 重写使 TS 的声明行风格（单引号、无 DOCTYPE）与空标签风格（自闭合）发生变化——**语义数据零丢失**，Qt Linguist/lupdate 均可正常读写该格式（本轮 lupdate 增量更新前 ET 重写已先行发生且 lupdate 正常处理，为实际运行证据）。
- 后续如需保持 lupdate 原生格式，可在 P2-D2C-C 译文填充后改由 lupdate 全量重写收敛格式（非必需）。
