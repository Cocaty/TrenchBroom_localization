# P2-D2C-B-R3 QM 检查器（加固版）
# 依据：Qt 6.10.3 qtranslator.cpp（官方源码，见 P2-D2C-B-R2 证据）
#   MagicLength = 16；魔数 = 3cb86418caef9c95cd211cbf60a1bddd
#   0xa7 = Language 块标签，不属于魔数
#   块结构：tag(1B, 大端) + blockLen(4B, 大端) + payload(blockLen)
# 注意：本脚本只验证「块结构」，不声称完成「完整 QM 语义验证」（译文正确性需加载器/运行期验证）
import struct, sys

MAGIC = bytes.fromhex("3cb86418caef9c95cd211cbf60a1bddd")
TAGS = {0x2f: "Contexts", 0x42: "Hashes", 0x69: "Messages",
        0x88: "NumerusRules", 0x96: "Dependencies", 0xa7: "Language"}

def check(path):
    print(f"== {path}")
    d = open(path, "rb").read()
    n = len(d)
    print(f"文件大小: {n}")
    errors, warnings = [], []

    # 1-2. 文件长度守卫（魔数与第 17 字节访问前检查）
    if n < 16:
        print(f"❌ 文件长度 {n} < 16，无法容纳魔数；拒绝检查")
        print("结构检查: 未通过 | 完整 QM 语义验证: 未执行")
        return 1
    print(f"前 20 字节: {' '.join(f'{b:02x}' for b in d[:20])}")
    print(f"标准魔数(16B): {' '.join(f'{b:02x}' for b in MAGIC)}")
    magic_ok = d[:16] == MAGIC
    print(f"前 16 字节 == 标准魔数: {magic_ok}")
    if not magic_ok:
        errors.append("魔数不匹配")
    if n > 16:
        b17 = d[16]
        print(f"第 17 字节: 0x{b17:02x}（块标签；魔数仅前 16 字节，不计入）")
    else:
        b17 = None
        warnings.append("文件仅 16 字节（只有魔数），没有第 17 字节/块数据")

    # 3-10. 块遍历：逐块边界检查 + 诊断
    off, seen, blocks = 16, [], []
    while off < n:
        hdr = n - off
        if hdr < 5:
            errors.append(f"偏移 {off}: 块头不完整（剩余 {hdr}B < 5B）")
            break
        tag = d[off]
        block_len = struct.unpack(">I", d[off+1:off+5])[0]
        payload_start = off + 5
        block_end = payload_start + block_len
        name = TAGS.get(tag, f"UNKNOWN(0x{tag:02x})")
        print(f"  块 @偏移={off}: tag=0x{tag:02x} ({name}) len={block_len} "
              f"header=5B payload=[{payload_start},{block_end})")
        if tag not in TAGS:
            warnings.append(f"偏移 {off}: 未知块标签 0x{tag:02x}（按数据跳过，语义未验证）")
        if block_len == 0:
            errors.append(f"偏移 {off}: 零长度块（QM 块长度不得为 0）")
            break
        if block_end > n:
            errors.append(f"偏移 {off}: 块长度 {block_len} 超出 EOF（块结束 {block_end} > 文件 {n}）")
            break
        if tag in seen:
            warnings.append(f"偏移 {off}: 重复块标签 0x{tag:02x} ({name})")
        seen.append(tag)
        blocks.append((tag, block_len, payload_start, block_end))
        off = block_end  # 块结束位置精确推进
    if not blocks:
        errors.append("未解析到任何块（仅有魔数/无块数据），QM 结构不完整")
    if not errors and off == n:
        print(f"块遍历: ✅ 完整消耗至 EOF（结束偏移 {off}/{n}）")
    elif not errors:
        errors.append(f"未完整消耗至 EOF（结束偏移 {off} != 文件 {n}）")

    # 语义命中仅为提示，不等于语义验证
    sem = []
    for tag, bl, ps, pe in blocks:
        if tag == 0xa7:
            sem.append(f"Language={d[ps:pe].decode('utf-8','replace')!r}")
        if tag == 0x69:
            hit = any(t.encode("utf-16-be") in d[ps:pe]
                      for t in ("语言", "语言更改将在重启"))
            sem.append(f"Messages 中译文 UTF-16 字节命中={'是' if hit else '否'}")
    print("提示信息（非语义验证）:", "; ".join(sem) if sem else "无")
    for w in warnings:
        print("⚠️", w)
    for e in errors:
        print("❌", e)
    print(f"块结构检查: {'通过' if not errors else '未通过'} | "
          f"完整 QM 语义验证: 未执行（本脚本不提供）")
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(check(sys.argv[1]))
