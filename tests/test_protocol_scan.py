import json
import unittest

from iosd_helper.memory import MemoryReadError
from iosd_helper.protocol_scan import literal_windows


class LiteralWindowsTests(unittest.TestCase):
    def scan(self,data,**kwargs):
        def read(ea,size):return data[ea-0x1000:ea-0x1000+size]
        return literal_windows(read,[{'address':0x1000,'end':0x1000+len(data),'name':'.rodata'}],'proto',**kwargs)

    def test_hit_limited_resume_inside_a_window_does_not_lose_or_duplicate_strings(self):
        data=b'\0proto one\0unrelated\0proto two\0proto three\0'
        rows=[];cursor=None
        for _ in range(5):
            page=self.scan(data,max_hits=1,cursor=cursor);rows.extend(page['rows'])
            cursor=json.loads(json.dumps(page['cursor']))
            if cursor is None:break
        self.assertIsNone(cursor)
        self.assertEqual(rows,self.scan(data)['rows'])
        self.assertEqual([r['text'] for r in rows],['proto one','proto two','proto three'])

    def test_crossing_64k_boundary_is_not_reemitted_as_a_tail_fragment(self):
        data=b'\0'*(65536-4)+b'xx proto crossing boundary\0'+b'\0proto later\0'
        rows=self.scan(data)['rows']
        self.assertEqual([r['text'] for r in rows],['xx proto crossing boundary','proto later'])
        self.assertEqual(len({r['ea'] for r in rows}),2)

    def test_tiny_budget_reports_required_window_without_skipping_it(self):
        data=b'\0proto one\0'+bytes(70000)
        page=self.scan(data,max_bytes=8)
        self.assertEqual(page['coverage']['bytes_attempted'],0)
        self.assertGreater(page['coverage']['minimum_next_read_bytes'],8)
        resumed=self.scan(data,cursor=page['cursor'])
        self.assertEqual(resumed['rows'],self.scan(data)['rows'])

    def test_cancellation_and_unread_regions_remain_explicit(self):
        data=b'\0proto one\0'
        cancelled=self.scan(data,cancelled=lambda:True)
        self.assertTrue(cancelled['coverage']['cancelled']);self.assertIsNotNone(cancelled['cursor'])
        def read(ea,size):raise MemoryReadError('page absent')
        page=literal_windows(read,[{'address':0x1000,'end':0x2000,'name':'.rodata'}],'proto')
        self.assertEqual(page['faults'][0]['error'],'page absent')
        self.assertFalse(page['rows']);self.assertIsNone(page['cursor'])


if __name__=='__main__':unittest.main()
