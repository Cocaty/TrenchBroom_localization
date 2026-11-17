#!/usr/bin/env python3
# D0-1 read-only PE dependency closure analysis.
# No EXE is launched. No files outside this report directory are written.
import csv, os, re, struct, subprocess, collections, hashlib

B = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN"
S = B + r"\src\TrenchBroom"
R = B + r"\reports\P2-D3B-B03-T4-2-3-B6-D1-D0-1"
BUILD = B + r"\build\v2026.2-msvc145-qt6103"
DD = BUILD + r"\app\DumpShortcuts\Release"
TBREL = BUILD + r"\app\TrenchBroom\Release"
DB = r"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\dumpbin.exe"
SYSTEM = r"C:\Windows\System32"
QTBIN = r"C:\Users\yoshi\tools\Qt\6.10.3\6.10.3\msvc2022_64\bin"

# Read actual vcpkg configuration from CMakeCache; do not guess.
cache = open(BUILD + r"\CMakeCache.txt", encoding="utf-8", errors="replace").read().splitlines()
cfg = {}
for line in cache:
    if line.startswith(("VCPKG_INSTALLED_DIR:", "VCPKG_TARGET_TRIPLET:")):
        k, v = line.split("=", 1)
        cfg[k.split(":")[0]] = v
VCPKG = os.path.join(cfg["VCPKG_INSTALLED_DIR"], cfg["VCPKG_TARGET_TRIPLET"], "bin")
VCRED = r"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Redist\MSVC\14.51.36231\x64\Microsoft.VC145.CRT"
PATH_DIRS = [p for p in os.environ.get("PATH", "").split(";") if p]
LOADER_DIRS = [DD, SYSTEM] + PATH_DIRS
SOURCE_DIRS = [DD, SYSTEM, VCRED, QTBIN, VCPKG] + PATH_DIRS


def norm(p):
    return os.path.abspath(p).replace('\\','/').lower()


def inside(path, root):
    return norm(path).startswith(norm(root))


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def arch(p):
    try:
        with open(p, "rb") as f:
            f.seek(0x3c); off = struct.unpack("<I", f.read(4))[0]
            f.seek(off + 4); machine = f.read(2)
        return "x64" if machine == b"\x64\x86" else ("x86" if machine == b"\x4c\x01" else "UNKNOWN")
    except Exception:
        return "UNKNOWN"


def resolve(name, dirs):
    for d in dirs:
        c = os.path.join(d, name)
        if os.path.isfile(c):
            return c
    return None


def imports(path):
    out = subprocess.run([DB, "/imports", path], capture_output=True, text=True, errors="replace").stdout
    ordinary, delay = set(), set()
    mode = "ORDINARY"
    for line in out.splitlines():
        low = line.lower()
        if "delay load import address table" in low:
            mode = "DELAY"
        elif "import address table" in low and "delay" not in low:
            mode = "ORDINARY"
        m = re.search(r"\b([A-Za-z0-9._-]+\.dll)\b", line, re.I)
        if m:
            (delay if mode == "DELAY" else ordinary).add(m.group(1))
    return ordinary | delay, ordinary, delay


def classification(name, actual):
    low = name.lower()
    if low.startswith(("api-ms-win-", "ext-ms-")):
        return "WINDOWS_APISET"
    if actual and inside(actual, SYSTEM):
        return "WINDOWS_SYSTEM"
    if actual and inside(actual, VCRED):
        return "MSVC_RUNTIME"
    if actual and inside(actual, QTBIN):
        return "QT_LIBRARY"
    if name.lower().startswith("qt6") or name.lower().startswith("icu"):
        return "QT_LIBRARY"
    if actual and inside(actual, VCPKG):
        return "VCPKG_THIRDPARTY"
    if actual and inside(actual, DD):
        return "DEPLOYED_IN_APP_DIR"
    return "OTHER"


root = DD + r"\DumpShortcuts.exe"
graph = []
seen = set()


def walk(path, parent, import_type, depth=0):
    name = os.path.basename(path)
    key = name.lower()
    if depth > 8:
        return
    # Keep repeated edges but recurse only once per physical module.
    loader = resolve(name, LOADER_DIRS)
    source = resolve(name, SOURCE_DIRS)
    actual = source
    cls = classification(name, actual)
    dep_names = []
    if actual and not cls.startswith("WINDOWS") and cls not in ("MSVC_RUNTIME",):
        try:
            dep_names, ords, delays = imports(actual)
        except Exception:
            dep_names, ords, delays = [], set(), set()
    else:
        ords, delays = set(), set()
    needs = "NO"
    if cls in ("VCPKG_THIRDPARTY", "QT_LIBRARY") and not (loader and inside(loader, DD)):
        needs = "YES"
    if cls == "OTHER" and not actual:
        needs = "YES_UNRESOLVED"
    graph.append([
        name, parent or "ROOT", import_type, ";".join(sorted(ords)), ";".join(sorted(delays)),
        actual or "", "YES" if actual else "NO", sha(actual) if actual else "", arch(actual) if actual else "",
        "NOT_VERIFIED", "YES" if actual and inside(actual, DD) else "NO",
        "YES" if actual and inside(actual, QTBIN) else "NO",
        "YES" if actual and inside(actual, VCPKG) else "NO",
        "YES" if actual and inside(actual, VCRED) else "NO",
        "YES" if actual and inside(actual, SYSTEM) else "NO",
        cls, "YES" if cls == "WINDOWS_APISET" else "NO", needs, depth,
    ])
    if key in seen:
        return
    seen.add(key)
    for d in sorted(dep_names):
        target = resolve(d, SOURCE_DIRS)
        walk(target or os.path.join(DD, d), name, "DELAY" if d in delays else "ORDINARY", depth + 1)


walk(root, "", "ROOT")

with open(R + r"\D0-1_PE_Dependency_Graph.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["File_Name", "Parent", "Import_Type", "Ordinary_Imports", "Delay_Imports", "Resolved_Path", "Exists", "SHA256", "PE_Architecture", "File_Version", "In_DumpShortcuts_Release", "In_Qt_Bin", "In_Vcpkg_Bin", "In_MSVC_Redist", "In_System32", "Classification", "API_Set", "Needs_App_Dir_Deployment", "Depth"])
    w.writerows(graph)

# Search path audit
rows = []
for label, d in [("EXE_DIR", DD), ("SYSTEM32", SYSTEM), ("MSVC_REDIST", VCRED), ("QT_BIN", QTBIN), ("VCPKG_BIN", VCPKG)] + [("PATH_" + str(i), p) for i, p in enumerate(PATH_DIRS)]:
    rows.append([label, d, "YES" if os.path.isdir(d) else "NO", "YES" if any(norm(d) == norm(p) for p in PATH_DIRS) else "NO"])
with open(R + r"\D0-1_Runtime_Search_Path_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Category", "Path", "Exists", "In_CURRENT_PATH"]); w.writerows(rows)

print("GRAPH_NODES", len(graph), "LOADER_DIRS", len(LOADER_DIRS), "VCPKG", VCPKG)
