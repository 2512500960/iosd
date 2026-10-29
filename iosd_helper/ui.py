"""Native IDA choosers: no third-party Qt or MCP dependency."""
from contextlib import contextmanager
from dataclasses import asdict
import json
import traceback

import ida_idaapi
import ida_kernwin as kw
import ida_segment

from . import __version__
from .ida_adapter import (IDBMemory, DebugMemory, identity, segments,
                          source_candidates, symbol_candidates, referencing_functions,
                          named_locators, anchor_candidates, module_metadata, extract_static_cli)
from .memory import AddressMap, ElfCoreMemory, decode_pointer
from .structures import NodeLayout, scan_subsystems, walk_nodes
from .grammar import extract_profile, to_dot
from .catalogue import catalogue_rows, catalogue_html
from .syntax_paths import recover_paths
from .syntax_view import syntax_html
from .candidate_space import build_candidate_space, candidate_space_html
from .addressing import ImageCoordinates
from .lifecycle import analyze_lifecycle, lifecycle_html
from .runtime_linkage import capture_runtime_linkage
from .project_ui import ProjectBrowser
from .integer_ui import IntegerDisplaySession
from .protocol_ui import ProtocolBrowser


class Cancelled(Exception):
    pass


def prompt(text, default=""):
    value = kw.ask_str(default, 0, text)
    if value is None:
        raise Cancelled()
    return value


def number(text, default=0):
    return int(prompt(text + " (0x... or decimal)", hex(default)), 0)


@contextmanager
def progress(text):
    kw.show_wait_box(text + "\nPress Cancel to keep partial results.")
    try:
        yield kw.user_cancelled
    finally:
        kw.hide_wait_box()


class Table(kw.Choose):
    def __init__(self, title, columns, rows, select=None):
        super().__init__(title, [[name, width] for name, width in columns])
        self.rows, self.select = rows, select

    def OnGetSize(self):
        return len(self.rows)

    def OnGetLine(self, n):
        return [str(value) for value in self.rows[n]]

    def OnSelectLine(self, n):
        if self.select:
            self.select(n)
        return (self.NOTHING_CHANGED,)


