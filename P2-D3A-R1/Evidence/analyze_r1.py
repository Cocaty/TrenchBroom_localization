# P2-D3A-R1 修正分析脚本（只读）
# 修正：① ActionManager/ActionBuilder 按函数名/动作路径/ActionContext 精细分类
#       ② 全部 location 逐项核验（非仅 locs[0]）
#       ③ 占位符 %1-%99/%L1-%L99/%n/%% 精确识别；快捷键 F10-F12 等
#       ④ 术语精确匹配计数；⑤ 批次重排（<=45，559 条唯一归属）
import xml.etree.ElementTree as ET, csv, json, os, re, hashlib, collections
BASE = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\src\TrenchBroom"
TS_DIR = os.path.join(BASE, r"app\TrenchBroom\translations")
TS = os.path.join(TS_DIR, "TrenchBroom_zh_CN.ts")
OUT = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A-R1\Evidence"
AM = os.path.join(BASE, r"lib\TbUiLib\src\ActionManager.cpp")
AB = os.path.join(BASE, r"lib\TbUiLib\src\ActionBuilder.cpp")
root = ET.parse(TS).getroot()

def sha_id(ctx, src):
    return hashlib.sha256((ctx+"\x1f"+src).encode("utf-8")).hexdigest()[:12]

# ---------- ActionManager 函数区间 ----------
am_lines = open(AM, encoding="utf-8", errors="ignore").readlines()
func_starts = []
for i, line in enumerate(am_lines):
    m = re.search(r"ActionManager::(\w+)\s*\(", line)
    if m:
        func_starts.append((i+1, m.group(1)))
    elif re.search(r"ActionManager::\s*$", line):
        m2 = re.match(r"\s*(\w+)\s*\(", am_lines[i+1]) if i+1 < len(am_lines) else None
        if m2: func_starts.append((i+2, m2.group(1)))
func_starts.sort()
def am_function(line):
    best = ""
    for start, name in func_starts:
        if start <= line: best = name
        else: break
    return best

