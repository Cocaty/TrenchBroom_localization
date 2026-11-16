# 04_Source_Context_Mapping — 源码上下文映射（逐条）

完整映射表：`Evidence/P2D3A_Usage_Hints.csv`（562 行：id/context/source/file/line/class_hint/function_hint/usage_hint/user_scene/source_snippet）；消息索引：`P2D3A_Message_Index.csv`。

## 覆盖率

| 指标 | 数量 | 比率 |
|---|---|---|
| TS location 指向的源码文件实际存在 | **562 / 562** | 100% |
| 已采集 location 行及前后代码片段 | **562 / 562** | 100% |
| 启发式推断出类名或函数名 | **417 / 562** | 74.2%（其余 145 条只有文件:行与片段，未强行猜测所属函数） |
| 用途提示（基于代码片段关键词） | 见下表 | 仅提示，非人工最终判定 |

## 用途提示分布（自动推断）

| 用途 | 条数 |
|---|---|
| tr() 调用（用途待人工确认） | 357 |
| 静态标签/说明 | 71 |
| 工具提示 | 42 |
| 菜单/动作 | 41 |
| 下拉选项 | 17 |
| 通知/错误 | 11 |
| 消息框 | 9 |
| 标题 | 9 |
| 输入占位提示 | 5 |

## 映射方法（可复核）

1. 从 TS 每条消息的 `<location filename line>` 解析相对 `.ts` 目录的源码绝对路径（如 `../../../lib/TbUiLib/src/…`）
2. 读取该行及前后各 1 行源码片段（snippet）
3. 向上搜索最近的类声明与 `Class::method(` 定义（启发式，最多 120 行）
4. 以片段关键词（addAction / setToolTip / QMessageBox / addRow / setWindowTitle 等）给出用途提示与用户场景

## 重点上下文例证

| source | 位置 | 用途 | 场景 |
|---|---|---|---|
| Requires restart after changing | ViewPreferencePane.cpp | 静态标签（setInfoStyle） | 打开 View 偏好页 |
| Language | ViewPreferencePane.cpp（2 处） | addRow 标签 + 消息框标题 | 偏好页与切换提示 |
| Toggle %1 visible | ActionManager.cpp（2 处） | QObject::tr 菜单模板 | 动态生成菜单项 |
| Could not build a path. | ChoosePathTypeDialog.cpp（3 处） | 错误/消息框 | 路径构造失败 |

## 限制

- 类名/函数名为**启发式推断**（417 条），字段标注 `class_hint/function_hint`；145 条空缺保持空缺，不伪造
- 用途提示基于片段关键词，存在误判可能；翻译时应以完整调用链为准
- 无源码位置的消息：**0 条**（不存在 UNKNOWN 位置的伪造条目）
