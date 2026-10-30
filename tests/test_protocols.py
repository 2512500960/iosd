import importlib
import json
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace as NS
import unittest
from unittest.mock import Mock, patch

from iosd_helper.protocols import protocol_query, match_kind, subsystem_seeds, investigation_plan, reviewed_protocol_paths


class ProtocolModelTests(unittest.TestCase):
    def test_prior_paths_are_sample_bound_and_do_not_become_live_execution(self):
        model={'input_md5':'abc','address_space':'rva','protocols':[
            {'name':'cdp','facts':[{'function_rva':'0x100','role':'queue'}],'unknown':['ingress']},
            {'name':'bgp','facts':[],'unknown':['stream']}]}
        for base in (0,0x55555000):
            result=reviewed_protocol_paths(model,{'input_md5':'ABC','imagebase':base},'CDP')
            self.assertFalse(result['verified_in_this_capture'])
            self.assertFalse(result['runtime_execution_proven'])
            self.assertEqual(result['protocols'][0]['facts'][0]['function_rva'],'0x100')
            result['protocols'][0]['unknown'].append('another gap')
        self.assertEqual(model['protocols'][0]['unknown'],['ingress'])
        self.assertEqual(reviewed_protocol_paths(model,{'input_md5':'abc'},'ospf')['protocols'],[])
        with self.assertRaisesRegex(ValueError,'different binary'):
            reviewed_protocol_paths(model,{'input_md5':'wrong'},'cdp')

    def test_matches_are_clues_and_false_positive_substrings_are_retained(self):
        self.assertEqual(protocol_query(' BGP '),'bgp')
        self.assertEqual(match_kind('ipcdp','cdp'),'substring_candidate')
        self.assertEqual(match_kind('bgp_ipv6','bgp'),'name_token_candidate')
        for query in ('a','../cdp','cdp;quit'):
            with self.assertRaises(ValueError):protocol_query(query)

    def test_seed_identity_rebase_and_plan_do_not_claim_packet_handler(self):
        model={'input_md5':'abc','address_space':'rva','subsystems':[
            {'name':'cdp','init_rva':0x123,'record_rva':0x456,'category':'Protocol'},
            {'name':'ipcdp','init_rva':0x789,'record_rva':0x890,'category':'Protocol'}]}
        for base in (0,0x55555000):
            rows=subsystem_seeds(model,{'input_md5':'ABC','imagebase':base},'cdp')
            self.assertEqual(rows[0]['rva'],0x123);self.assertIn('unverified',rows[0]['evidence'])
        with self.assertRaises(ValueError):subsystem_seeds(model,{'input_md5':'wrong'},'cdp')
        self.assertEqual(len(investigation_plan('bgp')['stages']),5)
        self.assertIn('TCP',investigation_plan('bgp')['protocol_hint']['focus'])

    def test_packaged_index_matches_current_saved_map(self):
        root=Path(__file__).resolve().parents[1]
        index=json.loads((root/'profiles/subsystems_26_01_02.json').read_text(encoding='utf-8'))
        self.assertEqual(len(index['subsystems']),5692)
        for query in ('cdp','bgp'):
            rows=subsystem_seeds(index,{'input_md5':index['input_md5']},query)
            self.assertEqual(rows[0]['name'],query)


