# P2-D3A-R1-A：动作注册语句级解析 + 562 消息重分类 + B01 放行审计（只读）
import xml.etree.ElementTree as ET, csv, json, os, re, hashlib, collections
BASE=r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\src\TrenchBroom"
TS_DIR=os.path.join(BASE,r"app\TrenchBroom\translations")
TS=os.path.join(TS_DIR,"TrenchBroom_zh_CN.ts")
AM=os.path.join(BASE,r"lib\TbUiLib\src\ActionManager.cpp")
OUT=r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A-R1-A\Evidence"
R1=r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A-R1\Evidence"
src_am=open(AM,encoding="utf-8",errors="ignore").read()
nl_start=[0]
for i,c in enumerate(src_am):
    if c=="\n": nl_start.append(i+1)
def lineno(pos): return bisect_right(nl_start,pos) if False else __import__("bisect").bisect_right(nl_start,pos)

# ---- 函数区间（含跨行签名）----
func_starts=[]
for m in re.finditer(r"ActionManager::\s*(?:\n\s*)?(\w+)\s*\(", src_am):
    func_starts.append((lineno(m.start()),m.group(1)))
def am_func(L):
    best=""
    for s,n in func_starts:
        if s<=L: best=n
        else: break
    return best

# ---- addAction(Action{...}) 语句：按花括号配对 ----
stmts=[]
for m in re.finditer(r"addAction\s*\(\s*Action\s*\{", src_am):
    brace=src_am.index("{",m.start()); depth=0; end=None; instr=False; esc=False
    for i in range(brace,len(src_am)):
        c=src_am[i]
        if instr:
            if esc: esc=False
            elif c=="\\": esc=True
            elif c=='"': instr=False
            continue
        if c=='"': instr=True; continue
        if c=="{": depth+=1
        elif c=="}":
            depth-=1
            if depth==0: end=i+1; break
    if not end: continue
    stmt=src_am[brace:end]
    p=re.search(r'(?:std::filesystem::path\s*\{\s*)?"([^"]+)"\s*\}?\s*,', stmt)
    path=p.group(1) if p else ""
    ctxs=re.findall(r"ActionContext::([A-Za-z_]\w*)", stmt)
    trs=[]
    for t in re.finditer(r'QObject::tr\(\s*"((?:[^"\\]|\\.)*)"', stmt):
        s=t.group(1).replace('\\"','"').replace('\\n','\n')
        trs.append((lineno(brace+t.start()),s))
    hs=re.search(r"\[\]\s*\(\s*auto\s*&\s*context\s*\)\s*\{([\s\S]{0,600}?)\}\s*,", stmt)
    handler=hs.group(1).strip()[:260] if hs else ""
    calls=re.findall(r"context\.([A-Za-z]+)\(\)\.([A-Za-z0-9_]+)\(\)", handler)
    stmts.append(dict(start=lineno(m.start()),end=lineno(end),path=path,ctxs=ctxs,trs=trs,handler=handler,calls=calls,stmt=stmt[:900]))

def stmt_for(L):
    hits=[s for s in stmts if any(tl==L for tl,_ in s["trs"])]
    if hits: return hits[0]
    hits=[s for s in stmts if s["start"]<=L<=s["end"]]
    return hits[0] if hits else None

