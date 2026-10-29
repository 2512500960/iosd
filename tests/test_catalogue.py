import json
import unittest

from iosd_helper.catalogue import catalogue_rows, catalogue_html


class CatalogueTests(unittest.TestCase):
    def graph(self):
        return {"nodes": [
            {"address": 0x1000, "status": "transition_candidate", "keyword_candidate": "show"},
            {"address": 0x2000, "status": "transition_candidate", "semantic_role": "command_terminal",
             "handler_candidate": 0x9000, "selector_candidate": 1},
            {"address": 0x2028, "status": "transition_candidate", "semantic_role": "command_terminal",
             "handler_candidate": 0x9000, "selector_candidate": 2}]}

    def test_shared_handler_does_not_collapse_distinct_terminals(self):
        tables = catalogue_rows(self.graph())
        self.assertEqual(len(tables["terminals"]), 2)
        self.assertEqual([row["selector_candidate"] for row in tables["terminals"]], [1, 2])
        self.assertEqual(tables["keywords"][0]["keyword"], "show")

    def test_binary_text_cannot_close_embedded_json_script(self):
        graph = self.graph()
        graph["nodes"][0]["help_candidate"] = '</script><script>alert("x")</script>'
        html = catalogue_html({"graph": graph})
        payload = html.split('<script id="catalogue-data" type="application/json">', 1)[1].split('</script>', 1)[0]
        self.assertNotIn("<", payload)
        self.assertEqual(json.loads(payload)["tables"]["keywords"][0]["help"], graph["nodes"][0]["help_candidate"])


if __name__ == "__main__":
    unittest.main()
