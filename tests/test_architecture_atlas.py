import json
from pathlib import Path
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET

from tools.build_architecture_atlas import figures,build

ROOT=Path(__file__).resolve().parents[1]


class ArchitectureAtlasTests(unittest.TestCase):
    def test_diagrams_have_resolved_unique_marker_ids_and_accessible_text(self):
        layout=json.loads((ROOT/'profiles/elf_layout_26_01_02.json').read_text(encoding='utf-8'))
        seen=set()
        for name,drawing in figures(layout).items():
            svg=drawing.svg();tree=ET.fromstring(svg)
            ids={node.attrib['id'] for node in tree.iter() if 'id' in node.attrib}
            self.assertFalse(ids&seen);seen|=ids
            self.assertEqual(tree.attrib['role'],'img')
            for marker in re.findall(r'url\(#([^)]*)\)',svg):self.assertIn(marker,ids)
            self.assertNotIn('<script',svg)
            self.assertTrue(''.join(tree.itertext()).strip())

    def test_reader_is_standalone_and_keeps_the_full_text_with_navigation(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);output=folder/'atlas.html'
            result=build(ROOT/'docs/iosd从大ELF到运行机制.md',ROOT/'profiles/elf_layout_26_01_02.json',folder/'assets',output)
            html=output.read_text(encoding='utf-8')
            self.assertFalse(result['ida_access'])
            self.assertEqual(len(list((folder/'assets').glob('*.svg'))),8)
            self.assertEqual(html.count('<svg '),8)
            for anchor in re.findall(r'<a href="#(atlas-\d+)"',html):self.assertIn('id="'+anchor+'"',html)
            self.assertNotRegex(html,r'<script[^>]+src=')
            self.assertNotIn('<img ',html)

    def test_wrong_sample_cannot_generate_this_samples_diagrams(self):
        layout=json.loads((ROOT/'profiles/elf_layout_26_01_02.json').read_text(encoding='utf-8'))
        layout['identity']['input_md5']='other'
        with self.assertRaisesRegex(ValueError,'matching'):figures(layout)
