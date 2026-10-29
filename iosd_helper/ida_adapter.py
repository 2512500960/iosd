"""IDA calls stay on the IDA UI thread; core parsing needs no IDA imports."""
import re
import ida_bytes
import ida_dbg
import ida_idaapi
import ida_idd
import ida_kernwin
import ida_nalt
import ida_segment
import idautils
import ida_funcs
import ida_loader
import ida_name
import idc

from .memory import MemoryReadError
from .locators import KEY_NAMES, ANCHORS, literal_matches, symbol_kind
from .structures import scan_module_records, scan_subsystems


class IDBMemory:
    source = "idb"

    def read(self, address, size):
        if size == 0:
            return b""
        # get_bytes can synthesize uninitialized BSS as zero: reject unloaded bytes.
        if size < 0 or address < 0:
            raise ValueError("Negative address or size")
        pair = ida_bytes.get_bytes_and_mask(address, size, 0)
        if pair is None:
            raise MemoryReadError("IDB read failed at %#x" % address)
        data, mask = pair
        whole, tail = divmod(size, 8)
        if (len(mask) < whole + bool(tail) or mask[:whole] != b"\xff" * whole
                or (tail and mask[whole] & ((1 << tail) - 1) != (1 << tail) - 1)):
            raise MemoryReadError("IDB has uninitialized/unmapped bytes at %#x" % address)
        if data is None or len(data) != size:
            raise MemoryReadError("IDB read failed at %#x (%d bytes)" % (address, size))
        return bytes(data)


class DebugMemory:
    source = "debugger-suspended"

    def __init__(self):
        self._check()
        ida_dbg.invalidate_dbgmem_contents(ida_idaapi.BADADDR, 0)

    @staticmethod
    def _check():
        if ida_dbg.get_process_state() != ida_dbg.DSTATE_SUSP:
            raise MemoryReadError("Attach the IDA debugger and suspend iosd before reading")

    def read(self, address, size):
        self._check()
        if size < 0 or address < 0:
            raise ValueError("Negative address or size")
        if not size:
            return b""
        data = ida_idd.dbg_read_memory(address, size)
        if data is None or len(data) != size:
            raise MemoryReadError("Debugger read failed at %#x (%d bytes)" % (address, size))
        return bytes(data)


def segments():
    result = []
    for ea in idautils.Segments():
        seg = ida_segment.getseg(ea)
        result.append({"address": seg.start_ea, "end": seg.end_ea,
                       "name": ida_segment.get_segm_name(seg), "permissions": seg.perm})
    return result


def identity():
    digest = ida_nalt.retrieve_input_file_md5()
    return {"input_path": ida_nalt.get_input_file_path(),
            "idb_path": ida_loader.get_path(ida_loader.PATH_TYPE_IDB),
            "input_md5": digest.hex() if isinstance(digest, bytes) else str(digest),
            "imagebase": ida_nalt.get_imagebase(),
            "ida_version": ida_kernwin.get_kernel_version()}


def named_locators():
    """Named hits are database facts, not necessarily original ELF symbols."""
    rows = []
    for name in KEY_NAMES:
        ea = ida_name.get_name_ea(ida_idaapi.BADADDR, name)
        rows.append({"name": name, "address": None if ea == ida_idaapi.BADADDR else ea,
                     "status": "missing" if ea == ida_idaapi.BADADDR else "IDA name found",
                     "evidence": "may be an original symbol or a prior analyst rename"})
    return rows


def anchor_candidates(cancelled=lambda: False):
    memory, rows, errors = IDBMemory(), [], []
    overlap = max(map(len, ANCHORS.values())) - 1
    for segment in segments():
        if segment["permissions"] & (ida_segment.SEGPERM_EXEC | ida_segment.SEGPERM_WRITE):
            continue
        for start in range(segment["address"], segment["end"], 65536):
            if cancelled():
                return rows, errors, True
            try:
                data = memory.read(start, min(65536 + overlap, segment["end"] - start))
            except MemoryReadError as exc:
                errors.append({"address": start, "error": str(exc)})
                continue
            for row in literal_matches(data, start, 65536):
                row["references"] = referencing_functions(row["address"], limit=64)
                row["reference_limit"] = 64
                rows.append(row)
    return rows, errors, False


