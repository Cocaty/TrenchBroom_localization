# Git_Status_and_Diff — Git 状态与修改范围证据

日期：2026-11-16 19:18 ｜ 全部输出为当日实测（非转述）

## 基本状态

| 项 | 值 |
|---|---|
| 分支 | feature/zh-CN-v2026.2 |
| HEAD | 4c756be1a54a28d921d18c77716a5f170bdc31d0 |
| tag | v2026.2 |

## git status --short

```
 M CMakeLists.txt
 M app/TrenchBroom/CMakeLists.txt
 M app/TrenchBroom/src/Main.cpp
 M lib/TbPreferencesLib/include/Preferences.h
 M lib/TbUiLib/include/ui/ViewPreferencePane.h
 M lib/TbUiLib/src/ViewPreferencePane.cpp
?? app/TrenchBroom/translations/
```

## git diff --name-status

```
M	CMakeLists.txt
M	app/TrenchBroom/CMakeLists.txt
M	app/TrenchBroom/src/Main.cpp
M	lib/TbPreferencesLib/include/Preferences.h
M	lib/TbUiLib/include/ui/ViewPreferencePane.h
M	lib/TbUiLib/src/ViewPreferencePane.cpp
```

## git diff --stat

```
 app/TrenchBroom/src/Main.cpp                | 30 +++++++++++++++++++++
 lib/TbPreferencesLib/include/Preferences.h  |  1 +
 lib/TbUiLib/include/ui/ViewPreferencePane.h |  2 ++
 lib/TbUiLib/src/ViewPreferencePane.cpp      | 41 +++++++++++++++++++++++++++++
 CMakeLists.txt                              | (D2B: 1 行替换)
 app/TrenchBroom/CMakeLists.txt              | (D2B: 6 行追加)
 6 files changed, 81 insertions(+), 1 deletion(-)
```

## 归属区分

| 归属 | 文件 | 规模 |
|---|---|---|
| **P2-D2B 既有修改** | CMakeLists.txt（顶层）、app/TrenchBroom/CMakeLists.txt | 7 增 1 删 |
| **P2-D2C-B 新增修改** | Main.cpp（+30）、Preferences.h（+1）、ViewPreferencePane.h（+2）、ViewPreferencePane.cpp（+41） | **74 增 0 删** |
| **未跟踪** | app/TrenchBroom/translations/（内含 TrenchBroom_zh_CN.ts，127,729 B） | 必须计入物理文件总数：**7 个物理文件（6 修改 + 1 新增 TS）** |

## 五个本轮授权文件的实际路径

1. `app/TrenchBroom/src/Main.cpp`（已修改）
2. `lib/TbPreferencesLib/include/Preferences.h`（已修改）
3. `lib/TbUiLib/src/ViewPreferencePane.cpp`（已修改）
4. `lib/TbUiLib/include/ui/ViewPreferencePane.h`（已修改——实际路径核实结果）
5. `app/TrenchBroom/translations/TrenchBroom_zh_CN.ts`（已更新，未跟踪目录内）

完整 diff 见 `Evidence/git_diff_full.txt`（SHA-256 见 SHA256SUMS.txt）。
