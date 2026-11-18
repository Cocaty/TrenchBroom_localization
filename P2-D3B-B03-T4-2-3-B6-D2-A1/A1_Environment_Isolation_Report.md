# A1_Environment_Isolation_Report — 临时环境隔离

## 结果：**PASS**

使用 Windows 原生 `GetEnvironmentStringsW` 从实际 PowerShell 父进程读取原始环境块，未经过 .NET 大小写不敏感环境字典。

- 原始条目 214；重复组仅 `http_proxy`、`https_proxy`
- 两组同组值完全相同；重复项按 A0/A1 规则只在内存副本中删除小写变体
- 清理后条目 212；其余变量原样保留（包括 PATH、INCLUDE、LIB、LIBPATH、VCPKG_*、Qt 与 MSVC 相关变量）
- 特殊环境条目：0
- 未输出任何代理值；仅记录存在性、长度与 SHA256

## 无害子进程验证
使用与正式构建完全相同的临时环境块，通过 `CreateProcessW` + `CREATE_UNICODE_ENVIRONMENT` 启动只读验证子进程：

- 退出码 0
- 子进程环境条目 212，重复组 0
- `HTTP_PROXY` / `HTTPS_PROXY` 各仅一次；小写变体不存在
- PATH 长度 826、20 段；父/子 PATH SHA256 一致
- `validation=PASS`

未修改父进程、用户级或系统级环境；未使用 setx、未改注册表或 PATH。正式构建仅使用一次性内存环境。