# ---- 分类 ----
def classify(m, st, fn):
    src=m["source"]; s=src.lower(); reason=[]
    if st:
        path=st["path"]; ctxs=" ".join(st["ctxs"]); calls=" ".join(a+"::"+b for a,b in st["calls"]).lower()
        h=st["handler"].lower(); reason.append(f'path={path or "缺失"}')
        reason.append(f"context={','.join(st['ctxs']) or '缺失'}")
        reason.append(f"handler={calls or '未识别'}")
        low=path.lower()
        if low.startswith("menu/file/"): return "文件操作与项目管理", " | ".join(reason)
        if low.startswith("menu/edit/"): return "2D 视图与地图编辑操作", " | ".join(reason)
        if low.startswith("menu/run/"): return "游戏配置与资源管理", " | ".join(reason)
        if low.startswith("menu/debug/"): return "其他或待确认", " | ".join(reason)
        if low.startswith("menu/help/") or low.startswith("menu/view/"):
            if re.search(r"entity|classname",s+" "+h): return "Entity 与属性编辑", " | ".join(reason)
            if re.search(r"texture|material",s+" "+h): return "Texture 与材质管理", " | ".join(reason)
            return "2D 视图与地图编辑操作", " | ".join(reason)
        if low.startswith("menu/tools/") or low.startswith("toolbar/"):
            if re.search(r"brush|clip|sweep|carve|face|vertex|geometry",s+" "+h): return "Brush、Face 和几何编辑", " | ".join(reason)
            return "工具快捷操作", " | ".join(reason)
        # 核心：功能优先于路径 Controls/Map view 和工具 ActionContext
        if re.search(r"entit(?:y|ies)|classname|point entit|brush entit", s+" "+h):
            return "Entity 与属性编辑", "实际处理逻辑/实体显示 | " + " | ".join(reason)
        if re.search(r"texture|material|uv", s+" "+h):
            return "Texture 与材质管理", "实际处理逻辑/材质 | " + " | ".join(reason)
        if re.search(r"sweep|assemblebrush|clip|carve|vertex|face|brush|geometry", s+" "+h):
            return "Brush、Face 和几何编辑", "实际处理逻辑/几何工具 | " + " | ".join(reason)
        if re.search(r"move|duplicate|select|snap|grid|translate|rotate|scale", s+" "+h):
            return "2D 视图与地图编辑操作", "对象编辑动作（非工具自身快捷键） | " + " | ".join(reason)
        if "View3D" in ctxs and re.search(r"3d|camera",s):
            return "3D 视图与摄像机操作", " | ".join(reason)
        return "UNKNOWN", "动作语句证据不足（路径/上下文/处理逻辑无法可靠判定） | " + " | ".join(reason)
    if m["context"]=="tb::ui::ActionBuilder" or "ActionBuilder" in m["file"]: return "工具快捷操作", "ActionBuilder 快捷键文本"
    for cat,pats in [
        ("Preferences 和设置页面",["preference","viewpreference","gamepreference","qpreferencestoredelegate","compilationprofile"]),
        ("游戏配置与资源管理",["updatelib","upd::","gameengine","package","compilation"]),
        ("Entity 与属性编辑",["entity","flagseditor","classname","spawn"]),
        ("Texture 与材质管理",["material","texture","uv","faceattribs"]),
        ("Brush、Face 和几何编辑",["brush","face","vertex","edge","geometry","sweep","clip","carve","drawshape"]),
        ("3D 视图与摄像机操作",["renderer","camera","view3d"]),
        ("2D 视图与地图编辑操作",["mapview","mapwindow","vieweditor","layereditor","selection","grid","toolbox","collapsible"]),
        ("错误信息和警告",["error","warning","fail","exception","could not","cannot"]),
        ("对话框和确认提示",["dialog","messagebox","wizard","prompt"]),
        ("文件操作与项目管理",["document","save","load","export","import","recent","prefab"]),
        ("工具提示与状态信息",["tooltip","status","console","issuebrowser"]),
        ("工具快捷操作",["toolpage","shortcut"]),
        ("主菜单和主窗口",["welcome","mainwindow"]),
    ]:
        hay=(m["context"]+" "+m["file"]).lower()
        if any(re.search(p,hay) or (cat in ("错误信息和警告","对话框和确认提示") and re.search(p,s)) for p in pats):
            return cat, "context/文件名关键词 | "+",".join(pats)
    if re.search(r"^(save|open|new|close|export|import|revert|reload|quit|exit)",s): return "文件操作与项目管理", "source 动词"
    return "UNKNOWN", "无动作语句且 context/文件名/source 无可靠线索"

# ---- 解析 TS（全部 location）----
root=ET.parse(TS).getroot(); msgs=[]
for cn in root.findall("context"):
    ctx=cn.find("name").text if cn.find("name") is not None else ""
    for m in cn.findall("message"):
        se=m.find("source"); te=m.find("translation")
        src=(se.text or "") if se is not None else ""; trn=(te.text or "") if te is not None else ""
        typ=te.get("type","") if te is not None else ""
        locs=[(l.get("filename",""),int(l.get("line","0") or 0)) for l in m.findall("location")]
        mid=hashlib.sha256((ctx+"\x1f"+src).encode()).hexdigest()[:12]
        st=None; fn=""
        for f,L in locs:
            if os.path.basename(f)=="ActionManager.cpp":
                st=stmt_for(L); fn=am_func(L); break
        cat,why=classify(dict(context=ctx,source=src,file=locs[0][0] if locs else ""),st,fn)
        conf="低" if cat=="UNKNOWN" else ("高" if st else "中")
        msgs.append(dict(id=mid,context=ctx,source=src,translation=trn,finished=(typ!="unfinished"),
            locations="; ".join(f"{a}:{b}" for a,b in locs),
            am_function=fn if st else "", action_path=st["path"] if st else "",
            action_context=",".join(st["ctxs"]) if st else "",
            handler=st["handler"] if st else "", category=cat, category_reason=why,
            evidence_confidence=conf, has_stmt=bool(st)))
