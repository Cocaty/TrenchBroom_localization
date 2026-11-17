# T3_Authorization_Record — B03 Qt 翻译编译授权

- 开始时间：2026-11-17 20:35:05 +0800
- 任务：P2-D3B-B03-T3，以 T2 写入后的正式 TS 为输入，使用 Qt 6.10.3 lrelease 生成独立 QM，并做静态验证
- 唯一允许写入 QM 的位置：`reports\P2-D3B-B03-T3\Artifacts\TrenchBroom_zh_CN.qm`
- 授权操作：只读核验工具、lrelease 默认行为编译、lconvert 回转至本阶段临时审计 TS、静态核验、生成报告
- 明确未授权：修改正式 TS/源码/CMake/QRC、替换正式 QM、运行 lupdate/lrelease 于正式资源目录、构建、启动、部署、Git 写操作、进入 T4

本轮未修改正式 TS；正式 QM 资源目录与安装目录未被写入。
