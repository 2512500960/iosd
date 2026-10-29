"""Read-only IDA view of the partial static parser graph."""
import ida_graph


class StaticParserGraph(ida_graph.GraphViewer):
    def __init__(self, title, graph, evidence):
        super().__init__(title)
        self.graph, self.evidence = graph, evidence

    def OnRefresh(self):
        self.Clear()
        indices = {}
        for row in self.graph["nodes"]:
            indices[row["address"]] = self.AddNode(row)
        for edge in self.graph["edges"]:
            target = edge["target"]
            if target not in indices:
                indices[target] = self.AddNode({"address": target, "status": "unvisited",
                                                "reason": "Not visited within extraction limit"})
            self.AddEdge(indices[edge["source"]], indices[target])
        return True

    def OnGetText(self, node_id):
        row = self[node_id]
        label = "%#x\n%s\n%s" % (row["address"],
                                   row.get("display_label", row.get("keyword_candidate", "op_%s" % row.get("opcode", "?"))),
                                   row.get("reason", row.get("action_name", row["status"])))
        for edge in self.graph["edges"]:
            if edge["source"] == row["address"]:
                label += "\n%s -> %#x" % (edge["kind"], edge["target"])
        color = 0xe0e0ff if row["status"] in ("unresolved", "unvisited") else 0xffffff
        if row.get("semantic_role") in ("command_terminal", "combined_command_terminal"):
            color = 0xe0ffe0
        return label, color

    def OnDblClick(self, node_id):
        row = self[node_id]
        self.evidence(row, row["address"])
        return True
