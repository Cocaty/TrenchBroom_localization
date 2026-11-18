#!/usr/bin/env python3
# Harmless child process: reads its own raw Windows environment block and emits
# only sanitized counts/hashes. Never prints environment values.
import ctypes, hashlib, json
from ctypes import wintypes

k = ctypes.WinDLL("kernel32", use_last_error=True)
k.GetEnvironmentStringsW.restype = ctypes.c_void_p
k.GetEnvironmentStringsW.argtypes = []
k.FreeEnvironmentStringsW.argtypes = [ctypes.c_void_p]

ptr = k.GetEnvironmentStringsW()
if not ptr:
    print(json.dumps({"validation": "FAIL", "error": "GetEnvironmentStringsW failed"}))
    raise SystemExit(2)

entries, p = [], ptr
try:
    while True:
        s = ctypes.wstring_at(p)
        if s == "":
            break
        entries.append(s)
        p += (len(s) + 1) * ctypes.sizeof(ctypes.c_wchar)
finally:
    k.FreeEnvironmentStringsW(ptr)

groups = {}
exact_names = set()
for e in entries:
    if e.startswith("=") or "=" not in e:
        continue
    name, value = e.split("=", 1)
    exact_names.add(name)
    groups.setdefault(name.lower(), []).append((name, value))

dup = {key: names for key, names in groups.items() if len(names) > 1}
expected_dup = {"http_proxy", "https_proxy"}
path_value = ""
for e in entries:
    if e.startswith("PATH="):
        path_value = e[5:]
        break

ok = (set(dup) == set() and "HTTP_PROXY" in exact_names and "HTTPS_PROXY" in exact_names and "http_proxy" not in exact_names and "https_proxy" not in exact_names)
result = {
    "validation": "PASS" if ok else "FAIL",
    "entry_count": len(entries),
    "variable_count": len(groups),
    "special_entry_count": sum(1 for e in entries if e.startswith("=")),
    "duplicate_group_count": len(dup),
    "duplicate_group_names": sorted(dup),
    "http_proxy_present": "http_proxy" in groups,
    "https_proxy_present": "https_proxy" in groups,
    "lowercase_http_present": "http_proxy" in exact_names,
    "lowercase_https_present": "https_proxy" in exact_names,
    "PATH_present": bool(path_value),
    "PATH_length": len(path_value),
    "PATH_segment_count": len(path_value.split(";")),
    "PATH_sha256": hashlib.sha256(path_value.encode("utf-8", "replace")).hexdigest() if path_value else "",
}
print(json.dumps(result, sort_keys=True))