# ---------- 分类 ----------
CAT_BASE = [
    ("Preferences 和设置页面", ["preference","gamespreference","viewpreference","mousepreference","keyboardpreference","qpreferencestoredelegate","compilationprofile"]),
    ("游戏配置与资源管理", ["updatelib","upd::","game preference","package"]),
    ("Entity 与属性编辑", ["entity","flagseditor","classname","spawn"]),
    ("Texture 与材质管理", ["material","texture","uv","faceattribs"]),
    ("Brush、Face 和几何编辑", ["brush","face","vertex","edge","geometry","sweep","clip","carve"]),
    ("错误信息和警告", ["error","warning","fail","exception","could not","cannot"]),
    ("对话框和确认提示", ["dialog","messagebox","wizard","prompt"]),
    ("文件操作与项目管理", ["file","document","save","load","export","import","recent","prefab"]),
    ("工具提示与状态信息", ["tooltip","status","console","issuebrowser"]),
    ("2D 视图与地图编辑操作", ["mapview","mapwindow","vieweditor","layereditor","selection","grid","toolbox","collapsible","swap"]),
    ("3D 视图与摄像机操作", ["renderer","camera","view3d"]),
    ("工具快捷操作", ["toolpage","toolbox","shortcut","tool "]),
    ("主菜单和主窗口", ["welcome","mainwindow","menu"]),
]
def classify(m, fpath, func, path_hint, ctx_flags):
    ctx, src = m["context"], m["source"]
    s = src.lower(); hay = (ctx+" "+os.path.basename(fpath)).lower()
    evid = []
    # 动态 tag/entity 动作
    if func in ("createTagActions","createEntityDefinitionActions"):
        return "Entity 与属性编辑", f"ActionManager::{func}（动态 tag/entity 动作）"
    if func == "createFileMenu": return "文件操作与项目管理", "ActionManager::createFileMenu 菜单路径"
    if func == "createRunMenu": return "游戏配置与资源管理", "ActionManager::createRunMenu（编译/运行）"
    if func == "createToolbar": return "工具栏和快捷操作", "ActionManager::createToolbar"
    if func == "createEditMenu": return "2D 视图与地图编辑操作", "ActionManager::createEditMenu（撤销/复制/粘贴等编辑操作）"
    if func == "createDebugMenu": return "其他或待确认", "ActionManager::createDebugMenu（开发者调试动作，非普通用户翻译批次）"
    if func == "createToolsMenu": return "工具快捷操作", "ActionManager::createToolsMenu"
    if func == "createSelectionMenu": return "2D 视图与地图编辑操作", "ActionManager::createSelectionMenu"
    if func == "createGroupsMenu": return "2D 视图与地图编辑操作", "ActionManager::createGroupsMenu（编组/图层）"
    if func in ("createDebugMenu","createHelpMenu","createMainMenu"): return "主菜单和主窗口", f"ActionManager::{func}"
    if func == "createViewMenu":
        if re.search(r"3d|camera|renderer", path_hint+" "+s): return "3D 视图与摄像机操作", "createViewMenu + 3D/摄像机线索"
        return "2D 视图与地图编辑操作", "ActionManager::createViewMenu"
    if func == "createViewActions":
        p = path_hint.lower(); cf = ctx_flags.lower(); evid.append(f"路径={path_hint or '无'}; ActionContext={ctx_flags or '无'}")
        if "texture" in p or "material" in p or "uv" in p: return "Texture 与材质管理", "路径:"+"; ".join(evid)
        if "entity" in p or "tag" in p: return "Entity 与属性编辑", "路径:"+"; ".join(evid)
        if re.search(r"brush|clip|face|vertex|edge|geometry|carve", p): return "Brush、Face 和几何编辑", "路径:"+"; ".join(evid)
        if "3d" in p or "view3d" in cf: return "3D 视图与摄像机操作", "ActionContext::View3D:"+"; ".join(evid)
        if "tool" in cf or "tool" in p: return "工具快捷操作", "工具相关:"+"; ".join(evid)
        if "anyview" in cf or "map view" in p: return "2D 视图与地图编辑操作", "路径/上下文:"+"; ".join(evid)
        if re.search(r"entity|point entity", s): return "Entity 与属性编辑", "source 实体线索:"+"; ".join(evid)
        if re.search(r"texture|material|uv", s): return "Texture 与材质管理", "source 材质线索:"+"; ".join(evid)
        if re.search(r"brush|face|vertex|clip|geometry", s): return "Brush、Face 和几何编辑", "source 几何线索:"+"; ".join(evid)
        if re.search(r"move|select|duplicate|grid|snap", s): return "2D 视图与地图编辑操作", "source 编辑动作:"+"; ".join(evid)
        return "UNKNOWN", "createViewActions 中路径与上下文均不足以判定"
    if os.path.basename(fpath) == "ActionBuilder.cpp":
        return "工具快捷操作", "ActionBuilder 生成快捷键显示文本"
    if os.path.basename(fpath) == "ActionManager.cpp":
        return "UNKNOWN", "ActionManager 中未命中已知 create* 函数/路径线索"
    for cat, pats in CAT_BASE:
        for pat in pats:
            if re.search(pat, hay) or (cat in ("错误信息和警告","对话框和确认提示") and re.search(pat, s)):
                return cat, "context/文件关键词:"+pat
    if re.search(r"^(save|open|new|close|export|import|revert|reload|quit|exit)", s): return "文件操作与项目管理", "source 动词"
    if re.search(r"(cancel|ok|yes|no|apply|reset|remove|delete|add|rename|browse|\.\.\.)", s): return "对话框和确认提示", "通用按钮词"
    return "UNKNOWN", "context/source/路径无可靠线索"

# ---------- 风险正则 ----------
PH = re.compile(r"%%|%L[1-9]\d*|%[1-9]\d*|%n")
MNEM = re.compile(r"(?<![&])&(?![&])[A-Za-z]")
AMP2 = re.compile(r"&&")
# 只把明确的组合键/F键视为真实按键标识；独立 Enter/Delete 等词多为普通动词，交人工复核
KEY = re.compile(r"\b(?:Ctrl|Shift|Alt)\s*\+\s*(?:[A-Za-z]\w*|F(?:[1-9]|1[0-2]))\b|\bF(?:[1-9]|1[0-2])\b", re.I)
TECH = re.compile(r"(?:\.[A-Za-z0-9]{2,5}\b|https?://|[A-Za-z]:\\[^\s\"']+|io\.github\.[\w.]+|Editor/|render/|Map view/|\bQ[A-Z][A-Za-z]+|<br\s*/?>|\(\*\.\w+\))")
AMBIG = ["face","brush","entity","group","world","layer","texture","material","apply","select","scale","snap","map","grid","plane","clip","carve","model","property","class","surface","projection","mapping","alignment","duplicate","package","primitive","vertex","edge","polygon","geometry","spawn","pref","view","tool","update"]
def flags(src):
    return dict(placeholders=",".join(sorted(set(PH.findall(src)))),
                has_mnemonic=bool(MNEM.search(src)), has_escaped_amp=bool(AMP2.search(src)),
                has_key_hint=bool(KEY.search(src)), has_technical=bool(TECH.search(src)),
                ambiguous_terms=",".join(sorted({w for w in AMBIG if re.search(r"\b"+re.escape(w)+r"\b",src,re.I)})),
                source_len=len(src))