class ProtocolBoundaryTests(unittest.TestCase):
    def setUp(self):
        names=('ida_bytes','ida_funcs','ida_idaapi','ida_idp','ida_name','ida_segment','ida_ua','ida_xref','idautils','idc')
        self.mods={name:ModuleType(name) for name in names}
        adapter=ModuleType('iosd_helper.ida_adapter');self.mods[adapter.__name__]=adapter
        adapter.identity=lambda:{'input_md5':'fixture','imagebase':0x1000}
        self.data=b'\0CDP Protocol\0cisco.comp/ios/cdp/input.c\0'
        adapter.segments=lambda:[{'address':0x2000,'end':0x2000+len(self.data),'permissions':4,'name':'.rodata'}]
        self.read=Mock(side_effect=lambda ea,size:self.data[ea-0x2000:ea-0x2000+size])
        adapter.IDBMemory=lambda:NS(read=self.read)
        seg=self.mods['ida_segment'];seg.SFL_DEBUG=1;seg.SEGPERM_EXEC=1;seg.SEGPERM_WRITE=2
        seg.getseg=lambda ea:NS(flags=1 if ea>=0x5000 else 0,perm=1 if 0x1000<=ea<0x2000 else 4,
                               name='extern' if ea==0x4000 else '.text' if ea<0x2000 else '.rodata')
        seg.get_segm_name=lambda s:s.name
        u=self.mods['idautils'];u.Names=lambda:iter([(0x1100,'cdp_read'),(0x4000,'bgp_import'),(0x5000,'cdp_runtime')])
        self.mods['ida_funcs'].get_func=lambda ea:NS(start_ea=ea) if ea in (0x1100,0x1200) else None
        self.mods['ida_name'].get_name=lambda ea:'name_%X'%ea
        self.mods['ida_idp'].is_call_insn=lambda insn:insn.site in (0x1101,0x1102)
        ua=self.mods['ida_ua'];ua.insn_t=lambda:NS(site=None)
        def decode(insn,ea):insn.site=ea;return 1
        ua.decode_insn=decode
        x=self.mods['ida_xref'];x.fl_CN=17;x.fl_CF=16;x.fl_F=21
        u.FuncItems=lambda ea:iter([0x1100,0x1101,0x1102])
        u.XrefsTo=lambda ea:iter([])
        def refs(ea):
            if ea==0x1100:return iter([NS(to=0x1200,iscode=False,type=1)])
            if ea==0x1101:return iter([NS(to=0x1200,iscode=True,type=17)])
            return iter([NS(to=0x2100,iscode=False,type=3)])
        u.XrefsFrom=refs;self.mods['idc'].generate_disasm_line=lambda *args:'call [slot]'
        self.patcher=patch.dict(sys.modules,self.mods);self.patcher.start();self.addCleanup(self.patcher.stop)
        sys.modules.pop('iosd_helper.protocol_ida',None)
        self.api=importlib.import_module('iosd_helper.protocol_ida')
        self.addCleanup(lambda:sys.modules.pop('iosd_helper.protocol_ida',None))

    def test_idb_only_clues_preserve_external_runtime_and_coverage(self):
        result=self.api.collect_protocol('cdp',max_bytes=4096)
        self.assertFalse(result['packet_path_verified'])
        self.assertEqual(result['source'],'saved_idb_only')
        self.assertEqual(result['coverage']['bytes_read'],len(self.data))
        runtime=next(r for r in result['candidates'] if r['name']=='cdp_runtime')
        self.assertIsNone(runtime['rva']);self.assertIn('unclassified',runtime['location'])
        literals=[r for r in result['candidates'] if r['kind'] in ('literal','source_path_literal')]
        self.assertEqual(len(literals),2);self.assertTrue(self.read.called)
        self.assertEqual(self.api.location(0x4000,0x1000)['location'],'external_symbol_not_implementation')

    def test_limits_and_cancel_are_reported(self):
        result=self.api.collect_protocol('cdp',max_names=1,max_bytes=0)
        self.assertTrue(result['coverage']['name_limit_reached'])
        self.assertEqual(result['cursor']['phase'],'names')
        self.assertTrue(result['coverage']['has_more'])
        result=self.api.collect_protocol('cdp',cancelled=lambda:True)
        self.assertTrue(result['coverage']['cancelled'])
        self.read.assert_not_called()

    def test_resumed_name_and_literal_pages_equal_one_full_scan_without_duplicates(self):
        full=self.api.collect_protocol('cdp',max_bytes=4096)
        pages=[];cursor=None
        for _ in range(10):
            page=self.api.collect_protocol('cdp',max_names=1,max_bytes=4096,max_hits=1,cursor=cursor)
            pages.extend(page['candidates']);cursor=json.loads(json.dumps(page['cursor']))
            if cursor is None:break
        self.assertIsNone(cursor)
        key=lambda r:(r['ea'],r['name'],r['kind'])
        self.assertEqual([key(r) for r in pages],[key(r) for r in full['candidates']])
        self.assertEqual(len({key(r) for r in pages}),len(pages))

    def test_cursor_rejects_rebase_query_and_name_boundary_changes(self):
        page=self.api.collect_protocol('cdp',max_names=1,max_bytes=0)
        with self.assertRaisesRegex(ValueError,'query'):self.api.collect_protocol('bgp',cursor=page['cursor'])
        self.mods['idautils'].Names=lambda:iter([(0x1100,'renamed'),(0x4000,'bgp_import')])
        with self.assertRaisesRegex(ValueError,'boundary'):self.api.collect_protocol('cdp',cursor=page['cursor'])
        self.mods['iosd_helper.ida_adapter'].identity=lambda:{'input_md5':'fixture','imagebase':0x2000}
        # The module retains the imported identity callable; patch that actual boundary.
        self.api.identity=lambda:{'input_md5':'fixture','imagebase':0x2000}
        with self.assertRaisesRegex(ValueError,'IDB/base'):self.api.collect_protocol('cdp',cursor=page['cursor'])

    def test_indexed_name_resume_skips_directly_and_rejects_count_changes(self):
        rows=[(0x1100,'cdp_read'),(0x4000,'bgp_import'),(0x5000,'cdp_runtime')]
        names=self.mods['ida_name'];names.get_nlist_size=lambda:len(rows)
        names.get_nlist_ea=lambda i:rows[i][0];names.get_nlist_name=lambda i:rows[i][1]
        self.mods['idautils'].Names=Mock(side_effect=AssertionError('Indexed scans must not enumerate from zero'))
        first=self.api.collect_protocol('cdp',max_names=1,max_bytes=0)
        second=self.api.collect_protocol('cdp',max_names=1,max_bytes=0,cursor=first['cursor'])
        self.assertEqual(second['coverage']['name_start_index'],1)
        self.assertEqual(second['coverage']['names_seen'],1)
        self.assertFalse(second['candidates'])
        rows.append((0x5100,'cdp_added'))
        with self.assertRaisesRegex(ValueError,'name table changed'):
            self.api.collect_protocol('cdp',cursor=second['cursor'])

    def test_call_pointer_and_slot_relationships_remain_distinct(self):
        result=self.api.relationships(0x1100)
        kinds=[r['kind'] for r in result['rows']]
        self.assertEqual(kinds,['code_pointer_reference_candidate','direct_call',
                               'indirect_call_slot_candidate','unresolved_indirect_call'])
        self.assertIsNone(result['rows'][-1]['target'])
        self.assertFalse(result['coverage']['limited'])
        result=self.api.relationships(0x1100,max_items=1)
        self.assertTrue(result['coverage']['limited'])


if __name__=='__main__':unittest.main()
