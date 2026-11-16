# T3_QM_Structure_Report — QM 结构静态验证（T3-4 A）

检查器：`T3_QM_Checker.py`（Qt QM 16 字节魔数版；从 P2-D2C-B-R3 加固检查器原样移植到本独立目录）；原始输出：`T3_QM_Structure_Checker_Output.txt`。

## 文件

`Output/TrenchBroom_zh_CN.qm`：1,805 B，SHA-256 `a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66`

## 实测结构

```
前 20 字节: 3c b8 64 18 ca ef 9c 95 cd 21 1c bf 60 a1 bd dd a7 00 00 00
前 16 字节 == 标准魔数(3cb86418caef9c95cd211cbf60a1bddd): True
第 17 字节: 0xa7（Language 块标签，不属魔数）
块 @16:   tag=0xa7 (Language) len=5    header=5B payload=[21,26)
块 @26:   tag=0x42 (Hashes)   len=168  header=5B payload=[31,199)
块 @199:  tag=0x69 (Messages) len=1601 header=5B payload=[204,1805)
块遍历: ✅ 完整消耗至 EOF（结束偏移 1805/1805）
提示: Language='zh_CN'; Messages 中译文 UTF-16 字节命中=是
块结构检查: 通过 | 完整 QM 语义验证: 未执行（本脚本不提供）
```

## 判定

- 16 字节魔数准确、第 17 字节为独立块标签 ✅
- Language / Hashes / Messages 块齐全、长度不越界、无未知块/重复块/零长度块 ✅
- 文件完整至 EOF，无截断 ✅
- 语义验证由独立的 lconvert 离线回转完成（见 Implementation_Report 与逐条 CSV），不与结构检查混为一谈 ✅
