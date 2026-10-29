from io import BytesIO
import unittest

from iosd_helper.cdl import (load_cdl, resolve_roots, analyze_root, candidate_paths,
                             legacy_count_for_terminal, walk_cdl)


def fixture(nodes, edges, encoding="UTF-8"):
    xml = '<?xml version="1.0" encoding="%s"?><root><nodes>' % encoding
    xml += nodes + '</nodes><edges>'
    xml += ''.join('<edge from-guid="%d" to-guid="%d"/>' % pair for pair in edges)
    xml += '</edges></root>'
    return BytesIO(xml.encode(encoding))


class CdlTests(unittest.TestCase):
    def diamond(self):
        return load_cdl(fixture('''
        <keyword guid="1" name="NODE_DAG_ROOT" str="NODE_DAG_ROOT"/>
        <keyword guid="2" name="a" str="a"/>
        <keyword guid="3" name="b" str="b"/>
        <keyword guid="4" name="shared" str="shared"/>
        <eol guid="5" name="shared_eol"/>
        ''', [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]))

    def test_shared_suffix_is_reused_and_legacy_bug_is_demonstrated(self):
        graph = self.diamond()
        analysis = analyze_root(graph, 1)
        self.assertEqual(analysis["summary"]["explicit_edge_path_count"], "2")
        paths, stats = candidate_paths(graph, 1, analysis["productive"])
        self.assertEqual(list(paths), [[1, 2, 4, 5], [1, 3, 4, 5]])
        self.assertEqual(stats["stop_reason"], "exhausted")
        self.assertEqual(legacy_count_for_terminal(graph, 1, 5)["emitted_paths"], 1)
        report, rows = walk_cdl(graph, [1], compare_legacy=1)
        self.assertTrue(report["roots"][0]["all_explicit_edge_paths_emitted"])
        self.assertEqual([r["syntax_candidate"] for r in rows], ["a shared <cr>", "b shared <cr>"])

    def test_encoding_filters_requests_and_unreachable_eol_are_preserved(self):
        graph = load_cdl(fixture('''
        <keyword guid="10" name="NODE_DAG_ROOT" str="café" accept-guid="30"/>
        <filter guid="30" name="check" nonzero-guid="40"/>
        <value guid="40" name="number" macro="NUMBER"/>
        <eol guid="50" name="ok_eol"/><eol guid="60" name="unreachable"/>
        <request name="ok_req" bundle="process_bundle"/>
        ''', [(10, 40), (40, 50)], "ISO-8859-1"))
        self.assertEqual(graph.nodes[10]["attributes"]["str"], "café")
        self.assertEqual(graph.nodes[30]["attributes"]["nonzero-guid"], "40")
        self.assertEqual(len(graph.requests), 1)
        self.assertEqual(resolve_roots(graph), [10])
        report, rows = walk_cdl(graph, [10])
        self.assertEqual(report["roots"][0]["unreachable_eol_guids"], [60])
        self.assertEqual(report["explicit_edges_touching_filters"], 0)
        self.assertFalse(rows[0]["conditions_evaluated"])
        self.assertIn("<NUMBER:number>", rows[0]["syntax_candidate"])
        self.assertNotIn("request", rows[0])

    def test_cycle_is_reported_and_does_not_lose_a_terminal_witness(self):
        graph = load_cdl(fixture('''
        <keyword guid="1" name="NODE_DAG_ROOT" str="ROOT"/>
        <keyword guid="2" name="loop" str="loop"/>
        <eol guid="3" name="done"/>
        ''', [(1, 2), (2, 1), (2, 3)]))
        report, rows = walk_cdl(graph, [1])
        self.assertFalse(report["roots"][0]["acyclic"])
        self.assertIsNone(report["roots"][0]["explicit_edge_path_count"])
        self.assertFalse(report["roots"][0]["all_explicit_edge_paths_emitted"])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["eol_guid"], 3)
        self.assertGreater(report["traversal_batches"][0]["cycle_edges_skipped"], 0)

    def test_limits_never_report_full_enumeration(self):
        graph = self.diamond()
        report, rows = walk_cdl(graph, [1], max_paths=1)
        self.assertEqual(len(rows), 1)
        self.assertFalse(report["roots"][0]["all_explicit_edge_paths_emitted"])
        report, rows = walk_cdl(graph, [1], max_depth=2)
        self.assertFalse(rows)
        self.assertFalse(report["roots"][0]["all_explicit_edge_paths_emitted"])
        self.assertGreater(report["traversal_batches"][0]["depth_edges_skipped"], 0)
        paths, stats = candidate_paths(graph, 1, analyze_root(graph, 1)["productive"], max_steps=1)
        self.assertFalse(list(paths))
        self.assertEqual(stats["stop_reason"], "step_limit")

    def test_duplicate_guid_rejected_and_dangling_edge_retained(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            load_cdl(fixture('<eol guid="1"/><eol guid="1"/>', []))
        graph = load_cdl(fixture('<eol guid="1"/>', [(1, 99)]))
        self.assertEqual(graph.errors[0]["kind"], "dangling_edge")
        self.assertEqual(len(graph.edges), 1)
        self.assertFalse(graph.adjacency)

    def test_edge_filter_ref_guid_is_not_a_duplicate_node_and_annotations_survive(self):
        xml = b'''<root><nodes node-num="3">
        <keyword guid="1" name="NODE_DAG_ROOT" str="ROOT"/>
        <filter guid="2" name="check"><filter-field param="FEATURE" value="X"/></filter>
        <eol guid="3" name="done"/>
        </nodes><edges><edge from-guid="1" to-guid="3">
        <filter-ref guid="2" name="check"/><set param="BINOS-AGENT" value="agent"/>
        </edge></edges></root>'''
        graph = load_cdl(BytesIO(xml))
        self.assertEqual(graph.nodes[2]["children"][0]["attributes"]["value"], "X")
        report, paths = walk_cdl(graph, [1])
        self.assertEqual(report["edges_with_metadata"], 1)
        self.assertEqual(report["edge_metadata_types"]["filter-ref"], 1)
        self.assertEqual(paths[0]["edge_annotations"][0]["metadata_alternatives"][0][0]["attributes"]["guid"], "2")
        self.assertTrue(report["guid_node_count_matches_header"])

    def test_root_selection_and_parallel_edges_do_not_duplicate_paths(self):
        graph = load_cdl(fixture('<keyword guid="1" name="config" str="config"/><eol guid="2"/>', [(1, 2), (1, 2)]))
        self.assertEqual(resolve_roots(graph, ["config"]), [1])
        self.assertEqual(resolve_roots(graph, ["0x1"]), [1])
        report, rows = walk_cdl(graph, [1])
        self.assertEqual(report["explicit_edges"], 2)
        self.assertEqual(report["unique_valid_edges"], 1)
        self.assertEqual(rows[0]["syntax_candidate"], "config <cr>")


if __name__ == "__main__":
    unittest.main()
