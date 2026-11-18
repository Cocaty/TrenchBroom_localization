#!/usr/bin/env python3
# A0 read-only MSBuild error-chain and toolchain metadata audit.
import os, csv, hashlib

B = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN"
R = B + r"\reports\P2-D3B-B03-T4-2-3-B6-D2-A0"
LOG = B + r"\reports\P2-D3B-B03-T4-2-3-B6-D2\D2_Build_stdout.txt"

lines = open(LOG, encoding="utf-8", errors="replace").read().splitlines()
chain = []
for n, line in enumerate(lines, 1):
    if "Generating gen-manual/shortcuts.js" in line:
        chain.append([n, line.strip()[:200], "GenerateManual", "PASS"])
    if "Generating TrenchBroom_zh_CN.qm" in line or "Generated 51 translation" in line:
        chain.append([n, line.strip()[:200], "QM_Generation", "PASS"])
    if "Running rcc for resource" in line:
        chain.append([n, line.strip()[:200], "RCC", "STARTED"])
    if "error MSB6001" in line:
        chain.append([n, line.strip()[:220], "Compiler_ToolTask", "FAIL"])
    if "get_EnvironmentVariables()" in line:
        chain.append([n, line.strip()[:220], "Environment_Dictionary", "FAIL_BEFORE_PROCESS_START"])
with open(R + r"\A0_MSBuild_Error_Chain_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Log_Line", "Evidence", "Stage", "Result"]); w.writerows(chain)

paths = {
    "CMake": r"C:\Users\yoshi\Tools\CMake\4.2.8\bin\cmake.exe",
    "MSBuild": r"C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Current\Bin\MSBuild.exe",
    "Compiler": r"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe",
}
rows = []
for name, path in paths.items():
    exists = os.path.isfile(path)
    rows.append([name, path, exists, os.path.getsize(path) if exists else "", hashlib.sha256(open(path, "rb").read()).hexdigest() if exists else "", "FILE_METADATA_ONLY"])
rows += [
    ["MSVC_toolset", "14.51.36231", "YES", "", "", "FROM_PATH"],
    ["CMake_generator", "Visual Studio 18 2026 / x64", "YES", "", "", "FROM_CMAKECACHE"],
    ["Build_config", "Release; target TrenchBroom", "YES", "", "", "FROM_D2_COMMAND"],
    ["Version_queries", "NOT_RUN; tool execution blocked by security policy", "", "", "", "LIMITATION"],
]
with open(R + r"\A0_Toolchain_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Item", "Path_Or_Value", "Exists", "Size_Bytes", "SHA256", "Note"]); w.writerows(rows)
print("chain", len(chain), "toolchain", len(rows))
