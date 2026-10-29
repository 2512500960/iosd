"""Package code and profiles only; never include Cisco binaries or captures."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper import __version__


def main():
    root = Path(__file__).resolve().parents[1]
    files = [root / name for name in ("iosd_helper_plugin.py", "dev_load.py", "README.md")]
    files += [root / "tools" / name for name in ("project_worker.py", "build_plugin_release.py", "build_architecture_map.py", "build_protocol_index.py", "analyze_nvgen_bindings.py", "build_nvgen_report.py", "check_nvgen_evidence.py", "build_ehsa_report.py", "check_ehsa_evidence.py")]
    files += sorted((root / "iosd_helper").glob("*.py"))
    files += sorted((root / "profiles").glob("*.json"))
    # README's local document links stay usable; reports/captures stay outside releases.
    files += sorted((root / "docs").glob("*.md"))
    files += sorted((root / "docs").glob("*.html"))
    destination = root / "dist" / ("iosd-helper-%s.zip" % __version__)
    destination.parent.mkdir(exist_ok=True)
    manifest = {"version": __version__, "files": {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                "scope": "Code, profiles and documentation; saved evidence projects are separate"}
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(root).as_posix())
        archive.writestr("release-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for name, sha in manifest["files"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == sha
    print(json.dumps({"archive": str(destination), "files": len(files), "bytes": destination.stat().st_size}))


if __name__ == "__main__":
    main()
