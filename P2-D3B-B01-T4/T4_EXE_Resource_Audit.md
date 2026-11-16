# T4_EXE_Resource_Audit — EXE 与资源嵌入静态证据（T4-4 B）

## EXE
路径：`build\v2026.2-msvc145-qt6103\app\TrenchBroom\Release\TrenchBroom.exe`

| 项 | 构建前 | 构建后 |
|---|---|---|
| 大小 | 29,761,536 B | 29,761,536 B（不变） |
| SHA-256 | 8ccfbb9937f7c119… | **9a1a84991c61d1d108477ab7f193c72d6336e1ed6c197d510339043d8b2c46d5** |
| mtime | 20:16:20 | 22:28:29 |
| PE Machine | — | 0x8664（x64） |

哈希变化源于新 QM 资源与翻译代码变更，属预期。

## 资源嵌入证据（非仅凭体积）

1. **qrc**（`Evidence/TrenchBroom_translations.qrc`，225 B）：`<qresource prefix="/translations"><file alias="TrenchBroom_zh_CN.qm">…/build/.../TrenchBroom_zh_CN.qm</file></qresource>`
2. **RCC 生成源码**（`Evidence/qrc_TrenchBroom_translations.cpp`，12,323 B）：含注释 `// :/translations/TrenchBroom_zh_CN.qm`；`qt_resource_data[]` 以十六进制数组嵌入载荷
3. **载荷逐字节比对**：解析 cpp 的十六进制数组得 1,809 B（4 B 长度字段 `0x070d`=1805 + 1,805 B 载荷）；**还原载荷 == QM 文件逐字节一致**，还原载荷 SHA `a2f5cc1f…` 与 QM 相同 ✅
4. **OBJ**（`Evidence/qrc_TrenchBroom_translations.obj`，15,191 B）：含完整 QM 原始字节与魔数 ✅
5. **EXE**：含资源路径 `:/translations/TrenchBroom_zh_CN.qm`（UTF-8）及 `TrenchBroom_zh_CN.qm`（UTF-16BE）；含 QM 魔数；新译文 UTF-16BE 字节命中：`语言`、`将当前地图导出为 .map 文件`、`加载点轨迹文件`、`还原文档` 均为 True ✅

## 结论

`:/translations/TrenchBroom_zh_CN.qm` 资源已正确嵌入 Release EXE，且本轮 QM 的完整字节可追溯至 RCC 源码与 OBJ；**未启动 EXE**，以上均为静态证据。
