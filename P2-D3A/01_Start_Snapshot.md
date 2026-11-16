# 01_Start_Snapshot — P2-D3A 开始快照（只读，2026-11-16 20:47）

## Git / 基线
- 分支 feature/zh-CN-v2026.2；HEAD 4c756be1a54a28d921d18c77716a5f170bdc31d0；tag v2026.2；dirty=7（P2-D2B 2 CMake + P2-D2C-B 4 代码 + translations/）
- TS 路径实测存在：`app\TrenchBroom\translations\TrenchBroom_zh_CN.ts`

## TS 属性
| 项 | 实测 |
|---|---|
| SHA-256 | 83a9aa45eaef5213ee58d44bb6096bf10288aa4668da6c63ca8e154742e0a198 |
| 大小 | 130,964 B |
| 编码 / 换行 | UTF-8 无 BOM；LF×3,151（无 CRLF）；XML 声明 `<?xml version="1.0" encoding="utf-8"?>` + `<!DOCTYPE TS>` |
| mtime | 2026-11-16 20:14:36 +0800 |

TS 哈希与 P2-D2C-C 验收版本（R3 lupdate 后）一致 ✅

## 历史报告存在性（文件数实测）
P2-D2B=9、P2-D2C-B-R1=8、P2-D2C-B-R2=4、P2-D2C-B-R3=13、P2-D2C-C=13（均存在）✅

## 原版 Release
TrenchBroom.exe `f5a02f40dde7108f…` / Qt6Core.dll `b712b4754588e89f…` ——与历史基线一致 ✅

## 声明
本轮所有统计均**重新解析当前 TS/源码**，未引用历史统计值作为事实；全程只读，未修改 TS/源码/CMake/构建产物。
