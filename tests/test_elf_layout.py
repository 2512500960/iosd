import hashlib
from pathlib import Path
import struct
import tempfile
import unittest

from iosd_helper.elf_layout import inspect_elf_layout


def image(order='<',extended=False):
    data=bytearray(512)
    data[:16]=b'\x7fELF\x02'+(b'\x01' if order=='<' else b'\x02')+b'\x01'+bytes(9)
    struct.pack_into(order+'HHIQQQIHHHHHH',data,16,3,62,1,0x1000,64,256,0,64,56,1,64,0 if extended else 4,0xffff if extended else 1)
    struct.pack_into(order+'IIQQQQQQ',data,64,1,5,128,0x1000,0,4,20,4096)
    data[128:132]=b'test'
    names=b'\0.shstrtab\0.text\0.bss\0';data[160:160+len(names)]=names
    if extended:struct.pack_into(order+'IIQQQQIIQQ',data,256,0,0,0,0,0,4,1,0,0,0)
    struct.pack_into(order+'IIQQQQIIQQ',data,320,1,3,0,0,160,len(names),0,0,1,0)
    struct.pack_into(order+'IIQQQQIIQQ',data,384,11,1,6,0x1000,128,4,0,0,1,0)
    struct.pack_into(order+'IIQQQQIIQQ',data,448,17,8,3,0x1004,512,16,0,0,4,0)
    return data


class ElfLayoutTests(unittest.TestCase):
    def inspect(self,data,expected=None):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'fixture.elf';path.write_bytes(data)
            return inspect_elf_layout(path,expected)

    def test_nobits_is_memory_only_and_file_accounting_is_exact(self):
        result=self.inspect(image())
        self.assertEqual(result['sections'][2]['name'],'.text')
        self.assertEqual(result['sections'][3]['size'],16)
        self.assertEqual(result['sections'][3]['file_bytes'],0)
        self.assertEqual(sum(result['file_buckets'].values()),512)
        self.assertEqual(result['load_summary']['file_bytes_sum'],4)
        self.assertEqual(result['load_summary']['memory_bytes_sum'],20)

    def test_big_endian_and_extended_counts(self):
        for order in ('<','>'):
            data=image(order,True);r=self.inspect(data,hashlib.md5(data).hexdigest())
            self.assertEqual(len(r['sections']),4)
            self.assertEqual(r['sections'][2]['address'],0x1000)

    def test_identity_mismatch_and_truncated_table_are_refused(self):
        with self.assertRaisesRegex(ValueError,'MD5'):self.inspect(image(),'wrong')
        with self.assertRaisesRegex(ValueError,'table'):self.inspect(image()[:-1])

    def test_invalid_file_segment_and_name_are_refused(self):
        data=image();struct.pack_into('<Q',data,64+40,2)
        with self.assertRaisesRegex(ValueError,'memory size'):self.inspect(data)
        data=image();struct.pack_into('<I',data,384,999)
        with self.assertRaisesRegex(ValueError,'name'):self.inspect(data)

    def test_overlapping_sections_disable_additive_unassigned_bucket(self):
        data=image();struct.pack_into('<IIQQQQIIQQ',data,448,17,1,2,0x1002,130,2,0,0,1,0)
        r=self.inspect(data)
        self.assertTrue(r['section_overlaps'])
        self.assertNotIn('headers_tables_padding_and_unassigned',r['file_buckets'])
