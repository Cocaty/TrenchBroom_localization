# A1_Menu_Translation_Static_Report — 九条顶级菜单静态验证

## 结果：**9/9 PASS**

使用 Qt 6.10.3 lconvert 将新 EXE 中提取的 embedded QM 回转至 `Artifacts/TrenchBroom_zh_CN.embedded.roundtrip.ts`（退出码 0），以 QM 实际内容而非正式 TS 或构建日志作为证据。

| Context | Source | Expected | QM Translation | Result |
|---|---|---|---|---|
| QObject | File | 文件 | 文件 | PASS |
| QObject | Edit | 编辑 | 编辑 | PASS |
| QObject | Selection | 选择 | 选择 | PASS |
| QObject | Groups | 分组 | 分组 | PASS |
| QObject | Tools | 工具 | 工具 | PASS |
| QObject | View | 视图 | 视图 | PASS |
| QObject | Run | 运行 | 运行 | PASS |
| QObject | Debug | 调试 | 调试 | PASS |
| QObject | Help | 帮助 | 帮助 | PASS |

回转 TS 共 51 条 finished，与正式 TS 的 51 条 finished 数量一致。静态 QM 证据证明这九条译文已进入新 EXE 的嵌入资源；不证明运行期 QTranslator 加载或中文界面实际显示，后者留待 B7。
