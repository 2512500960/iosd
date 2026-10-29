"""Show the saved catalogue with the current plugin UI in a matching IDA."""
import argparse
import ast
from pathlib import Path
from string import Template

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("report", help="Saved JSON accessible to IDA at the same absolute path")
    parser.add_argument("--syntax", action="store_true", help="Recover and display config/config-if syntax witnesses")
    parser.add_argument("--pool", action="store_true", help="Display all acquired definitions, including unbound fragments")
    parser.add_argument("--trigger-audit", help="Optional audit JSON accessible at the same absolute path in IDA")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    names = ("memory", "locators", "structures", "grammar_semantics", "grammar_registry", "grammar", "ida_adapter",
             "catalogue", "syntax_paths", "syntax_view", "candidate_space", "addressing", "lifecycle", "runtime_linkage", "graph_view", "ui")
    sources = [(name, (root / "iosd_helper" / (name + ".py")).read_text(encoding="utf-8")) for name in names]
    code = Template('''import sys,types,uuid,json,builtins
import ida_nalt
with open($report,encoding="utf-8") as stream: report=json.load(stream)
if ida_nalt.retrieve_input_file_md5().hex()!=report["identity"]["input_md5"]: raise RuntimeError("Input hash mismatch")
if ida_nalt.get_imagebase()!=report["identity"]["imagebase"]: raise RuntimeError("IDB imagebase mismatch")
prefix="_iosd_catalogue_"+uuid.uuid4().hex
pkg=types.ModuleType(prefix)
pkg.__path__=[]
exec($init,pkg.__dict__)
sys.modules[prefix]=pkg
try:
    for name,source in $sources:
        module=types.ModuleType(prefix+"."+name)
        module.__package__=prefix
        sys.modules[module.__name__]=module
        exec(compile(source,"<catalogue-preview-"+name+">","exec"),module.__dict__)
    previous=getattr(builtins,"_iosd_helper_catalogue_preview",None)
    if previous is not None: previous.close()
    app=sys.modules[prefix+".ui"].Application()
    app.last_grammar=report["graph"]
    trigger_audit=None
    $load_audit
    $operation
    builtins._iosd_helper_catalogue_preview=app
    print(json.dumps({"tables":len(app.tables),"rows":[table.OnGetSize() for table in app.tables],"plugin_version":pkg.__version__}))
    result=None
finally:
    for name in list(sys.modules):
        if name==prefix or name.startswith(prefix+"."): del sys.modules[name]
''').substitute(report=repr(str(Path(args.report).resolve())), sources=repr(sources),
                  init=repr((root / "iosd_helper" / "__init__.py").read_text(encoding="utf-8")),
                  load_audit=("with open(%r,encoding='utf-8') as stream: trigger_audit=json.load(stream)" % str(Path(args.trigger_audit).resolve())) if args.trigger_audit else "pass",
                  operation="app.build_pool(trigger_audit)" if args.pool else ("app.recover_syntax()" if args.syntax else "app.cli_catalogue()"))
    ast.parse(code)
    client = McpClient(args.url, timeout=60)
    client.initialize()
    print(tool_result(client, code))


if __name__ == "__main__":
    main()
