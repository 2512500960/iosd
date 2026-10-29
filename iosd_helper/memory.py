"""Exact, read-only memory access. Never substitute absent core pages with zeroes."""
from bisect import bisect_right
from dataclasses import dataclass
import mmap
import struct


class MemoryReadError(RuntimeError):
    pass


@dataclass(frozen=True)
class AddressMap:
    # Use the bases of the SAME image-relative address (normally ELF RVA 0).
    idb_base: int
    runtime_base: int

    def to_runtime(self, ea):
        return ea - self.idb_base + self.runtime_base

    def to_idb(self, va):
        return va - self.runtime_base + self.idb_base


def decode_pointer(data, mode="little"):
    if len(data) != 8:
        raise ValueError("Expected an eight-byte pointer")
    if mode in ("little", "big"):
        return int.from_bytes(data, mode)
    if mode == "mask_then_swap":
        raw = int.from_bytes(data, "little") & 0x7fffffffffffffff
        return int.from_bytes(raw.to_bytes(8, "little"), "big")
    if mode == "swap_then_mask":
        return int.from_bytes(data, "big") & 0x7fffffffffffffff
    raise ValueError("Unknown pointer encoding: " + mode)


def read_cstring(memory, address, limit=512):
    if not address:
        raise MemoryReadError("NULL string pointer")
    # Small reads allow a terminating NUL just before an unmapped boundary.
    result = bytearray()
    for offset in range(limit):
        byte = memory.read(address + offset, 1)
        if byte == b"\0":
            return result.decode("utf-8", errors="replace")
        result.extend(byte)
    raise MemoryReadError("Unterminated string at %#x (limit %d)" % (address, limit))


@dataclass(frozen=True)
class CoreSegment:
    address: int
    memory_size: int
    file_offset: int
    file_size: int
    flags: int


class ElfCoreMemory:
    """Uncompressed ELF64 ET_CORE / x86-64. PT_LOAD is authoritative.

    Missing bytes (p_memsz > p_filesz) are NOT ELF executable BSS zero-fill.
    They are unavailable snapshot pages. No fallback to IDB is performed.
    """
    source = "elf-core"

    def __init__(self, path):
        self.path = str(path)
        self._file = open(path, "rb")
        self._map = None
        try:
            self._map = mmap.mmap(self._file.fileno(), 0, access=mmap.ACCESS_READ)
            self._parse()
        except Exception:
            self.close()
            raise

    def _parse(self):
        data = self._map
        if len(data) < 64 or data[:4] != b"\x7fELF" or data[4] != 2:
            raise ValueError("Expected uncompressed ELF64 core; decompress .gz first")
        if data[5] not in (1, 2):
            raise ValueError("Invalid ELF endianness")
        endian = "<" if data[5] == 1 else ">"
        header = struct.unpack_from(endian + "HHIQQQIHHHHHH", data, 16)
        kind, machine, version, _, phoff, _, _, ehsize, phsize, phnum, *_ = header
        if kind != 4 or machine != 62 or version != 1 or data[6] != 1 or ehsize < 64:
            raise ValueError("Only ELF64 x86-64 ET_CORE version 1 is supported")
        if phnum == 0xffff:
            raise ValueError("Extended ELF program-header counts are not supported yet")
        if phsize < 56 or phoff + phsize * phnum > len(data):
            raise ValueError("Truncated or invalid ELF program-header table")
        segments = []
        for index in range(phnum):
            typ, flags, off, va, _, filesz, memsz, _ = struct.unpack_from(
                endian + "IIQQQQQQ", data, phoff + index * phsize)
            if typ != 1 or not memsz:
                continue
            if filesz > memsz or off + filesz > len(data) or va + memsz > 2**64:
                raise ValueError("Invalid or truncated PT_LOAD segment")
            segments.append(CoreSegment(va, memsz, off, filesz, flags))
        self.segments = sorted(segments, key=lambda s: s.address)
        for left, right in zip(self.segments, self.segments[1:]):
            if left.address + left.memory_size > right.address:
                raise ValueError("Overlapping PT_LOAD mappings are ambiguous")
        self._starts = [s.address for s in self.segments]

    def read(self, address, size):
        if address < 0 or size < 0:
            raise ValueError("Negative address or size")
        if self._map is None:
            raise MemoryReadError("Core is closed")
        result = bytearray()
        while len(result) < size:
            current = address + len(result)
            index = bisect_right(self._starts, current) - 1
            if index < 0:
                raise MemoryReadError("Unmapped core address %#x" % current)
            seg = self.segments[index]
            delta = current - seg.address
            if delta >= seg.memory_size:
                raise MemoryReadError("Unmapped core address %#x" % current)
            if delta >= seg.file_size:
                raise MemoryReadError("Core page not captured at %#x" % current)
            take = min(size - len(result), seg.file_size - delta)
            offset = seg.file_offset + delta
            result.extend(self._map[offset:offset + take])
        return bytes(result)

    def close(self):
        if self._map is not None:
            self._map.close()
            self._map = None
        self._file.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
