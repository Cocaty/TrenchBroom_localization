# P2-D3A：术语候选与 UI 长度风险（只读，基于 P2D3A_Message_Index.json）
import json, csv, os, re, collections
OUT = r"C:\Users\yoshi\Projects\TrenchBroom-zhCN\reports\P2-D3A\Evidence"
msgs = json.load(open(os.path.join(OUT,"P2D3A_Message_Index.json"),encoding="utf-8"))["messages"]

# 候选译法（建议，待 ChatGPT 校阅；不写入 TS）
GLOSSARY = [
 ("Brush","笔刷","刷子","可编辑的几何体，由面构成","LayerEditor/Brush-related tr() sources","中"),
 ("Face","面","面片","Brush 的一个平面","FaceAttribsEditor / 'Face' sources","中"),
 ("Vertex","顶点","—","几何顶点","Brush/geometry sources","高"),
 ("Edge","边","边缘","几何边","geometry sources","高"),
 ("Plane","平面","—","几何平面/参考平面","geometry sources","中"),
 ("Polygon","多边形","—","多边形几何","geometry sources","高"),
 ("Geometry","几何体","几何","几何数据总称","geometry sources","高"),
 ("Primitive","图元","基本体","创建基本形状","drawshape sources","中"),
 ("Entity","实体","图元实体","地图中的游戏对象","EntityInspector/EntityBrowser sources","高"),
 ("Point Entity","点实体","—","无几何体、由属性定义的实体","entity sources","中"),
 ("Brush Entity","笔刷实体","固体实体","由 brush 构成的实体","entity sources","中"),
 ("World","世界","世界场景","地图的世界级实体","entity/world sources","中"),
 ("Property","属性","特性","Entity 的 key-value 属性","EntityPropertyEditor sources","中"),
 ("Class","类","类别","Entity classname 等","entity sources","中"),
 ("Model","模型","—","Entity 显示的 3D 模型","entity/model sources","高"),
 ("Spawn","生成","出生","实体在游戏中的初始化","entity sources","中"),
 ("Texture","纹理","贴图","旧术语；与 Material 对应","MaterialBrowser sources","中"),
 ("Material","材质","贴图","当前使用的贴图资源","MaterialBrowser/FaceAttribs sources","高"),
 ("UV","UV","纹理坐标","UV 贴图坐标","UV editor sources","高"),
 ("Surface","表面","曲面","实体/笔刷表面","face/material sources","中"),
 ("Mapping","映射","贴图映射","UV 映射方式","UV sources","中"),
 ("Alignment","对齐","贴图对齐","UV 对齐","UV sources","中"),
 ("Projection","投影","贴图投影","UV 投影模式","UV sources","中"),
 ("Select","选择","选中","选择操作","ActionManager 'Select…'","高"),
 ("Move","移动","—","平移操作","ActionManager 'Move…'","高"),
 ("Rotate","旋转","—","旋转操作","RotateToolPage sources","高"),
 ("Scale","缩放","—","缩放操作","ScaleToolPage sources","高"),
 ("Snap","吸附","对齐网格","网格吸附","grid/snap sources","中"),
 ("Grid","网格","栅格","编辑器网格","grid sources","高"),
 ("Duplicate","复制","副本","复制对象","ActionManager 'Duplicate'","高"),
 ("Group","编组","组","对象编组（与 layer 区分）","QObject 'Group' / layer context","中"),
 ("Ungroup","取消编组","解组","解除编组","ActionManager sources","中"),
 ("Clip","剪裁","剪切","Clip 工具","ActionManager 'Perform Clip'","中"),
 ("Carve","雕刻","切割","Carve 工具","carve sources","中"),
 ("Map","地图","关卡","TrenchBroom 编辑的地图文件","file/map sources","高"),
 ("Prefab","预制件","预设","可复用地图片段","prefab sources","中"),
 ("Package","包","资源包","资源/package 文件","resource sources","中"),
 ("Export","导出","—","导出地图或资源","export sources","高"),
 ("Import","导入","—","导入地图或资源","import sources","高"),
 ("Save","保存","—","保存地图","file sources","高"),
 ("Load","加载","载入","加载地图/资源","file sources","中"),
 ("Game Configuration","游戏配置","游戏设置","Game PreferencePane 配置","GamePreferencePane sources","高"),
 ("Layer","图层","层","地图图层（与 Group 不同）","LayerEditor sources","中"),
 ("Apply","应用","套用","对话框应用按钮","dialog buttons","高"),
 ("Fix","修复","修正","IssueBrowser 修复操作","IssueBrowserView 'Fix'","中"),
 ("Launch Engine","启动引擎","运行游戏","编译后启动游戏","Compilation sources","中"),
]
with open(os.path.join(OUT,"P2D3A_Glossary.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["English","Chinese_candidate","Alternative","Context","Evidence","Confidence","Review_status"])
    for e,c,a,ctx,ev,conf in GLOSSARY:
        pat = re.compile(r"\b" + re.escape(e) + r"\b", re.I)
        hits = sum(1 for m in msgs if pat.search(m["source"]))
        if hits == 0:
            ev2 = "当前 TS 无精确匹配（预备术语，非本批翻译对象）"
            conf2 = "低"
        else:
            ev2 = f"{ev}；TS 精确匹配 {hits} 条"
            conf2 = conf
        w.writerow([e,c,a,ctx,ev2,conf2,"待 ChatGPT 校阅"])

# UI 长度风险（预测，非实测）
def risk(m):
    s=m["source"]; n=m["source_len"]; ctx=m["context"]
    if m["placeholders"] or len(s)>90: return "高","长文本/含占位符，中文可能更长"
    if m["has_key_hint"] or m["has_technical"]: return "中","含按键/技术标识，需保持原样"
    usage = m.get("function","")
    if n<=12: return "中","短按钮/菜单词，中文可能变宽"
    if n<=55: return "低","中等长度普通 UI 文本"
    return "中","较长文本，需布局复核"
rows=[]
for m in msgs:
    if m["finished"]: continue
    r,why = risk(m); rows.append([m["id"],m["context"],m["source"][:100],m["source_len"],r,why,"预测风险（无布局实测）"])
with open(os.path.join(OUT,"P2D3A_Length_Risk.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["id","context","source","source_len","risk_level","reason","evidence_type"]); w.writerows(rows)
print("术语:", len(GLOSSARY), "| 长度风险分布:", dict(collections.Counter(r[4] for r in rows)))
print("术语在 TS 出现情况（前 8）:")
for e,*_ in GLOSSARY[:8]:
    pat=re.compile(r"\b"+re.escape(e)+r"\b",re.I)
    print("  ", e, sum(1 for m in msgs if pat.search(m["source"])))
