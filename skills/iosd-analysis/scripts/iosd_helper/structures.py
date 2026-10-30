"""Evidence-preserving, configurable candidate parsers, independent of IDA."""
from dataclasses import dataclass, asdict
from collections import deque
from typing import Optional

from .memory import MemoryReadError, decode_pointer, read_cstring


@dataclass(frozen=True)
class NodeLayout:
    size: int = 72
    pointer_mode: str = "big"
    scalar_order: str = "big"
    command_pointer: int = 48
    command_offset: Optional[int] = 60
    command_size: Optional[int] = 64
    # Unresolved in the supplied document. Enable only after manual validation.
    handler_offset: Optional[int] = None
    links: tuple = ()
    max_text: int = 1024
    text_policy: str = "generic"
    tree_root: Optional[int] = None
    rejected_reason: Optional[str] = None

    def __post_init__(self):
        if self.rejected_reason:
            raise ValueError("Rejected layout: " + self.rejected_reason)
        if self.text_policy not in ("generic", "icm_print_observed"):
            raise ValueError("Unknown text policy")
        if self.text_policy == "icm_print_observed" and self.pointer_mode != "swap_then_mask":
            raise ValueError("Observed ICM policy needs swap_then_mask for tagged BE pointers")
        if self.tree_root is not None and self.tree_root <= 0:
            raise ValueError("tree_root must be a positive address in the selected source")
        if self.size < 72 or self.max_text < 1 or self.max_text > 65536:
            raise ValueError("Invalid node/text size")
        if self.scalar_order not in ("little", "big"):
            raise ValueError("Invalid scalar byte order")
        decode_pointer(bytes(8), self.pointer_mode)
        for off in [self.command_pointer, self.handler_offset, *self.links]:
            if off is not None and (off < 0 or off + 8 > self.size):
                raise ValueError("Pointer offset outside node")
        for off in (self.command_offset, self.command_size):
            if off is not None and (off < 0 or off + 4 > self.size):
                raise ValueError("Scalar offset outside node")


def inspect_node(memory, address, layout):
    raw = memory.read(address, layout.size)
    ptr = lambda off: decode_pointer(raw[off:off + 8], layout.pointer_mode)
    scalar = lambda off: int.from_bytes(raw[off:off + 4], layout.scalar_order)
    row = {"address": address, "raw_hex": raw.hex(),
           "pointer_candidates": [ptr(off) for off in range(0, 40, 8)],
           "level_candidate": scalar(40), "flags_raw_hex": raw[56:60].hex(),
           "index_candidate": int.from_bytes(raw[68:70], layout.scalar_order),
           "links": [ptr(off) for off in layout.links], "status": "candidate",
           "handler_candidate": ptr(layout.handler_offset) if layout.handler_offset is not None else None}
    base = ptr(layout.command_pointer)
    offset = scalar(layout.command_offset) if layout.command_offset is not None else 0
    row["text_address"] = base + offset
    try:
        if layout.text_policy == "icm_print_observed":
            flags = int.from_bytes(raw[56:60], "big")
            row["flags_candidate"] = flags
            row["text_policy"] = layout.text_policy
            if flags & 0x40:
                array_offset = 48 if flags & 0x80 else 8240 if flags & 0x100 else None
                if array_offset is not None:
                    if layout.tree_root is None:
                        raise MemoryReadError("ICM text is root-array-backed; provide tree_root, do not use inline +48")
                    index = int.from_bytes(raw[68:70], "big")
                    if index >= 1024:
                        raise MemoryReadError("ICM buffer index exceeds observed array capacity")
                    slot = layout.tree_root + array_offset + 8 * index
                    base = decode_pointer(memory.read(slot, 8), "swap_then_mask")
                    row["text_buffer_slot"] = slot
                offset = int.from_bytes(raw[60:64], "big")
                end_offset = int.from_bytes(raw[64:68], "big")
                # print routine temporarily changes buffer[end_offset-1] from newline to NUL.
                size = end_offset - offset - 1
                if size < 0 or size > layout.max_text:
                    raise MemoryReadError("Invalid ICM text bounds: end-offset-1 = %d" % size)
                if not base:
                    raise MemoryReadError("NULL ICM text buffer")
                row["text_address"] = base + offset
                text = memory.read(base + offset, size).decode("utf-8", "replace")
            else:
                # Without 0x40 the print routine uses +48 as a C string directly.
                row["text_address"] = base
                text = read_cstring(memory, base, layout.max_text)
            row["text_candidate"] = text
            return row
        if not base:
            raise MemoryReadError("NULL command buffer")
        if layout.command_size is None:
            text = read_cstring(memory, base + offset, layout.max_text)
        else:
            size = scalar(layout.command_size)
            if size > layout.max_text:
                raise MemoryReadError("Candidate text size exceeds configured limit: %d" % size)
            text = memory.read(base + offset, size).rstrip(b"\0").decode("utf-8", "replace")
        row["text_candidate"] = text
    except MemoryReadError as exc:
        row["text_candidate"] = ""
        row["text_error"] = str(exc)
    return row


