#!/usr/bin/env python3
# A1 raw Windows environment block reader / temporary env isolation launcher.
# Safety: never writes raw environment values or proxy values to disk.
import ctypes, csv, hashlib, json, os, shlex, sys, time
from ctypes import wintypes

R = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3B-B03-T4-2-3-B6-D2-A1"
D2_CMD_FILE = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3B-B03-T4-2-3-B6-D2\D2_Build_Command.txt"
CHILD_SCRIPT = R + r"\Evidence\env_validate_child.py"
EXPECTED_DUP_GROUPS = {"http_proxy", "https_proxy"}
DROP_NAMES = {"http_proxy", "https_proxy"}

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
kernel32.GetEnvironmentStringsW.restype = ctypes.c_void_p
kernel32.GetEnvironmentStringsW.argtypes = []
kernel32.FreeEnvironmentStringsW.argtypes = [ctypes.c_void_p]
kernel32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
kernel32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
kernel32.CreateProcessW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, ctypes.c_void_p, ctypes.c_void_p, wintypes.BOOL, ctypes.c_void_p, wintypes.LPCWSTR, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
kernel32.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]

class STARTUPINFOW(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("lpReserved", wintypes.LPWSTR), ("lpDesktop", wintypes.LPWSTR), ("lpTitle", wintypes.LPWSTR), ("dwX", wintypes.DWORD), ("dwY", wintypes.DWORD), ("dwXSize", wintypes.DWORD), ("dwYSize", wintypes.DWORD), ("dwXCountChars", wintypes.DWORD), ("dwYCountChars", wintypes.DWORD), ("dwFillAttribute", wintypes.DWORD), ("dwFlags", wintypes.DWORD), ("wShowWindow", wintypes.WORD), ("cbReserved2", wintypes.WORD), ("lpReserved2", ctypes.c_void_p), ("hStdInput", wintypes.HANDLE), ("hStdOutput", wintypes.HANDLE), ("hStdError", wintypes.HANDLE)]

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [("hProcess", wintypes.HANDLE), ("hThread", wintypes.HANDLE), ("dwProcessId", wintypes.DWORD), ("dwThreadId", wintypes.DWORD)]

class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [("nLength", wintypes.DWORD), ("lpSecurityDescriptor", ctypes.c_void_p), ("bInheritHandle", wintypes.BOOL)]


def raw_entries():
    ptr = kernel32.GetEnvironmentStringsW()
    if not ptr:
        raise RuntimeError("GetEnvironmentStringsW failed")
    out = []
    p = ptr
    try:
        while True:
            s = ctypes.wstring_at(p)
            if s == "":
                break
            out.append(s)
            p += (len(s) + 1) * ctypes.sizeof(ctypes.c_wchar)
    finally:
        kernel32.FreeEnvironmentStringsW(ptr)
    return out


def parse(entry):
    if entry.startswith("="):
        return ("", entry, True)  # special environment entry; preserve verbatim
    if "=" not in entry:
        return (entry, "", False)
    name, value = entry.split("=", 1)
    return (name, value, False)


def groups(entries):
    d = {}
    for e in entries:
        name, value, special = parse(e)
        if name and not special:
            d.setdefault(name.lower(), []).append((name, value))
    return d


def h(value):
    return hashlib.sha256(value.encode("utf-8", "replace")).hexdigest()


def check_environment():
    entries = raw_entries()
    g = groups(entries)
    dup_groups = {k: v for k, v in g.items() if len(v) > 1}
    status = "PASS"
    reasons = []
    if set(dup_groups) != EXPECTED_DUP_GROUPS:
        status = "FAIL"; reasons.append("unexpected duplicate group set")
    for key in EXPECTED_DUP_GROUPS:
        vals = {h(v) for _, v in dup_groups.get(key, [])}
        if len(vals) != 1:
            status = "FAIL"; reasons.append(key + " values differ")
    return entries, g, dup_groups, status, reasons


def sanitize(entries):
    out = []
    for e in entries:
        name, value, special = parse(e)
        if not special and name.lower() in DROP_NAMES and name.islower():
            continue
        out.append(e)
    return out


def env_block(entries):
    # Preserve order; CreateProcessW accepts a double-NUL terminated Unicode block.
    text = "\0".join(entries) + "\0\0"
    return ctypes.create_unicode_buffer(text)