def symbol_candidates(cancelled=lambda: False):
    rows = []
    for index, (ea, name) in enumerate(idautils.Names()):
        if index % 256 == 0 and cancelled():
            return rows, True
        kind = symbol_kind(name)
        if kind is None:
            continue
        # Names() includes strings, globals and imports as well as functions.
        func = ida_funcs.get_func(ea)
        if func is None or func.start_ea != ea:
            continue
        rows.append({"address": ea, "name": name, "kind": kind,
                     "dot_prefixed_name": name.startswith("."),
                     "is_thunk": bool(getattr(func, "flags", 0) & ida_funcs.FUNC_THUNK),
                     "evidence": "IDA function-entry name; registration/semantics not verified"})
    return rows, False


def module_metadata(cancelled=lambda: False):
    memory, headers, link_rows, errors = IDBMemory(), [], [], []
    all_segments = segments()
    for seg in all_segments:
        if "module_header_section" not in seg["name"]:
            continue
        rows, faults, partial = scan_module_records(memory, seg["address"], seg["end"], cancelled=cancelled)
        headers.extend(rows)
        errors.extend(faults)
        if partial:
            return {"headers": headers, "links": link_rows, "errors": errors, "cancelled": True}
    addresses = {row["address"] for row in headers}
    names = {row["address"]: row.get("name", "") for row in headers}
    for seg in all_segments:
        if "module_link_section" not in seg["name"]:
            continue
        rows, faults, partial = scan_module_records(memory, seg["address"], seg["end"], links=True,
                                                   module_addresses=addresses, cancelled=cancelled)
        for row in rows:
            row["endpoint_a_name"] = names.get(row["endpoint_a"], "")
            row["endpoint_b_name"] = names.get(row["endpoint_b"], "")
        link_rows.extend(rows)
        errors.extend(faults)
        if partial:
            return {"headers": headers, "links": link_rows, "errors": errors, "cancelled": True}
    return {"headers": headers, "links": link_rows, "errors": errors, "cancelled": False,
            "schema_note": "26.01.02 observed signatures; relationship semantics unverified"}


def resolve_function(ea):
    func = ida_funcs.get_func(ea)
    if not func or func.start_ea != ea:
        return None
    return {"address": ea, "name": ida_name.get_name(ea),
            "is_thunk": bool(func.flags & ida_funcs.FUNC_THUNK), "size": func.end_ea - ea}