def walk_nodes(memory, start, layout=None, max_nodes=1000, cancelled=lambda: False):
    layout = layout or NodeLayout()
    if not start or max_nodes < 1 or max_nodes > 100000:
        raise ValueError("Provide nonzero first-node address and max_nodes in 1..100000")
    pending, visited, nodes, errors = deque([start]), set(), [], []
    reason = "complete_for_configured_links"
    while pending:
        if cancelled():
            reason = "cancelled"
            break
        if len(visited) >= max_nodes:
            reason = "node_limit"
            break
        address = pending.popleft()
        if address in visited or not address:
            continue
        visited.add(address)
        try:
            row = inspect_node(memory, address, layout)
            nodes.append(row)
            for link in row["links"]:
                if link and link not in visited:
                    pending.append(link)
        except MemoryReadError as exc:
            errors.append({"address": address, "error": str(exc)})
    if errors and reason == "complete_for_configured_links":
        reason = "partial_read_errors"
    return {"source": memory.source, "start": start, "layout": asdict(layout),
            "nodes": nodes, "errors": errors, "stop_reason": reason,
            "warning": "Candidate ICM fields; not a recovered CLI grammar or verified command-handler map."}


def scan_subsystems(memory, start, end, pointer_mode="little", cancelled=lambda: False):
    """Search double magic, NOT an assumed fixed entry stride.

    New document's icm sample: relative to magic, name +24, init +32.
    No inferred module hierarchy, size semantics, or code range is asserted.
    """
    magic = bytes.fromhex("c15c0515c15c0515")
    rows, errors = [], []
    chunk_size = 65536
    for block in range(start, end, chunk_size):
        if cancelled():
            return rows, errors, True
        size = min(chunk_size + 63, end - block)
        try:
            data = memory.read(block, size)
        except MemoryReadError as exc:
            errors.append({"address": block, "error": str(exc)})
            continue
        pos = data.find(magic)
        while pos >= 0 and pos < chunk_size:
            if cancelled():
                return rows, errors, True
            address = block + pos
            try:
                raw = memory.read(address, 56)
                name_ptr = decode_pointer(raw[24:32], pointer_mode)
                init = decode_pointer(raw[32:40], pointer_mode)
                name = read_cstring(memory, name_ptr, 256)
                if not name or not all(32 <= ord(c) < 127 for c in name):
                    raise MemoryReadError("Candidate name is empty or non-ASCII")
                rows.append({"address": address, "name": name, "name_address": name_ptr,
                             "init_candidate": init, "value_raw_hex": raw[40:48].hex(),
                             "raw_hex": raw.hex(), "pointer_mode": pointer_mode,
                             "status": "candidate: double magic and readable name"})
            except MemoryReadError as exc:
                errors.append({"address": address, "error": str(exc)})
            pos = data.find(magic, pos + 1)
    return rows, errors, False


def scan_module_records(memory, start, end, links=False, module_addresses=None,
                        cancelled=lambda: False):
    """Observed 26.01.02 schema; tags/fields remain explicit candidate evidence.

    Headers: 32 bytes, magic + tag AFECAFEC, name pointer +8.
    Links: 24 bytes, magic + tag DFEADFEA or ABEFABEF, endpoint A/B +8/+16.
    Endpoint direction and +16/+24 header semantics are deliberately unresolved.
    """
    size = 24 if links else 32
    tags = {0xdfeadfea, 0xabefabef} if links else {0xafecafec}
    if end < start:
        raise ValueError("Invalid section range")
    rows, errors = [], []
    for address in range(start, end - size + 1, size):
        if cancelled():
            return rows, errors, True
        try:
            raw = memory.read(address, size)
        except MemoryReadError as exc:
            errors.append({"address": address, "error": str(exc)})
            continue
        magic, tag = int.from_bytes(raw[:4], "little"), int.from_bytes(raw[4:8], "little")
        if magic != 0x15055cc1 or tag not in tags:
            errors.append({"address": address, "error": "Unrecognized module/link record signature",
                           "raw_hex": raw.hex()})
            continue
        fields = [int.from_bytes(raw[off:off + 8], "little") for off in range(8, size, 8)]
        row = {"address": address, "tag": tag, "raw_hex": raw.hex(),
               "pointer_mode": "little", "record_size": size, "status": "candidate"}
        if links:
            row.update(endpoint_a=fields[0], endpoint_b=fields[1],
                       relation="unresolved; do not assume dependency/parent direction")
            if module_addresses is not None:
                row["endpoint_a_is_header"] = fields[0] in module_addresses
                row["endpoint_b_is_header"] = fields[1] in module_addresses
        else:
            row.update(name_address=fields[0], field_10_candidate=fields[1], field_18_candidate=fields[2])
            try:
                name = read_cstring(memory, fields[0], 256)
                if not name or not all(32 <= ord(c) < 127 for c in name):
                    raise MemoryReadError("Invalid candidate module name")
                row["name"] = name
            except MemoryReadError as exc:
                row["name"] = ""
                row["name_error"] = str(exc)
                errors.append({"address": address, "error": str(exc)})
        rows.append(row)
    trailing = (end - start) % size
    if trailing:
        errors.append({"address": end - trailing, "error": "Trailing partial record", "byte_count": trailing})
    return rows, errors, False
