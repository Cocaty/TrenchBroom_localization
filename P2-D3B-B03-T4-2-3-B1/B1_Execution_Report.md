# B1_Execution_Report — 九条顶级菜单译文冻结与实施前最终核验

## 最终状态：**PASS_WITH_LIMITATIONS**

技术复核通过，A1 方案 D 无未解决结构风险；**九条译文未获用户明确确认**，Decision_Status 全部为 `PENDING_USER_CONFIRMATION`，Message_ID 为 `PENDING_LUPDATE`，未冻结、未写入。限制即“等待用户确认 + lupdate 未验证”。

## B1-0 基线
分支 `feature/zh-CN-v2026.2`、HEAD `4c756be1…`、dirty=7。五个目标源码文件、正式 TS `f021e509…`、QRC `de72b206…`、CMake/Main.cpp、QM `707011a3…`、构建/测试 EXE、测试配置与 A0/A1 报告均与基线一致，无 BASELINE_MISMATCH。开始快照 18 项，保护对照 19/19 未变。

## B1-1 术语审查
正式 TS 中九个 Source 精确匹配均为 0（`NOT_PRESENT_IN_TS`）。候选“文件/编辑/选择/分组/工具/视图/运行/调试/帮助”与现有译文作交叉检查：
- “文件”已用于“地图文件...”“加载点轨迹文件...”等，但作为顶级菜单“File”简洁可用
- “选择”与“选择路径类型”“进行选择”一致；“编辑”“工具”仅出现在更长表述中，无冲突
- “分组/视图/运行/调试/帮助”未发现现有同词条目，无冲突
逐条结果见 `B1_Terminology_Review.csv`。九条仍为候选，须用户确认。

## B1-2 技术复核
- `Menu::name` 为 `std::string`；所有用途见 `A1_Menu_Name_Usage_Audit.csv` 与本阶段 `B1_Menu_Initialization_Audit.csv`
- **发现 A1 未单列的第三处 tb::ui::Menu 聚合初始化**：`ActionManager.h:60` 的 `m_toolBar = Menu{"Toolbar", ...}`；仍在已计划五文件内，不扩大修改范围，但 B2 必须处理
- 全仓无第五个文件外的 `tb::ui::Menu` 初始化点；其他 `QMenu{...}` 属 Qt 类，无关
- 内部英文标识保护：`KeyboardShortcutModel.cpp:260` 与 `DumpShortcuts/src/Main.cpp:141` 继续读取 `name`；方案 D 通过 `displayName` 隔离中文显示
- Context 复核：ActionManager 非 QObject 派生，但现有 `QObject::tr("New Document")` 等大量案例；九条静态字面量可被 Qt 工具识别，但本阶段未运行 lupdate（`LUPDATE_BEHAVIOR_NOT_VERIFIED`）

## B1-3 冻结矩阵
`B1_Frozen_Decision_Matrix.csv` 9 行：Context `QObject`、Source 逐字匹配源码、Translation 为候选、Translation_Status 预定 `finished`、Decision_Status `PENDING_USER_CONFIRMATION`、Message_ID `PENDING_LUPDATE`、Display_Field `displayName`、内部标识保留英文。技术方案可标记为 `TECHNICAL_DESIGN_FROZEN`，但译文未冻结。

## B1-4 B2 准备
见 `B1_B2_Implementation_Readiness.md`；重点新增发现为 Toolbar 初始化点必须适配。

## 归档
报告目录 `reports\P2-D3B-B03-T4-2-3-B1\`，新增 11 个文件；SHA256SUMS 覆盖 10 项、独立复算全部通过、清单不自列。未上传 GitHub，无可验证链接。未修改源码/TS/QM，未运行 lupdate/lrelease，未构建、启动或部署，未进入 B2。
