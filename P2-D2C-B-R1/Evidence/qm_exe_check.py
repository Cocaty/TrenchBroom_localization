# P2-D2C-B-R1 检测脚本：QM 魔数与 EXE 嵌入字节检查
# 修正说明：魔数为 16 字节；此前脚本误定义 17 字节列表并与 qm[:16] 比较，恒为 False
import sys
MAGIC = bytes.fromhex("3cb86418caef9c95cd211cbf60a1bddda7")  # 17 字节标准 Qt QM 魔数
qm = open(sys.argv[1], "rb").read()
print("QM 大小:", len(qm), "| 魔数(17B)匹配:", qm[:17] == MAGIC)
exe = open(sys.argv[2], "rb").read()
for label, text in (("重启提示译文", "语言更改将在重启"), ("语言", "语言")):
    print(f"EXE 含 {label}(UTF-16BE):", text.encode("utf-16-be") in exe)
print("EXE 含资源名 TrenchBroom_zh_CN(UTF-16BE):", "TrenchBroom_zh_CN".encode("utf-16-be") in exe)
