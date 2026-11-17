# M1_Execution_Report — 人工验证证据归档

## 结论状态：**PARTIAL_RUNTIME_TRANSLATION_CONFIRMED**

本阶段为只读证据归档。WorkBuddy 未启动程序、未操作 GUI、未修改配置或源码。结论仅表示：用户截图直接证明 File 下拉菜单已出现部分中文、顶级菜单仍为英文；不表示全部汉化成功。

## 证据来源分级

### 直接证据（截图 / 文件哈希）
- 原始截图 `C:\Users\yoshi\Pictures\Screenshots\屏幕截图 2026-11-17 214337.png` 已原样复制到 `Evidence\Manual_UI_Observation.png`
  - PNG，755×520，RGBA，34,353 B
  - SHA-256 源/目标均为 `206fabfba3d048f8b009af7f1fcf8656921853f3e5a06ffdb76171b2ee11a1f4`
- 截图直接可见：窗口标题 `* unnamed.map - TrenchBroom`（英文）；顶级菜单 File/Edit/Selection/Groups/Tools/View/Run/Debug/Help 全为英文；File 下拉菜单中“新建文档”“打开文档...”“保存文档”“文档另存为...”“加载/重新加载/卸载点云文件”“重新加载材质集合”“重新加载实体定义”“还原文档”“关闭文档”等为中文；“Open Recent”“Export”仍为英文；BSP 门户相关为混合文字。
- 当前测试副本 `config/Preferences.json` 可解析，大小 127 B，SHA `c048b77a…`，包含 `"Editor/Interface language": "zh_CN"`。与历史基线 `65f46db9…` 不同，属于用户人工操作后的预期变化。

### 用户声明（USER_REPORTED）
用户确认简体中文选项存在、通过界面选择了简体中文、正常退出并重新启动、观察到 File 下拉菜单部分汉化。详见 `M1_Manual_Action_Declaration.md`。WorkBuddy 未亲自执行这些操作。

### 尚未验证
- QTranslator 是否成功加载：NOT_VERIFIED
- 39 条冻结译文是否全部在运行期正确显示：NOT_VERIFIED
- 设置页面与语言下拉列表：NOT_SHOWN（截图未展示）
- 其他菜单、对话框、AboutDialog、CrashDialog 等界面内容：NOT_VERIFIED

## 保护状态
正式 TS、测试副本 EXE、构建 EXE、构建 QM、QRC、根 CMake、app CMake、Main.cpp、原版 Release 与 Git 分支/HEAD/dirty=7 均与既有基线一致。唯一差异是测试副本 Preferences，属于用户授权范围内的人工语言设置，不是非授权修改。

## 截图归档
成功；源文件与归档文件大小和 SHA256 一致，未裁剪、压缩、重编码或标注。未制作替代截图。

## 归档
本阶段新增报告/CSV/证据共 10 个文件（含原始截图归档与前后快照）；SHA256SUMS 覆盖 9 项（清单自身不自列），逐项校验通过。未上传 GitHub，无可验证链接。

**完成后停止，不进入 T4-2-3。**
