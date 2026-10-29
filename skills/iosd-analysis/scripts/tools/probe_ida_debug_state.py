"""Read IDA identity/base/debugger state only; never read target memory or pause."""
import argparse
import json
from pathlib import Path

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    client = McpClient(args.url, timeout=8)
    client.initialize()
    code = '''import json,ida_nalt,ida_loader,ida_dbg,ida_kernwin
print(json.dumps({"input_md5":ida_nalt.retrieve_input_file_md5().hex(),
 "imagebase":ida_nalt.get_imagebase(),"idb_path":ida_loader.get_path(ida_loader.PATH_TYPE_IDB),
 "ida_version":ida_kernwin.get_kernel_version(),"process_state":ida_dbg.get_process_state(),
 "state_suspended":ida_dbg.DSTATE_SUSP,"state_running":ida_dbg.DSTATE_RUN,
 "target_memory_read":False,"target_execution_changed":False}))
'''
    result = json.loads(tool_result(client, code))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({**result, "imagebase_hex":hex(result["imagebase"])}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
