"""Static link slots consumed by DEF70B0 in the pinned 26.01.02 sample."""
from .memory import MemoryReadError, decode_pointer


def read_link_registry(memory, base, sentinel, max_entries=512):
    if not 1 <= max_entries <= 4096:
        raise ValueError("Invalid link registry bound")
    rows, errors = [], []
    for index in range(max_entries):
        ea = base + index * 48
        try:
            raw = memory.read(ea, 48)
            key = decode_pointer(raw[:8], "little")
            if key == sentinel:
                return rows, errors
            kind = int.from_bytes(raw[24:28], "big")
            target = decode_pointer(raw[16:24], "little")
            if not key or not target or kind not in (1, 2):
                raise MemoryReadError("Invalid static link slot")
            rows.append({"address": ea, "key": key, "root": target, "type": kind,
                         "raw_hex": raw.hex(), "evidence": "DFF1C10 stride=48; DEF70B0 key+0/root+16/type+24"})
        except MemoryReadError as exc:
            errors.append({"address": ea, "error": str(exc)})
            break
    errors.append({"address": base, "error": "Link registry sentinel not established"})
    return rows, errors
