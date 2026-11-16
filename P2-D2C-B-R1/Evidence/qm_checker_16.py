# P2-D2C-B-R2 修正版 QM 检测器
# 依据：Qt 6.10.3 qtranslator.cpp（code.qt.io v6.10.3 实测源码）
#   MagicLength = 16（L1327-1328 附近，mcookie 生成注释）
#   魔数 = 3cb86418caef9c95cd211cbf60a1bddd（16 字节，无 0xa7）
#   块枚举：Contexts=0x2f, Hashes=0x42, Messages=0x69, NumerusRules=0x88,
#           Dependencies=0x96, Language=0xa7
#   块结构：tag(1B) + blockLen(4B, 大端) + payload(blockLen)，do_load while 循环
import struct, sys

MAGIC = bytes.fromhex("3cb86418caef9c95cd211cbf60a1bddd")  # 16 字节
TAGS = {0x2f: "Contexts", 0x42: "Hashes", 0x69: "Messages",
        0x88: "NumerusRules", 0x96: "Dependencies", 0xa7: "Language"}

def check(path):
    d = open(path, "rb").read()
    print(f"== {path}")
    print(f"文件大小: {len(d)}")
    print(f"前 20 字节: {' '.join(f'{b:02x}' for b in d[:20])}")
    print(f"标准魔数(16B): {' '.join(f'{b:02x}' for b in MAGIC)}")
    print(f"前 16 字节 == 标准魔数: {d[:16] == MAGIC}")
    print(f"第 17 字节(0xa7=Language 块标签，不属魔数): 0x{d[16]:02x}")
    # 块遍历（do_load 同款：tag + u32 BE len + payload）
    off = 16
    blocks = []
    while off + 5 <= len(d):
        tag = d[off]; blockLen = struct.unpack(">I", d[off+1:off+5])[0]
        payload = d[off+5:off+5+blockLen]
        blocks.append((tag, blockLen, payload))
        off += 5 + blockLen
        if tag not in TAGS or blockLen == 0:
            break
    ok = off == len(d)
    print(f"块遍历: {'完整消耗至 EOF ✅ 结构有效' if ok else '❌ 未对齐'}")
    for tag, bl, pl in blocks:
        name = TAGS.get(tag, f"0x{tag:02x}")
        extra = f" 内容={pl.decode('utf-8','replace')!r}" if tag == 0xa7 else f" 含译文UTF-16命中={any(t.encode('utf-16-be') in pl for t in ('语言','语言更改将在重启'))}"
        print(f"  块 0x{tag:02x} ({name}): {bl}B{extra}")

if __name__ == "__main__":
    check(sys.argv[1])
