# A0_Temporary_Environment_Isolation_Proposal — 临时子进程环境隔离方案（仅设计）

## 分类：**TEMP_ENV_ISOLATION_FEASIBLE**

当前 PowerShell 构建进程中，`HTTPS_PROXY`/`https_proxy` 与 `HTTP_PROXY`/`http_proxy` 两组重复变量的值各自完全相同；因此可以在**单次构建子进程**中仅保留一个规范名称，不会造成代理配置功能差异。用户级和系统级注册表不存在重复变量，无需也不得修改持久环境。

## 方案
1. 不动系统、用户注册表、当前终端或 WorkBuddy 全局环境
2. 在启动下一次构建前，于内存中复制当前进程环境字典
3. 按 Windows 大小写不敏感规则归一化变量名
4. 对每组重复代理变量：
   - 比较值哈希；若完全相同，保留一个规范名称（建议全大写 `HTTPS_PROXY`、`HTTP_PROXY`）
   - 若不完全相同，停止并要求用户选择，不得自行取舍
5. 将其余变量（PATH、INCLUDE、LIB、LIBPATH、VCPKG_*、Qt 相关等）原样保留
6. 仅把整理后的 environment block 传给下一次构建子进程
7. 构建结束后该环境随子进程销毁，不写回任何位置

## 问题回答
- **A 值是否相同**：是（PowerShell 当前进程两组均 SAME_VALUE）。可保留一个规范名称；若未来不同则必须用户确认
- **B Windows 大小写不敏感**：是。方案按小写归一化检测重复，符合 Windows/MSBuild 行为
- **C 仅本次构建**：是。不调用 setx、不改注册表、不改父进程，仅影响新建子进程
- **D 防泄露**：代理值只在内存比较和哈希，不写入日志/报告/CSV；本阶段归档文件没有代理值
- **E 保证正常继承**：从当前进程完整环境复制，只删除重复键中的一个，不重造不完整环境
- **F 安全实施**：可行，但必须用户另行授权；本阶段不执行

## 伪代码（仅说明，不执行）
```text
env = copy(current_process_environment)
groups = group_by_lower(env.names)
for group in groups:
    if len(group) > 1:
        if hashes(group.values) are not all equal: stop_and_ask_user()
        keep canonical uppercase name; remove other case variants from env copy
start_build_subprocess(command=authorized_cmake_build_command, environment=env)
```

## 禁止事项
不得在本阶段或未经授权的下一次行动中：修改注册表、使用 setx、修改 PATH、把代理值写入文件、启动 CL.exe/构建/GUI、手动启动 DumpShortcuts.exe 或 TrenchBroom.exe。

本文件仅为方案设计，未执行任何隔离或构建。