# ---------- 解析消息 + 全部 location ----------
msgs, loc_rows = [], []
by_file_cache = {}
def lines_of(p):
    if p not in by_file_cache:
        try: by_file_cache[p] = open(p,encoding="utf-8",errors="ignore").readlines()
        except Exception: by_file_cache[p] = []
    return by_file_cache[p]
for ctxn in root.findall("context"):
    cname = ctxn.find("name").text if ctxn.find("name") is not None else ""
    for m in ctxn.findall("message"):
        se=m.find("source"); te=m.find("translation")
        src=(se.text or "") if se is not None else ""
        trn=(te.text or "") if te is not None else ""
        ttype=te.get("type","") if te is not None else ""
        locs=[(l.get("filename",""), int(l.get("line","0") or 0)) for l in m.findall("location")]
        mid=sha_id(cname,src); fl=flags(src)
        first_cls=first_fn=""; first_usage=""
        for idx,(f,ln) in enumerate(locs):
            full=os.path.normpath(os.path.join(TS_DIR,f)) if f else ""
            exists=os.path.exists(full)
            lines=lines_of(full) if exists else []
            valid=exists and 1<=ln<=len(lines)
            snippet=" ".join(x.strip() for x in lines[max(0,ln-2):min(len(lines),ln+1)]) if valid else ""
            fn=am_function(ln) if os.path.basename(full)=="ActionManager.cpp" and valid else ""
            path_hint=""; ctx_flags=""
            if fn and valid:
                for j in range(max(0,ln-25),min(len(lines),ln+2)):
                    mm=re.search(r'path\{"([^"]+)"\}',lines[j])
                    if mm: path_hint=mm.group(1)
                    mm2=re.search(r'ActionContext::([A-Za-z0-9_| ]+)',lines[j])
                    if mm2: ctx_flags=mm2.group(1).strip()
            usage="tr() 调用"
            for pat,lab in [(r"addAction|QAction","菜单/QAction"),(r"setToolTip|toolTip","工具提示"),(r"setPlaceholderText","占位提示"),(r"QMessageBox|critical\(|information\(|warning\(","消息框"),(r"setWindowTitle|setTitle","标题"),(r"addRow|QLabel|setText|setInfoStyle","标签/说明"),(r"addItem|setCurrentText","下拉项"),(r"setStatusTip|statusBar","状态提示")]:
                if re.search(pat,snippet,re.I): usage=lab; break
            cat,why = classify(dict(context=cname,source=src), f, fn, path_hint, ctx_flags) if idx==0 else ("","")
            if idx==0: first_cls,first_fn,first_usage = fn, path_hint, usage
            loc_rows.append([mid,cname,src[:80],len(locs),idx+1,f,ln,"YES" if exists else "NO","YES" if valid else "NO",fn,path_hint,ctx_flags,usage,snippet[:200],cat,why])
        cat,why = classify(dict(context=cname,source=src), locs[0][0] if locs else "", first_cls, first_fn, "")
        msgs.append(dict(id=mid,context=cname,source=src,translation=trn,type=ttype or "finished",
                         numerus=m.get("numerus",""),locations=locs,location_count=len(locs),
                         finished=(ttype!="unfinished"),**fl,category=cat,category_reason=why,
                         am_function=first_cls,action_path=first_fn))

# ---------- 输出 ----------
cols=["id","context","source","translation","type","numerus","location_count","locations","finished",
      "placeholders","has_mnemonic","has_escaped_amp","has_key_hint","has_technical","ambiguous_terms","source_len",
      "category","category_reason","am_function","action_path"]
