"""Run with IDA 9.1 File > Script file. Static reads only; no debugger/core.

Saves per-step outcomes and raw candidates in reports/. Does not save the IDB.
"""
import builtins
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Use freshly edited code, same development-session restriction as dev_load.py.
previous = getattr(builtins, "_iosd_helper_dev", None)
if previous is not None:
    previous.close()
    del builtins._iosd_helper_dev
for module_name in list(sys.modules):
    if module_name == "iosd_helper" or module_name.startswith("iosd_helper."):
        del sys.modules[module_name]

import ida_auto
import ida_funcs
import ida_kernwin as kw
from iosd_helper import __version__
from iosd_helper.ida_adapter import (identity, segments, IDBMemory, named_locators,
                                      source_candidates, symbol_candidates, anchor_candidates, section_samples, module_metadata)
from iosd_helper.structures import scan_subsystems
from iosd_helper.ui import Application


def run():
    output_dir = ROOT / "reports"
    output_dir.mkdir(exist_ok=True)
    report_path = output_dir / ("static-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    ident = identity()
    report = {"plugin_version": __version__, "identity": ident,
              "started_utc": datetime.now(timezone.utc).isoformat(),
              "mode": "static-idb-only", "auto_state": ida_auto.get_auto_state(),
              "function_count": ida_funcs.get_func_qty(), "steps": []}
    if not ident["ida_version"].startswith("9.1"):
        report["version_note"] = "Requested IDA 9.1; actual version differs, see identity"
    stopped = False

    def save():
        with report_path.open("w", encoding="utf-8") as stream:
            json.dump(report, stream, ensure_ascii=False, indent=2)

    def step(name, operation):
        nonlocal stopped
        if stopped:
            report["steps"].append({"name": name, "status": "skipped_after_cancel"})
            save()
            return
        kw.msg("[iosd-helper] static test: %s\n" % name)
        kw.replace_wait_box("iosd-helper static test: %s\nCancel keeps partial results" % name)
        started = time.monotonic()
        row = {"name": name}
        try:
            result = operation()
            row["result"] = result
            cancelled = isinstance(result, dict) and result.get("cancelled", False)
            row["status"] = "cancelled" if cancelled else "completed"
            # Completed means the operation ran; empty hits are not semantic success.
            stopped = cancelled
        except Exception:
            row["status"] = "error"
            row["traceback"] = traceback.format_exc()
            kw.msg(row["traceback"] + "\n")
        row["seconds"] = round(time.monotonic() - started, 3)
        report["steps"].append(row)
        save()

    def scan(operation):
        rows, errors, partial = operation(kw.user_cancelled)
        return {"count": len(rows), "rows": rows, "read_errors": errors, "cancelled": partial}

    def classify_names():
        rows, partial = symbol_candidates(kw.user_cancelled)
        return {"count": len(rows), "rows": rows, "cancelled": partial}

    def subsystem_sections():
        sections = [s for s in segments() if "subsys_header_section" in s["name"]]
        runs = []
        for section in sections:
            for mode in ("little", "big", "mask_then_swap", "swap_then_mask"):
                if kw.user_cancelled():
                    return {"sections": sections, "runs": runs, "cancelled": True}
                kw.replace_wait_box("iosd-helper: %s [%s]\nCancel keeps partial results" % (section["name"], mode))
                rows, errors, partial = scan_subsystems(IDBMemory(), section["address"],
                                                       section["end"], mode, kw.user_cancelled)
                runs.append({"section": section["name"], "pointer_mode": mode,
                             "count": len(rows), "rows": rows, "read_error_count": len(errors),
                             "first_read_errors": errors[:20]})
                if partial:
                    return {"sections": sections, "runs": runs, "cancelled": True}
        return {"sections": sections, "runs": runs,
                "note": "No hits is inconclusive: section naming, relocations, pointer encoding or layout may differ"}

    save()
    kw.show_wait_box("iosd-helper static test\nCancel preserves the report and skips remaining scans")
    try:
        step("segments", lambda: {"rows": segments()})
        step("named_locators", lambda: {"rows": named_locators()})
        step("section_raw_samples", lambda: {"rows": section_samples()})
        step("module_metadata", lambda: module_metadata(kw.user_cancelled))
        step("symbol_classification", classify_names)
        step("subsystem_candidates_all_encodings", subsystem_sections)
        step("source_path_candidates", lambda: scan(source_candidates))
        step("string_anchor_candidates", lambda: scan(anchor_candidates))
    finally:
        kw.hide_wait_box()
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        save()
    app = Application()
    builtins._iosd_helper_dev = app
    # Expose report for inspection without re-running the scans.
    builtins._iosd_helper_static_report = report
    app.last = report
    rows = report["steps"]
    app.table("Static test summary", [("Step", 45), ("Status", 25), ("Seconds", 12)],
              [[r["name"], r["status"], r.get("seconds", "-")] for r in rows],
              lambda n: kw.msg(json.dumps({k: v for k, v in rows[n].items() if k != "result"}, ensure_ascii=False, indent=2) + "\n"))
    kw.msg("[iosd-helper] Static report saved: %s\n" % report_path)
    kw.msg("[iosd-helper] completed = scan ran, not proof that candidate semantics are correct.\n")
    return report_path


if __name__ == "__main__":
    run()
