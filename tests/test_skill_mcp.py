"""Skill boundary tests: exact sources, paused reads, transient modules and timeout recovery."""
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import subprocess
from types import ModuleType,SimpleNamespace as NS
import unittest
from unittest.mock import Mock,patch
from contextlib import redirect_stdout

from iosd_helper import mcp_runtime as runtime
from iosd_helper.memory import MemoryReadError

SPEC=importlib.util.spec_from_file_location('iosd_skill_cli',Path(__file__).resolve().parents[1]/'tools/iosd_mcp.py')
cli=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(cli)


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.identity={'input_md5':'abc','imagebase':0x1000,'idb_path':'test.i64','input_path':'/bin/iosd',
                       'processor':'metapc','bits':64,'byteorder':'little','ida_pid':1,'dbctx_id':0}
        self.identity_patch=patch.object(runtime,'identity',return_value=self.identity.copy());self.identity_patch.start()
        self.addCleanup(self.identity_patch.stop)
        dbg=ModuleType('ida_dbg');dbg.DSTATE_SUSP=-1;dbg.get_process_state=Mock(return_value=-1)
        idd=ModuleType('ida_idd');idd.dbg_read_memory=Mock(side_effect=lambda ea,size:b'ABCD' if ea==0x8020 else bytes(size))
        utils=ModuleType('idautils');utils.Modules=lambda:iter([NS(name='/bin/iosd',base=0x8000,size=0x10000)])
        self.dbg=dbg;self.idd=idd
        self.modules=patch.dict(sys.modules,{'ida_dbg':dbg,'ida_idd':idd,'idautils':utils});self.modules.start()
        self.addCleanup(self.modules.stop)
        self.memory=NS(read=Mock(return_value=b'ABCD'))
        self.reader=patch.object(runtime,'idb_reader',return_value=self.memory);self.reader.start();self.addCleanup(self.reader.stop)

    def request(self):
        return {'source':'debugger','runtime_base':0x8000,'anchors':{'input_md5':'abc','anchors':[{'rva':0x20,'expected_hex':'41424344'}]},
                'ranges':[{'space':'image','rva':0x100,'size':8},{'space':'runtime','va':0x9000,'size':4}]}

    def test_running_target_and_bad_anchor_cannot_fall_back_to_idb(self):
        self.dbg.get_process_state.return_value=1
        with self.assertRaisesRegex(ValueError,'suspended'):runtime.read_ranges(self.request(),self.identity)
        self.idd.dbg_read_memory.assert_not_called();self.memory.read.assert_not_called()
        self.dbg.get_process_state.return_value=-1
        self.memory.read.return_value=b'FAIL'
        with self.assertRaisesRegex(ValueError,'saved IDB'):runtime.read_ranges(self.request(),self.identity)
        self.idd.dbg_read_memory.assert_not_called()

    def test_debugger_va_rva_mapping_and_unread_pages_are_retained(self):
        self.idd.dbg_read_memory.side_effect=lambda ea,size:b'ABCD' if ea==0x8020 else None if ea==0x8100 else bytes(size)
        result=runtime.read_ranges(self.request(),self.identity)
        self.assertEqual(result['ranges'][0]['address'],0x8100)
        self.assertIn('error',result['ranges'][0]);self.assertNotIn('raw_hex',result['ranges'][0])
        self.assertEqual(result['ranges'][1]['raw_hex'],'00000000')
        self.assertFalse(result['complete_requested_ranges']);self.assertFalse(result['atomic_snapshot'])
        self.assertFalse(result['target_execution_changed'])
        self.memory.read.assert_called_once_with(0x1020,4)  # anchors only; no memory fallback

    def test_idb_requires_image_rva_and_preserves_real_read_failure(self):
        request={'source':'idb','ranges':[{'space':'runtime','va':0x1000,'size':4}]}
        with self.assertRaisesRegex(ValueError,'RVAs'):runtime.read_ranges(request,self.identity)
        request['ranges']=[{'rva':0x100,'size':4}]
        self.memory.read.side_effect=MemoryReadError('not loaded')
        result=runtime.read_ranges(request,self.identity)
        self.assertIn('not loaded',result['ranges'][0]['error']);self.assertNotIn('raw_hex',result['ranges'][0])
        self.idd.dbg_read_memory.assert_not_called()

    def test_base_change_after_capture_retains_result_with_invalid_identity_marker(self):
        def sample(*args):
            runtime.identity.return_value={**self.identity,'imagebase':0x2000}
            return {'gaps':[{'reason':'unknown_callback'}]}
        with patch.object(runtime,'function',side_effect=sample):
            result=runtime.run({'operation':'function','identity':self.identity,'rva':0x100})
        self.assertFalse(result['identity_stable']);self.assertEqual(result['result']['gaps'][0]['reason'],'unknown_callback')

    def test_invalid_ranges_are_rejected_before_any_target_read(self):
        for ranges in ([],[{'rva':0,'va':1,'size':4}],[{'rva':-1,'size':4}],
                       [{'rva':0,'size':65537}],[{'rva':True,'size':4}]):
            with self.assertRaises(ValueError):runtime.validated_ranges(ranges)
        self.idd.dbg_read_memory.assert_not_called()


