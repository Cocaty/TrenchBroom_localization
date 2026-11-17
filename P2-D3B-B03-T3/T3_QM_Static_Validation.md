# T3_QM_Static_Validation — QM 静态验证

## 编译产物
- 输入 TS：`src\TrenchBroom\app\TrenchBroom\translations\TrenchBroom_zh_CN.ts`，写入前 SHA `f021e509cf9a8679eeda64624df0f5474335c0872f73940e1d48ef77447a261a`，132,589 B，85 Context / 562 Message / 42 finished / 520 unfinished
- 输出 QM：`Artifacts\TrenchBroom_zh_CN.qm`，6,631 B，SHA `707011a3216511d051b07d0dba249af6d834e6795a447a4f09611c6a9bd2102c`
- 命令：`lrelease.exe <TS> -qm <QM>`（与 B02-T3 记录的默认编译策略一致，未使用 `-nounfinished`/`-removeidentical` 等过滤参数）
- lrelease 版本 6.10.3；stdout/stderr、退出码与时间见 `T3_Lrelease_Log.txt`

## QM 文件头
前 16 字节为 Qt QM 魔数 `3cb86418caef9c95cd211cbf60a1bddd`，有效；第 17 字节 `0xA7` 为 Language 块标签，文件非空且未截断。

## lconvert 回转
- 命令：`lconvert.exe -i <QM> -o Artifacts\TrenchBroom_zh_CN_roundtrip.ts`
- 退出码 0；日志 `Evidence\lconvert_log.txt`
- 回转 TS：9,177 B，XML 解析成功；包含 8 Context / 42 message，全部为正式 TS 中 finished 的条目
- lconvert 不提供 `-version` 输出；工具来源通过真实路径 `C:\Users\yoshi\tools\Qt\6.10.3\6.10.3\msvc2022_64\bin\lconvert.exe`、SHA `707af8e9963027ef2cff9ac03ab538d46c22cb78d9486c8bf1d66fb814d2aae8` 与 B02-T3 记录交叉确认

## 字段可比性
- 可比字段：Context、Source、Translation（42/42 与正式 TS finished 集完全一致）
- 不适用于 QM 回转比较的字段：Message ID（由 Context+Source 导出用于审计，不是 QM 存储字段）、location 行号、comment/translatorcomment、TS 节点顺序、unfinished 状态
- 不以 basename 或仅 Source 文本匹配；使用 Context+Source 联合定位

**结论：QM 编译与静态结构/回转验证通过。此结果不代表程序启动或运行期汉化。**