class Application:
    def __init__(self):
        self.tables = []
        self.core = None
        self.source = "idb"
        self.mapping = None
        self.mapping_verified = False
        self.mapping_identity = None
        self.last = None
        self.counter = 0
        self.graphs = []
        self.last_grammar = None
        self.last_paths = None
        self.last_candidates = None
        self.last_lifecycle = None
        self.project_browser = ProjectBrowser(self)
        self.architecture_model = None
        self.protocol_browser = ProtocolBrowser(self)
        self.integer_display = None
        try:
            self.integer_display = IntegerDisplaySession()
        except Exception as exc:
            kw.msg('[iosd-helper] Integer display unavailable: %s\n' % exc)

    def close(self):
        if self.integer_display:
            self.integer_display.close()
            self.integer_display = None
        self.project_browser.close()
        for graph in self.graphs:
            graph.Close()
        self.graphs.clear()
        for table in self.tables:
            table.Close()
        self.tables.clear()
        if self.core:
            self.core.close()
            self.core = None

    def guard(self, operation):
        try:
            operation()
        except Cancelled:
            pass
        except Exception as exc:
            kw.msg("[iosd-helper] " + traceback.format_exc() + "\n")
            kw.warning("iosd-helper: %s" % exc)

    def table(self, label, columns, rows, select=None):
        self.counter += 1
        table = Table("iosd-helper | %s #%d" % (label, self.counter), columns, rows, select)
        self.tables.append(table)
        table.Show(False)

    def save_result(self, kind, **data):
        self.last = {"schema_version": 1, "plugin_version": __version__, "kind": kind,
                     "identity": identity(), **data}
        kw.msg("[iosd-helper] %s ready; export via main menu.\n" % kind)

    def menu(self):
        options = [("Architecture: browse saved subsystem/module organization map", self.architecture_map),
                   ("Protocols: investigate packet handling (clues / calls / unknown callbacks)", self.protocol_browser.find),
                   ("Integer display: use context menu in disassembly / pseudocode", self.show_integer_display),
                   ("Project: create from saved runtime export", self.project_browser.create),
                   ("Project: open existing analysis project", self.project_browser.open),
                   ("Project: browse/search candidates, conditions and unknown evidence", self.project_browser.browse),
                   ("Project: start/resume local evidence index", self.project_browser.start),
                   ("Project: task status / progress", self.project_browser.status),
                   ("Project: cancel indexing (keep checkpoint)", self.project_browser.cancel),
                   ("Binary overview / segments", self.overview),
                   ("Subsystem candidates (IDB)", self.subsystems),
                   ("Module headers / links (IDB)", self.modules),
                   ("Source path candidates (IDB)", self.sources),
                   ("Message / model / parser names (IDB)", self.symbols),
                   ("Static locators: known IDA names", self.locators),
                   ("Static locators: log strings + direct xrefs", self.anchors),
                   ("Static CLI graph (experimental profile)", self.static_grammar),
                   ("Browse last static CLI catalogue: keywords / EOL / actions", self.cli_catalogue),
                   ("Recover config / config-if syntax paths (experimental)", self.recover_syntax),
                   ("Build acquired candidate pool (keep unknown / unbound definitions)", self.build_pool),
                   ("Export last candidate pool as searchable HTML", self.export_pool),
                   ("Analyze saved registration / state evidence (RVA, no decompilation)", self.lifecycle_analysis),
                   ("Export last registration / state analysis as HTML", self.export_lifecycle),
                   ("Export last syntax paths as searchable HTML", self.export_syntax),
                   ("Export last static CLI catalogue as searchable HTML", self.export_catalogue),
                   ("Export last static CLI graph as DOT", self.export_grammar),
                   ("Select memory source: IDB / debugger / ELF core", self.select_source),
                   ("Set runtime address mapping + verify bytes", self.set_mapping),
                   ("Read runtime dynamic linkage / pending bindings (verified mapping)", self.runtime_linkage),
                   ("Read memory / decode pointer", self.probe),
                   ("Inspect / traverse candidate ICM nodes", self.nodes),
                   ("Export last result as JSON", self.export)]
        chooser = Table("iosd-helper %s | source=%s" % (__version__, self.source),
                        [("Action", 75)], [[label] for label, _ in options])
        selected = chooser.Show(True)
        if selected >= 0:
            self.guard(options[selected][1])

    def show_integer_display(self):
        if not self.integer_display:
            raise ValueError('Integer formats failed to register; see Output log')
        kw.info('Place the cursor on an integer in a disassembly/data or Hex-Rays view.\n'
                'Right-click > iosd Helper > Integer display / BE interpretation...\n'
                'Bytes and ctree semantics are unchanged. Hex-Rays replaces the printed literal only.\n'
                'Rules are saved in this IDB and reapplied after F5 when uniquely matched.')

    def architecture_map(self):
        path = kw.ask_file(False, "architecture.json", "Open saved iosd initialization organization map")
        if not path:
            return
        with open(path, encoding="utf-8") as stream:
            model = json.load(stream)
        if model.get("kind") != "iosd_architecture_map" or model.get("schema_version") != 1 or model.get("address_space") != "rva":
            raise ValueError("Unsupported architecture map")
        def check():
            current = identity()
            if current["input_md5"].lower() != model["input_md5"].lower():
                raise ValueError("Architecture map belongs to a different binary")
            return current
        check()
        self.architecture_model = model
        def browse(label, rows, fields, jump_field):
            def select(index):
                current = check()
                rva = rows[index].get(jump_field)
                self.evidence(rows[index], current["imagebase"] + rva if rva is not None else None)
            self.table(label, [(field, 38) for field in fields],
                       [[hex(row[field]) if field.endswith("_rva") and row.get(field) is not None else row.get(field, "")
                         for field in fields] for row in rows], lambda index: self.guard(lambda: select(index)))
        def categories():
            rows = model["categories"]
            def select(index):
                check()
                browse(rows[index]["name"] + " subsystem candidates",
                       [r for r in model["subsystems"] if r["category_id"] == rows[index]["id"]],
                       ["name", "category", "record_rva", "init_rva", "status"], "init_rva")
            self.table("Subsystem categories (not module groups)", [("Category", 35), ("Candidate records", 20)],
                       [[r["name"],r["candidate_records"]] for r in rows], lambda index:self.guard(lambda:select(index)))
        views = [("Subsystem categories / 子系统类别", categories),
                 ("All subsystem candidates / 全部候选实体", lambda:browse("Subsystem candidates",model["subsystems"],
                    ["name","category","record_rva","init_rva","status"],"init_rva")),
                 ("Module groups and callbacks / 模块分组与回调节点", lambda:browse("Module nodes",model["modules"],
                    ["name","kind","record_rva","init_rva","second_callback_rva"],"record_rva")),
                 ("Module dependencies and membership / 模块依赖与分组", lambda:browse("Module links",model["module_links"],
                    ["a","relation","b","record_rva"],"record_rva")),
                 ("Scope and evidence / 范围与原始证据", lambda:self.evidence({k:v for k,v in model.items() if k not in ("subsystems","modules","module_links")}))]
        self.table("iosd initialization organization (two mechanisms)", [("View", 90)], [[label] for label,_ in views],
                   lambda index:self.guard(views[index][1]))

    def memory(self):
        if self.source != "idb" and self.mapping_verified:
            self.check_mapping_identity()
        if self.source == "core":
            if not self.core:
                raise ValueError("Select an ELF core first")
            return self.core
        if self.source == "debugger":
            return DebugMemory()
        return IDBMemory()

    def check_mapping_identity(self):
        current = identity()
        if self.mapping_identity is None or any(current.get(k) != self.mapping_identity.get(k) for k in ("input_md5","imagebase")):
            self.mapping, self.mapping_verified, self.mapping_identity = None, False, None
            raise ValueError("Input/imagebase changed; establish and verify address mapping again")

    def lifecycle_analysis(self):
        def load(title):
            path = kw.ask_file(False,"*.json",title)
            if not path:raise Cancelled()
            with open(path,encoding="utf-8") as stream:return json.load(stream)
        capture = load("Open saved lifecycle expression evidence / offline capture")
        graph = load("Open saved static CLI graph (capture identity retained)")
        profile = load("Open lifecycle API profile (RVA)")
        if identity()["input_md5"] != profile["input_md5"]:
            raise ValueError("Current input does not match lifecycle profile")
        paths = self.last_paths["paths"] if self.last_paths and graph["identity"]["imagebase"] == identity()["imagebase"] else []
        result = analyze_lifecycle(capture,graph,profile,paths)
        self.last_lifecycle = result
        self.save_result("registration_state_candidates",result=result)
        rows = result["trigger_candidates"]
        def select(index):
            current = identity()
            ea = current["imagebase"] + rows[index]["handler"] if current["input_md5"] == result["identity"]["input_md5"] else None
            self.evidence(rows[index],ea)
        self.table("Registration trigger groups (RVA; selector unresolved retained)",
                   [("Handler RVA",18),("Caller RVA",18),("Command definitions",18),("Condition status",55)],
                   [[hex(r["handler"]),hex(r["registration"]["caller"]),len(r["commands"]),r["status"]] for r in rows],select)

    def export_lifecycle(self):
        if self.last_lifecycle is None:raise ValueError("Analyze saved lifecycle evidence first")
        path = kw.ask_file(True,"iosd-registration-state.html","Export conditional evidence and unknown items")
        if path:
            with open(path,"w",encoding="utf-8") as stream:stream.write(lifecycle_html(self.last_lifecycle))

    def runtime_linkage(self):
        if self.source == "idb" or not self.mapping_verified or self.mapping is None:
            raise ValueError("Choose debugger/core, then establish and verify the current address mapping")
        self.check_mapping_identity()
        path = kw.ask_file(False,"*.json","Open lifecycle API/runtime layout profile (RVA)")
        if not path:return
        with open(path,encoding="utf-8") as stream:profile=json.load(stream)
        current = identity()
        if current["input_md5"] != profile["input_md5"]:raise ValueError("Runtime profile input mismatch")
        coords=ImageCoordinates(current["input_md5"],current["imagebase"],current["imagebase"],self.mapping.to_runtime(current["imagebase"]))
        ranges=[(s["address"]-current["imagebase"],s["end"]-current["imagebase"]) for s in segments()]
        specs=[{**s,"head_rva":int(s["head_rva"],0) if isinstance(s["head_rva"],str) else s["head_rva"]} for s in profile["runtime"]["lists"]]
        states=[{**s,"rva":int(s["rva"],0) if isinstance(s["rva"],str) else s["rva"]} for s in profile["runtime"].get("states",[])]
        limit=number("Maximum records per runtime list (1..10000)",128)
        result=capture_runtime_linkage(self.memory(),coords,ranges,specs,states,limit,self.check_mapping_identity)
        self.save_result("runtime_registration_snapshot",result=result)
        kw.msg("[iosd-helper] Runtime lists: "+json.dumps([{k:v for k,v in r.items() if k!="nodes"} for r in result["lists"]])+"\n")

    def overview(self):
        rows = segments()
        self.save_result("overview", segments=rows)
        kw.msg("[iosd-helper] " + json.dumps(identity(), ensure_ascii=False) + "\n")
        self.table("Segments", [("Start", 18), ("End", 18), ("Name", 45), ("Perm", 8)],
                   [[hex(r["address"]), hex(r["end"]), r["name"], r["permissions"]] for r in rows],
                   lambda n: kw.jumpto(rows[n]["address"]))

    def subsystems(self):
        selected = [s for s in segments() if "subsys_header_section" in s["name"]]
        if not selected:
            start = number("Section start (IDA address)", kw.get_screen_ea())
            end = number("Section end, exclusive (IDA address)", start + 0x1000)
            if end <= start:
                raise ValueError("End must be greater than start")
            selected = [{"address": start, "end": end, "name": "manual"}]
        mode = prompt("Pointer encoding: little / big / mask_then_swap / swap_then_mask", "little")
        decode_pointer(bytes(8), mode)
        rows, errors, partial = [], [], False
        with progress("Scanning double-magic subsystem candidates") as cancelled:
            for seg in selected:
                found, faults, stopped = scan_subsystems(IDBMemory(), seg["address"], seg["end"], mode, cancelled)
                for row in found:
                    row["section"] = seg["name"]
                rows.extend(found)
                errors.extend(faults)
                if stopped:
                    partial = True
                    break
        self.save_result("subsystem_candidates", rows=rows, errors=errors, cancelled=partial,
                         pointer_mode=mode, sections=selected)
        self.table("Subsystem candidates", [("Header", 18), ("Name", 40), ("Init?", 18), ("Section", 30)],
                   [[hex(r["address"]), r["name"], hex(r["init_candidate"]), r["section"]] for r in rows],
                   lambda n: self.evidence(rows[n], rows[n]["address"]))

    def sources(self):
        with progress("Scanning read-only data for source paths") as cancelled:
            rows, errors, partial = source_candidates(cancelled)
        self.save_result("source_path_candidates", rows=rows, errors=errors, cancelled=partial)
        def select(n):
            kw.jumpto(rows[n]["address"])
            kw.msg("[iosd-helper] Direct XrefsTo: " + json.dumps(referencing_functions(rows[n]["address"])) + "\n")
        self.table("Source paths", [("Address", 18), ("Component?", 30), ("Path", 100)],
                   [[hex(r["address"]), r["component_candidate"], r["path"]] for r in rows], select)

    def modules(self):
        with progress("Reading module/header signatures independently of subsystems") as cancelled:
            result = module_metadata(cancelled)
        self.save_result("module_metadata", result=result)
        headers, links = result["headers"], result["links"]
        self.table("Module headers", [("Address", 18), ("Name candidate", 65), ("Field +10?", 18), ("Field +18?", 18)],
                   [[hex(r["address"]), r["name"], hex(r["field_10_candidate"]), hex(r["field_18_candidate"])] for r in headers],
                   lambda n: self.evidence(headers[n], headers[n]["address"]))
        self.table("Module links (direction unresolved)", [("Address", 18), ("Tag", 12), ("Endpoint A", 45), ("Endpoint B", 45)],
                   [[hex(r["address"]), hex(r["tag"]), r["endpoint_a_name"] or hex(r["endpoint_a"]),
                     r["endpoint_b_name"] or hex(r["endpoint_b"])] for r in links],
                   lambda n: self.evidence(links[n], links[n]["address"]))
        kw.msg("[iosd-helper] module headers=%d links=%d errors=%d\n" % (len(headers), len(links), len(result["errors"])))

    def symbols(self):
        with progress("Classifying existing IDA names") as cancelled:
            rows, partial = symbol_candidates(cancelled)
        self.save_result("symbol_candidates", rows=rows, cancelled=partial)
        self.table("Symbol candidates", [("Address", 18), ("Kind", 40), ("Name", 90)],
                   [[hex(r["address"]), r["kind"], r["name"]] for r in rows],
                   lambda n: kw.jumpto(rows[n]["address"]))

    def locators(self):
        rows = named_locators()
        self.save_result("named_locators", rows=rows)
        self.table("Known names", [("Name", 50), ("Address", 18), ("Status", 25)],
                   [[r["name"], hex(r["address"]) if r["address"] is not None else "-", r["status"]] for r in rows],
                   lambda n: self.evidence(rows[n], rows[n]["address"]))

    def static_grammar(self):
        from pathlib import Path
        from .graph_view import StaticParserGraph
        default = Path(__file__).resolve().parents[1] / "profiles" / "static_cli_flow_26_01_02.json"
        path = kw.ask_file(False, str(default), "Choose input-hash-pinned static grammar profile")
        if not path:
            return
        with open(path, encoding="utf-8") as stream:
            profile = json.load(stream)
        with progress("Extracting partial static parser graph; unknown operations stay unresolved") as cancelled:
            graph = extract_static_cli(profile, cancelled)
        self.last_grammar = graph
        self.last_paths = None
        self.last_candidates = None
        self.save_result("static_cli_graph", graph=graph)
        self.counter += 1
        view_graph = graph
        suffix = ""
        if len(graph["nodes"]) > 400:
            view_graph = dict(graph)
            view_graph["nodes"] = graph["nodes"][:400]
            visible = {row["address"] for row in view_graph["nodes"]}
            view_graph["edges"] = [edge for edge in graph["edges"] if edge["source"] in visible]
            suffix = " (first 400 of %d)" % len(graph["nodes"])
        viewer = StaticParserGraph("iosd-helper | Partial static CLI graph #%d%s" % (self.counter, suffix),
                                   view_graph, self.evidence)
        self.graphs.append(viewer)
        if not viewer.Show():
            kw.msg("[iosd-helper] Native graph view unavailable; node table and JSON remain usable.\n")
        rows = graph["nodes"]
        self.table("Static parser nodes", [("Address", 18), ("Action", 35), ("Token / parameter", 45), ("Handler?", 18), ("Status / gap", 65)],
                   [[hex(r["address"]), r.get("action_name", r.get("opcode", "?")), r.get("display_label", ""),
                     hex(r["handler_candidate"]) if r.get("handler_candidate") else "-",
                     r.get("semantic_error", r.get("reason", r["status"]))] for r in rows],
                   lambda n: self.evidence(rows[n], rows[n]["address"]))
        registrations = graph["registrations"]
        selected_roots = set(graph.get("selected_roots", []))
        self.table("Static registrations (not command count)", [("Record", 18), ("Link key", 18), ("Root", 18), ("Owner?", 50), ("Selected", 10)],
                   [[hex(r["address"]), hex(r["link_key"]), hex(r["root"]), r.get("owner_candidate", ""),
                     "yes" if r["root"] in selected_roots else "no"] for r in registrations],
                   lambda n: self.evidence(registrations[n], registrations[n]["address"]))
        kw.msg("[iosd-helper] Partial graph: %d registrations, %d nodes, %d edges; %s\n" %
               (len(graph["registrations"]), len(rows), len(graph["edges"]), graph["stop_reason"]))
        kw.msg("[iosd-helper] Summary: " + json.dumps(graph.get("summary", {})) + "\n")
        kw.msg("[iosd-helper] Coverage: " + json.dumps(graph.get("coverage", {})) + "\n")
        kw.msg("[iosd-helper] Use Browse last static CLI catalogue for keywords / EOL / action tables.\n")

    def cli_catalogue(self):
        if self.last_grammar is None:
            raise ValueError("Extract a static CLI graph first")
        tables = catalogue_rows(self.last_grammar)
        for key, label in (("keywords", "CLI keyword nodes (not full commands)"),
                           ("terminals", "CLI EOL / handler candidates"),
                           ("actions", "Parser action IDs (not CLI command IDs)")):
            rows = tables[key]
            columns = list(rows[0]) if rows else ["address"]
            def select(index, rows=rows):
                row = rows[index]
                self.evidence(row, int(row["address"], 0) if row.get("address") else None)
            self.table(label, [(column, 40 if column in ("help", "action", "handler_name") else 22) for column in columns],
                       [[row.get(column, "") for column in columns] for row in rows], select)

    def recover_syntax(self):
        if self.last_grammar is None or not self.last_grammar.get("mode_definitions"):
            raise ValueError("First extract Static CLI graph with profiles/static_cli_config_paths_26_01_02.json")
        with progress("Recovering config / config-if syntax witnesses; runtime gates remain unverified") as cancelled:
            result = recover_paths(self.last_grammar, cancelled=cancelled)
        self.last_paths = result
        self.save_result("static_syntax_paths", result=result)
        rows = result["paths"]
        self.table("Config syntax candidates (one witness per EOL/context)",
                   [("Mode", 20), ("Syntax candidate", 100), ("EOL", 18), ("Handler", 18), ("Conditions", 12), ("Gaps", 10)],
                   [[r["prompt"], r["syntax_candidate"], hex(r["eol_node"]), hex(r["handler"]),
                     len(r["conditions"]), len(r["gaps"])] for r in rows],
                   lambda n: self.evidence(rows[n], rows[n]["eol_node"]))
        kw.msg("[iosd-helper] Syntax mode coverage: " + json.dumps(
            [{k: v for k, v in mode.items() if k != "frontiers"} for mode in result["summary"]["modes"]]) + "\n")

    def export_syntax(self):
        if self.last_paths is None:
            raise ValueError("Recover syntax paths first")
        path = kw.ask_file(True, "iosd-config-syntax.html", "Export searchable syntax candidates with conditions and gaps")
        if path:
            with open(path, "w", encoding="utf-8") as stream:
                stream.write(syntax_html(identity(), self.last_paths))
            kw.msg("[iosd-helper] Exported syntax candidates: %s\n" % path)

    def build_pool(self, trigger_audit=None):
        if self.last_grammar is None:
            raise ValueError("Extract a static CLI graph first")
        space = build_candidate_space(self.last_grammar, trigger_audit)
        self.last_candidates = space
        self.save_result("acquired_candidate_pool", space=space)
        terminals, fragments, unknown = space["terminals"], space["fragments"], space["unknown_nodes"]
        self.table("All acquired handler definitions (mode unknown retained)",
                   [("Node", 18), ("Handler", 18), ("Possible modes", 45), ("Nearby words (not syntax)", 65)],
                   [[hex(r["node"]), hex(r["handler"]), " | ".join(r["mode_candidates"]) or "unknown; retained",
                     " | ".join(r["nearby_keyword_hints"])] for r in terminals],
                   lambda n: self.evidence(terminals[n], terminals[n]["node"]))
        self.table("All registration fragments (unknown binding retained)",
                   [("Record", 18), ("Root", 18), ("Key", 18), ("Binding", 40), ("Owner?", 45)],
                   [[hex(r["address"]), hex(r["root"]), hex(r["link_key"]), r["binding_status"], r.get("owner_candidate") or ""] for r in fragments],
                   lambda n: self.evidence(fragments[n], fragments[n]["address"]))
        self.table("Unknown / incomplete definitions (retained)",
                   [("Node", 18), ("Action", 40), ("Reason / unresolved semantics", 80)],
                   [[hex(r["address"]), r.get("action_name", ""), r.get("semantic_error", r.get("reason", r.get("semantic_status", "unresolved")))] for r in unknown],
                   lambda n: self.evidence(unknown[n], unknown[n]["address"]))
        kw.msg("[iosd-helper] Candidate pool: " + json.dumps({k: v for k, v in space["summary"].items() if k not in ("notes", "mode_projection")}) + "\n")

    def export_pool(self):
        if self.last_candidates is None:
            raise ValueError("Build the acquired candidate pool first")
        path = kw.ask_file(True, "iosd-candidate-pool.html", "Export all acquired definitions; unknown fragments retained")
        if path:
            with open(path, "w", encoding="utf-8") as stream:
                stream.write(candidate_space_html(identity(), self.last_candidates))
            kw.msg("[iosd-helper] Exported acquired candidate pool: %s\n" % path)

    def export_catalogue(self):
        if self.last_grammar is None:
            raise ValueError("Extract a static CLI graph first")
        path = kw.ask_file(True, "iosd-static-cli-catalogue.html", "Export searchable static evidence inventory")
        if path:
            report = {"identity": identity(), "graph": self.last_grammar}
            with open(path, "w", encoding="utf-8") as stream:
                stream.write(catalogue_html(report))
            kw.msg("[iosd-helper] Exported searchable catalogue: %s\n" % path)

    def export_grammar(self):
        if self.last_grammar is None:
            raise ValueError("Extract a static CLI graph first")
        path = kw.ask_file(True, "iosd-static-cli.dot", "Export partial graph with edge labels")
        if path:
            with open(path, "w", encoding="utf-8") as stream:
                stream.write(to_dot(self.last_grammar))
            kw.msg("[iosd-helper] Exported labeled graph: %s\n" % path)

    def anchors(self):
        with progress("Searching version-independent log/string anchors") as cancelled:
            rows, errors, partial = anchor_candidates(cancelled)
        self.save_result("string_anchor_candidates", rows=rows, errors=errors, cancelled=partial)
        self.table("String anchors", [("String address", 18), ("Anchor", 40), ("Direct refs (capped)", 18)],
                   [[hex(r["address"]), r["anchor"], len(r["references"])] for r in rows],
                   lambda n: self.evidence(rows[n], rows[n]["address"]))

    def select_source(self):
        choice = prompt("Memory source: idb / debugger / core", self.source).lower()
        if choice not in ("idb", "debugger", "core"):
            raise ValueError("Unknown memory source")
        if choice == "debugger":
            DebugMemory()
        if choice == "core":
            path = kw.ask_file(False, "*.core", "Open uncompressed ELF64 iosd core")
            if not path:
                return
            core = ElfCoreMemory(path)
            if self.core:
                self.core.close()
            self.core = core
            self.table("Core mappings (runtime VA)", [("VA", 18), ("Mem size", 18), ("Captured", 18)],
                       [[hex(s.address), hex(s.memory_size), hex(s.file_size)] for s in core.segments])
        self.source = choice
        self.mapping = None
        self.mapping_verified = False
        self.mapping_identity = None
        kw.msg("[iosd-helper] Source=%s; address mapping reset.\n" % choice)

    def set_mapping(self):
        if self.source == "idb":
            raise ValueError("Choose debugger or core first; IDB already uses IDA addresses")
        idb_base = number("IDA address corresponding to image RVA 0", identity()["imagebase"])
        runtime_base = number("Runtime address corresponding to SAME image RVA 0")
        mapping = AddressMap(idb_base, runtime_base)
        # Invalidate old mapping before any validation attempt.
        self.mapping, self.mapping_verified, self.mapping_identity = None, False, None
        ea = number("Verify using a known, unchanged 16-byte string/code address in IDB", kw.get_screen_ea())
        expected = IDBMemory().read(ea, 16)
        actual = self.memory().read(mapping.to_runtime(ea), 16)
        if expected != actual or len(set(expected)) < 4:
            raise ValueError("Mapping probe mismatched or has insufficient byte diversity; choose another anchor")
        self.mapping, self.mapping_verified = mapping, True
        self.mapping_identity = identity()
        kw.msg("[iosd-helper] Mapping probe matched. This verifies an anchor, not whole-image identity.\n")

    def probe(self):
        memory = self.memory()
        address = number("Read address (%s address space)" % self.source, kw.get_screen_ea() if self.source == "idb" else 0)
        size = number("Byte count (1..4096)", 72)
        if not 1 <= size <= 4096:
            raise ValueError("Byte count outside 1..4096")
        raw = memory.read(address, size)
        pointers = {mode: hex(decode_pointer(raw[:8], mode)) for mode in
                    ("little", "big", "mask_then_swap", "swap_then_mask")} if size >= 8 else {}
        self.save_result("memory_probe", source=memory.source, address=address,
                         raw_hex=raw.hex(), pointer_decodings=pointers)
        kw.msg("[iosd-helper] " + json.dumps(self.last, ensure_ascii=False, indent=2) + "\n")

    def nodes(self):
        address = number("FIRST NODE address, not tree root or global slot (%s)" % self.source)
        profile_path = kw.ask_file(False, "*.json", "Optional layout JSON; Cancel uses conservative 72-byte layout")
        config = {}
        if profile_path:
            with open(profile_path, encoding="utf-8") as stream:
                config = json.load(stream)
        layout = NodeLayout(**config) if config else NodeLayout(
            pointer_mode="swap_then_mask", text_policy="icm_print_observed")
        max_nodes = number("Maximum attempted nodes", 1000)
        memory = self.memory()
        with progress("Reading candidate nodes; layout semantics remain unverified") as cancelled:
            result = walk_nodes(memory, address, layout, max_nodes, cancelled)
        self.save_result("candidate_nodes", result=result,
                         address_mapping=asdict(self.mapping) if self.mapping else None,
                         mapping_anchor_verified=self.mapping_verified,
                         core_path=self.core.path if self.source == "core" else None)
        rows = result["nodes"]
        # Capture mapping at acquisition time, never use mutable source state in callbacks.
        mapping = self.mapping if self.source != "idb" else None
        is_idb = self.source == "idb"
        def select(n):
            row = rows[n]
            ea = row["address"] if is_idb else mapping.to_idb(row["address"]) if mapping else None
            self.evidence(row, ea)
        self.table("ICM candidates", [("Node VA", 18), ("Text?", 70), ("Handler?", 18), ("Error", 60)],
                   [[hex(r["address"]), r["text_candidate"],
                     hex(r["handler_candidate"]) if r["handler_candidate"] is not None else "unresolved",
                     r.get("text_error", "")] for r in rows], select)
        kw.msg("[iosd-helper] %d nodes, %d read faults, stop=%s\n" %
               (len(rows), len(result["errors"]), result["stop_reason"]))

    def evidence(self, row, ea=None):
        kw.msg("[iosd-helper] Evidence: " + json.dumps(row, ensure_ascii=False, indent=2) + "\n")
        if ea is not None and ea >= 0 and ida_segment.getseg(ea):
            kw.jumpto(ea)

    def export(self):
        if self.last is None:
            raise ValueError("Run a scan or memory read first")
        path = kw.ask_file(True, "iosd-helper-result.json", "Export last result (partial results included)")
        if path:
            with open(path, "w", encoding="utf-8") as stream:
                json.dump(self.last, stream, ensure_ascii=False, indent=2)
            kw.msg("[iosd-helper] Exported %s\n" % path)