class ClientTests(unittest.TestCase):
    def test_protocol_cli_resume_preserves_session_and_parent_capture_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);session=root/'session.json';previous=root/'page1.json';output=root/'page2.json'
            identity={'input_md5':'fixture','imagebase':0x1000}
            session.write_text(json.dumps({'kind':'iosd_mcp_session','identity':identity}))
            cursor={'schema_version':1,'phase':'names','name_index':10}
            previous.write_text(json.dumps({'operation':'protocol','identity':identity,'identity_stable':True,
                                           'result':{'protocol':'bgp','cursor':cursor}}))
            args=['--url','http://fixture/mcp','protocol','--session',str(session),'--query','BGP',
                  '--resume',str(previous),'--output',str(output)]
            with patch.object(cli,'invoke',return_value={'kind':'iosd_mcp_capture'}) as invoke,redirect_stdout(io.StringIO()):
                self.assertEqual(cli.main(args),0)
                request=invoke.call_args.args[1]
                self.assertEqual(request['cursor'],cursor);self.assertEqual(request['query'],'bgp')
                self.assertEqual(request['identity'],identity)
                self.assertEqual(request['continuation_from_sha256'],cli.hashlib.sha256(previous.read_bytes()).hexdigest())
            with patch.object(cli,'invoke') as invoke:
                with self.assertRaisesRegex(ValueError,'new output'):cli.main(args[:-1]+[str(previous)])
                invoke.assert_not_called()

    def test_capability_discovery_includes_later_pages_and_detects_repeated_cursor(self):
        client=Mock();client.send.side_effect=[{'tools':[{'name':'first'}],'nextCursor':'next'},
                                              {'tools':[{'name':'py_eval'}]}]
        self.assertEqual([r['name'] for r in cli.discover_tools(client)['tools']],['first','py_eval'])
        client.send.assert_called_with('tools/list',{'cursor':'next'})
        client.send.side_effect=[{'tools':[],'nextCursor':'same'},{'tools':[],'nextCursor':'same'}]
        with self.assertRaisesRegex(ValueError,'repeated'):cli.discover_tools(client)

    def test_full_bundle_status_uses_actual_runtime_and_leaves_no_resident_modules(self):
        modules={name:ModuleType(name) for name in ('ida_nalt','ida_loader','ida_ida','ida_kernwin','ida_dbg','ida_auto','idautils')}
        modules['ida_nalt'].retrieve_input_file_md5=lambda:bytes.fromhex('12'*16)
        modules['ida_nalt'].get_imagebase=lambda:0x400000
        modules['ida_nalt'].get_input_file_path=lambda:'/sample/iosd'
        modules['ida_loader'].PATH_TYPE_IDB=1;modules['ida_loader'].get_path=lambda kind:'sample.i64'
        ida=modules['ida_ida'];ida.inf_get_procname=lambda:'metapc';ida.inf_is_64bit=lambda:True
        ida.inf_is_be=lambda:False;ida.get_dbctx_id=lambda:0
        modules['ida_kernwin'].get_kernel_version=lambda:'9.1'
        dbg=modules['ida_dbg'];dbg.DSTATE_SUSP=-1;dbg.DSTATE_RUN=1;dbg.get_process_state=lambda:0
        modules['ida_auto'].auto_is_ok=lambda:True
        code,_=cli.remote_code({'operation':'status'});output=io.StringIO()
        with patch.dict(sys.modules,modules),redirect_stdout(output):exec(code,{})
        result=json.loads(output.getvalue());self.assertEqual(result['identity']['imagebase'],0x400000)
        self.assertFalse(result['target_memory_read']);self.assertFalse(result['target_execution_changed'])
        self.assertFalse(any(name.startswith('_iosd_skill_') for name in sys.modules))

    def test_installed_skill_core_cli_works_from_an_unrelated_directory_and_preserves_holes(self):
        from tools.make_fixtures import core_bytes
        script=Path(__file__).resolve().parents[1]/'skills/iosd-analysis/scripts/iosd_mcp.py'
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);core=folder/'tiny.core';request=folder/'read.json';output=folder/'result.json'
            core.write_bytes(core_bytes([(0x1000,b'abcd',8)]))
            request.write_text(json.dumps({'ranges':[{'space':'runtime','va':0x1000,'size':4},
                                                    {'space':'runtime','va':0x1004,'size':1}]}))
            process=subprocess.run([sys.executable,str(script),'core-read','--core',str(core),'--request',str(request),
                                    '--output',str(output)],cwd=directory,capture_output=True,text=True,timeout=10)
            self.assertEqual(process.returncode,0,process.stderr)
            result=json.loads(output.read_text());self.assertEqual(result['ranges'][0]['raw_hex'],'61626364')
            self.assertIn('not captured',result['ranges'][1]['error']);self.assertNotIn('raw_hex',result['ranges'][1])
            self.assertFalse(result['image_identity_verified'])

    def test_remote_bundle_is_lazy_json_only_and_removes_its_modules(self):
        sources={'__init__':'','mcp_runtime':'def run(request):\n from .helper import value\n return {"value":value,"request":request}\n','helper':'value=7'}
        with patch.object(cli,'runtime_sources',return_value=sources):code,sha=cli.remote_code({'operation':'test'})
        before=set(sys.modules);output=io.StringIO()
        with redirect_stdout(output):exec(code,{})
        self.assertEqual(json.loads(output.getvalue())['value'],7)
        self.assertEqual([n for n in set(sys.modules)-before if n.startswith('_iosd_skill_')],[])
        self.assertEqual(len(sha),64)

    def test_timeout_is_not_retried_and_unresolved_request_blocks_next_capture(self):
        with tempfile.TemporaryDirectory() as directory:
            session=Path(directory)/'session.json';out=Path(directory)/'capture.json'
            client=Mock();client.send.return_value={'tools':[{'name':'py_eval'}]}
            with patch.object(cli,'McpClient',return_value=client),patch.object(cli,'tool_result',side_effect=TimeoutError('pending')) as call:
                with self.assertRaises(TimeoutError):cli.invoke('http://fixture/mcp',{'operation':'read'},session,out)
                self.assertEqual(call.call_count,1)
                self.assertTrue(session.with_suffix('.json.pending.json').exists())
                with self.assertRaisesRegex(ValueError,'unresolved'):cli.invoke('http://fixture/mcp',{'operation':'read'},session,out)
                self.assertEqual(call.call_count,1)

    def test_success_commits_output_and_clears_pending_without_followup_ida_call(self):
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'session.json';client=Mock();client.send.return_value={'tools':[{'name':'py_eval'}]}
            with patch.object(cli,'McpClient',return_value=client),patch.object(cli,'tool_result',return_value='{"kind":"iosd_mcp_session"}') as call:
                cli.invoke('http://fixture/mcp',{'operation':'status'},out,out)
                self.assertEqual(call.call_count,1)
            self.assertEqual(json.loads(out.read_text())['kind'],'iosd_mcp_session')
            self.assertFalse(out.with_suffix('.json.pending.json').exists())


if __name__=='__main__':unittest.main()
