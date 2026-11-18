#!/usr/bin/env python3
# A0 read-only environment-variable audit. Never prints or stores raw proxy values.
import csv, hashlib, os, re

R = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3B-B03-T4-2-3-B6-D2-A0"
FOCUS = ["HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy", "NO_PROXY", "no_proxy", "PATH"]

env = dict(os.environ)
# Build case-insensitive duplicate groups across all visible env vars.
groups = {}
for name in sorted(env):
    groups.setdefault(name.lower(), []).append(name)

rows = []
for name in sorted(env):
    norm = name.lower()
    peers = groups[norm]
    value = env[name]
    h = hashlib.sha256(value.encode("utf-8", "replace")).hexdigest()
    equality = "ONLY_ONE_NAME"
    if len(peers) > 1:
        vals = {hashlib.sha256(env[p].encode("utf-8", "replace")).hexdigest() for p in peers}
        equality = "SAME_VALUE" if len(vals) == 1 else "DIFFERENT_VALUES"
    rows.append([name, norm, norm if len(peers) > 1 else "", "YES", len(value), h, equality, "FOCUS" if norm in [x.lower() for x in FOCUS] else "OTHER"])

with open(R + r"\A0_Environment_Variable_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Variable_Name", "Normalized_Name", "Duplicate_Group", "Value_Present", "Value_Length", "Value_Hash", "Value_Equality", "Scope"])
    w.writerows(rows)

# PATH audit: keep raw PATH in memory only; output counts and hashes, never full value or personal paths.
raw = env.get("PATH", "")
segments = raw.split(";")
norm_seen = {}
dupes = []
for i, seg in enumerate(segments):
    key = re.sub(r"\\+", "/", seg.strip()).lower()
    if key in norm_seen:
        dupes.append([i, norm_seen[key], "DUPLICATE_PATH_HASH", hashlib.sha256(seg.encode("utf-8", "replace")).hexdigest()])
    else:
        norm_seen[key] = i
empty = [i for i, s in enumerate(segments) if not s.strip()]
path_rows = [
    ["PATH_length", len(raw), "INTEGER"],
    ["PATH_segment_count", len(segments), "INTEGER"],
    ["PATH_raw_sha256", hashlib.sha256(raw.encode("utf-8", "replace")).hexdigest(), "HASH_ONLY"],
    ["PATH_empty_segments", ";".join(str(i) for i in empty) or "NONE", "INDICES_ONLY"],
    ["PATH_duplicate_segments", str(len(dupes)), "COUNT_ONLY"],
    ["PATH_case_insensitive_normalization", "APPLIED", "METHOD"],
    ["D0-1_PATH_0_C_explanation", "Likely caused by splitting Windows PATH on POSIX ':' instead of ';'; A0 uses ';'.", "EXPLANATION"],
]
for row in dupes:
    path_rows.append(["PATH_duplicate_segment", f"index {row[0]} == index {row[1]}", row[2]])
with open(R + r"\A0_Path_Audit.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Metric", "Value", "Type"]); w.writerows(path_rows)

print("ENV_VARS", len(rows), "DUP_GROUPS", sum(1 for g in groups.values() if len(g) > 1), "PATH_SEGMENTS", len(segments))
for n in ["https_proxy", "http_proxy", "all_proxy", "no_proxy"]:
    peers = groups.get(n, [])
    if len(peers) > 1:
        vals = {hashlib.sha256(env[p].encode("utf-8", "replace")).hexdigest() for p in peers}
        print("DUP", ",".join(peers), "SAME" if len(vals) == 1 else "DIFFERENT")
