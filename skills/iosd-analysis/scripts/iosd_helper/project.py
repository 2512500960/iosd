"""Persistent saved-evidence projects. No IDA imports or target access.

The SQLite file is a disposable index; original JSONL remains the evidence.
Source offsets and line hashes allow detail reads without loading the graph.
"""
import hashlib
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import time

from . import __version__


SCHEMA = 1
COLLECTIONS = {
    "paths": "paths.jsonl", "variants": "option-path-variants.jsonl",
    "nodes": "nodes.jsonl", "unknown": "unknown-nodes.jsonl",
    "registrations": "static-registration-comparison.jsonl",
    "options": "keyword-option-nodes.jsonl", "branches": "indirect-branches.jsonl",
    "pending": "pending-records.jsonl", "slots": "dynamic-slots.jsonl",
}


def atomic_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.flush()
        os.fsync(stream.fileno())
    # Windows readers/AV can briefly deny delete-sharing during status reads.
    for attempt in range(25):
        try:
            os.replace(temporary, path)
            break
        except PermissionError:
            if attempt == 24:
                raise
            time.sleep(0.04)


def number(value):
    return int(value, 0) if isinstance(value, str) else int(value)


def signature(path):
    stat = Path(path).stat()
    return {"size": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def create_project(folder, tree, current_identity, image_ranges=()):
    """Create a new directory; never overwrite another project or its evidence."""
    tree = Path(tree).resolve()
    summary_path = tree / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    captured = summary["identity"]
    if captured["input_md5"].lower() != current_identity["input_md5"].lower():
        raise ValueError("Saved evidence belongs to a different binary")
    capture_base = number(captured["imagebase"])
    ranges = [[number(a), number(b)] for a, b in image_ranges]
    if any(a < 0 or b <= a for a, b in ranges):
        raise ValueError("Invalid image RVA ranges")
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    ranges = merged
    files = {key: {"path": os.path.relpath(tree / filename, Path(folder).resolve()),
                   **signature(tree / filename)}
             for key, filename in COLLECTIONS.items() if (tree / filename).is_file()}
    if "paths" not in files:
        raise ValueError("Expected runtime export tree with paths.jsonl and summary.json")
    folder = Path(folder).resolve()
    folder.mkdir(parents=False, exist_ok=False)
    metadata = {}
    for name in ("summary.json", "analysis-profile.json", "runtime-path-settings.json", "mode-definitions.json"):
        source = tree / name
        if source.is_file():
            # Small metadata is copied; multi-GB evidence is referenced, never rewritten.
            data = source.read_bytes()
            (folder / name).write_bytes(data)
            metadata[name] = hashlib.sha256(data).hexdigest()
    manifest = {"schema_version": SCHEMA, "plugin_version": __version__,
                "created_at": time.time(), "input_md5": captured["input_md5"].lower(),
                "capture_identity": captured, "capture_base": capture_base,
                "creation_identity": current_identity, "image_rva_ranges": ranges,
                "files": files, "metadata_sha256": metadata,
                "scope": "Saved candidate evidence; snapshot values are historical, not live target state"}
    atomic_json(folder / "project.json", manifest)
    return Project(folder)


class Project:
    def __init__(self, path):
        path = Path(path).resolve()
        self.folder = path.parent if path.name == "project.json" else path
        self.manifest = json.loads((self.folder / "project.json").read_text(encoding="utf-8"))
        if self.manifest.get("schema_version") != SCHEMA:
            raise ValueError("Unsupported project schema")
        self.database = self.folder / "index.sqlite"

    def assert_identity(self, current):
        if current["input_md5"].lower() != self.manifest["input_md5"]:
            raise ValueError("Project binary does not match current IDB")

    def source(self, collection):
        return (self.folder / self.manifest["files"][collection]["path"]).resolve()

    def validate_sources(self):
        for key, spec in self.manifest["files"].items():
            if signature(self.source(key)) != {k: spec[k] for k in ("size", "mtime_ns")}:
                raise ValueError("Evidence changed: %s; create a new project" % key)
        for name, expected in self.manifest["metadata_sha256"].items():
            if digest(self.folder / name) != expected:
                raise ValueError("Project metadata changed: " + name)

    def connect(self):
        connection = sqlite3.connect(self.database.as_uri() + "?mode=ro", uri=True, timeout=2)
        connection.row_factory = sqlite3.Row
        return connection

    def status(self):
        path = self.folder / "task.json"
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"state": "not_started"}

    def search(self, collection="paths", query="", mode="", offset=0, limit=200):
        if collection not in self.manifest["files"]:
            raise ValueError("Collection unavailable: " + collection)
        if offset < 0 or not 1 <= limit <= 500:
            raise ValueError("Invalid result page")
        self.validate_sources()
        # Literal substring matching: % and _ are not user-supplied SQL wildcards.
        where, values = "collection=?", [collection]
        if query:
            where += " AND instr(search_text,?)>0"
            values.append(query.casefold())
        if mode:
            where += " AND instr('|' || mode || '|',?)>0"
            values.append("|" + mode.casefold() + "|")
        with closing(self.connect()) as connection:
            count = connection.execute("SELECT count(*) FROM records WHERE " + where, values).fetchone()[0]
            rows = connection.execute(
                "SELECT * FROM records WHERE " + where + " ORDER BY id LIMIT ? OFFSET ?",
                values + [limit, offset]).fetchall()
        return count, [dict(row) for row in rows]

    def detail(self, record):
        self.validate_sources()
        with self.source(record["collection"]).open("rb") as stream:
            stream.seek(record["byte_offset"])
            raw = stream.read(record["byte_length"])
        if hashlib.sha256(raw).hexdigest() != record["line_sha256"]:
            raise ValueError("Evidence record changed; refusing stale index")
        return json.loads(raw)

    def references(self, collection, row):
        """Only known address fields; never recursively relocate raw integers."""
        refs = []
        rva_fields = {"handler_rva": "handler", "eol_rva": "EOL", "image_rva": "node",
                      "registration_rva": "registration", "key_rva": "link key", "root_rva": "fragment root"}
        if collection == "registrations":
            va_fields = {}  # legacy address/root/key fields in this export are RVAs
        else:
            va_fields = {"address": "node", "handler": "handler", "handler_candidate": "handler",
                         "eol_node": "EOL", "action_function": "action", "mode_root": "mode root"}
        for field, label in rva_fields.items():
            if row.get(field) is not None:
                rva = number(row[field])
                refs.append({"label": label, "rva": rva, "space": "image", "field": field})
        for field, label in va_fields.items():
            if row.get(field) is None:
                continue
            va = number(row[field])
            if not va:
                continue
            rva = va - self.manifest["capture_base"]
            if any(a <= rva < b for a, b in self.manifest["image_rva_ranges"]):
                refs.append({"label": label, "rva": rva, "space": "image", "field": field})
            else:
                refs.append({"label": label, "capture_va": va, "space": "capture_va", "field": field})
        # Raw condition/function addresses are explicitly addressed fields too.
        for condition in row.get("conditions", []):
            if isinstance(condition, dict):
                for field in ("node", "function"):
                    if condition.get(field):
                        va = number(condition[field])
                        rva = va - self.manifest["capture_base"]
                        space = any(a <= rva < b for a, b in self.manifest["image_rva_ranges"])
                        refs.append({"label": "condition " + field, "space": "image" if space else "capture_va",
                                     **({"rva": rva} if space else {"capture_va": va})})
        return refs

    def jump_address(self, reference, current):
        self.assert_identity(current)
        if reference["space"] != "image":
            return None
        rva = reference["rva"]
        if not any(a <= rva < b for a, b in self.manifest["image_rva_ranges"]):
            return None
        return number(current["imagebase"]) + rva


