#!/usr/bin/env python3
# A1 EXE embedded QM resource audit, following the T4-1 static method.
import csv, hashlib, os

B = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN"
R = B + r"\reports\P2-D3B-B03-T4-2-3-B6-D2-A1"
EXE = B + r"\build\v2026.2-msvc145-qt6103\app\TrenchBroom\Release\TrenchBroom.exe"
B5QM = B + r"\reports\P2-D3B-B03-T4-2-3-B5\Artifacts\TrenchBroom_zh_CN.qm"
BUILDQM = B + r"\build\v2026.2-msvc145-qt6103\app\TrenchBroom\TrenchBroom_zh_CN.qm"
OUT = R + r"\Artifacts\TrenchBroom_zh_CN.embedded.qm"
MAGIC = bytes.fromhex("3cb86418caef9c95cd211cbf60a1bddd")
PATH_BYTES = b":/translations/TrenchBroom_zh_CN.qm"

exe = open(EXE, "rb").read()
a = open(B5QM, "rb").read()
b = open(BUILDQM, "rb").read()
path_off = exe.find(PATH_BYTES)
magic_offsets = []
pos = 0
while True:
    pos = exe.find(MAGIC, pos)
    if pos < 0:
        break
    magic_offsets.append(pos)
    pos += 1
chosen = -1
for off in magic_offsets:
    if exe[off:off + len(b)] == b:
        chosen = off
        break
embedded = exe[chosen:chosen + len(b)] if chosen >= 0 else b""
if embedded:
    open(OUT, "wb").write(embedded)

def sha(x):
    return hashlib.sha256(x).hexdigest()

rows = [
    ["Resource_Path", ":/translations/TrenchBroom_zh_CN.qm", "PASS" if path_off >= 0 else "FAIL"],
    ["Resource_Path_Offset", path_off, "INFO"],
    ["QM_Magic_Offsets", ",".join(str(x) for x in magic_offsets), "INFO"],
    ["Chosen_Magic_Offset", chosen, "PASS" if chosen >= 0 else "FAIL"],
    ["B5_QM_SHA256", sha(a), "INFO"],
    ["Build_QM_SHA256", sha(b), "INFO"],
    ["Embedded_QM_SHA256", sha(embedded) if embedded else "", "PASS" if embedded and sha(embedded) == sha(a) else "FAIL"],
    ["A_B_Size", f"{len(a)}/{len(b)}", "PASS" if len(a) == len(b) else "FAIL"],
    ["A_B_ByteEqual", "YES" if a == b else "NO", "PASS" if a == b else "FAIL"],
    ["B_C_ByteEqual", "YES" if b == embedded else "NO", "PASS" if b == embedded else "FAIL"],
]
with open(R + r"\A1_QM_Embedded_Resource_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Metric", "Value", "Result"]); w.writerows(rows)
with open(R + r"\A1_QM_Byte_Comparison.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Artifact", "Path", "Size_Bytes", "SHA256", "Byte_Equal_To_Build_QM"])
    w.writerow(["A_B5_QM", B5QM, len(a), sha(a), "YES" if a == b else "NO"])
    w.writerow(["B_Build_QM", BUILDQM, len(b), sha(b), "YES"])
    w.writerow(["C_Embedded_QM", OUT, len(embedded), sha(embedded) if embedded else "", "YES" if embedded == b else "NO"])
print("PATH_OFFSET", path_off, "MAGIC_OFFSETS", magic_offsets, "CHOSEN", chosen, "EMBED_SHA", sha(embedded) if embedded else "")
