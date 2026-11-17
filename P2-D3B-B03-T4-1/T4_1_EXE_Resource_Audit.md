# T4_1_EXE_Resource_Audit — 最终 EXE 资源静态检查

## 对象
`build\v2026.2-msvc145-qt6103\app\TrenchBroom\Release\TrenchBroom.exe`，29,761,536 B，SHA `268df3904f16dc2e329542397531be4ef35f530cebde07cd720753707fca7212`，配置 Release / x64（CMake generator `Visual Studio 18 2026`）。

## 静态证据（未启动程序）
1. 资源路径字符串 `:/translations/TrenchBroom_zh_CN.qm` 在 EXE 中出现，ASCII 偏移 **22,238,728**；UTF-16 变体未出现。
2. 生成文件 `build\...\app\TrenchBroom\.qt\rcc\qrc_TrenchBroom_translations.cpp`（SHA `08bafc1e…`）由 Qt rcc 6.10.3 生成，头部明确包含 `// TrenchBroom_zh_CN.qm` 与 QM 魔数字节，证明 Qt 资源系统已生成该资源对象。
3. EXE 中 QM 魔数出现在偏移 **23,382,020**；从该偏移提取 6,631 字节与本次构建 QM 完整字节逐字节相同，SHA 同为 `707011a3216511d051b07d0dba249af6d834e6795a447a4f09611c6a9bd2102c`。

## 结论边界
- QM 文件存在：**YES**
- QM 已被 Qt 资源系统生成：**YES**（rcc 生成文件）
- QM 已进入最终 EXE：**YES**（路径字符串 + 内嵌 QM 字节完整匹配）
- QTranslator 运行时可成功加载：**NOT VERIFIED**（本阶段禁止启动程序；留待 T4-2）

不使用“QM 文件存在”替代“资源嵌入成功”；上述三项均有独立静态证据。