def record_summary(project, collection, row):
    mode = row.get("mode", row.get("connected_mode_candidates", row.get("connected_modes", [])))
    mode = mode if isinstance(mode, str) else "|".join(mode)
    label = row.get("syntax_candidate") or row.get("display_label") or row.get("action_name") or row.get("owner_candidate") or collection
    state = row.get("availability") or row.get("runtime_status") or row.get("syntax_status") or row.get("status", "unknown")
    uncertainties = row.get("gaps", row.get("remaining_uncertainties", row.get("unknown", [])))
    refs = project.references(collection, row)
    addresses = " ".join(hex(r.get("rva", r.get("capture_va", 0))) for r in refs)
    # Index compact summaries, never duplicate full traces. Raw evidence remains lossless.
    search_text = " ".join((mode, str(label), str(state), addresses,
                             str(row.get("action_name", "")), json.dumps(row.get("conditions", []), ensure_ascii=False),
                             json.dumps(uncertainties, ensure_ascii=False)))
    return mode.casefold(), str(label), str(state), len(uncertainties), addresses, search_text.casefold()


def build_index(project, cancelled=lambda: False, batch_size=256):
    """Checkpoint each committed batch. Resume only against unchanged sources."""
    if batch_size < 1:
        raise ValueError("Invalid batch size")
    lock = project.folder / "worker.lock"
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, str(os.getpid()).encode("ascii"))
    os.close(fd)
    connection = None
    started = time.time()

    def report(state, **fields):
        atomic_json(project.folder / "task.json", {"state": state, "pid": os.getpid(),
                    "started_at": started, "updated_at": time.time(), **fields})

    try:
        report("validating")
        project.validate_sources()
        connection = sqlite3.connect(project.database)
        connection.execute("PRAGMA journal_mode=WAL")
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS records(
              id INTEGER PRIMARY KEY, collection TEXT, byte_offset INTEGER, byte_length INTEGER,
              line_sha256 TEXT, mode TEXT, label TEXT, state TEXT, gaps INTEGER, addresses TEXT, search_text TEXT,
              UNIQUE(collection,byte_offset));
            CREATE INDEX IF NOT EXISTS record_collection ON records(collection);
            CREATE TABLE IF NOT EXISTS checkpoints(collection TEXT PRIMARY KEY, byte_offset INTEGER, count INTEGER,
              complete INTEGER, source_sha256 TEXT);
        """)
        total_bytes = sum(s["size"] for s in project.manifest["files"].values())
        completed_bytes = 0
        for key, spec in project.manifest["files"].items():
            previous = connection.execute("SELECT byte_offset,count,complete,source_sha256 FROM checkpoints WHERE collection=?", (key,)).fetchone()
            start, count, complete, sha = previous or (0, 0, 0, None)
            if sha is None:
                report("hashing", collection=key, completed_bytes=completed_bytes, total_bytes=total_bytes)
                sha = digest(project.source(key))
            elif digest(project.source(key)) != sha:
                raise ValueError("Evidence hash changed: " + key)
            if complete:
                completed_bytes += spec["size"]
                continue
            with project.source(key).open("rb") as stream:
                stream.seek(start)
                while True:
                    if cancelled() or (project.folder / "cancel.request").exists():
                        report("cancelled", collection=key, count=count, completed_bytes=completed_bytes + stream.tell(), total_bytes=total_bytes)
                        return
                    entries = []
                    for _ in range(batch_size):
                        position = stream.tell()
                        raw = stream.readline()
                        if not raw:
                            break
                        if not raw.strip():
                            continue
                        row = json.loads(raw)
                        entries.append((key, position, len(raw), hashlib.sha256(raw).hexdigest(),
                                        *record_summary(project, key, row)))
                    count += len(entries)
                    with connection:
                        connection.executemany("INSERT INTO records(collection,byte_offset,byte_length,line_sha256,mode,label,state,gaps,addresses,search_text) VALUES(?,?,?,?,?,?,?,?,?,?)", entries)
                        connection.execute("INSERT OR REPLACE INTO checkpoints VALUES(?,?,?,?,?)", (key, stream.tell(), count, int(not raw), sha))
                    report("indexing", collection=key, count=count, completed_bytes=completed_bytes + stream.tell(), total_bytes=total_bytes)
                    if not raw:
                        break
            completed_bytes += spec["size"]
        project.validate_sources()
        report("complete", completed_bytes=total_bytes, total_bytes=total_bytes,
               records=connection.execute("SELECT count(*) FROM records").fetchone()[0])
    except Exception as exc:
        report("failed", error=str(exc))
        raise
    finally:
        if connection:
            connection.close()
        lock.unlink()
