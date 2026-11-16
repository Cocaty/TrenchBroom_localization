# P2D2CB_R1_Final_Report — 独立验收证据补充最终报告

日期：2026-11-16 19:18–19:30 ｜ 方法：只读实测 + 原始证据打包（`Evidence\` 17 项 + SHA256SUMS.txt）

## 一、证据包清单

`Evidence\`：Main.cpp / Preferences.h / ViewPreferencePane.cpp / ViewPreferencePane.h（修改后完整源码）、TS_before_D2CB.ts（修改前备份）、TrenchBroom_zh_CN.ts（修改后）、TrenchBroom_zh_CN.qm、TrenchBroom_translations.qrc、qrc_TrenchBroom_translations.cpp、qrc_TrenchBroom_translations.obj、git_diff_full.txt、git_status.txt、p2d2cb_lupdate.log、p2d2cb_build.log（失败现场）、p2d2cb_build2.log（成功）、qm_exe_check.py（修正版检测脚本）、SHA256SUMS.txt——**共 17 项**。

## 二、七项审计结论

| # | 审计项 | 结论 |
|---|---|---|
| 1 | Git 状态与范围 | 分支/HEAD/tag 正确；修改 = D2B 既有 2 文件 + **D2C-B 4 文件（74 增 0 删）**；未跟踪 translations/ 已计入物理文件总数（**7 个物理文件**） |
| 2 | 源码证据 | 8 个确认点全部按当前行号复核通过（initTranslator L173-193、调用 L359、InterfaceLanguage L210、UI L129-141/L364-367/L277-283/L482-494/reset L320）；QTranslator 父对象=app 覆盖全生命周期；load 失败 qWarning+deleteLater；白名单回退；resetToDefault 恢复英文；QMessageBox 模态已如实标注 |
| 3 | TS 完整性 | 560→562（+2 消息）；finished 0→3；unfinished 559 保留；obsolete/vanished/numerusform 全 0；按 (context,source) 核对 **0 条丢失**；−2,569 B 体积变化 = 序列化风格（DOCTYPE 移除 −14、空标签自闭合 ≈−7,200、引号 −2、location 空格 +570、+2 消息 +3 译文 ≈+3,700）**语义数据零丢失** |
| 4 | QM 与嵌入 | QM 366 B、**17 字节魔数匹配（修正脚本后 True）**；含 3 条译文（UTF-16BE 命中）；EXE 内**直接命中**译文字节与资源名（本批资源未压缩）→ "OBJ 已链接进 EXE" 升级为**字节级已验证** |
| 5 | 构建证据 | lupdate exit=0（562 条）；构建 exit=0（第二次，第一次为已知宿主缺陷）；configure 本轮未执行（无 CMake 变更，如实注明）；shortcuts.js 人工补救 1 次（如实记录） |
| 6 | 边界完整 | 原版 Release 哈希一致；用户 INI mtime 12:42（本轮前）且无语言键；**TrenchBroom 进程数 = 0**；安装目录未动 |
| 7 | 生命周期/回退设计符合性 | 全部 8 个确认点通过（见 Source_Implementation_Evidence.md §9） |

## 三、重要更正（本轮发现并修正）

1. **QM 魔数比较脚本缺陷（两轮均受影响）**：Qt QM 魔数为 **17 字节**（`3cb86418…bddda7`），此前脚本以 16 字节切片与 17 字节定义比较——D2B-R1 的"26 字节 QM 通过"实为方向巧合误判，D2C-B 的"False"亦为误报。修正脚本（`Evidence/qm_exe_check.py`）后，366 字节 QM **魔数匹配 True**。
2. **P2-D2B-R1 中"OBJ 链接 = 部分验证"** 现升级为 **已验证**（EXE 内直接命中明文译文与资源名——本批资源未压缩，字节级直接证据成立）。

## 四、P2-D2C-B 验收判定

**建议：验收通过。** 运行时机制与语言选择 UI 实施完整、证据链闭合（源码行为 → TS 数据 → QM 内容 → EXE 字节四层全部实测一致）；运行期表现归 P2-D2C-C（10 用例待授权）。

## 五、结束核验

| 项 | 结果 |
|---|---|
| Git HEAD/分支/tag | 不变 ✅ |
| TS/QM/QRC/RCC/OBJ/EXE 哈希 | 与快照一致（SHA256SUMS.txt）✅ |
| 源码/构建/启动/部署/用户配置 | 零操作 ✅ |

**本轮停止，等待独立审查。未授权 P2-D2C-C。**