def write_audit(entries, g, dup_groups, status, reasons):
    path = R + r"\A1_Environment_Variable_Audit.csv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(["Variable_Name", "Normalized_Name", "Duplicate_Group", "Value_Present", "Value_Length", "Value_Hash", "Value_Equality", "Scope"])
        for e in entries:
            name, value, special = parse(e)
            if special:
                w.writerow(["<SPECIAL_ENTRY>", "<SPECIAL>", "", "YES", len(e), h(e), "PRESERVED", "RAW_BLOCK"])
                continue
            norm = name.lower()
            peers = g.get(norm, [])
            eq = "ONLY_ONE_NAME" if len(peers) == 1 else ("SAME_VALUE" if len({h(v) for _, v in peers}) == 1 else "DIFFERENT_VALUES")
            w.writerow([name, norm, norm if len(peers) > 1 else "", "YES", len(value), h(value), eq, "RAW_BLOCK"])
    with open(R + r"\A1_Environment_Block_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(["Metric", "Value", "Note"])
        w.writerows([
            ["Raw_Entry_Count", len(entries), "GetEnvironmentStringsW; no .NET dictionary"],
            ["Special_Entry_Count", sum(1 for e in entries if e.startswith("=")), "preserved verbatim"],
            ["Duplicate_Group_Count", len(dup_groups), "case-insensitive"],
            ["Duplicate_Group_Names", ",".join(sorted(dup_groups)), "names only"],
            ["Check_Result", status, ";".join(reasons) if reasons else "expected duplicates only"],
            ["Drop_List", ",".join(sorted(DROP_NAMES)), "lowercase case variants in memory only"],
            ["Sensitive_Values_Written", "NO", "value hashes only"],
        ])


def recover_build_command():
    raw = open(D2_CMD_FILE, encoding="utf-8-sig").readline().strip()
    if raw.startswith("Command:"):
        raw = raw[len("Command:"):].strip()
    parts = shlex.split(raw)
    conv = []
    for p in parts:
        if p.startswith("/c/"):
            p = "C:" + p[2:].replace("/", "\\")
        conv.append(p)
    cmdline = " ".join('"' + p + '"' if (" " in p or "\t" in p) else p for p in conv)
    cwd = conv[conv.index("--build") + 1]
    return raw, cmdline, cwd


def spawn(cmdline, cwd, env_entries, stdout_path, stderr_path):
    sa = SECURITY_ATTRIBUTES(); sa.nLength = ctypes.sizeof(SECURITY_ATTRIBUTES); sa.lpSecurityDescriptor = None; sa.bInheritHandle = True
    out = kernel32.CreateFileW(stdout_path, 0x40000000, 1, ctypes.byref(sa), 2, 0x80, None)
    err = kernel32.CreateFileW(stderr_path, 0x40000000, 1, ctypes.byref(sa), 2, 0x80, None)
    si = STARTUPINFOW(); si.cb = ctypes.sizeof(STARTUPINFOW); si.dwFlags = 0x100; si.hStdOutput = out; si.hStdError = err; si.hStdInput = None
    pi = PROCESS_INFORMATION()
    block = env_block(env_entries)
    cmd_buf = ctypes.create_unicode_buffer(cmdline)
    ok = kernel32.CreateProcessW(None, cmd_buf, None, None, True, 0x400, block, cwd, ctypes.byref(si), ctypes.byref(pi))
    if not ok:
        raise OSError(ctypes.get_last_error(), "CreateProcessW failed")
    code = wintypes.DWORD()
    kernel32.WaitForSingleObject(pi.hProcess, 0xFFFFFFFF)
    kernel32.GetExitCodeProcess(pi.hProcess, ctypes.byref(code))
    for hnd in (pi.hThread, pi.hProcess, out, err):
        kernel32.CloseHandle(hnd)
    return code.value, pi.dwProcessId


mode = sys.argv[1] if len(sys.argv) > 1 else "audit"
entries, g, dups, status, reasons = check_environment()
if status != "PASS":
    write_audit(entries, g, dups, status, reasons)
    raise SystemExit("ENVIRONMENT_CHECK_FAILED:" + ";".join(reasons))
clean = sanitize(entries)
write_audit(entries, g, dups, status, reasons)

if mode == "audit":
    print("RAW_ENV_OK entries=" + str(len(entries)) + " clean=" + str(len(clean)) + " duplicates=" + ",".join(sorted(dups)))
elif mode == "validate":
    cmd = '"' + sys.executable + '" "' + CHILD_SCRIPT + '"'
    start = time.time()
    code, pid = spawn(cmd, R, clean, R + r"\A1_Temporary_Process_stdout.txt", R + r"\A1_Temporary_Process_stderr.txt")
    print("VALIDATION_EXIT=" + str(code) + " PID=" + str(pid) + " ELAPSED=" + str(round(time.time() - start, 2)))
elif mode == "build":
    original, cmdline, cwd = recover_build_command()
    with open(R + r"\A1_Build_Command.txt", "w", encoding="utf-8") as f:
        f.write("Original_D2_Command: " + original + "\n")
        f.write("Normalized_CreateProcessW_Command: " + cmdline + "\n")
        f.write("WorkingDirectory: " + cwd + "\n")
        f.write("Start: " + time.strftime("%Y-%m-%d %H:%M:%S %z") + "\n")
    start = time.time()
    code, pid = spawn(cmdline, cwd, clean, R + r"\A1_Build_stdout.txt", R + r"\A1_Build_stderr.txt")
    with open(R + r"\A1_Build_Command.txt", "a", encoding="utf-8") as f:
        f.write("ExitCode: " + str(code) + "\n")
        f.write("End: " + time.strftime("%Y-%m-%d %H:%M:%S %z") + "\n")
        f.write("ElapsedSeconds: " + str(round(time.time() - start, 2)) + "\n")
        f.write("CreateProcessW_PID: " + str(pid) + "\n")
    print("BUILD_EXIT=" + str(code) + " PID=" + str(pid) + " ELAPSED=" + str(round(time.time() - start, 2)))
else:
    raise SystemExit("UNKNOWN_MODE")
