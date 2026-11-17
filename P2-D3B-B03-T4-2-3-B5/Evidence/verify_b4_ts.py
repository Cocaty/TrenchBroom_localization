#!/usr/bin/env python3
# B5 reproducible B4 TS verification.
# Algorithm:
# 1) Read B4 backup and current formal TS as UTF-8 text with newline preservation.
# 2) Extract exact raw <message> ... </message> blocks using regex.
# 3) Compare a collections.Counter of raw blocks:
#      added = current - backup; missing = backup - current.
#    Raw-block multiset comparison handles duplicate Source/Context correctly.
# 4) Parse both files with ElementTree for field-level checks (Context/Source/Translation/type/numerusform/locations).
# 5) Write CSV evidence to the B5 report directory.
import csv, re, collections, hashlib
import xml.etree.ElementTree as ET

B = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN"
R = B + r"\reports\P2-D3B-B03-T4-2-3-B5"
BACKUP = B + r"\reports\P2-D3B-B03-T4-2-3-B4\Backup\TrenchBroom_zh_CN.ts.before"
CURRENT = B + r"\src\TrenchBroom\app\TrenchBroom\translations\TrenchBroom_zh_CN.ts"
T3_AUDIT = B + r"\reports\P2-D3B-B03-T3\T3_Completed_Translation_Audit.csv"

BLOCK_RE = re.compile(r'    <message>\n.*?    </message>\n', re.S)


def blocks(path):
    text = open(path, encoding="utf-8", newline="").read()
    return BLOCK_RE.findall(text), text


def messages(path):
    root = ET.parse(path).getroot()
    out = []
    for ctx_el in root.findall("context"):
        ctx = ctx_el.find("name").text
        for m in ctx_el.findall("message"):
            tr = m.find("translation")
            out.append({
                "ctx": ctx,
                "src": m.find("source").text or "",
                "tr": tr.text if tr is not None else None,
                "type": tr.get("type") if tr is not None else None,
                "xml": ET.tostring(m, encoding="unicode"),
            })
    return out


def index(ms):
    d = collections.defaultdict(list)
    for m in ms:
        d[(m["ctx"], m["src"])].append(m)
    return d


old_blocks, _ = blocks(BACKUP)
new_blocks, _ = blocks(CURRENT)
old_msgs, new_msgs = messages(BACKUP), messages(CURRENT)
co, cn = collections.Counter(old_blocks), collections.Counter(new_blocks)
added = {k: cn[k] - co.get(k, 0) for k in cn if cn[k] > co.get(k, 0)}
missing = {k: co[k] - cn.get(k, 0) for k in co if co[k] > cn.get(k, 0)}

# 562 independent verification by exact raw-block multiset.
with open(R + r"\B5_B4_562_Message_Independent_Verification.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Metric", "Value", "Algorithm_Note"])
    w.writerows([
        ["Backup_SHA256", hashlib.sha256(open(BACKUP, "rb").read()).hexdigest(), "input file"],
        ["Current_SHA256", hashlib.sha256(open(CURRENT, "rb").read()).hexdigest(), "input file"],
        ["Backup_Raw_Message_Blocks", len(old_blocks), "regex: 4-space <message> block"],
        ["Current_Raw_Message_Blocks", len(new_blocks), "same regex"],
        ["Added_Raw_Blocks", sum(added.values()), "Counter(current) - Counter(backup)"],
        ["Missing_Raw_Blocks", sum(missing.values()), "Counter(backup) - Counter(current)"],
        ["Result", "PASS" if len(old_blocks) == 562 and len(new_blocks) == 571 and sum(added.values()) == 9 and sum(missing.values()) == 0 else "FAIL", "raw-block multiset"],
    ])

oi, ni = index(old_msgs), index(new_msgs)

# Nine B4 new menu messages.
targets = [("File", "文件"), ("Edit", "编辑"), ("Selection", "选择"), ("Groups", "分组"),
           ("Tools", "工具"), ("View", "视图"), ("Run", "运行"), ("Debug", "调试"), ("Help", "帮助")]
rows = []
for src, tr in targets:
    hits = ni.get(("QObject", src), [])
    m = hits[0] if len(hits) == 1 else None
    ok = bool(m and m["tr"] == tr and m["type"] is None and len(hits) == 1)
    rows.append(["QObject", src, tr, m["tr"] if m else "MISSING", m["type"] or "finished" if m else "MISSING", len(hits), "PASS" if ok else "FAIL"])
with open(R + r"\B5_New_9_Menu_Verification.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Context", "Source", "Frozen_Translation", "Actual_Translation", "Status", "Hit_Count", "Result"])
    w.writerows(rows)

# Existing 39 frozen translations from T3 audit.
frozen = list(csv.DictReader(open(T3_AUDIT, encoding="utf-8-sig")))
rows = []
for x in frozen:
    key = (x["Context"], x["Source"])
    m = ni.get(key, [None])[0]
    ok = bool(m and m["tr"] == x["Expected_Translation"] and m["type"] in (None, "finished"))
    rows.append([x["Batch"], x["Target_ID"], x["Context"], x["Source"], x["Expected_Translation"], m["tr"] if m else "MISSING", m["type"] or "finished" if m else "MISSING", "PASS" if ok else "FAIL"])
with open(R + r"\B5_Existing_39_Frozen_Translation_Verification.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Batch", "Target_ID", "Context", "Source", "Frozen_Translation", "Actual_Translation", "Status", "Result"])
    w.writerows(rows)

# AppController/Open Map specialized protection.
key = ("tb::ui::AppController", "Open Map")
b, n = oi.get(key, [None])[0], ni.get(key, [None])[0]
ok = bool(b and n and b["xml"] == n["xml"] and n["tr"] in (None, "") and n["type"] == "unfinished")
with open(R + r"\B5_AppController_Open_Map_Protection.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Context", "Source", "Backup_Translation", "Current_Translation", "Backup_Status", "Current_Status", "Raw_XML_Identical", "Result"])
    w.writerow([key[0], key[1], repr(b["tr"]) if b else "MISSING", repr(n["tr"]) if n else "MISSING", b["type"] if b else "", n["type"] if n else "", bool(b and n and b["xml"] == n["xml"]), "PASS" if ok else "FAIL"])
