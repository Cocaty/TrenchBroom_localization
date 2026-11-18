# A1_QM_Embedded_Resource_Report — QM 编译与 EXE 嵌入验证

## 结果：**PASS**

沿用 T4-1 已验证的静态资源方法，不启动 EXE。

- 新 EXE 中资源路径 `:/translations/TrenchBroom_zh_CN.qm` 出现，ASCII 偏移 22,238,728
- EXE 中 QM 魔数偏移 23,382,020，唯一匹配
- 从该偏移提取 7,035 B，保存为 `Artifacts/TrenchBroom_zh_CN.embedded.qm`
- 提取 QM SHA256：`4b213ce5b33639069b87f435dddce6ba9fae54e552f19cb02a231c27ecd926ab`

## A/B/C
| 项 | 路径 | SHA256 |
|---|---|---|
| A | B5 QM | `4b213ce5…` |
| B | 本次构建目录 QM | `4b213ce5…` |
| C | 新 EXE 提取 QM | `4b213ce5…` |

三份文件大小均为 7,035 B，A==B、B==C，字节级一致。构建目录 QM 与 B5 QM 相同，属于预期结果（B5 QM 已由正确 TS 编译并经回转验证）。

运行时 QTranslator 是否加载仍属 B7 运行期验证范围；本阶段不启动程序。
