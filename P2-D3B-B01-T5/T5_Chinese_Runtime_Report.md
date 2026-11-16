# T5_Chinese_Runtime_Report — 中文加载与 B01 逐条结果（T5-4）

## QTranslator 实际加载（运行观察）
切换到简体中文并重启后（PID 23996），界面出现：
- Language 标签 → **“语言”**
- 下拉框 → **“简体中文”**，两个选项为 **English / 简体中文**
- 两处信息提示 → **“更改后需要重启”**
- 切回 English 时模态提示 → **“语言更改将在重启 TrenchBroom 后生效。”**

以上文本来自既有的 3 条 finished 译文（context `tb::ui::ViewPreferencePane`），说明 **QTranslator 已成功加载 `:/translations/TrenchBroom_zh_CN.qm` 并生效**（功能级证据，非仅静态字节）；未观察到加载失败警告（stderr2.log 为 0 B）。

截图：`Evidence/T5_05_restart_prompt_english.png`（英文提示）、`T5_06_chinese_preferences.png`、`T5_07_language_chinese.png`、`T5_08_chinese_main.png`、`T5_09_language_menu_chinese.png`、`T5_12_prompt_chinese.png`（中文提示）

## B01 18 条逐项结果
见 `T5_Chinese_Runtime_Verification.csv`（18 行）。**18/18 均为 NOT TESTED**，无一条标记 PASS：
- 这 18 条全部位于 `createFileMenu` 的 File 菜单及其 tooltip；Welcome 窗口没有 File 菜单
- 打开地图文档需要先配置游戏路径并创建/打开地图；本轮授权明确禁止打开、修改、创建或保存真实地图，也未授权修改游戏配置
- 因此无法在不越界的前提下触达这些菜单项与提示
- **不以 TS/QM/EXE 中存在译文字节代替界面实测**；Wavefront OBJ... 按冻结决策应保留英文，亦未实测

## tooltip 截图
尝试悬停 Language 行与信息标签，未出现 tooltip（`T5_10_tooltip_attempt.png`、`T5_11_tooltip_retry.png`）；B01 的 tooltip 位于不可触达的 File 菜单，故未采集到 B01 中文 tooltip 截图。

## 结论
中文翻译管线运行期加载成功；B01 18 条 UI 显示未能验证，全部诚实标记 NOT TESTED。
