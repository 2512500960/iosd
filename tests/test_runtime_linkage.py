import struct
import unittest

from iosd_helper.addressing import ImageCoordinates
from iosd_helper.runtime_linkage import capture_runtime_linkage
from test_modules import SparseMemory


def pointer(value):return struct.pack(">Q",value|0x8000000000000000) if value else bytes(8)


class RuntimeLinkageTests(unittest.TestCase):
    def spec(self):
        return {"name":"fixture","head_rva":0x100,"record_size":56,"next_offset":0,
                "fields":[{"name":"key","offset":8,"kind":"pointer"},{"name":"anchor","offset":24,"kind":"pointer"},
                          {"name":"type","offset":32,"size":4,"encoding":"big"}]}

    def memory(self,next_node=0):
        raw=bytearray(56);raw[:8]=pointer(next_node);raw[8:16]=pointer(0x7100);raw[24:32]=pointer(0x7200);raw[32:36]=struct.pack(">I",1)
        return SparseMemory({0x7100:pointer(0x9000),0x9000:bytes(raw)})

    def test_runtime_heap_remains_va_and_module_fields_get_rva(self):
        r=capture_runtime_linkage(self.memory(),ImageCoordinates("abc",0,0x7000,0x7000),[(0,0x1000)],[self.spec()])
        n=r["lists"][0]["nodes"][0]
        self.assertEqual(n["address"],0x9000)
        self.assertEqual(n["address_space"],"runtime_only")
        self.assertEqual(n["fields"]["anchor"]["reference"]["rva"],0x200)
        self.assertEqual(n["fields"]["type"]["value"],1)
        self.assertFalse(r["atomic_snapshot"])

    def test_cycle_missing_page_and_node_bound_retained(self):
        coordinates=ImageCoordinates("abc",0,0x7000,0x7000)
        r=capture_runtime_linkage(self.memory(0x9000),coordinates,[(0,0x1000)],[self.spec()])
        self.assertEqual(r["lists"][0]["frontiers"][0]["reason"],"cycle")
        r=capture_runtime_linkage(self.memory(0xA000),coordinates,[(0,0x1000)],[self.spec()],max_nodes=1)
        self.assertEqual(r["lists"][0]["frontiers"][0]["reason"],"node_limit")
        r=capture_runtime_linkage(self.memory(0xA000),coordinates,[(0,0x1000)],[self.spec()])
        self.assertIn("unmapped",r["lists"][0]["frontiers"][0]["reason"])

    def test_mapping_change_aborts_and_keeps_partial_evidence(self):
        count=[0]
        def guard():
            count[0]+=1
            if count[0]==3:raise ValueError("imagebase changed")
        r=capture_runtime_linkage(self.memory(),ImageCoordinates("abc",0,0x7000,0x7000),[(0,0x1000)],[self.spec()],session_guard=guard)
        self.assertEqual(len(r["lists"][0]["nodes"]),1)
        self.assertEqual(r["stop_reason"],"session_or_layout_invalid")
        self.assertIn("changed",r["errors"][0])

    def test_continuation_rejects_head_changed_and_preserves_heap_va(self):
        spec=self.spec();spec.update(start_runtime_va=0x9000,expected_head_raw_hex=pointer(0x9000).hex())
        r=capture_runtime_linkage(self.memory(),ImageCoordinates('abc',0,0x7000,0x7000),[(0,0x1000)],[spec])
        self.assertTrue(r['lists'][0]['terminated_at_null'])
        self.assertEqual(r['lists'][0]['continuation_start_va'],0x9000)
        spec['expected_head_raw_hex']=pointer(0xA000).hex()
        r=capture_runtime_linkage(self.memory(),ImageCoordinates('abc',0,0x7000,0x7000),[(0,0x1000)],[spec])
        self.assertEqual(r['stop_reason'],'session_or_layout_invalid')
        self.assertFalse(r['lists'][0]['nodes'])
