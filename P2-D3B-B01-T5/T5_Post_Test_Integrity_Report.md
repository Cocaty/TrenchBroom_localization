# T5_Post_Test_Integrity_Report — 运行结束后保护核验（T5-6）

| 对象 | 开始 | 结束 | 判定 |
|---|---|---|---|
| 原版 Release/TrenchBroom.exe | f5a02f40dde7108f… | 同值 | ✅ |
| 原版 Release/Qt6Core.dll | b712b4754588e89f… | 同值 | ✅ |
| 构建树 EXE | 9a1a84991c61d1d1… | 同值 | ✅ |
| 构建树 QM | a2f5cc1f892cfd8a… | 同值 | ✅ |
| Git HEAD / dirty | 4c756be1… / 7 | 同值 | ✅ |
| 正式 TS | 6582a38280e7ac1c… | 同值 | ✅ |
| T2 证据清单 | 8/8 OK | 8/8 OK | ✅（E1 补证位于 T2 目录内） |
| T3 证据清单 | 12/12 OK | 12/12 OK | ✅ |
| T4 证据清单 | 12/12 OK | 12/12 OK | ✅ |
| 日常 INI | 5062ef854b994caf…，1,399 B，12:42:23 | 同值 | ✅ |
| 日常 Preferences.json / 两个日志 | 50705006…/495d87fa…/04d055c3… | 同值 | ✅ |
| TrenchBroom 进程 | 0 | **0**（3 次启动均正常关闭，含多窗口实例二次关闭） | ✅ |
| 正式安装目录 | 未部署 | 未部署 | ✅ |
| Documents 下真实地图 | 未打开/未创建/未修改 | 同左 | ✅ |

## 测试副本内部（预期变化）
- `app\config\Preferences.json` 由无语言键 → zh_CN → en（最终 en）
- stdout/stderr 日志 6 个文件均 0 B（无崩溃与 Qt 警告）
- `T5_Test_Copy_Manifest.csv` 记录初始 395 个文件，运行后仅 config 为新增数据

**结论：无越权变化。**
