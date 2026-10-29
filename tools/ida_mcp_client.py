"""Small Streamable HTTP MCP client for local IDA validation (Python stdlib)."""
import argparse
import json
from pathlib import Path
import urllib.request


class McpClient:
    def __init__(self, url, timeout=60):
        self.url, self.timeout = url, timeout
        self.headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        self.sequence = 0

    def send(self, method, params=None, notification=False):
        payload = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            payload["params"] = params
        if not notification:
            self.sequence += 1
            payload["id"] = self.sequence
        request = urllib.request.Request(self.url, json.dumps(payload).encode(), self.headers, method="POST")
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            session = response.headers.get("Mcp-Session-Id")
            if session:
                self.headers["Mcp-Session-Id"] = session
            if response.status == 202:
                return None
            if "text/event-stream" in response.headers.get("Content-Type", ""):
                parts, total = [], 0
                message = None
                for line in response:
                    total += len(line)
                    if total > 16 * 1024 * 1024:
                        raise ValueError("MCP response exceeds 16 MiB")
                    line = line.decode("utf-8").rstrip("\r\n")
                    if line.startswith("data:"):
                        parts.append(line[5:].lstrip())
                    elif not line and parts:
                        candidate = json.loads("\n".join(parts))
                        parts = []
                        if candidate.get("id") == payload.get("id"):
                            message = candidate
                            break
                if message is None:
                    raise ValueError("No matching JSON-RPC response in SSE stream")
            else:
                raw = response.read(16 * 1024 * 1024 + 1)
                if len(raw) > 16 * 1024 * 1024:
                    raise ValueError("MCP response exceeds 16 MiB")
                if not raw and notification:
                    return None
                message = json.loads(raw)
        if "error" in message:
            raise RuntimeError(json.dumps(message["error"], ensure_ascii=False))
        return message.get("result")

    def initialize(self):
        result = self.send("initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                                           "clientInfo": {"name": "iosd-helper-validation", "version": "0.1.0"}})
        self.headers["MCP-Protocol-Version"] = result["protocolVersion"]
        self.send("notifications/initialized", notification=True)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("method", choices=("discover", "call"))
    parser.add_argument("--tool")
    parser.add_argument("--arguments", help="JSON file containing tool arguments")
    parser.add_argument("--output", required=True)
    parser.add_argument("--quiet", action="store_true", help="Save full response without printing the tool payload")
    args = parser.parse_args()
    client = McpClient(args.url)
    initialized = client.initialize()
    if args.method == "discover":
        result = client.send("tools/list", {})
    else:
        if not args.tool:
            parser.error("call needs --tool")
        arguments = json.loads(Path(args.arguments).read_text(encoding="utf-8")) if args.arguments else {}
        result = client.send("tools/call", {"name": args.tool, "arguments": arguments})
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"initialize": initialized, "result": result}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Saved", output)
    if args.quiet:
        return
    if args.method == "discover":
        print(json.dumps({"server": initialized.get("serverInfo"),
                          "tools": [{"name": t["name"], "description": t.get("description", "")[:160]}
                                    for t in result.get("tools", [])]}, ensure_ascii=False, indent=2))
    else:
        printable = result.get("structuredContent") if isinstance(result, dict) else None
        if printable is None and isinstance(result, dict):
            printable = [block.get("text", "") for block in result.get("content", []) if block.get("type") == "text"]
        print(json.dumps(printable if printable is not None else result, ensure_ascii=False)[:18000])


if __name__ == "__main__":
    main()
