"""Read-only Hex-Rays expression acquisition in short, resumable batches.

Image references are RVAs; raw expressions also keep the capture EA. No target
predicate, registration API or handler is executed. Requires a local decompiler.
"""
import time


def acquire_batch(graph_report, profile, checkpoint=None, audit=None, batch_size=4, seconds=5):
    import ida_nalt, ida_funcs, ida_name, ida_hexrays as hr, idautils, idc
    digest = ida_nalt.retrieve_input_file_md5().hex()
    base = ida_nalt.get_imagebase()
    if digest != profile["input_md5"] or digest != graph_report["identity"]["input_md5"]:
        raise ValueError("Lifecycle input MD5 mismatch")
    if not 1 <= batch_size <= 32 or not 0 < seconds <= 30:
        raise ValueError("Invalid acquisition batch bounds")
    integer = lambda value: int(value, 0) if isinstance(value, str) else int(value)
    apis = {integer(a["rva"]): a for a in profile["apis"]}
    limits = profile.get("limits", {})
    if checkpoint:
        result = checkpoint
        if result["identity"]["input_md5"] != digest or result["identity"]["imagebase"] != base:
            raise ValueError("Checkpoint identity/base changed; begin a fresh capture and merge by RVA offline")
    else:
        old_base = graph_report["identity"]["imagebase"]
        known = {n["handler_candidate"] - old_base for n in graph_report["graph"]["nodes"] if n.get("handler_candidate")}
        result = {"schema_version": 1, "identity": {**graph_report["identity"], "imagebase": base},
                  "functions": [], "api_xrefs": [], "noncall_api_refs": [], "call_edges": [],
                  "pending_functions": [], "xref_limits": [], "getter_xrefs_inspected": [],
                  "coverage": {"scope": "API direct references plus prioritized CLI ancestry and small getter/callback followups", "runtime_read": False}}
        if audit:
            if audit["identity"]["input_md5"] != digest:
                raise ValueError("Ancestry input identity mismatch")
            audit_base = audit["identity"]["imagebase"]
            result["call_edges"] = [{"caller": e["caller"] - audit_base, "callee": e["callee"] - audit_base,
                                     "site_rva": e["callsite"] - audit_base} for e in audit.get("call_edges", [])]
        seed_callers = []
        for api in apis:
            count = 0
            for ref in idautils.XrefsTo(base + api):
                function = ida_funcs.get_func(ref.frm)
                if not function:
                    continue
                if count >= limits.get("max_xrefs_per_api", 5000):
                    result["xref_limits"].append({"target_rva": api, "reason": "API reference bound"})
                    break
                count += 1
                row = {"caller": function.start_ea - base, "callee": api, "site_rva": ref.frm - base}
                if idc.print_insn_mnem(ref.frm).lower() in ("call", "jmp") and idc.get_operand_value(ref.frm, 0) == base + api:
                    result["api_xrefs"].append(row)
                    seed_callers.append(row["caller"])
                else:
                    result["noncall_api_refs"].append(row)
        result["call_edges"].extend(result["api_xrefs"])
        reverse = {}
        for edge in result["call_edges"]:
            reverse.setdefault(edge["callee"], []).append(edge["caller"])
        reg_seeds = {site["caller"] - old_base for row in graph_report["graph"]["registrations"]
                     for site in row.get("source_call_sites", [])}
        found, ancestry_seen = set(), set()
        ancestry = [(seed, 0) for seed in reg_seeds]
        for current, depth in ancestry:
            if current in ancestry_seen:
                continue
            ancestry_seen.add(current)
            if current in known:
                found.add(current)
            elif depth < 4:
                ancestry.extend((caller, depth + 1) for caller in reverse.get(current, []))
        trigger_handlers = sorted(found)
        adjacency = {}
        for edge in result["call_edges"]:
            adjacency.setdefault(edge["caller"], []).append(edge["callee"])
        priority, pending = list(trigger_handlers), [(h, 0) for h in trigger_handlers]
        seen = set(priority)
        for current, depth in pending:
            if depth >= 4:
                continue
            for target in adjacency.get(current, []):
                if target not in seen and target not in apis:
                    seen.add(target)
                    priority.append(target)
                    pending.append((target, depth + 1))
        result["pending_functions"] = list(dict.fromkeys(priority + seed_callers))
    pending = result["pending_functions"]
    acquired = {f["rva"] for f in result["functions"]}
    queued = set(pending) | acquired
    inspected = set(result["getter_xrefs_inspected"])
    deadline, completed = time.monotonic() + seconds, 0
    assignment_ops={getattr(hr,name):operation for name,operation in
                    (("cot_asg","assign"),("cot_asgbor","or"),("cot_asgband","and"),("cot_asgxor","xor"),
                     ("cot_asgadd","add"),("cot_asgsub","sub"),("cot_asgmul","mul")) if hasattr(hr,name)}

    def enqueue(rva):
        if rva not in queued and rva not in apis and len(queued) < 20000:
            queued.add(rva)
            pending.append(rva)

    def serialize(expr, depth=0):
        if expr is None or depth > 7 or time.monotonic() >= deadline:
            return {"kind": "unknown", "reason": "expression nesting bound"}
        op = expr.op
        if op == hr.cot_num:
            return {"kind": "number", "value": int(expr.numval())}
        if op == hr.cot_obj:
            ea = int(expr.obj_ea)
            function = ida_funcs.get_func(ea)
            return {"kind": "global", "ea": ea, "rva": ea - base,
                    "name": ida_name.get_name(ea), "is_function": bool(function and function.start_ea == ea)}
        if op == hr.cot_var:
            return {"kind": "var", "index": int(expr.v.idx)}
        if op == hr.cot_helper:
            return {"kind": "helper", "name": str(expr.helper)}
        if op == hr.cot_call:
            target = int(expr.x.obj_ea) - base if expr.x.op == hr.cot_obj else None
            return {"kind": "call", "target": target, "target_expression": serialize(expr.x, depth + 1),
                    "args": [serialize(a, depth + 1) for a in expr.a]}
        unary = {hr.cot_ref: "ref", hr.cot_ptr: "deref", hr.cot_cast: "cast", hr.cot_lnot: "not",
                 hr.cot_bnot: "bit_not", hr.cot_neg: "neg"}
        if op in unary:
            row = {"kind": unary[op], "arg": serialize(expr.x, depth + 1)}
            if op == hr.cot_ptr:
                row["width"] = int(expr.ptrsize)
            return row
        if op in (hr.cot_memptr, hr.cot_memref):
            return {"kind": "member", "base": serialize(expr.x, depth + 1), "offset": int(expr.m),
                    "pointer": op == hr.cot_memptr}
        operators = {"cot_add": "add", "cot_sub": "sub", "cot_band": "and", "cot_bor": "or", "cot_xor": "xor",
                     "cot_mul": "mul", "cot_eq": "eq", "cot_ne": "ne", "cot_sge": "ge", "cot_uge": "ge",
                     "cot_sle": "le", "cot_ule": "le", "cot_sgt": "gt", "cot_ugt": "gt", "cot_slt": "lt", "cot_ult": "lt",
                     "cot_land": "logical_and", "cot_lor": "logical_or", "cot_shl": "shl", "cot_ushr": "shr", "cot_sshr": "shr"}
        names = {getattr(hr, name): value for name, value in operators.items() if hasattr(hr, name)}
        if op in names:
            return {"kind": "binary", "op": names[op], "left": serialize(expr.x, depth + 1), "right": serialize(expr.y, depth + 1)}
        return {"kind": "unknown", "op": int(op), "reason": "unsupported expression; source function retained"}

    def specific(item):
        value = getattr(item, "to_specific_type", item)
        return value() if callable(value) else value

    class Visitor(hr.ctree_visitor_t):
        def __init__(self):
            hr.ctree_visitor_t.__init__(self, hr.CV_PARENTS)
            self.events, self.order, self.truncated = [], 0, False

        def guards(self):
            rows = []
            try:
                parents = [specific(p) for p in self.parents]
                for index, parent in enumerate(parents):
                    if parent.op == hr.cit_if:
                        branch = "unresolved"
                        if index + 1 < len(parents):
                            child = parents[index + 1]
                            if parent.cif.ithen and child.index == parent.cif.ithen.index:
                                branch = "then"
                            elif parent.cif.ielse and child.index == parent.cif.ielse.index:
                                branch = "else"
                        rows.append({"kind": "if", "expression": serialize(parent.cif.expr), "branch": branch, "evaluated": False})
                    elif parent.op == hr.cit_switch:
                        rows.append({"kind": "switch", "expression": serialize(parent.cswitch.expr),
                                     "case": "unresolved", "evaluated": False})
                    elif parent.op in (hr.cit_for, hr.cit_while, hr.cit_do):
                        rows.append({"kind": "loop_ancestor", "op": int(parent.op), "evaluated": False})
            except Exception as exc:
                rows.append({"kind": "unknown_guard", "reason": str(exc), "evaluated": False})
            return rows

        def visit_expr(self, expr):
            self.order += 1
            if self.order > limits.get("max_expressions_per_function", 2000) or time.monotonic() >= deadline:
                self.truncated = True
                return 1
            common = {"order": self.order, "site_rva": None if expr.ea == idc.BADADDR else int(expr.ea) - base,
                      "guards": self.guards()}
            if expr.op == hr.cot_call and expr.x.op != hr.cot_helper:
                self.events.append({**common, **serialize(expr)})
            elif expr.op in assignment_ops:
                operation=assignment_ops[expr.op]
                rhs=serialize(expr.y) if operation=="assign" else {"kind":"binary","op":operation,"left":serialize(expr.x),"right":serialize(expr.y)}
                self.events.append({**common, "kind": "assignment", "left": serialize(expr.x), "right": rhs,"operation":operation})
            elif expr.op == hr.cot_obj:
                row = serialize(expr)
                if row["is_function"]:
                    return 0
                parent = specific(self.parents.back()) if self.parents.size() else None
                if parent and parent.op == hr.cot_ref:
                    return 0
                write = bool(parent and parent.op in assignment_ops and parent.x.index == expr.index)
                parents = [specific(p) for p in self.parents]
                in_condition = any(p.op == hr.cit_if and
                                   (parents[i+1] if i+1<len(parents) else expr).index == p.cif.expr.index
                                   for i,p in enumerate(parents))
                self.events.append({**common, "kind": "global_access", "global_rva": row["rva"], "name": row["name"],
                                    "access": "write" if write else "read", "in_guard": in_condition,
                                    "value_expression": serialize(parent.y) if write else None})
                if write and assignment_ops[parent.op] != "assign":
                    self.events.append({**common,"kind":"global_access","global_rva":row["rva"],"name":row["name"],
                                        "access":"read","in_guard":False,"compound_update":True})
            return 0

    while pending and completed < batch_size and time.monotonic() < deadline:
        rva = pending.pop(0)
        if rva in acquired:
            continue
        acquired.add(rva)
        function = ida_funcs.get_func(base + rva)
        row = {"rva": rva, "capture_ea": base + rva, "name": ida_name.get_name(base + rva), "events": [],
               "path_conditions_complete": False, "evidence_source": "hexrays_ctree"}
        try:
            if not function or function.start_ea != base + rva:
                raise ValueError("Not a current IDA function entry")
            count = sum(1 for _ in idautils.FuncItems(function.start_ea))
            if count > limits.get("max_function_instructions", 12000):
                raise ValueError("Function instruction bound; decompilation skipped")
            cfunc = hr.decompile(function.start_ea)
            if cfunc is None:
                raise ValueError("Decompiler unavailable for this function")
            visitor = Visitor()
            row["code"] = str(cfunc)
            visitor.apply_to(cfunc.body, None)
            row.update(events=visitor.events, truncated=visitor.truncated, code=str(cfunc),
                       argument_variables=[int(index) for index in cfunc.argidx])
            # Small no-argument call targets are getter candidates. Inspect
            # their direct users to find pointer stores outside CLI handlers.
            for event in visitor.events:
                if event["kind"] != "call" or event.get("target") is None or event.get("args"):
                    continue
                target = event["target"]
                getter = ida_funcs.get_func(base + target)
                if not getter or getter.start_ea != base + target or getter.end_ea - getter.start_ea > 160 or target in inspected:
                    continue
                inspected.add(target)
                enqueue(target)
                users = 0
                for ref in idautils.XrefsTo(base + target):
                    owner = ida_funcs.get_func(ref.frm)
                    if not owner or idc.print_insn_mnem(ref.frm).lower() not in ("call", "jmp"):
                        continue
                    users += 1
                    if users > 64:
                        result["xref_limits"].append({"target_rva": target, "reason": "getter user reference bound"})
                        break
                    enqueue(owner.start_ea - base)
        except Exception as exc:
            row["error"] = str(exc)
        result["functions"].append(row)
        completed += 1
    if ida_nalt.get_imagebase() != base or ida_nalt.retrieve_input_file_md5().hex() != digest:
        raise ValueError("Identity/base changed during acquisition; batch not committed")
    result["getter_xrefs_inspected"] = sorted(inspected)
    result["coverage"].update(acquired_functions=len(result["functions"]), pending_functions=len(pending),
                              xref_limits=result["xref_limits"], last_batch_functions=completed,
                              stop_reason="pending_functions_retained" if pending else "exhausted_acquired_worklist",
                              conditions_complete=False, individual_decompilation_may_exceed_batch_deadline=True)
    return result