with open(os.path.join(OUT,"P2D3A_R1_Message_Index.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction="ignore"); w.writeheader()
    for m in msgs:
        r=dict(m); r["locations"]="; ".join(f"{a}:{b}" for a,b in m["locations"]); w.writerow(r)
with open(os.path.join(OUT,"P2D3A_R1_All_Locations.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["message_id","context","source","location_total","location_index","file","line","file_exists","line_valid","action_function","action_path","action_context","usage_hint","snippet","primary_category","category_reason"])
    w.writerows(loc_rows)
# 术语表：精确匹配复核
gloss=list(csv.DictReader(open(r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A\Evidence\P2D3A_Glossary.csv",encoding="utf-8-sig")))
srcs=[m["source"] for m in msgs]
with open(os.path.join(OUT,"P2D3A_R1_Glossary.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["English","Chinese_candidate","Alternative","Context","Evidence","Confidence","Review_status","TS_exact_matches","In_current_batch"])
    for g in gloss:
        pat=re.compile(r"\b"+re.escape(g["English"])+r"\b",re.I)
        n=sum(1 for s in srcs if pat.search(s))
        w.writerow([g["English"],g["Chinese_candidate"],g["Alternative"],g["Context"],g["Evidence"],
                    g["Confidence"] if n else "低",g["Review_status"],n,"否（无精确匹配，预备）" if n==0 else "待批次分配"])
# 批次：按分类分块 <=45，不沿用旧编号
order=["文件操作与项目管理","主菜单和主窗口","对话框和确认提示","工具提示与状态信息","Preferences 和设置页面",
       "2D 视图与地图编辑操作","3D 视图与摄像机操作","工具快捷操作","Brush、Face 和几何编辑",
       "Entity 与属性编辑","Texture 与材质管理","游戏配置与资源管理","错误信息和警告","其他或待确认","UNKNOWN"]
pool=[m for m in msgs if not m["finished"]]
batches=[]; k=0
for cat in order:
    ids=[m["id"] for m in pool if m["category"]==cat]
    for st in range(0,len(ids),45):
        k+=1; batches.append([f"R1-B{k:02d}",cat,len(ids[st:st+45]),",".join(ids[st:st+45])])
with open(os.path.join(OUT,"P2D3A_R1_Batches.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["batch","category","count","ids"]); w.writerows(batches)
# 无法可靠识别的样本（人工复核）
unc=[]
for m in msgs:
    s=m["source"]; reasons=[]
    if re.search(r"%[^1-9nL%]", s): reasons.append("可疑 % 序列")
    if "&" in s and not m["has_mnemonic"] and not m["has_escaped_amp"]: reasons.append("& 符号")
    if re.search(r"\b(?:Left|Right|Up|Down|Home|End|Enter|Esc|Delete|Tab|Space)\b", s, re.I) and not m["has_key_hint"]:
        reasons.append("方向/按键词（普通文字还是按键？）")
    if re.search(r"\b[A-Z][a-z]+\+[A-Za-z]", s) and not m["has_key_hint"]: reasons.append("疑似快捷键未识别")
    if reasons: unc.append([m["id"],m["context"],s[:120],"; ".join(reasons),m["category"]])
with open(os.path.join(OUT,"P2D3A_R1_Uncertain_Samples.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["id","context","source","reason","category"]); w.writerows(unc)
# 统计
stats=dict(messages=len(msgs),contexts=len(root.findall("context")),
           finished=sum(m["finished"] for m in msgs),unfinished=sum(not m["finished"] for m in msgs),
           locations=len(loc_rows), files_exist=sum(r[7]=="YES" for r in loc_rows), lines_valid=sum(r[8]=="YES" for r in loc_rows),
           multi=sum(m["location_count"]>1 for m in msgs),
           placeholder=sum(bool(m["placeholders"]) for m in msgs),
           key_hint=sum(m["has_key_hint"] for m in msgs), mnemonic=sum(m["has_mnemonic"] for m in msgs),
           tech=sum(m["has_technical"] for m in msgs),
           glossary_no_match=sum(1 for g in gloss if not re.search(r"\b"+re.escape(g["English"])+r"\b"," ".join(srcs),re.I)),
           batches=len(batches), batch_total=sum(b[2] for b in batches))
print(json.dumps(stats,ensure_ascii=False,indent=2))
print("分类:", json.dumps(dict(collections.Counter(m["category"] for m in msgs)),ensure_ascii=False))
print("批次:", [(b[0],b[1],b[2]) for b in batches][:8], "... 共", len(batches))
print("B01 前 8 source:", [next(m["source"] for m in msgs if m["id"]==i)[:45] for i in batches[0][3].split(",")[:8]])
