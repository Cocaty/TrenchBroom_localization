# P2D2CB_R2_Final_Report — QM 魔数定义纠错与检测脚本复核最终报告

日期：2026-11-16 19:26–19:35 ｜ 性质：只读纠错审计（零构建、零启动、零部署、零原始产物修改）

## 一、纠错核心（以 Qt 6.10.3 官方源码为最终依据）

**权威证据**：`code.qt.io/cgit/qt/qtbase.git` tag `v6.10.3`，文件 `src/corelib/kernel/qtranslator.cpp`（本轮 curl 实取，含语法高亮的 195KB 页面已净化提取）：

```cpp
static const int MagicLength = 16;
static const uchar magic[MagicLength] = {
    0x3c, 0xb8, 0x64, 0x18, 0xca, 0xef, 0x9c, 0x95,
    0xcd, 0x21, 0x1c, 0xbf, 0x60, 0xa1, 0xbd, 0xdd
};
// 源码注释：$ mcookie → 3cb86418caef9c95cd211cbf60a1bddd
enum { Contexts = 0x2f, Hashes = 0x42, Messages = 0x69,
       NumerusRules = 0x88, Dependencies = 0x96, Language = 0xa7 };
```

- **裁定：MagicLength = 16，标准魔数 = `3cb86418caef9c95cd211cbf60a1bddd`（16 字节）**——任务书纠错标准正确
- 0xa7（第 17 字节）= **Language 块标签**，是魔数后的第一个结构字节，**不得计入魔数**
- 加载校验：`memcmp(data, magic, 16)`；`fileSize < 16` 直接拒绝

## 二、实测输出（修正版检查器 qm_checker_16.py，已存档 Evidence）

### D2B 历史 QM（26 B）
- 前 16 字节 == 标准魔数：**True**
- 第 17 字节：**0xa7**（Language 块标签）
- 结构：Language 块（"zh_CN"）→ 块遍历完整消耗至 EOF ✅

### D2C-B 当前 QM（366 B）
- 前 16 字节 == 标准魔数：**True**
- 第 17 字节：**0xa7**（Language 块标签）
- 结构：Language("zh_CN") + Hashes(24B) + Messages(306B，含 3 条译文的 UTF-16 命中) → 块遍历完整消耗至 EOF ✅

**两个 QM 的结构有效性均有实际解析输出支撑，不依赖魔数单一判据。**

## 三、历史脚本与结论复核（详见 QM_Checker_Review.md）

| 结论 | 状态 |
|---|---|
| D2B "26B QM 生成正确" | ✅ 成立（修正判据下仍通过；块解析证实 Language="zh_CN"） |
| D2B-R1 "魔数 True" | ✅ 成立（其 `magic[:16]` 切片实质=标准 16 字节比较）；**"17 字节标准魔数"表述撤回** |
| D2C-B "魔数 False" | ❌ **撤回**（未切片的 16 vs 17 无效比较）；修正后 True |
| D2C-B "EXE 嵌入译文/资源名" | ✅ 成立（与魔数无关，独立证据） |
| D2C-B-R1 "17 字节魔数 + 巧合误判" | ❌ **撤回/修正**（0xa7 是 Language 块标签；R1-D2B 的 True 有效且判据兼容） |

**影响范围：仅"魔数长度/第 17 字节归属"的表述维度；三轮关于 QM 有效性、译文写入、资源嵌入、构建成功的实质结论全部维持成立。**

## 四、结束条件核验

| 项 | 结果 |
|---|---|
| 魔数定义纠正为 16 字节 | ✅（含官方源码逐字证据） |
| 检测脚本逻辑正确 | ✅（qm_checker_16.py：16B 魔数 + 块遍历，已存档 Evidence；旧 qm_exe_check.py 保留作为历史记录未修改） |
| QM 结构检查有实际输出 | ✅（两个 QM 均输出块级解析） |
| 原始构建产物 | 未修改（仅只读）✅ |
| 启动/部署 | 无 ✅ |
| 旧报告 | 全部保留未覆盖 ✅ |