# 动作级证据 CSV（所有 ActionManager 消息）
with open(os.path.join(OUT,"Action_Registration_Audit.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["message_id","context","source","source_line","am_function","action_path","action_context_full","handler_callback","statement_start","statement_end","category","category_reason","evidence_confidence"])
    for m in msgs:
        if m["has_stmt"]:
            L=int(m["locations"].split("ActionManager.cpp:")[-1].split(";")[0]) if "ActionManager.cpp:" in m["locations"] else 0
            st=stmt_for(L)
            w.writerow([m["id"],m["context"],m["source"][:100],L,m["am_function"],m["action_path"],m["action_context"],m["handler"][:200],st["start"],st["end"],m["category"],m["category_reason"],m["evidence_confidence"]])
# 完整索引
cols=["id","context","source","translation","finished","locations","am_function","action_path","action_context","handler","category","category_reason","evidence_confidence"]
with open(os.path.join(OUT,"Revised_Message_Index.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction="ignore"); w.writeheader()
    for m in msgs: w.writerow(m)
# B01 审计
old=list(csv.DictReader(open(os.path.join(R1,"P2D3A_R1_Batches.csv"),encoding="utf-8-sig")))
oldb01=next(r for r in old if r["batch"]=="R1-B01")["ids"].split(",")
idx={m["id"]:m for m in msgs}
rows=[]
for order,mid in enumerate(oldb01,1):
    m=idx.get(mid); r=[order,mid,m["source"][:100] if m else "NOT_FOUND",m["am_function"] if m else "",m["action_path"] if m else "",m["category"] if m else "",m["evidence_confidence"] if m else ""]
    if not m: r+=["不存在","无法核验"]
    elif m["am_function"]!="createFileMenu" or not m["action_path"].startswith("Menu/File"):
        r+=["不应进入本批次","非 createFileMenu/Menu/File 动作："+m["context"]]
    elif "OBJ" in m["source"] or ".map" in m["source"] or "file" in m["source"].lower() or "point file" in m["source"].lower() or "portal file" in m["source"].lower():
        r+=["需额外术语确认","保留文件格式/扩展名/技术标识"]
    else: r+=["允许翻译",""]
    rows.append(r)
with open(os.path.join(OUT,"B01_Release_Audit.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["order","id","source","am_function","action_path","new_category","confidence","verdict","note"]); w.writerows(rows)
# 新批次：基于新分类；文件操作批次仅取 createFileMenu 且 verdict 允许/需确认
order=["文件操作与项目管理","主菜单和主窗口","对话框和确认提示","工具提示与状态信息","Preferences 和设置页面",
       "2D 视图与地图编辑操作","3D 视图与摄像机操作","工具快捷操作","Brush、Face 和几何编辑","Entity 与属性编辑",
       "Texture 与材质管理","游戏配置与资源管理","错误信息和警告","其他或待确认","UNKNOWN"]
pool=[m for m in msgs if not m["finished"]]
batches=[]
for cat in order:
    ids=[m["id"] for m in pool if m["category"]==cat]
    if cat=="文件操作与项目管理":
        keep={r[1] for r in rows if r[7] in ("允许翻译","需额外术语确认")}
        ids=[i for i in ids if i in keep]
        removed=[m["id"] for m in pool if m["category"]==cat and m["id"] not in keep]
    for st in range(0,len(ids),45):
        batches.append([f"RA-B{len([b for b in batches if b[0].startswith('RA-')])+1:02d}",cat,len(ids[st:st+45]),",".join(ids[st:st+45])])
if removed:
    batches.append([f"RA-B{len([b for b in batches if b[0].startswith('RA-')])+1:02d}","隔离待确认（非文件操作，禁止进入 B01）",len(removed),",".join(removed)])
with open(os.path.join(OUT,"Revised_Batches.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["batch","category","count","ids"]); w.writerows(batches)
# 统计
from collections import Counter
print(json.dumps(dict(messages=len(msgs),contexts=len(root.findall("context")),
    finished=sum(m["finished"] for m in msgs),unfinished=sum(not m["finished"] for m in msgs),
    action_stmt_msgs=sum(m["has_stmt"] for m in msgs),
    b01_verdict=Counter(r[7] for r in rows),
    categories=Counter(m["category"] for m in msgs)),ensure_ascii=False,indent=1,default=dict))
print("样本:")
for src in ["Toggle Show Entity Classnames","Toggle Show Brush Entity Bounds","Toggle Show Point Entity Bounds","Toggle Show Point Entities","Toggle Show Point Entity Models","Perform Sweep","Decrease Sweep Scale","Increase Sweep Scale","Move Forward","Move Backward","Move Left","Move Right","Move Up","Move Down","Duplicate and Move Forward","Duplicate and Move Backward"]:
    hits=[m for m in msgs if m["source"]==src]
    for m in hits: print(f"  {src!r} -> {m['category']} | path={m['action_path'] or '缺失'} | ctx={m['action_context'] or '缺失'} | conf={m['evidence_confidence']}")
