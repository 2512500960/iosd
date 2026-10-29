"""Generate a tiny ELF executable + matching core for IDA integration testing.

No proprietary binaries, no IDA installation, no external Python dependencies.
"""
from pathlib import Path
import struct

IDB_BASE = 0x400000
RUNTIME_BASE = 0x555555554000


def elf_header(kind, phnum, shoff=0, shnum=0, shstr=0):
    return b"\x7fELF\x02\x01\x01" + bytes(9) + struct.pack(
        "<HHIQQQIHHHHHH", kind, 62, 1, IDB_BASE + 0x1000 if kind == 2 else 0,
        64, shoff, 0, 64, 56, phnum, 64 if shnum else 0, shnum, shstr)


def core_bytes(mappings):
    """mappings: (runtime_va, captured_bytes, memory_size)."""
    offset = 64 + 56 * len(mappings)
    headers, payload = bytearray(), bytearray()
    for address, data, memsz in mappings:
        headers.extend(struct.pack("<IIQQQQQQ", 1, 6, offset, address, 0, len(data), memsz, 1))
        payload.extend(data)
        offset += len(data)
    return elf_header(4, len(mappings)) + headers + payload


def make(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    static = bytearray(0x3000)
    strings = {0x2000: b"fixture_subsystem\0",
               0x2040: b"VIEW_ROOT/cisco.comp/parser/src/fixture.c\0",
               0x2100: b"show fixture\0"}
    for offset, data in strings.items():
        static[offset:offset + len(data)] = data
    static[0x1000:0x1001] = b"\xc3"  # ret
    static[0x2200:0x2208] = bytes.fromhex("c15c0515c15c0515")
    struct.pack_into("<Q", static, 0x2218, IDB_BASE + 0x2000)
    struct.pack_into("<Q", static, 0x2220, IDB_BASE + 0x1000)
    struct.pack_into("<Q", static, 0x2228, 0x400)
    # Headers/section table give IDA usable names and a segment for subsystem scanning.
    shnames = b"\0.text\0.rodata\0subsys_header_section\0.shstrtab\0"
    static[0x2400:0x2400 + len(shnames)] = shnames
    shoff = 0x2600
    sections = [(0, 0, 0, 0, 0, 0),
                (shnames.index(b".text"), 1, 6, IDB_BASE + 0x1000, 0x1000, 1),
                (shnames.index(b".rodata"), 1, 2, IDB_BASE + 0x2000, 0x2000, 0x200),
                (shnames.index(b"subsys_header_section"), 1, 2, IDB_BASE + 0x2200, 0x2200, 56),
                (shnames.index(b".shstrtab"), 3, 0, 0, 0x2400, len(shnames))]
    for index, (name, typ, flags, va, off, size) in enumerate(sections):
        struct.pack_into("<IIQQQQIIQQ", static, shoff + 64 * index,
                         name, typ, flags, va, off, size, 0, 0, 1, 0)
    static[:64] = elf_header(2, 1, shoff, len(sections), 4)
    static[64:120] = struct.pack("<IIQQQQQQ", 1, 5, 0, IDB_BASE, IDB_BASE,
                                len(static), len(static), 0x1000)
    image = output / "fixture-iosd.elf"
    image.write_bytes(static)

    heap = bytearray(0x1000)
    # Conservative layout: text buffer pointer +48, offset +60, length +64.
    struct.pack_into(">Q", heap, 48, RUNTIME_BASE + 0x2100)
    struct.pack_into(">I", heap, 40, 1)
    struct.pack_into(">I", heap, 60, 0)
    struct.pack_into(">I", heap, 64, len(b"show fixture"))
    core = output / "fixture-iosd.core"
    core.write_bytes(core_bytes([(RUNTIME_BASE, bytes(static), len(static)),
                                 (RUNTIME_BASE + 0x10000, bytes(heap), 0x2000)]))
    return image, core


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", default="tests/fixtures/generated")
    args = parser.parse_args()
    for path in make(args.output):
        print(path.resolve())
    print("IDB image base: %#x; runtime image base: %#x" % (IDB_BASE, RUNTIME_BASE))
    print("Mapping anchor IDB: %#x; first node runtime VA: %#x" %
          (IDB_BASE + 0x2040, RUNTIME_BASE + 0x10000))
