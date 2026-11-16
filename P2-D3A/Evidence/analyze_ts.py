# P2-D3A 只读分析脚本：解析 TS → 消息索引/分类/风险/批次（不修改 TS/源码）
import xml.etree.ElementTree as ET, csv, json, os, re, hashlib, collections
BASE = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\src\TrenchBroom"
TS_DIR = os.path.join(BASE, r"app\TrenchBroom\translations")
TS = os.path.join(TS_DIR, "TrenchBroom_zh_CN.ts")
OUT = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A\Evidence"
root = ET.parse(TS).getroot()

# ---------- 分类规则（基于 context / 源文件 / source 关键词；UNKNOWN 保守标记） ----------
CAT_RULES = [
    ("Preferences 和设置页面", ["preference", "gamespreference", "viewpreference", "mousepreference", "keyboardpreference", "filter", "compilationprofile", "qpreferencestoredelegate", "updat.*setting"]),
    ("游戏配置与资源管理", ["game", "updatelib", "upd::", "package", "resource", "model"]),
    ("Entity 与属性编辑", ["entity", "flagseditor", "property", "spawn", "classname"]),
    ("Texture 与材质管理", ["material", "texture", "uv", "faceattribs"]),
    ("Brush、Face 和几何编辑", ["brush", "face", "vertex", "edge", "clip", "carve", "geometry", "sweep", "scale", "rotate", "drawshape"]),
    ("2D 视图与地图编辑操作", ["mapview", "mapwindow", "mapdocument", "mapeditor", "toolbox", "grid", "camera", "selection", "snap", "tool"]),
    ("3D 视图与摄像机操作", ["renderer", "view3d", "camera"]),
    ("文件操作与项目管理", ["file", "document", "map", "save", "load", "export", "import", "recent", "prefab"]),
    ("对话框和确认提示", ["dialog", "messagebox", "wizard", "prompt"]),
    ("错误信息和警告", ["error", "warning", "fail", "exception", "invalid", "could not", "cannot"]),
    ("主菜单和主窗口", ["actionmanager", "actionbuilder", "mainwindow", "menu", "welcome"]),
    ("工具栏和快捷操作", ["toolbar", "shortcut", "action"]),
    ("工具提示与状态信息", ["tooltip", "status", "info", "console", "issuebrowser", "collapsible"]),
    ("2D 视图与地图编辑操作", ["layereditor", "layerlistbox", "layer"]),
    ("文件操作与项目管理", ["compilation", "launch_engine", "compile"]),
]
def classify(ctx, src, path):
    hay = (ctx + " " + os.path.basename(path) + " " + os.path.dirname(path)).lower()
    s = src.lower()
    for cat, pats in CAT_RULES:
        for p in pats:
            if re.search(p, hay) or (cat in ("错误信息和警告", "对话框和确认提示") and re.search(p, s)):
                return cat, "context/source 关键词:" + p
    # 仅按 source 关键词兜底
    if re.search(r"^(save|open|new|close|export|import|revert|reload|quit|exit)", s): return "文件操作与项目管理", "source 动词"
    if re.search(r"(cancel|ok|yes|no|apply|reset|remove|delete|add|rename|browse|\.\.\.)", s): return "对话框和确认提示", "通用按钮词"
    return "UNKNOWN", "context/source/路径均无可靠功能线索"

# ---------- 占位符/快捷键/技术标识 ----------
PH = re.compile(r"%(?:[1-9]|\*|n|L1|s|\.)")
MNEM = re.compile(r"(?<![&])&(?![&])[A-Za-z]")
ESC_AMP = re.compile(r"&&")
KEYS = re.compile(r"\b(?:Ctrl|Shift|Alt)\s*\+\s*\w+|\b(?:Enter|Escape|Esc|Tab|Space|Backspace|Delete|Home|End|PageUp|PageDown|F[1-9])\b", re.I)
TECH = re.compile(r"(?:\.[\w]{2,5}\b|[A-Za-z]:\\[^\s\"']+|io\.github\.[\w.]+|Editor/|render/|Map view/|Q[A-Z][A-Za-z]+|\bQT_|\bQ[A-Z])")
AMBIG = ["face","brush","entity","group","world","layer","texture","material","apply","select","scale","snap","map","grid","plane","clip","carve","model","property","class","surface","projection","mapping","alignment","duplicate","package","primitive","vertex","edge","polygon","geometry","spawn","pref","view","tool","update"]
def flags(src):
    return {
        "placeholders": ",".join(sorted(set(PH.findall(src)))),
        "has_mnemonic": bool(MNEM.search(src)),
        "has_escaped_amp": bool(ESC_AMP.search(src)),
        "has_key_hint": bool(KEYS.search(src)),
        "has_technical": bool(TECH.search(src)),
        "ambiguous_terms": ",".join(sorted({w for w in AMBIG if re.search(r"\b"+re.escape(w)+r"\b", src, re.I)})),
        "source_len": len(src),
    }

