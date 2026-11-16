# T4_Before_After_Integrity_Report — 构建前后保护核验（T4-5）

| 保护对象 | 构建前 | 构建后 | 判定 |
|---|---|---|---|
| 正式 TS SHA | 6582a38280e7ac1c… | 6582a38280e7ac1c… | ✅ 未修改 |
| C++ / CMake 文件 | git tracked diff 6 files/81 行（既有授权修改） | 同值 | ✅ 未改 |
| Git HEAD / dirty | 4c756be1… / 7 | 同值 | ✅ |
| 未跟踪 translations/ | 1 目录 | 同值 | ✅ |
| T2 证据 SHA 清单 | 8/8 OK | 8/8 OK | ✅ 未覆盖 |
| T3 证据 SHA 清单 | 12/12 OK | 12/12 OK | ✅ 未覆盖 |
| 原版 Release/TrenchBroom.exe | f5a02f40dde7108f… | 同值 | ✅ |
| 原版 Release/Qt6Core.dll | b712b4754588e89f… | 同值 | ✅ |
| 用户 INI | 5062ef854b994caf…，1,399 B，mtime 12:42:23 | 同值 | ✅ 未修改 |
| TrenchBroom 进程 | 0 | 0 | ✅ 未启动 |
| 正式安装目录 | 未部署 | 未部署 | ✅ |

构建过程中发生的预期变化仅限：构建树 QM（366 B → 1,805 B）、构建树 EXE 哈希变化、RCC cpp/OBJ 重新生成——全部位于指定构建目录；未清理或删除既有构建文件。

**结论：无超出授权的变化。**