def discover_registration_tables(consumer, sentinel, max_call_sites=2000, max_tables=1000,
                                 max_entries=128, cancelled=lambda: False):
    """Bounded x86-64 RDI constant-reference recovery near direct register calls.

    Stops at earlier calls/function boundaries. Does not claim to solve computed
    arguments, branch predicates, wrapper registrations or interprocedural flow.
    Every candidate must also pass the static pair/sentinel table check.
    """
    from .grammar import registration_roots
    if not 1 <= max_call_sites <= 10000 or not 1 <= max_tables <= 5000:
        raise ValueError("Discovery limits out of range")
    memory, tables, unresolved = IDBMemory(), {}, []
    owners = {}
    for segment in segments():
        if "subsys_header_section" in segment["name"]:
            records, _, partial = scan_subsystems(memory, segment["address"], segment["end"], "little", cancelled)
            for record in records:
                owners.setdefault(record["init_candidate"], []).append(record["name"])
            if partial:
                return {"tables": [], "unresolved_call_sites": [], "call_sites_seen": 0,
                        "cancelled": True, "limited": False}
    count, limited = 0, False
    aliases = {"edi": "rdi", "esi": "rsi", "eax": "rax", "ebx": "rbx",
               "ecx": "rcx", "edx": "rdx", "r8d": "r8", "r9d": "r9"}
    for ref in idautils.XrefsTo(consumer):
        if cancelled():
            return {"tables": list(tables.values()), "unresolved_call_sites": unresolved,
                    "call_sites_seen": count, "cancelled": True, "limited": limited}
        func = ida_funcs.get_func(ref.frm)
        if not func or idc.print_insn_mnem(ref.frm).lower() != "call":
            continue
        if idc.get_operand_value(ref.frm, 0) != consumer:
            continue
        if count >= max_call_sites or len(tables) >= max_tables:
            limited = True
            break
        count += 1
        ea, tracked, candidates, operations = ref.frm, "rdi", [], []
        for _ in range(18):
            ea = ida_bytes.prev_head(ea, func.start_ea)
            if ea == ida_idaapi.BADADDR or ea < func.start_ea:
                break
            mnemonic = idc.print_insn_mnem(ea).lower()
            if mnemonic.startswith("j") or mnemonic in ("call", "ret", "retn"):
                break
            target = idc.print_operand(ea, 0).lower()
            target = aliases.get(target, target)
            if target != tracked:
                continue
            if mnemonic == "or":
                operations.append({"address": ea, "operation": "OR in address construction; low-bit effects not proven"})
                continue
            source = idc.print_operand(ea, 1).lower()
            source = aliases.get(source, source)
            if mnemonic == "mov" and source in ("rax", "rbx", "rcx", "rdx", "rsi", "rdi", "r12", "r13", "r14", "r15"):
                tracked = source
                continue
            if mnemonic in ("lea", "mov"):
                for data in idautils.DataRefsFrom(ea):
                    candidates.append((data, ea))
                if not candidates and idc.get_operand_type(ea, 1) == idc.o_imm:
                    candidates.append((idc.get_operand_value(ea, 1) & 0x7fffffffffffffff, ea))
            break
        found = False
        for base, evidence_ea in candidates:
            seg = ida_segment.getseg(base)
            if not seg or seg.perm & ida_segment.SEGPERM_EXEC:
                continue
            rows, errors, partial = registration_roots(memory, [{"address": base}], sentinel,
                                                       max_entries=max_entries, cancelled=cancelled)
            if errors or partial or not rows:
                continue
            plausible = True
            for row in rows:
                root_seg = ida_segment.getseg(row["root"])
                if not root_seg or root_seg.perm & ida_segment.SEGPERM_EXEC or not ida_segment.getseg(row["link_key"]):
                    plausible = False
                    break
                try:
                    raw = memory.read(row["root"], 40)
                    if not any(raw) or not 1 <= int.from_bytes(raw[16:20], "big") <= 313:
                        plausible = False
                        break
                except MemoryReadError:
                    plausible = False
                    break
            if not plausible:
                continue
            found = True
            if base not in tables:
                owner_names = owners.get(func.start_ea, [])
                tables[base] = {"address": base, "owner_candidate": ", ".join(owner_names) or ida_name.get_name(func.start_ea),
                                "owner_subsystems": list(owner_names),
                                "conditions": ["Caller branch/runtime predicates unresolved; direct argument recovery is a candidate"],
                                "source_call_sites": [], "entry_count": len(rows)}
            tables[base]["source_call_sites"].append({"call": ref.frm, "caller": func.start_ea,
                                                       "argument_reference": evidence_ea,
                                                       "address_operations": operations})
            for owner in owners.get(func.start_ea, []):
                if owner not in tables[base]["owner_subsystems"]:
                    tables[base]["owner_subsystems"].append(owner)
        if not found:
            unresolved.append({"call": ref.frm, "caller": func.start_ea,
                               "reason": "Constant registration argument not established within bounded block scan"})
    return {"tables": sorted(tables.values(), key=lambda t: t["address"]),
            "unresolved_call_sites": unresolved, "call_sites_seen": count,
            "cancelled": False, "limited": limited,
            "consumer": consumer, "sentinel": sentinel}


