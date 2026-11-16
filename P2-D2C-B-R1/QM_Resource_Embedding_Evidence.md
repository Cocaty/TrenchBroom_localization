# QM_Resource_Embedding_Evidence — QM 与资源嵌入证据

日期：2026-11-16 ｜ 检测脚本：`Evidence/qm_exe_check.py`（已存档可复跑）

## 一、QM 文件核验

| 项 | 值 |
|---|---|
| 路径 | `build\v2026.2-msvc145-qt6103\app\TrenchBroom\TrenchBroom_zh_CN.qm` |
| 大小 | **366 字节**（P2-D2B 时 26 字节——3 条译文写入后增长）|
| SHA-256 | 8992562d9ad154602a3fcca55562016bce9dc96ebe91044360519260e49ac978 |

### 魔数检查（含此前脚本错误的修正说明）

- **此前脚本缺陷**：Qt QM 标准魔数为 **17 字节** `3c b8 64 18 ca ef 9c 95 cd 21 1c bf 60 a1 bd dd a7`；此前脚本把它定义成 17 字节列表却与 `qm[:16]`（16 字节切片）比较——16 ≠ 17 恒为 False（D2B-R1 曾将 26 字节 QM 的"通过"记录下来，实际是比较对象长度巧合误判；本轮两处均已修正）。
- **修正后检查**（qm_exe_check.py 实测输出）：
  ```
  QM 大小: 366 | 魔数(17B)匹配: True
  ```
  366 字节 QM 的前 17 字节与标准魔数**逐字节一致** ✅

### QM 内容解析（提取的译文存在性）

| 检查 | 结果 |
|---|---|
| "语言"（UTF-16BE） | 存在 ✅ |
| "语言更改将在重启"（UTF-16BE） | 存在 ✅ |
| 与 TS 关系 | 3 条 finished 译文写入 QM；559 条 unfinished 被 lrelease 默认排除（P2-D2B-R1 已确认该语义）|

## 二、QRC / RCC 证据

| 文件 | 内容要点 |
|---|---|
| `TrenchBroom_translations.qrc`（90eeb6a8…，225 B） | `<qresource prefix="/translations">` + `<file alias="TrenchBroom_zh_CN.qm">…构建树…/TrenchBroom_zh_CN.qm</file>` ✅ |
| `qrc_TrenchBroom_translations.cpp`（3f88b754…，3,577 B→本轮重建后含 366B 载荷） | qt_resource_data/name/struct 三段；资源名 UTF-16BE 编码 |
| `qrc_TrenchBroom_translations.obj`（本轮 13,399 B 级） | 已编译 ✅ |

## 三、EXE 嵌入字节检查（检测脚本实测输出）

```
EXE 含 重启提示译文(UTF-16BE): True
EXE 含 语言(UTF-16BE): True
EXE 含资源名 TrenchBroom_zh_CN(UTF-16BE): True
```

- **本批资源未压缩**（rcc 对小载荷/特定输入选择存储策略），因此译文中文字节与资源名可直接在 EXE 中命中——**这是比 P2-D2B 更强的直接嵌入证据**（当时 26 B 载荷被压缩，仅能靠间接证据）。
- EXE：29,728,256 → **29,761,536**（+33,280），SHA-256 `e138ba45483efd91…`（完整值见 SHA256SUMS.txt 相应条目，此处前 16）。

## 四、状态分级

| 环节 | 状态 |
|---|---|
| QM 已生成（含 3 条译文） | ✅ 已验证 |
| QRC / RCC CPP / OBJ | ✅ 已验证 |
| OBJ 链接进 EXE | ✅ **已验证（升级）**——EXE 内直接命中译文与资源名字节，字节级直接证据成立 |
| 运行期 QTranslator 加载 | ❌ 未验证（禁止启动，归 P2-D2C-C） |