# ---------- 源码上下文提取 ----------
line_cache = {}
def file_lines(path):
    if path not in line_cache:
        try: line_cache[path] = open(path, encoding="utf-8", errors="ignore").readlines()
        except Exception: line_cache[path] = []
    return line_cache[path]
def context_of(path, line):
    ls = file_lines(path)
    if not ls or not (1 <= line <= len(ls)):
        return "", "", "FILE_NOT_FOUND", ""
    snippet = " ".join(x.strip() for x in ls[max(0,line-2):min(len(ls),line+1)])
    fn = cls = ""
    for i in range(min(line, len(ls))-1, max(-1, min(line, len(ls))-121), -1):
        t = ls[i].strip()
        if not fn:
            m = re.match(r"^\s*(?:const\s+)?[A-Za-z_][\w:<>,\s\*&]*?\s+(\w+)::(\w+)\s*\(", t)
            if m: fn = m.group(1)+"::"+m.group(2)
        if not cls:
            m = re.match(r"class\s+(\w+)\s*(?::|\{)", t)
            if m: cls = m.group(1)
        if fn and cls: break
    usage = "tr() 调用"
    for pat, lab in [
        (r"addAction|QAction", "菜单/QAction"), (r"setToolTip|toolTip", "工具提示"),
        (r"setPlaceholderText", "占位提示文本"), (r"QMessageBox|critical\(|information\(|warning\(", "消息框"),
        (r"setWindowTitle|setTitle", "窗口/分组标题"), (r"addRow|QLabel|setText|setInfoStyle", "标签/信息文本"),
        (r"setCurrentText|addItem", "下拉项"), (r"setStatusTip|statusBar", "状态提示"),
        (r"notify|error|warn", "错误/通知"),
    ]:
        if re.search(pat, snippet, re.I): usage = lab; break
    return cls, fn, "OK", snippet[:220]

# ---------- 解析全部消息 ----------
msgs = []
for ctxn in root.findall("context"):
    cname = ctxn.find("name").text if ctxn.find("name") is not None else ""
    for m in ctxn.findall("message"):
        se = m.find("source"); te = m.find("translation")
        src = (se.text or "") if se is not None else ""
        trn = (te.text or "") if te is not None else ""
        ttype = te.get("type", "") if te is not None else ""
        locs = [(l.get("filename",""), int(l.get("line","0") or 0)) for l in m.findall("location")]
        mid = hashlib.sha256((cname+"\x1f"+src).encode("utf-8")).hexdigest()[:12]
        fl = flags(src)
        f, ln = (locs[0] if locs else ("",0))
        full = os.path.normpath(os.path.join(TS_DIR, f)) if f else ""
        cls, fn, status, snippet = context_of(full, ln) if full else ("", "", "NO_LOCATION", "")
        cat, why = classify(cname, src, f)
        msgs.append(dict(id=mid, context=cname, source=src, translation=trn, type=ttype or "finished",
                         numerus=m.get("numerus",""), locations=locs, location_count=len(locs),
                         finished=(ttype != "unfinished"), file=f, line=ln, cls=cls, function=fn,
                         source_status=status, snippet=snippet, category=cat, category_reason=why, **fl))

