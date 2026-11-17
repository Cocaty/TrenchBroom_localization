# B3_Execution_Report — lupdate 提取与 TS 差异审计

## 结论：**PASS_WITH_LIMITATIONS**

B3 核心目标达成：九条新消息正确提取、39 条冻结译文全部保留、正式 TS 未变。限制为一条非冻结重复消息的 lupdate same-text heuristic 译文复制与大量 location 元数据规范化，详见 B4 准备度评估。

## B3-0 基线
分支 `feature/zh-CN-v2026.2`、HEAD `4c756be1…`、dirty=12；五个 B2 源码文件哈希与 B2 结束快照一致，九处静态 `QObject::tr()` 各 1 次。正式 TS `f021e509…`，85 Context / 562 Message / 42 finished / 520 unfinished。开始快照 16 项。

## B3-1 工具链
`lupdate.exe`：`C:\Users\yoshi\tools\Qt\6.10.3\6.10.3\msvc2022_64\bin\lupdate.exe`，大小与 SHA 见 `B3_Toolchain_Audit.csv`，`-version` 输出 `lupdate version 6.10.3`。未运行 lrelease/lconvert。

## B3-2/3 lupdate 执行
正式 TS 原样复制到 `Artifacts/TrenchBroom_zh_CN.lupdate.tmp.ts`，复制前后 SHA 一致。命令使用项目既有 `TrenchBroom_lupdate_project.json` 指定源码范围，并以 `-ts` 指向临时 TS；命令、工作目录、时间、退出码见 `Evidence/lupdate_command.txt`。lupdate 退出码 0，stdout：`Found 571 source text(s) (9 new and 562 already existing)`；stderr 有项目既有扫描范围警告（generated manual HTML、vcpkg headers、Q_OBJECT 提示等），无致命错误。未修改正式 TS。

## B3-4 九条提取
9/9 在 `QObject` Context 精确命中，Source 与 B1 冻结矩阵逐字一致；各恰好 1 次，均为 `unfinished` 且无译文自动写入。无重复、无意外 Context。详见 `B3_Menu_Extraction_Audit.csv`。

## B3-5 39 条保护
B01 18 + B02 1 + B03 20 = 39 条，以 Context+Source 定位，正式 TS 与临时 TS 中 Translation 均与冻结决策一致，39/39 PASS。AboutDialog 完整 HTML 未变化。无冻结译文被清空、改写或改为 unfinished。

## B3-6 整体差异
- 新增 9：九个顶级菜单，QObject，预期
- 删除 0
- Translation 变化 1：`tb::ui::AppController/Open Map`（非冻结消息），lupdate same-text heuristic 从 WelcomeWindow 复制“打开地图”；该变化仅在临时 TS
- Location 变化 561：lupdate 路径规范化，内容未变
- Source/Context/状态的其他变化：0
- 非授权中文译文写入冻结消息：0

## B3-7 保护
正式 TS、五个源码、QRC、CMake、Main.cpp、构建/测试 EXE、测试配置、原版 Release 与 Git 状态均与开始快照一致；Git dirty 仍为 12。报告目录新增文件属预期。

## 归档与停止
`reports\P2-D3B-B03-T4-2-3-B3\` 含执行报告、六份审计 CSV、B4 准备度、开始/结束快照、临时 TS、lupdate 命令/stdout/stderr、SHA256SUMS。SHA 覆盖全部应归档文件、清单不自列，独立复算全部通过。未上传 GitHub，无可验证链接。未进入 B4。
