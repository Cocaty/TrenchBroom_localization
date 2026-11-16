# QM_Magic_Correction — Qt QM 魔数定义纠错

日期：2026-11-16 19:26 ｜ 依据：**Qt 6.10.3 官方源码**（code.qt.io cgit，`qtbase` tag `v6.10.3`，文件 `src/corelib/kernel/qtranslator.cpp`——注意实际路径为 `kernel/` 而非 `serialization/`）

## 一、官方源码证据（净化后原文引用）

```cpp
/*
$ mcookie
3cb86418caef9c95cd211cbf60a1bddd
$
*/

// magic number for the file
static const int MagicLength = 16;
static const uchar magic[MagicLength] = {
    0x3c, 0xb8, 0x64, 0x18, 0xca, 0xef, 0x9c, 0x95,
    0xcd, 0x21, 0x1c, 0xbf, 0x60, 0xa1, 0xbd, 0xdd
};
```

- **MagicLength = 16**（本轮实测源码 L1327，与任务书纠错标准一致）
- **标准魔数 = `3cb86418caef9c95cd211cbf60a1bddd`（16 字节，末字节 0xdd）**——Qt 源码注释表明它由 `mcookie` 工具生成
- **`0xa7` 不属于魔数**——它是 QM 块标签枚举中的 **Language 块标签**：
  ```cpp
  enum { Contexts = 0x2f, Hashes = 0x42, Messages = 0x69,
         NumerusRules = 0x88, Dependencies = 0x96, Language = 0xa7 };
  ```
- `load()` / `load(const uchar*, int, ...)` 均以 `memcmp(data, magic, MagicLength)` 比较 **16 字节**；文件小于 16 字节直接返回 false

## 二、本轮两个 QM 的实测（修正版检查器 `Evidence/qm_checker_16.py`）

### D2B 历史 QM（26 字节）
```
前 20 字节: 3c b8 64 18 ca ef 9c 95 cd 21 1c bf 60 a1 bd dd a7 00 00 00
标准魔数(16B): 3c b8 64 18 ca ef 9c 95 cd 21 1c bf 60 a1 bd dd
前 16 字节 == 标准魔数: True
第 17 字节(0xa7=Language 块标签，不属魔数): 0xa7
块遍历: 完整消耗至 EOF ✅
  块 0xa7 (Language): 5B 内容='zh_CN'
```

### D2C-B 当前 QM（366 字节）
```
前 16 字节 == 标准魔数: True
第 17 字节: 0xa7（Language 块标签）
块遍历: 完整消耗至 EOF ✅ 结构有效
  块 0xa7 (Language): 5B 内容='zh_CN'
  块 0x42 (Hashes): 24B
  块 0x69 (Messages): 306B 含译文 UTF-16 命中=True
```

## 三、文件结构判定（不凭魔数单一判据）

两个 QM 均按 do_load 的块结构（`tag(1B) + blockLen(4B, 大端) + payload`）**完整遍历且精确消耗至 EOF**：26B = 仅 Language 块；366B = Language + Hashes + Messages（含 3 条译文）。**结构有效性有实际解析输出支撑。**

## 四、对历史报告结论的影响（详见 QM_Checker_Review.md）

- 涉及"魔数"的表述需修正：**"17 字节标准魔数"撤回**，改为 16 字节标准 + 0xa7 为 Language 块标签；
- 涉及"QM 有效/嵌入"的**结论本身全部仍然成立**（两个 QM 在 16 字节标准下均匹配、结构均有效）。