# ---------- 统计输出 ----------
stats = dict(
    contexts=len(root.findall("context")), messages=len(msgs),
    finished=sum(1 for m in msgs if m["finished"]), unfinished=sum(1 for m in msgs if not m["finished"]),
    obsolete=sum(1 for m in msgs if m["type"] in ("obsolete","vanished")),
    vanished=sum(1 for m in msgs if m["type"]=="vanished"),
    multi_location=sum(1 for m in msgs if m["location_count"]>1),
    no_location=sum(1 for m in msgs if m["location_count"]==0),
    duplicate_ctx_src=sum(v-1 for v in collections.Counter((m["context"],m["source"]) for m in msgs).values() if v>1),
    empty_source=sum(1 for m in msgs if not m["source"].strip()),
    empty_translation=sum(1 for m in msgs if not m["translation"].strip()),
    numerus=sum(1 for m in msgs if m["numerus"]),
    placeholder=sum(1 for m in msgs if m["placeholders"]),
    mnemonic=sum(1 for m in msgs if m["has_mnemonic"]),
    escaped_amp=sum(1 for m in msgs if m["has_escaped_amp"]),
    key_hint=sum(1 for m in msgs if m["has_key_hint"]),
    technical=sum(1 for m in msgs if m["has_technical"]),
    ambiguous=sum(1 for m in msgs if m["ambiguous_terms"]),
    context_mapped=sum(1 for m in msgs if m["cls"] or m["function"]),
    source_ok=sum(1 for m in msgs if m["source_status"]=="OK"),
    unknown_category=sum(1 for m in msgs if m["category"]=="UNKNOWN"),
)
print(json.dumps(stats, ensure_ascii=False, indent=2))
print("分类分布:", json.dumps(dict(collections.Counter(m["category"] for m in msgs)), ensure_ascii=False))

# ---------- 输出 CSV/JSON ----------
cols = ["id","context","source","translation","type","numerus","location_count","locations","finished",
        "placeholders","has_mnemonic","has_escaped_amp","has_key_hint","has_technical","ambiguous_terms","source_len",
        "file","line","cls","function","source_status","snippet","category","category_reason"]
with open(os.path.join(OUT,"P2D3A_Message_Index.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for m in msgs:
        r=dict(m); r["locations"]="; ".join(f"{a}:{b}" for a,b in m["locations"])
        w.writerow(r)
with open(os.path.join(OUT,"P2D3A_Message_Index.json"),"w",encoding="utf-8") as f:
    json.dump(dict(stats=stats, messages=msgs), f, ensure_ascii=False, indent=1)
with open(os.path.join(OUT,"P2D3A_Context_Stats.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["context","message_count","finished","unfinished","categories"])
    agg=collections.defaultdict(lambda:[0,0,0,collections.Counter()])
    for m in msgs:
        a=agg[m["context"]]; a[0]+=1; a[1]+=m["finished"]; a[2]+=(not m["finished"]); a[3][m["category"]]+=1
    for c,a in sorted(agg.items(), key=lambda x:-x[1][0]):
        w.writerow([c,a[0],a[1],a[2],"; ".join(f"{k}:{v}" for k,v in a[3].most_common())])

# ---------- 分批：按分类分组，每批 30-50 条，未完成优先，消息不重叠 ----------
batches = []
pool = [m for m in msgs if not m["finished"]]
bycat = collections.defaultdict(list)
for m in pool: bycat[m["category"]].append(m["id"])
order = ["主菜单和主窗口","文件操作与项目管理","Preferences 和设置页面","2D 视图与地图编辑操作","3D 视图与摄像机操作",
         "Brush、Face 和几何编辑","Entity 与属性编辑","Texture 与材质管理","工具栏和快捷操作","对话框和确认提示",
         "工具提示与状态信息","错误信息和警告","游戏配置与资源管理","UNKNOWN","其他或待确认"]
idx=0
for cat in order:
    ids = bycat.get(cat, [])
    for st in range(0, len(ids), 45):
        idx+=1
        chunk = ids[st:st+45]
        batches.append(dict(batch=f"B{idx:02d}", category=cat, count=len(chunk), ids=",".join(chunk)))
with open(os.path.join(OUT,"P2D3A_Batches.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f, fieldnames=["batch","category","count","ids"]); w.writeheader(); w.writerows(batches)
print("批次:", [(b["batch"],b["category"],b["count"]) for b in batches])