def extract_static_cli(profile, cancelled=lambda: False):
    from .grammar import extract_profile, address
    profile = dict(profile)
    current = identity()
    if current["input_md5"].lower() != profile.get("input_md5", "").lower():
        raise ValueError("Static CLI profile input MD5 mismatch")
    if "idb_imagebase" in profile and current["imagebase"] != address(profile["idb_imagebase"]):
        raise ValueError("Static CLI profile addresses require a different IDB imagebase")
    discovery = None
    if profile.get("discovery"):
        config = profile["discovery"]
        discovery = discover_registration_tables(address(config["consumer"]), address(profile["sentinel"]),
                                                  max_call_sites=config.get("max_call_sites", 2000),
                                                  max_tables=config.get("max_tables", 1000),
                                                  max_entries=profile.get("max_registration_entries", 128),
                                                  cancelled=cancelled)
        manual = profile.get("registration_tables", [])
        discovered = {address(row["address"]) for row in discovery["tables"]}
        profile["registration_tables"] = discovery["tables"] + [row for row in manual if address(row["address"]) not in discovered]
    result = extract_profile(IDBMemory(), profile, current["input_md5"], cancelled,
                             function_resolver=resolve_function)
    if discovery is not None:
        result["discovery"] = discovery
        result["coverage"]["discovery_limited"] = discovery["limited"]
        result["coverage"]["unresolved_registration_call_sites"] = len(discovery["unresolved_call_sites"])
        if discovery["cancelled"]:
            result["cancelled"] = True
            result["stop_reason"] = "cancelled"
    return result


def section_samples():
    """Raw evidence before assuming module/link share the subsystem schema."""
    rows, memory = [], IDBMemory()
    for seg in segments():
        if not any(key in seg["name"] for key in (
                "subsys_header_section", "module_header_section", "module_link_section")):
            continue
        row = dict(seg)
        row["sample_size"] = min(seg["end"] - seg["address"], 512)
        try:
            raw = memory.read(seg["address"], row["sample_size"])
            row["raw_hex"] = raw.hex()
            row["qwords"] = [{"offset": off, "little": int.from_bytes(raw[off:off + 8], "little"),
                              "big": int.from_bytes(raw[off:off + 8], "big")}
                             for off in range(0, len(raw) - 7, 8)]
        except MemoryReadError as exc:
            row["error"] = str(exc)
        rows.append(row)
    return rows


SOURCE_PATTERN = re.compile(rb"(?:\.\./)?VIEW_ROOT/cisco\.comp/[A-Za-z0-9_./+\-]{1,1500}\.(?:c|cpp|h)(?=\x00)")


def source_candidates(cancelled=lambda: False):
    memory, rows, errors = IDBMemory(), [], []
    # Do not build IDA's million-string index. Scan read-only data in bounded chunks.
    for segment in segments():
        if segment["permissions"] & (ida_segment.SEGPERM_EXEC | ida_segment.SEGPERM_WRITE):
            continue
        for start in range(segment["address"], segment["end"], 65536):
            if cancelled():
                return rows, errors, True
            try:
                data = memory.read(start, min(65536 + 2048, segment["end"] - start))
            except MemoryReadError as exc:
                errors.append({"address": start, "error": str(exc)})
                continue
            for match in SOURCE_PATTERN.finditer(data):
                if match.start() >= 65536:
                    continue
                ea = start + match.start()
                path = match.group().decode("ascii")
                component = path.split("cisco.comp/", 1)[1].split("/", 1)[0]
                rows.append({"address": ea, "path": path, "component_candidate": component,
                             "evidence": "source path literal; not recovered compilation-unit ownership"})
    return rows, errors, False


def referencing_functions(ea, limit=1000):
    rows = []
    for index, ref in enumerate(idautils.XrefsTo(ea)):
        if index >= limit:
            break
        func = ida_funcs.get_func(ref.frm)
        rows.append({"reference": ref.frm, "function": func.start_ea if func else None})
    return rows
