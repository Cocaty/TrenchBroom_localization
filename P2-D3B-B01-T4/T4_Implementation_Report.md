# T4_Implementation_Report — B01 翻译集成与 Release 构建验证总结

日期：2026-11-16 22:27–22:55 ｜ 本轮**首次授权构建 TrenchBroom Release 主程序**；未启动、未部署

## 验收结论：**PASS**

| 条件 | 判定 |
|---|---|
| 构建前基线正确（TS/工具链/原版 Release） | ✅ |
| CMake 翻译配置符合冻结设计 | ✅ |
| Release 构建成功（exit 0） | ✅ |
| QM 生成成功且与 T3 内容对应（哈希一致） | ✅ |
| QM 正确嵌入 EXE（RCC 载荷/OBJ/EXE 字节证据） | ✅ |
| 无越权修改；原版 Release 与用户配置不变 | ✅ |
| 证据归档完整 | ✅ |

## 实际执行命令

```
cmake --build "C:\Users\yoshi\Projects\TrenchBroom-zhCN\build\v2026.2-msvc145-qt6103" \
      --config Release --target TrenchBroom -- -m:1 -v:m
```
- 退出码 **0**；完整输出见 `T4_Release_Build_Log.txt`
- 未重新 configure（沿用现有生成器与配置）；未更换编译器/依赖；未清理构建目录
- 已知 shortcuts.js 宿主问题本轮**未出现**（无需人工补救）
- 代理变量仅在本 shell 进程内清空（进程级，未修改系统环境变量）

## CMake 自动翻译

构建日志中自动执行：
```
Generating TrenchBroom_zh_CN.qm
  Generated 21 translation(s) (21 finished and 0 unfinished)
  Ignored 541 untranslated source text(s)
```
lrelease 由 CMake 规则自动调用（非手工执行）；21=18 B01 新译文+3 既有完成项，541 未完成项被忽略属正常行为；无警告/错误。

## 产物

- QM：1,805 B，SHA `a2f5cc1f892cfd8a52e6accc619b5ba79fcaf8a9524331013bd615a33d3d2f66`（与 T3 完全一致）
- EXE：29,761,536 B，SHA `9a1a84991c61d1d108477ab7f193c72d6336e1ed6c197d510339043d8b2c46d5`，PE x64
- RCC cpp 十六进制数组还原载荷与 QM **逐字节一致**；OBJ 含完整 QM 字节；EXE 含资源路径与译文 UTF-16BE 字节（详见 T4_EXE_Resource_Audit.md）

## 边界与保护

正式 TS、C++/CMake、其他翻译批次、用户配置、原版 Release、T2/T3 证据均未修改；Git dirty=7 与基线一致；TrenchBroom 进程 0；未启动/部署/提交 Git。

## 未解决事项

无阻塞项。本轮为**静态构建验证**，未验证运行期显示；lrelease 与构建产物路径正确，运行期检查需另行授权。

**本轮完成后立即停止，不进入 T5。**
